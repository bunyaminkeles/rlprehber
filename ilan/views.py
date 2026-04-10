from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse
from .models import Ilan, IlanYorum, ILAN_KATEGORI, SATILIK_KATEGORILER, ARANIYOR_KATEGORILER
from rehber.models import Kaynak
from accounts.utils import email_dogrulandi_mi, dogrulama_maili_gonder


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    kategori = request.GET.get('kategori', '')

    bugun = timezone.localdate()
    if stadt:
        qs = Ilan.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug),
            aktif=True, onaylandi=True, yayin_bitis__gte=bugun
        )
    else:
        qs = Ilan.objects.filter(scope='eyalet', eyalet__slug=eyalet_slug, aktif=True, onaylandi=True, yayin_bitis__gte=bugun)

    if kategori:
        qs = qs.filter(kategori=kategori)

    satilik  = qs.filter(kategori__in=SATILIK_KATEGORILER)
    araniyor = qs.filter(kategori__in=ARANIYOR_KATEGORILER)

    if stadt:
        platformlar = Kaynak.objects.filter(
            Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug),
            kategori='ilan', yayinda=True, tip='link'
        ).order_by('sira')
    else:
        platformlar = Kaynak.objects.filter(
            scope='eyalet', eyalet__slug=eyalet_slug, kategori='ilan', yayinda=True, tip='link'
        ).order_by('sira')

    return render(request, 'ilan/liste.html', {
        'satilik':              satilik,
        'araniyor':             araniyor,
        'kategoriler':          ILAN_KATEGORI,
        'satilik_kategoriler':  [k for k in ILAN_KATEGORI if k[0] in SATILIK_KATEGORILER],
        'araniyor_kategoriler': [k for k in ILAN_KATEGORI if k[0] in ARANIYOR_KATEGORILER],
        'secili':               kategori,
        'platformlar':          platformlar,
        'stadt':                stadt,
        'eyalet_slug':          eyalet_slug,
    })


def detay_json(request, pk, eyalet_slug='rlp', stadt_slug=None):
    """Offcanvas için ilan detayını JSON olarak döner."""
    bugun = timezone.localdate()
    ilan = get_object_or_404(
        Ilan.objects.select_related('sahip', 'stadt', 'eyalet'),
        pk=pk, aktif=True, onaylandi=True, yayin_bitis__gte=bugun
    )
    data = {
        'baslik':    ilan.baslik,
        'icerik':    ilan.icerik,
        'kategori':  ilan.get_kategori_display(),
        'fiyat':     str(ilan.fiyat) if ilan.fiyat else '',
        'resim_url': ilan.resim.url if ilan.resim else '',
        'sahip':     ilan.sahip.get_full_name() or ilan.sahip.username,
        'tarih':     ilan.olusturulma.strftime('%d.%m.%Y'),
        'stadt':     ilan.stadt.name if ilan.stadt else '',
        'iletisim':  ilan.iletisim if request.user.is_authenticated else '',
    }
    return JsonResponse(data)


def detay(request, pk, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    bugun = timezone.localdate()
    ilan = get_object_or_404(Ilan, pk=pk, aktif=True, onaylandi=True, yayin_bitis__gte=bugun)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if request.method == 'POST' and request.user.is_authenticated:
        icerik = request.POST.get('icerik', '').strip()
        if icerik:
            IlanYorum.objects.create(ilan=ilan, yazar=request.user, icerik=icerik)
        return redirect(request.path)

    return render(request, 'ilan/detay.html', {
        'ilan':        ilan,
        'yorumlar':    ilan.yorumlar.select_related('yazar').all(),
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })


@login_required
def ilan_ver(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if not email_dogrulandi_mi(request.user):
        dogrulama_maili_gonder(request, request.user)
        messages.error(request, 'İlan verebilmek için e-posta adresinizi doğrulamanız gerekiyor. Doğrulama bağlantısı e-postanıza gönderildi.')
        return redirect('account_email')

    if request.method == 'POST':
        yayin_bitis = request.POST.get('yayin_bitis', '').strip()
        if not yayin_bitis:
            messages.error(request, 'Yayın bitiş tarihi zorunludur.')
            return render(request, 'ilan/ilan_ver.html', {
                'kategoriler': ILAN_KATEGORI,
                'stadt': stadt,
                'eyalet_slug': eyalet_slug,
            })
        from stadt.models import Eyalet
        eyalet = Eyalet.objects.filter(slug=eyalet_slug).first()
        ilan = Ilan(
            sahip=request.user,
            baslik=request.POST['baslik'],
            icerik=request.POST['icerik'],
            kategori=request.POST['kategori'],
            iletisim=request.POST['iletisim'],
            resim=request.FILES.get('resim'),
            stadt=stadt,
            eyalet=eyalet,
            scope='stadt' if stadt else 'eyalet',
            yayin_bitis=yayin_bitis,
        )
        fiyat = request.POST.get('fiyat')
        if fiyat:
            ilan.fiyat = fiyat
        ilan.save()
        messages.success(request, 'İlanınız alındı, inceleme sonrası yayınlanacaktır.')
        if stadt_slug:
            return redirect(f'/{eyalet_slug}/{stadt_slug}/ilan/')
        return redirect(f'/{eyalet_slug}/ilan/')

    return render(request, 'ilan/ilan_ver.html', {
        'kategoriler': ILAN_KATEGORI,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })
