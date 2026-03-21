from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import OnemliLink, LINK_KATEGORI


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if stadt:
        base_qs = OnemliLink.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            aktif=True
        )
    else:
        base_qs = OnemliLink.objects.filter(aktif=True)

    kategoriler = {}
    for k, v in LINK_KATEGORI:
        if k == 'ilan':
            continue
        linkler = base_qs.filter(kategori=k)
        if linkler.exists():
            kategoriler[k] = {'ad': v, 'linkler': linkler}

    return render(request, 'linkler/liste.html', {
        'kategoriler': kategoriler,
        'tum_kategoriler': LINK_KATEGORI,
        'stadt': stadt,
    })


def git(request, pk, stadt_slug=None):
    link = get_object_or_404(OnemliLink, pk=pk, aktif=True)
    return render(request, 'linkler/git.html', {'link': link})
