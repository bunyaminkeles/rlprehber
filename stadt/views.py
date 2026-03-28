from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Stadt, Eyalet
from duyurular.models import Duyuru
from takvim.models import Etkinlik
from django.utils import timezone
from yerler.models import Yer, YerKategori
from rehber.models import Kaynak
import feedparser

# Şehir sayfasındaki dizin sekmesi → Kaynak kategorileri eşleşmesi
_YER_TAB_KAYNAK = {
    'resmi_kurum': [('resmi', 'Resmi Bağlantılar'), ('is', 'İş & Kariyer'), ('konut', 'Konut & Belgeler')],
    'egitim':      [('egitim', 'Eğitim'), ('almanca', 'Almanca Öğrenimi')],
    'saglik':      [('saglik', 'Sağlık')],
    'gezi':        [('gezi', 'Gezi & Kültür')],
}


def eyalet_home(request, eyalet_slug='rlp'):
    eyalet = get_object_or_404(Eyalet, slug=eyalet_slug, aktif=True)
    sehirler = Stadt.objects.filter(eyalet=eyalet, aktiv=True).order_by('name')

    yaklasan_qs = Etkinlik.objects.filter(
        scope='eyalet', eyalet=eyalet,
        tarih__gte=timezone.now().date()
    ).order_by('tarih')

    seen = set()
    yaklasan = []
    for e in yaklasan_qs:
        key = (e.baslik, e.tarih)
        if key not in seen:
            seen.add(key)
            yaklasan.append(e)
            if len(yaklasan) == 6:
                break

    return render(request, 'eyalet/home.html', {
        'eyalet':      eyalet,
        'eyalet_slug': eyalet_slug,
        'sehirler':    sehirler,
        'yaklasan':    yaklasan,
    })


def home(request, eyalet_slug='rlp', stadt_slug=None):
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True)

    son_duyurular = Duyuru.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        yayinda=True
    ).order_by('-olusturulma')[:4]

    yaklasan_qs = Etkinlik.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(eyalet=stadt.eyalet, scope='eyalet'),
        tarih__gte=timezone.now().date()
    ).order_by('tarih')

    # Aynı isim+tarih kombinasyonu birden fazla kez girilmiş olabilir; dedupe et
    seen = set()
    yaklasan = []
    for e in yaklasan_qs:
        key = (e.baslik, e.tarih)
        if key not in seen:
            seen.add(key)
            yaklasan.append(e)
            if len(yaklasan) == 3:
                break

    # ── Önemli Yerler Dizini ─────────────────────────────────────────────────
    yer_kategorileri = list(YerKategori.objects.filter(tur='yer').order_by('sira', 'ad'))
    yer_kodlari = [k.slug for k in yer_kategorileri]

    base_yer_qs = Yer.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug),
        aktif=True, tur='yer', kategori__in=yer_kodlari,
    )

    kategoriler = {}
    for k in yer_kategorileri:
        yerler = base_yer_qs.filter(kategori=k.slug)
        if yerler.exists():
            kategoriler[k.slug] = {'ad': k.ad, 'yerler': yerler}

    tum_kaynak_kat = list({k for gruplari in _YER_TAB_KAYNAK.values() for k, _ in gruplari})
    kaynak_qs = Kaynak.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug) | Q(scope='almanya'),
        yayinda=True, kategori__in=tum_kaynak_kat,
    ).order_by('sira')

    for tab_slug, gruplari in _YER_TAB_KAYNAK.items():
        rehber_alt = {}
        for kat_k, kat_v in gruplari:
            items = list(kaynak_qs.filter(kategori=kat_k))
            if items:
                rehber_alt[kat_v] = items
        if rehber_alt:
            if tab_slug not in kategoriler:
                kat_obj = next((k for k in yer_kategorileri if k.slug == tab_slug), None)
                if kat_obj:
                    kategoriler[tab_slug] = {'ad': kat_obj.ad, 'yerler': Yer.objects.none()}
            if tab_slug in kategoriler:
                kategoriler[tab_slug]['rehber_alt'] = rehber_alt

    # ── Belediye RSS Haberleri ────────────────────────────────────────────────
    belediye_haberleri = []
    if stadt.rss_duyuru_url:
        try:
            feed = feedparser.parse(stadt.rss_duyuru_url)
            for entry in feed.entries[:5]:
                belediye_haberleri.append({
                    'baslik': entry.get('title', ''),
                    'link':   entry.get('link', ''),
                    'tarih':  entry.get('published', ''),
                })
        except Exception:
            pass

    return render(request, 'stadt/home.html', {
        'stadt':               stadt,
        'eyalet_slug':         eyalet_slug,
        'son_duyurular':       son_duyurular,
        'yaklasan':            yaklasan,
        'belediye_haberleri':  belediye_haberleri,
        'kategoriler':         kategoriler,
        'tum_kategoriler':     [(k.slug, k.ad) for k in yer_kategorileri],
    })
