from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.cache import cache
from stadt.models import Stadt
from duyurular.models import Duyuru
from ilan.models import Ilan
from takvim.models import Etkinlik
from forum.models import Konu
from ilan.models import SATILIK_KATEGORILER, ARANIYOR_KATEGORILER
from rehber.models import Kaynak, Belge, BELGE_KATEGORI
from almanca import engine as almanca_engine
from blog.models import BlogYazisi


def _rss_haberleri(url, cache_key, limit=8):
    sonuc = cache.get(cache_key)
    if sonuc is not None:
        return sonuc
    try:
        import requests
        import xml.etree.ElementTree as ET
        r = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        r.raise_for_status()
        root = ET.fromstring(r.content)
        haberler = []
        # RSS 2.0
        items = root.findall('./channel/item')
        # RDF/RSS 1.0 (ör. DW Türkçe)
        if not items:
            NS = 'http://purl.org/rss/1.0/'
            items = root.findall(f'{{{NS}}}item')
        for item in items[:limit]:
            NS = 'http://purl.org/rss/1.0/'
            baslik = (item.findtext(f'{{{NS}}}title') or item.findtext('title') or '').strip()
            link   = (item.findtext(f'{{{NS}}}link')  or item.findtext('link')  or '').strip()
            if baslik and link:
                haberler.append({'baslik': baslik, 'link': link})
        cache.set(cache_key, haberler, 1800)
        return haberler
    except Exception:
        cache.set(cache_key, [], 300)
        return []


def _tagesschau_haberleri():
    return _rss_haberleri(
        'https://www.tagesschau.de/xml/rss2',
        'tagesschau_rss',
    )


def _dw_turkce_haberleri():
    return _rss_haberleri(
        'https://rss.dw.com/rdf/rss-tur-all',
        'dw_turkce_rss',
    )


def anasayfa(request):
    """Ana sayfa: son forum konuları, duyurular ve ilanlar widget'ları."""
    import random
    tum_sehirler = list(Stadt.objects.filter(aktiv=True).select_related('eyalet'))
    sehirler = random.sample(tum_sehirler, min(4, len(tum_sehirler)))
    son_konular = (
        Konu.objects
        .select_related('eyalet', 'stadt__eyalet', 'yazar')
        .order_by('-olusturulma')[:8]
    )
    son_duyurular = (
        Duyuru.objects
        .filter(yayinda=True, kaynak_tipi='kullanici', yayin_bitis__gte=timezone.localdate())
        .select_related('stadt__eyalet')
        .order_by('-olusturulma')[:5]
    )
    son_ilanlar = (
        Ilan.objects
        .filter(aktif=True, onaylandi=True, yayin_bitis__gte=timezone.localdate())
        .select_related('stadt', 'eyalet')
        .order_by('-olusturulma')[:4]
    )

    from collections import defaultdict
    from rehber.models import KAYNAK_KATEGORI
    _kat_display = dict(KAYNAK_KATEGORI)
    _kaynaklar_qs = (
        Kaynak.objects
        .filter(scope='almanya', yayinda=True)
        .order_by('kategori', 'sira')
    )
    _gruplar = defaultdict(list)
    for k in _kaynaklar_qs:
        _gruplar[k.kategori].append(k)
    ulusal_kaynaklar = [
        {'ad': _kat_display.get(kat, kat), 'kaynaklar': items}
        for kat, items in _gruplar.items()
    ]

    son_blog_yazilari = BlogYazisi.objects.filter(yayinda=True).order_by('-olusturulma')[:3]

    _belge_kat_display = dict(BELGE_KATEGORI)
    _belgeler_qs = Belge.objects.filter(yayinda=True, stadt__isnull=True).order_by('kategori', 'sira')
    _b_gruplar = defaultdict(list)
    for b in _belgeler_qs:
        _b_gruplar[b.kategori].append(b)
    belgeler_gruplari = [
        {'ad': _belge_kat_display.get(kat, kat), 'slug': kat, 'belgeler': items}
        for kat, items in _b_gruplar.items()
    ]

    return render(request, 'core/anasayfa.html', {
        'sehirler':           sehirler,
        'son_konular':        son_konular,
        'son_blog_yazilari':  son_blog_yazilari,
        'son_duyurular':    son_duyurular,
        'son_ilanlar':        son_ilanlar,
        'tagesschau':       _tagesschau_haberleri(),
        'dw_turkce':        _dw_turkce_haberleri(),
        'ulusal_kaynaklar': ulusal_kaynaklar,
        'belgeler_gruplari': belgeler_gruplari,
    })


def hakkinda(request):
    from .models import Oneri
    gonderildi = False
    if request.method == 'POST':
        from django.core.mail import send_mail
        from django.conf import settings as django_settings
        tur   = request.POST.get('tur', 'oneri')
        ad    = request.POST.get('ad', '').strip()
        eposta = request.POST.get('eposta', '').strip()
        mesaj = request.POST.get('mesaj', '').strip()
        if mesaj:
            Oneri.objects.create(tur=tur, ad=ad, eposta=eposta, mesaj=mesaj)
            send_mail(
                subject=f'[RLP Rehber] Yeni Öneri — {tur}',
                message=f'Tür: {tur}\nGönderen: {ad or "Anonim"}\nE-posta: {eposta or "—"}\n\n{mesaj}',
                from_email=django_settings.DEFAULT_FROM_EMAIL,
                recipient_list=['info@analizus.com'],
                fail_silently=True,
            )
            gonderildi = True
    return render(request, 'core/hakkinda.html', {'gonderildi': gonderildi})


def arama(request):
    from forum.models import Konu
    from blog.models import BlogYazisi
    from duyurular.models import Duyuru
    from rehber.models import Kaynak, Belge
    from yerler.models import Yer
    from stadt.models import Stadt
    from django.db.models import Q as DQ
    from django.shortcuts import redirect as _redirect

    q = request.GET.get('q', '').strip()
    stad_param = request.GET.get('stad', '').strip()
    if not q:
        return render(request, 'core/arama.html', {'q': q, 'sonuclar': []})

    q_lower = q.lower()
    tum_sehirler = list(Stadt.objects.select_related('eyalet').all())

    def _sehir_url(s):
        return f'/{s.eyalet.slug if s.eyalet else "rlp"}/{s.slug}/'

    def _es(obj):
        if hasattr(obj, 'scope') and obj.scope == 'stadt' and obj.stadt and obj.stadt.eyalet:
            return obj.stadt.eyalet.slug
        if obj.stadt and obj.stadt.eyalet:
            return obj.stadt.eyalet.slug
        return 'rlp'

    # Sadece tek başına şehir adı/slug yazıldıysa → şehir sayfasına git
    for s in tum_sehirler:
        if q_lower == s.name.lower() or q_lower == s.slug.lower():
            return _redirect(_sehir_url(s))

    # Şehir bağlamını belirle: form parametresinden ya da query'den
    bulunan_sehir = None
    if stad_param:
        bulunan_sehir = next((s for s in tum_sehirler if s.slug == stad_param), None)
    if not bulunan_sehir:
        for s in tum_sehirler:
            if s.name.lower() in q_lower or s.slug.lower() in q_lower:
                bulunan_sehir = s
                break

    # Şehir bağlamı varsa: o şehir + federal; yoksa: tüm içerik
    def _filtre(qs):
        if bulunan_sehir:
            return qs.filter(DQ(stadt=bulunan_sehir) | DQ(stadt__isnull=True))
        return qs

    sonuclar = []

    # Resmi Belgeler
    for obj in _filtre(
        Belge.objects.filter(DQ(baslik__icontains=q) | DQ(ozet__icontains=q), yayinda=True)
    ).select_related('stadt__eyalet')[:10]:
        if obj.stadt:
            es = obj.stadt.eyalet.slug if obj.stadt.eyalet else 'rlp'
            url = f'/{es}/{obj.stadt.slug}/rehber/belgeler/'
            stad_ad = obj.stadt.name
        else:
            url = '/rehber/belgeler/'
            stad_ad = 'Tüm Almanya'
        sonuclar.append({'tip': 'Resmi Belge', 'icon': 'bi-file-earmark-text',
                         'baslik': obj.baslik, 'ozet': obj.ozet, 'url': url, 'stadt': stad_ad})

    # Kaynaklar
    for obj in _filtre(
        Kaynak.objects.filter(DQ(baslik__icontains=q) | DQ(ozet__icontains=q), yayinda=True)
    ).select_related('stadt__eyalet')[:10]:
        es = _es(obj)
        prefix = f'/{es}/{obj.stadt.slug}' if obj.scope == 'stadt' and obj.stadt else f'/{es}'
        url = obj.url if obj.tip == 'link' else f'{prefix}/rehber/{obj.slug}/'
        sonuclar.append({'tip': 'Kaynak', 'icon': 'bi-journal-bookmark-fill',
                         'baslik': obj.baslik, 'ozet': obj.ozet, 'url': url,
                         'stadt': obj.stadt.name if obj.stadt else 'Tüm Almanya'})

    # Blog yazıları
    for obj in BlogYazisi.objects.filter(
        yayinda=True
    ).filter(DQ(baslik__icontains=q) | DQ(ozet__icontains=q) | DQ(icerik__icontains=q)
    ).select_related('stadt__eyalet')[:5]:
        es = _es(obj)
        prefix = f'/{es}/{obj.stadt.slug}' if obj.scope == 'stadt' and obj.stadt else f'/{es}'
        sonuclar.append({'tip': 'Blog', 'icon': 'bi-pencil-square',
                         'baslik': obj.baslik, 'ozet': obj.ozet or obj.icerik[:120],
                         'url': f'{prefix}/blog/{obj.slug}/',
                         'stadt': obj.stadt.name if obj.stadt else 'Tüm Almanya'})

    # Forum konuları
    for obj in Konu.objects.filter(baslik__icontains=q).select_related('stadt__eyalet')[:5]:
        es = _es(obj)
        prefix = f'/{es}/{obj.stadt.slug}' if obj.scope == 'stadt' and obj.stadt else f'/{es}'
        sonuclar.append({'tip': 'Forum', 'icon': 'bi-chat-dots',
                         'baslik': obj.baslik, 'ozet': obj.icerik[:120],
                         'url': f'{prefix}/forum/konu/{obj.pk}/',
                         'stadt': obj.stadt.name if obj.stadt else 'Tüm Almanya'})

    # Duyurular
    for obj in Duyuru.objects.filter(yayinda=True, baslik__icontains=q).select_related('stadt__eyalet')[:5]:
        es = _es(obj)
        prefix = f'/{es}/{obj.stadt.slug}' if obj.scope == 'stadt' and obj.stadt else f'/{es}'
        sonuclar.append({'tip': 'Duyuru', 'icon': 'bi-megaphone',
                         'baslik': obj.baslik, 'ozet': obj.icerik[:120],
                         'url': f'{prefix}/duyurular/{obj.pk}/',
                         'stadt': obj.stadt.name if obj.stadt else 'Tüm Almanya'})

    # Önemli yerler
    for obj in Yer.objects.filter(ad__icontains=q).select_related('stadt__eyalet')[:5]:
        es = obj.stadt.eyalet.slug if obj.stadt and obj.stadt.eyalet else 'rlp'
        prefix = f'/{es}/{obj.stadt.slug}' if obj.stadt else f'/{es}'
        sonuclar.append({'tip': 'Yer', 'icon': 'bi-geo-alt',
                         'baslik': obj.ad, 'ozet': obj.adres,
                         'url': f'{prefix}/yerler/{obj.pk}/',
                         'stadt': obj.stadt.name if obj.stadt else 'Tüm Almanya'})

    return render(request, 'core/arama.html', {
        'q': q,
        'sonuclar': sonuclar,
        'primary_city_match': bulunan_sehir,
        'primary_city_url': _sehir_url(bulunan_sehir) if bulunan_sehir else None,
    })


def iletisim(request):
    gonderildi = False
    if request.method == 'POST':
        from django.core.mail import send_mail
        from django.conf import settings
        ad      = request.POST.get('ad', '').strip()
        eposta  = request.POST.get('eposta', '').strip()
        mesaj   = request.POST.get('mesaj', '').strip()
        if mesaj:
            send_mail(
                subject=f'[RLP Rehber] İletişim — {ad or "Anonim"}',
                message=f'Gönderen: {ad}\nE-posta: {eposta}\n\n{mesaj}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['info@analizus.com'],
                fail_silently=True,
            )
            gonderildi = True
    return render(request, 'core/iletisim.html', {'gonderildi': gonderildi})


@login_required
def dashboard(request):
    son_duyurular = Duyuru.objects.filter(yayinda=True).order_by('-olusturulma')[:5]
    yaklasan = Etkinlik.objects.filter(tarih__gte=timezone.now().date()).order_by('tarih')[:5]
    benim_ilanim = Ilan.objects.filter(sahip=request.user).order_by('-olusturulma')[:5]
    return render(request, 'core/dashboard.html', {
        'son_duyurular': son_duyurular,
        'yaklasan': yaklasan,
        'benim_ilanim': benim_ilanim,
    })
