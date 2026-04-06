from django.shortcuts import render, get_object_or_404, redirect
from .models import Kaynak, KAYNAK_KATEGORI, Belge, BELGE_KATEGORI


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    """Kaynaklar sayfası yerler sayfasına taşındı."""
    from django.http import HttpResponsePermanentRedirect
    if stadt_slug:
        return HttpResponsePermanentRedirect(f'/{eyalet_slug}/{stadt_slug}/yerler/')
    return HttpResponsePermanentRedirect(f'/{eyalet_slug}/yerler/')


class _KaynakBelgeAdapter:
    """Kaynak nesnesini Belge arayüzüne uyumlu hale getirir (belgeler sayfası için)."""
    dosya_uzantisi = 'pdf'
    dosya = None

    def __init__(self, kaynak):
        self.baslik = kaynak.baslik
        self.ozet = kaynak.ozet
        self.indirme_url = kaynak.url or '#'


def belgeler(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    from django.db.models import Q
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    aktif_kat = request.GET.get('kat', '')

    # Şehir bağlamı varsa o şehir + federal; yoksa sadece federal
    if stadt:
        base_qs = Belge.objects.filter(yayinda=True).filter(Q(stadt=stadt) | Q(stadt__isnull=True))
    else:
        base_qs = Belge.objects.filter(yayinda=True, stadt__isnull=True)

    # Şehir sayfasındaki konut Kaynakları (Kaynak modeli) belgeler sayfasına dahil et
    konut_kaynaklar = []
    if stadt:
        konut_qs = Kaynak.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug) | Q(scope='almanya'),
            yayinda=True, kategori='konut',
        ).order_by('sira')
        konut_kaynaklar = [_KaynakBelgeAdapter(k) for k in konut_qs]

    kategoriler = []
    for k, v in BELGE_KATEGORI:
        items = list(base_qs.filter(kategori=k))
        if k == 'konut':
            items = konut_kaynaklar + items
        if items:
            kategoriler.append((k, v, items))

    if aktif_kat == 'konut':
        filtered_list = konut_kaynaklar + list(base_qs.filter(kategori='konut'))
    elif aktif_kat:
        filtered_list = list(base_qs.filter(kategori=aktif_kat))
    else:
        filtered_list = list(base_qs)

    return render(request, 'rehber/belgeler.html', {
        'belgeler':          filtered_list,
        'kategoriler':       kategoriler,
        'belge_kategoriler': BELGE_KATEGORI,
        'aktif_kat':         aktif_kat,
        'stadt':             stadt,
        'eyalet_slug':       eyalet_slug if stadt else '',
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
