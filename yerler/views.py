from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Yer, YER_KATEGORI


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    kategori = request.GET.get('kategori', '')

    if stadt:
        base_qs = Yer.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            aktif=True
        )
    else:
        base_qs = Yer.objects.filter(aktif=True)

    kategoriler = {}
    for k, v in YER_KATEGORI:
        if kategori and k != kategori:
            continue
        yerler = base_qs.filter(kategori=k)
        if yerler.exists():
            kategoriler[k] = {'ad': v, 'yerler': yerler}

    return render(request, 'yerler/liste.html', {
        'kategoriler': kategoriler,
        'secili': kategori,
        'tum_kategoriler': YER_KATEGORI,
        'stadt': stadt,
    })


def detay(request, pk, stadt_slug=None):
    from stadt.models import Stadt
    yer = get_object_or_404(Yer, pk=pk, aktif=True)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'yerler/detay.html', {
        'yer': yer,
        'stadt': stadt,
    })
