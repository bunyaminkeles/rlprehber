from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Case, When, IntegerField
from .models import Yer, YerFoto, ReklamPaketi, YER_KATEGORILERI, ISLETME_KATEGORILERI


def _get_stadt(stadt_slug):
    if not stadt_slug:
        return None
    from stadt.models import Stadt
    return get_object_or_404(Stadt, slug=stadt_slug, aktiv=True)


def _base_qs(stadt):
    if stadt:
        return Yer.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            aktif=True
        )
    return Yer.objects.filter(aktif=True)


# ── Önemli Yerler ────────────────────────────────────────────────────────────

def liste(request, stadt_slug=None):
    stadt = _get_stadt(stadt_slug)
    kategori = request.GET.get('kategori', '')
    yer_kodlari = [k for k, _ in YER_KATEGORILERI]

    base_qs = _base_qs(stadt).filter(tur='yer', kategori__in=yer_kodlari)

    kategoriler = {}
    for k, v in YER_KATEGORILERI:
        if kategori and k != kategori:
            continue
        yerler = base_qs.filter(kategori=k)
        if yerler.exists():
            kategoriler[k] = {'ad': v, 'yerler': yerler}

    return render(request, 'yerler/liste.html', {
        'kategoriler': kategoriler,
        'secili': kategori,
        'tum_kategoriler': YER_KATEGORILERI,
        'stadt': stadt,
    })


# ── İşletmeler ───────────────────────────────────────────────────────────────

def isletmeler(request, stadt_slug=None):
    stadt = _get_stadt(stadt_slug)
    kategori = request.GET.get('kategori', '')

    paket_sira = Case(
        When(paket='pro', then=0),
        When(paket='plus', then=1),
        When(paket='temel', then=2),
        default=3,
        output_field=IntegerField(),
    )

    isletme_kodlari = [k for k, _ in ISLETME_KATEGORILERI]
    base_qs = _base_qs(stadt).filter(
        tur='isletme', kategori__in=isletme_kodlari
    ).annotate(paket_sira=paket_sira).order_by('paket_sira', 'ad')

    kategoriler = {}
    for k, v in ISLETME_KATEGORILERI:
        if kategori and k != kategori:
            continue
        islt = base_qs.filter(kategori=k)
        if islt.exists():
            kategoriler[k] = {'ad': v, 'yerler': islt}

    paketler = ReklamPaketi.objects.filter(aktif=True)

    return render(request, 'yerler/isletmeler.html', {
        'kategoriler': kategoriler,
        'secili': kategori,
        'tum_kategoriler': ISLETME_KATEGORILERI,
        'stadt': stadt,
        'paketler': paketler,
    })


# ── Detay (ortak) ────────────────────────────────────────────────────────────

def detay(request, pk, stadt_slug=None):
    stadt = _get_stadt(stadt_slug) if stadt_slug else None
    yer = get_object_or_404(Yer, pk=pk, aktif=True)
    fotolar = yer.fotolar.all()
    return render(request, 'yerler/detay.html', {
        'yer': yer,
        'stadt': stadt,
        'fotolar': fotolar,
    })


# ── Reklam Paketleri ─────────────────────────────────────────────────────────

def paketler(request):
    paket_listesi = ReklamPaketi.objects.filter(aktif=True)
    iletisim_notu = paket_listesi.exclude(iletisim_notu='').values_list('iletisim_notu', flat=True).first()
    return render(request, 'yerler/paketler.html', {
        'paketler': paket_listesi,
        'iletisim_notu': iletisim_notu,
    })
