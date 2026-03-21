from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import BlogYazisi


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if stadt:
        yazilar = BlogYazisi.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            yayinda=True
        )
    else:
        yazilar = BlogYazisi.objects.filter(scope='eyalet', yayinda=True)

    return render(request, 'blog/liste.html', {
        'yazilar': yazilar,
        'stadt': stadt,
    })


def detay(request, slug, stadt_slug=None):
    from stadt.models import Stadt
    yazi = get_object_or_404(BlogYazisi, slug=slug, yayinda=True)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'blog/detay.html', {
        'yazi': yazi,
        'stadt': stadt,
    })
