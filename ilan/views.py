from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Ilan, ILAN_KATEGORI, SATILIK_KATEGORILER, ARANIYOR_KATEGORILER
from linkler.models import OnemliLink
from accounts.utils import email_dogrulandi_mi


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    kategori = request.GET.get('kategori', '')

    if stadt:
        qs = Ilan.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            aktif=True, onaylandi=True
        )
    else:
        qs = Ilan.objects.filter(aktif=True, onaylandi=True)

    if kategori:
        qs = qs.filter(kategori=kategori)

    satilik  = qs.filter(kategori__in=SATILIK_KATEGORILER)
    araniyor = qs.filter(kategori__in=ARANIYOR_KATEGORILER)

    if stadt:
        platformlar = OnemliLink.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
            kategori='ilan', aktif=True
        ).order_by('sira')
    else:
        platformlar = OnemliLink.objects.filter(kategori='ilan', aktif=True).order_by('sira')

    return render(request, 'ilan/liste.html', {
        'satilik':              satilik,
        'araniyor':             araniyor,
        'kategoriler':          ILAN_KATEGORI,
        'satilik_kategoriler':  [k for k in ILAN_KATEGORI if k[0] in SATILIK_KATEGORILER],
        'araniyor_kategoriler': [k for k in ILAN_KATEGORI if k[0] in ARANIYOR_KATEGORILER],
        'secili':               kategori,
        'platformlar':          platformlar,
        'stadt':                stadt,
    })


def detay(request, pk, stadt_slug=None):
    from stadt.models import Stadt
    ilan = get_object_or_404(Ilan, pk=pk, aktif=True, onaylandi=True)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'ilan/detay.html', {
        'ilan': ilan,
        'stadt': stadt,
    })


@login_required
def ilan_ver(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if request.method == 'POST':
        if not email_dogrulandi_mi(request.user):
            messages.error(request, 'İlan verebilmek için e-posta adresinizi doğrulamanız gerekiyor.')
            return redirect('account_email')
        ilan = Ilan(
            sahip=request.user,
            baslik=request.POST['baslik'],
            icerik=request.POST['icerik'],
            kategori=request.POST['kategori'],
            iletisim=request.POST['iletisim'],
            stadt=stadt,
            scope='stadt' if stadt else 'eyalet',
        )
        fiyat = request.POST.get('fiyat')
        if fiyat:
            ilan.fiyat = fiyat
        ilan.save()
        messages.success(request, 'İlanınız alındı, inceleme sonrası yayınlanacaktır.')
        if stadt_slug:
            return redirect('ilan:liste', stadt_slug=stadt_slug)
        return redirect('ilan:liste')


    return render(request, 'ilan/ilan_ver.html', {
        'kategoriler': ILAN_KATEGORI,
        'stadt': stadt,
    })
