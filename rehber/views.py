from django.shortcuts import render, get_object_or_404, redirect
from .models import Kaynak, KAYNAK_KATEGORI


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    """Kaynaklar sayfası yerler sayfasına taşındı."""
    from django.http import HttpResponsePermanentRedirect
    if stadt_slug:
        return HttpResponsePermanentRedirect(f'/{eyalet_slug}/{stadt_slug}/yerler/')
    return HttpResponsePermanentRedirect(f'/{eyalet_slug}/yerler/')


def belgeler(request, eyalet_slug='rlp', stadt_slug=None):
    from django.db.models import Q
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    BELGE_KATEGORILER = [
        ('konut', 'Konut & Kira'),
    ]
    belge_kat_list = [k for k, _ in BELGE_KATEGORILER]

    if stadt:
        qs = Kaynak.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug),
            yayinda=True, kategori__in=belge_kat_list,
        ).order_by('sira')
    else:
        qs = Kaynak.objects.filter(
            scope='eyalet', eyalet__slug=eyalet_slug,
            yayinda=True, kategori__in=belge_kat_list,
        ).order_by('sira')

    kategoriler = []
    for k, v in BELGE_KATEGORILER:
        items = list(qs.filter(kategori=k))
        if items:
            kategoriler.append((k, v, items))

    return render(request, 'rehber/belgeler.html', {
        'kategoriler': kategoriler,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })


def anabin_widget(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'rehber/anabin_widget.html', {
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })


def detay(request, slug, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    if not slug or slug == 'None':
        if stadt_slug:
            return redirect(f'/{eyalet_slug}/{stadt_slug}/rehber/')
        return redirect(f'/{eyalet_slug}/rehber/')

    kaynak = get_object_or_404(Kaynak, slug=slug, yayinda=True)
    if kaynak.tip == 'link':
        return redirect(kaynak.url)

    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'rehber/detay.html', {
        'sayfa':       kaynak,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })
