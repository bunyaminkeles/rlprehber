from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import BlogYazisi


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if stadt:
        # Şehir bağlamı → şehre özel + eyalete özel + almanya geneli
        yazilar = BlogYazisi.objects.filter(yayinda=True).filter(
            Q(scope='genel') |
            Q(scope='eyalet', eyalet__slug=eyalet_slug) |
            Q(scope='stadt', stadt=stadt)
        )
    else:
        # Eyalet / ana sayfa bağlamı → tüm yazılar
        yazilar = BlogYazisi.objects.filter(yayinda=True)

    return render(request, 'blog/liste.html', {
        'yazilar':      yazilar,
        'stadt':        stadt,
        'eyalet_slug':  eyalet_slug,
    })


def detay_root(request, slug):
    """Kök URL'den erişilen blog yazısı — /blog/<slug>/"""
    yazi = get_object_or_404(BlogYazisi, slug=slug, yayinda=True)
    return render(request, 'blog/detay.html', {'yazi': yazi, 'eyalet_slug': 'rlp'})


def detay(request, slug, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    yazi = get_object_or_404(BlogYazisi, slug=slug, yayinda=True)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'blog/detay.html', {
        'yazi':        yazi,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })
