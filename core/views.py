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
from rehber.models import Kaynak


def _tagesschau_haberleri():
    CACHE_KEY = 'tagesschau_rss'
    sonuc = cache.get(CACHE_KEY)
    if sonuc is not None:
        return sonuc
    try:
        import requests
        import xml.etree.ElementTree as ET
        r = requests.get(
            'https://www.tagesschau.de/xml/rss2',
            timeout=5,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        r.raise_for_status()
        root = ET.fromstring(r.content)
        haberler = []
        for item in root.findall('./channel/item')[:8]:
            baslik = item.findtext('title', '').strip()
            link   = item.findtext('link', '').strip()
            if baslik and link:
                haberler.append({'baslik': baslik, 'link': link})
        cache.set(CACHE_KEY, haberler, 1800)
        return haberler
    except Exception:
        cache.set(CACHE_KEY, [], 300)
        return []


def anasayfa(request):
    """Ana sayfa: son forum konuları, duyurular ve ilanlar widget'ları."""
    sehirler = Stadt.objects.filter(aktiv=True).select_related('eyalet').order_by('eyalet__slug', 'name')
    son_konular = (
        Konu.objects
        .select_related('eyalet', 'stadt__eyalet', 'yazar')
        .order_by('-olusturulma')[:8]
    )
    son_duyurular = (
        Duyuru.objects
        .filter(yayinda=True, kaynak_tipi='kullanici')
        .select_related('stadt__eyalet')
        .order_by('-olusturulma')[:5]
    )
    son_satilik = (
        Ilan.objects
        .filter(aktif=True, kategori__in=SATILIK_KATEGORILER)
        .select_related('stadt')
        .order_by('-olusturulma')[:4]
    )
    son_araniyor = (
        Ilan.objects
        .filter(aktif=True, kategori__in=ARANIYOR_KATEGORILER)
        .select_related('stadt')
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

    return render(request, 'core/anasayfa.html', {
        'sehirler':         sehirler,
        'son_konular':      son_konular,
        'son_duyurular':    son_duyurular,
        'son_satilik':      son_satilik,
        'son_araniyor':     son_araniyor,
        'tagesschau':       _tagesschau_haberleri(),
        'ulusal_kaynaklar': ulusal_kaynaklar,
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
    from rehber.models import Kaynak
    from yerler.models import Yer

    q = request.GET.get('q', '').strip()
    sonuclar = []

    if q:
        def _eyalet_slug(obj):
            """Nesnenin eyalet slug'ını döndür, yoksa 'rlp' kullan."""
            if obj.scope == 'stadt' and obj.stadt and obj.stadt.eyalet:
                return obj.stadt.eyalet.slug
            return 'rlp'

        def _yer_eyalet_slug(obj):
            if obj.stadt and obj.stadt.eyalet:
                return obj.stadt.eyalet.slug
            return 'rlp'

        konular = Konu.objects.filter(baslik__icontains=q).select_related('stadt__eyalet')[:5]
        for obj in konular:
            es = _eyalet_slug(obj)
            prefix = f'/{es}/{obj.stadt.slug}' if obj.scope == 'stadt' and obj.stadt else f'/{es}'
            sonuclar.append({
                'tip': 'Forum', 'icon': 'bi-chat-dots', 'baslik': obj.baslik,
                'ozet': obj.icerik[:120],
                'url': f'{prefix}/forum/konu/{obj.pk}/',
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

        yazilar = BlogYazisi.objects.filter(yayinda=True, baslik__icontains=q).select_related('stadt__eyalet')[:5]
        for obj in yazilar:
            es = _eyalet_slug(obj)
            prefix = f'/{es}/{obj.stadt.slug}' if obj.scope == 'stadt' and obj.stadt else f'/{es}'
            sonuclar.append({
                'tip': 'Blog', 'icon': 'bi-pencil-square', 'baslik': obj.baslik,
                'ozet': obj.ozet or obj.icerik[:120],
                'url': f'{prefix}/blog/{obj.slug}/',
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

        duyurular = Duyuru.objects.filter(yayinda=True, baslik__icontains=q).select_related('stadt__eyalet')[:5]
        for obj in duyurular:
            es = _eyalet_slug(obj)
            prefix = f'/{es}/{obj.stadt.slug}' if obj.scope == 'stadt' and obj.stadt else f'/{es}'
            sonuclar.append({
                'tip': 'Duyuru', 'icon': 'bi-megaphone', 'baslik': obj.baslik,
                'ozet': obj.icerik[:120],
                'url': f'{prefix}/duyurular/{obj.pk}/',
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

        kaynaklar = Kaynak.objects.filter(yayinda=True, baslik__icontains=q).select_related('stadt__eyalet')[:5]
        for obj in kaynaklar:
            es = _eyalet_slug(obj)
            prefix = f'/{es}/{obj.stadt.slug}' if obj.scope == 'stadt' and obj.stadt else f'/{es}'
            url = obj.url if obj.tip == 'link' else f'{prefix}/rehber/{obj.slug}/'
            sonuclar.append({
                'tip': 'Kaynak', 'icon': 'bi-journal-bookmark-fill', 'baslik': obj.baslik,
                'ozet': obj.ozet,
                'url': url,
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

        yerler = Yer.objects.filter(ad__icontains=q).select_related('stadt__eyalet')[:5]
        for obj in yerler:
            es = _yer_eyalet_slug(obj)
            prefix = f'/{es}/{obj.stadt.slug}' if obj.stadt else f'/{es}'
            sonuclar.append({
                'tip': 'Yer', 'icon': 'bi-geo-alt', 'baslik': obj.ad,
                'ozet': obj.adres,
                'url': f'{prefix}/yerler/{obj.pk}/',
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

    return render(request, 'core/arama.html', {'q': q, 'sonuclar': sonuclar})


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
