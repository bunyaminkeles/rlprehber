import json
from datetime import timedelta
from decimal import Decimal

from django import template
from django.contrib.auth.models import User
from django.db.models import Count, DecimalField, ExpressionWrapper, F, Sum
from django.utils import timezone

from blog.models import BlogYazisi
from businesses.models import LocalBusiness
from duyurular.models import Duyuru
from forum.models import Konu, Yorum
from ilan.models import Ilan
from rehber.models import Kaynak
from takvim.models import Etkinlik
from yerler.models import Yer

register = template.Library()


def _week_count(qs, field='olusturulma'):
    since = timezone.now() - timedelta(days=7)
    return qs.filter(**{f'{field}__gte': since}).count()


def _delta(current, previous):
    if previous == 0:
        return None
    return round((current - previous) / previous * 100, 1)


def _trend(qs, days, date_field='olusturulma'):
    today = timezone.now().date()
    labels, values = [], []
    for i in range(days - 1, -1, -1):
        d = today - timedelta(days=i)
        count = qs.filter(**{
            f'{date_field}__date': d
        }).count()
        labels.append(d.strftime('%d.%m'))
        values.append(count)
    return labels, values


@register.simple_tag
def get_dashboard_stats():
    now = timezone.now()
    week_ago = now - timedelta(days=7)
    two_weeks_ago = now - timedelta(days=14)

    all_users = User.objects.all()
    all_konular = Konu.objects.all()
    all_yorumlar = Yorum.objects.all()
    all_ilanlar = Ilan.objects.all()

    # ── Temel sayılar ──────────────────────────────
    total_users = all_users.count()
    week_users = all_users.filter(date_joined__gte=week_ago).count()
    prev_users = all_users.filter(date_joined__gte=two_weeks_ago, date_joined__lt=week_ago).count()

    total_konular = all_konular.count()
    week_konular = all_konular.filter(olusturulma__gte=week_ago).count()
    prev_konular = all_konular.filter(olusturulma__gte=two_weeks_ago, olusturulma__lt=week_ago).count()

    total_yorumlar = all_yorumlar.count()
    week_yorumlar = all_yorumlar.filter(olusturulma__gte=week_ago).count()
    prev_yorumlar = all_yorumlar.filter(olusturulma__gte=two_weeks_ago, olusturulma__lt=week_ago).count()

    total_ilanlar = all_ilanlar.filter(aktif=True).count()
    week_ilanlar = all_ilanlar.filter(aktif=True, olusturulma__gte=week_ago).count()

    # ── Onay bekleyenler ────────────────────────────
    pending_ilanlar = Ilan.objects.filter(aktif=True, onaylandi=False).order_by('-olusturulma')

    # ── Son kayıtlar ────────────────────────────────
    recent_users = all_users.order_by('-date_joined')[:12]

    # ── İçerik özeti ────────────────────────────────
    blog_count = BlogYazisi.objects.filter(yayinda=True).count()
    duyuru_count = Duyuru.objects.filter(yayinda=True).count()
    etkinlik_count = Etkinlik.objects.filter(tarih__gte=now.date()).count()
    yer_count = Yer.objects.filter(aktif=True).count()
    kaynak_count = Kaynak.objects.filter(yayinda=True).count()
    today = now.date()
    aktif_isletme_count = LocalBusiness.objects.filter(
        is_published=True, end_date__gte=today,
    ).count()
    toplam_isletme_count = LocalBusiness.objects.count()
    verified_isletme_count = LocalBusiness.objects.filter(is_verified=True).count()

    # MRR — plan_fiyat / duration_days * 30, tek aggregate sorgusu
    mrr_sonuc = (
        LocalBusiness.objects
        .filter(is_published=True, end_date__gte=today, subscription_plan__isnull=False)
        .aggregate(
            mrr=Sum(
                ExpressionWrapper(
                    F('subscription_plan__price') / F('subscription_plan__duration_days') * 30,
                    output_field=DecimalField(max_digits=10, decimal_places=2),
                )
            )
        )
    )
    mrr = mrr_sonuc['mrr'] or Decimal('0')

    # Churn — son 30 günde aboneliği biten ve yenilenmeyen işletmeler
    thirty_days_ago = today - timedelta(days=30)
    churned = LocalBusiness.objects.filter(
        end_date__gte=thirty_days_ago,
        end_date__lt=today,
    ).count()
    churn_base = aktif_isletme_count + churned
    churn_rate = round(churned / churn_base * 100, 1) if churn_base else 0.0

    # ── Platform sağlığı ─────────────────────────────
    score = min(100, int(
        (min(total_users, 50) / 50) * 30 +
        (min(total_konular, 20) / 20) * 25 +
        (min(total_ilanlar, 10) / 10) * 20 +
        (min(blog_count, 5) / 5) * 15 +
        (min(yer_count, 50) / 50) * 10
    ))
    if score >= 80:
        health_color, health_label = '#10b981', 'Mükemmel'
    elif score >= 60:
        health_color, health_label = '#6366f1', 'İyi'
    elif score >= 40:
        health_color, health_label = '#f59e0b', 'Gelişiyor'
    else:
        health_color, health_label = '#ef4444', 'Başlangıç'

    # ── Trend verileri ───────────────────────────────
    def build_chart(days):
        ul, uv = _trend(all_users, days, 'date_joined')
        kl, kv = _trend(all_konular, days)
        _, yv = _trend(all_yorumlar, days)
        return ul, uv, kv, yv

    l7, u7, k7, y7 = build_chart(7)
    l30, u30, k30, y30 = build_chart(30)
    l90, u90, k90, y90 = build_chart(90)

    return {
        # Stat kartları
        'total_users': total_users,
        'week_users': week_users,
        'delta_users': _delta(week_users, prev_users),

        'total_konular': total_konular,
        'week_konular': week_konular,
        'delta_konular': _delta(week_konular, prev_konular),

        'total_yorumlar': total_yorumlar,
        'week_yorumlar': week_yorumlar,
        'delta_yorumlar': _delta(week_yorumlar, prev_yorumlar),

        'total_ilanlar': total_ilanlar,
        'week_ilanlar': week_ilanlar,

        # Platform sağlığı
        'health_score': score,
        'health_color': health_color,
        'health_label': health_label,

        # Onay
        'pending_ilanlar': pending_ilanlar,
        'pending_ilanlar_count': pending_ilanlar.count(),

        # Son kullanıcılar
        'recent_users': recent_users,

        # İçerik özeti
        'blog_count': blog_count,
        'duyuru_count': duyuru_count,
        'etkinlik_count': etkinlik_count,
        'yer_count': yer_count,
        'kaynak_count': kaynak_count,
        'aktif_isletme_count': aktif_isletme_count,
        'toplam_isletme_count': toplam_isletme_count,
        'verified_isletme_count': verified_isletme_count,
        'mrr': mrr,
        'churn_rate': churn_rate,
        'churned_count': churned,

        # Grafik (7 gün)
        'chart_labels_json': json.dumps(l7),
        'user_trend_json': json.dumps(u7),
        'konu_trend_json': json.dumps(k7),
        'yorum_trend_json': json.dumps(y7),
        # Grafik (30 gün)
        'chart_labels_30_json': json.dumps(l30),
        'user_trend_30_json': json.dumps(u30),
        'konu_trend_30_json': json.dumps(k30),
        'yorum_trend_30_json': json.dumps(y30),
        # Grafik (90 gün)
        'chart_labels_90_json': json.dumps(l90),
        'user_trend_90_json': json.dumps(u90),
        'konu_trend_90_json': json.dumps(k90),
        'yorum_trend_90_json': json.dumps(y90),
    }
