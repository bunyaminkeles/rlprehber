from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Duyuru


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    kategori = request.GET.get('kategori', '')

    if stadt:
        qs = Duyuru.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            yayinda=True
        )
    else:
        qs = Duyuru.objects.filter(scope='eyalet', yayinda=True)

    if kategori:
        qs = qs.filter(kategori=kategori)

    return render(request, 'duyurular/liste.html', {
        'duyurular': qs.order_by('-id')[:20],
        'secili': kategori,
        'stadt': stadt,
    })


def detay(request, pk, stadt_slug=None):
    from stadt.models import Stadt
    duyuru = get_object_or_404(Duyuru, pk=pk, yayinda=True)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'duyurular/detay.html', {
        'duyuru': duyuru,
        'stadt': stadt,
    })
