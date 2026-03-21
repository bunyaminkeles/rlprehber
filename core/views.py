from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from stadt.models import Stadt
from duyurular.models import Duyuru
from ilan.models import Ilan
from takvim.models import Etkinlik
from forum.models import Konu
from ilan.models import SATILIK_KATEGORILER, ARANIYOR_KATEGORILER


def anasayfa(request):
    """Ana sayfa: son forum konuları ve ilanlar widget'ları."""
    sehirler = Stadt.objects.filter(aktiv=True)
    son_konular = (
        Konu.objects
        .select_related('stadt', 'yazar')
        .order_by('-olusturulma')[:8]
    )
    son_satilik = (
        Ilan.objects
        .filter(aktif=True, kategori__in=SATILIK_KATEGORILER)
        .select_related('stadt')
        .order_by('-olusturulma')[:5]
    )
    son_araniyor = (
        Ilan.objects
        .filter(aktif=True, kategori__in=ARANIYOR_KATEGORILER)
        .select_related('stadt')
        .order_by('-olusturulma')[:5]
    )
    return render(request, 'core/anasayfa.html', {
        'sehirler': sehirler,
        'son_konular': son_konular,
        'son_satilik': son_satilik,
        'son_araniyor': son_araniyor,
    })


def hakkinda(request):
    from .models import Oneri
    gonderildi = False
    if request.method == 'POST':
        Oneri.objects.create(
            tur=request.POST.get('tur', 'oneri'),
            ad=request.POST.get('ad', '').strip(),
            eposta=request.POST.get('eposta', '').strip(),
            mesaj=request.POST.get('mesaj', '').strip(),
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
        konular = Konu.objects.filter(baslik__icontains=q).select_related('stadt')[:5]
        for obj in konular:
            slug = obj.stadt.slug if obj.scope == 'stadt' and obj.stadt else 'rlp'
            sonuclar.append({
                'tip': 'Forum', 'icon': 'bi-chat-dots', 'baslik': obj.baslik,
                'ozet': obj.icerik[:120],
                'url': f'/{slug}/forum/konu/{obj.pk}/',
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

        yazilar = BlogYazisi.objects.filter(yayinda=True, baslik__icontains=q).select_related('stadt')[:5]
        for obj in yazilar:
            slug = obj.stadt.slug if obj.scope == 'stadt' and obj.stadt else 'rlp'
            sonuclar.append({
                'tip': 'Blog', 'icon': 'bi-pencil-square', 'baslik': obj.baslik,
                'ozet': obj.ozet or obj.icerik[:120],
                'url': f'/{slug}/blog/{obj.slug}/',
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

        duyurular = Duyuru.objects.filter(yayinda=True, baslik__icontains=q).select_related('stadt')[:5]
        for obj in duyurular:
            slug = obj.stadt.slug if obj.scope == 'stadt' and obj.stadt else 'rlp'
            sonuclar.append({
                'tip': 'Duyuru', 'icon': 'bi-megaphone', 'baslik': obj.baslik,
                'ozet': obj.icerik[:120],
                'url': f'/{slug}/duyurular/{obj.pk}/',
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

        kaynaklar = Kaynak.objects.filter(yayinda=True, baslik__icontains=q).select_related('stadt')[:5]
        for obj in kaynaklar:
            slug = obj.stadt.slug if obj.scope == 'stadt' and obj.stadt else 'rlp'
            url = obj.url if obj.tip == 'link' else f'/{slug}/rehber/{obj.slug}/'
            sonuclar.append({
                'tip': 'Kaynak', 'icon': 'bi-journal-bookmark-fill', 'baslik': obj.baslik,
                'ozet': obj.ozet,
                'url': url,
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

        yerler = Yer.objects.filter(ad__icontains=q).select_related('stadt')[:5]
        for obj in yerler:
            slug = obj.stadt.slug if obj.stadt else 'rlp'
            sonuclar.append({
                'tip': 'Yer', 'icon': 'bi-geo-alt', 'baslik': obj.ad,
                'ozet': obj.adres,
                'url': f'/{slug}/yerler/{obj.pk}/',
                'stadt': obj.stadt.name if obj.stadt else 'RLP',
            })

    return render(request, 'core/arama.html', {'q': q, 'sonuclar': sonuclar})


def iletisim(request):
    return render(request, 'core/iletisim.html')


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
