from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Stadt, Eyalet
from takvim.models import Etkinlik
from django.utils import timezone
from yerler.models import Yer, YerKategori
from rehber.models import Kaynak
from blog.models import BlogYazisi
import feedparser
import logging
import requests
from django.core.cache import cache

logger = logging.getLogger(__name__)

_HAVA_IKONLARI = {
    0:  ('bi-sun',                  'Açık'),
    1:  ('bi-cloud-sun',            'Az Bulutlu'),
    2:  ('bi-cloud-sun',            'Parçalı Bulutlu'),
    3:  ('bi-clouds',               'Bulutlu'),
    45: ('bi-cloud-fog2',           'Sisli'),
    48: ('bi-cloud-fog2',           'Sisli'),
    51: ('bi-cloud-drizzle',        'Çiseleyen'),
    53: ('bi-cloud-drizzle',        'Çiseleyen'),
    55: ('bi-cloud-drizzle',        'Çiseleyen'),
    61: ('bi-cloud-rain',           'Yağmurlu'),
    63: ('bi-cloud-rain',           'Yağmurlu'),
    65: ('bi-cloud-rain-heavy',     'Sağanak'),
    71: ('bi-cloud-snow',           'Karlı'),
    73: ('bi-cloud-snow',           'Karlı'),
    75: ('bi-cloud-snow',           'Yoğun Kar'),
    80: ('bi-cloud-rain',           'Sağanak'),
    81: ('bi-cloud-rain-heavy',     'Sağanak'),
    82: ('bi-cloud-rain-heavy',     'Kuvvetli Sağanak'),
    95: ('bi-cloud-lightning-rain', 'Fırtınalı'),
    99: ('bi-cloud-lightning-rain', 'Fırtınalı'),
}

def _hava_durumu(lat, lng, cache_key):
    cached = cache.get(cache_key)
    if cached is not None:
        return cached
    try:
        url = (
            f'https://api.open-meteo.com/v1/forecast'
            f'?latitude={lat}&longitude={lng}'
            f'&current=temperature_2m,weather_code'
            f'&timezone=Europe%2FBerlin'
        )
        r = requests.get(url, timeout=4)
        r.raise_for_status()
        data = r.json()['current']
        kod  = data['weather_code']
        icon, aciklama = _HAVA_IKONLARI.get(kod, ('bi-cloud', ''))
        sonuc = {
            'sicaklik': round(data['temperature_2m']),
            'icon':     icon,
            'aciklama': aciklama,
        }
        cache.set(cache_key, sonuc, 1800)
        return sonuc
    except Exception:
        cache.set(cache_key, None, 300)
        return None

# Şehir sayfasındaki dizin sekmesi → Kaynak kategorileri eşleşmesi
_YER_TAB_KAYNAK = {
    'resmi_kurum': [('resmi', 'Resmi Bağlantılar'), ('is', 'İş & Kariyer')],
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
        except Exception as e:
            logger.error(f"Belediye RSS feed ({stadt.rss_duyuru_url}) parse edilemedi: {e}")

    son_blog_yazilari = BlogYazisi.objects.filter(
        scope='eyalet', eyalet__slug=eyalet_slug, yayinda=True
    ).order_by('-olusturulma')[:3]

    konut_belgeler = list(Kaynak.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug) | Q(scope='almanya'),
        yayinda=True, kategori='konut',
    ).order_by('sira'))

    hava = None
    if stadt.lat and stadt.lng:
        hava = _hava_durumu(stadt.lat, stadt.lng, f'hava_{stadt.slug}')

    return render(request, 'stadt/home.html', {
        'stadt':               stadt,
        'eyalet_slug':         eyalet_slug,
        'yaklasan':            yaklasan,
        'belediye_haberleri':  belediye_haberleri,
        'kategoriler':         kategoriler,
        'hava':                hava,
        'tum_kategoriler':     [(k.slug, k.ad) for k in yer_kategorileri],
        'son_blog_yazilari':   son_blog_yazilari,
        'konut_belgeler':      konut_belgeler,
    })
