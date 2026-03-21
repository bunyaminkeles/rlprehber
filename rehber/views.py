from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Kaynak, KAYNAK_KATEGORI


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if stadt:
        qs = Kaynak.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            yayinda=True
        )
    else:
        # /rlp/rehber/ — sadece eyalet geneli
        qs = Kaynak.objects.filter(scope='eyalet', yayinda=True)

    kategoriler = {}
    for k, v in KAYNAK_KATEGORI:
        kaynaklar = qs.filter(kategori=k)
        if kaynaklar.exists():
            kategoriler[v] = kaynaklar

    return render(request, 'rehber/liste.html', {
        'kategoriler': kategoriler,
        'stadt': stadt,
    })


def detay(request, slug, stadt_slug=None):
    from stadt.models import Stadt
    if not slug or slug == 'None':
        if stadt_slug:
            return redirect('rehber:liste', stadt_slug=stadt_slug)
        return redirect('rehber:liste')

    kaynak = get_object_or_404(Kaynak, slug=slug, yayinda=True)
    if kaynak.tip == 'link':
        return redirect(kaynak.url)

    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'rehber/detay.html', {
        'sayfa': kaynak,
        'stadt': stadt,
    })
