from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Duyuru
from accounts.utils import email_dogrulandi_mi, dogrulama_maili_gonder


def _kapsam_filtresi(stadt, eyalet_slug):
    if stadt:
        return Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug)
    return Q(scope='eyalet', eyalet__slug=eyalet_slug)


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    temel = Duyuru.objects.filter(_kapsam_filtresi(stadt, eyalet_slug), yayinda=True)

    konsolosluk = temel.filter(kaynak_tipi='konsolosluk').order_by('-olusturulma')[:20]
    belediye    = temel.filter(kaynak_tipi='belediye').order_by('-olusturulma')[:20] if stadt else []
    kullanici   = temel.filter(kaynak_tipi='kullanici').order_by('-olusturulma')[:20]

    return render(request, 'duyurular/liste.html', {
        'konsolosluk':  konsolosluk,
        'belediye':     belediye,
        'kullanici':    kullanici,
        'stadt':        stadt,
        'eyalet_slug':  eyalet_slug,
    })


@login_required
def duyuru_ekle(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if not email_dogrulandi_mi(request.user):
        dogrulama_maili_gonder(request, request.user)
        messages.error(request, 'Duyuru eklemek için e-posta adresinizi doğrulamanız gerekiyor. Doğrulama bağlantısı e-postanıza gönderildi.')
        return redirect('account_email')

    if request.method == 'POST':

        baslik = request.POST.get('baslik', '').strip()
        icerik = request.POST.get('icerik', '').strip()
        if not baslik or not icerik:
            messages.error(request, 'Başlık ve içerik zorunludur.')
        else:
            from stadt.models import Eyalet
            eyalet = Eyalet.objects.filter(slug=eyalet_slug).first()
            Duyuru.objects.create(
                yazar=request.user,
                kaynak_tipi='kullanici',
                baslik=baslik,
                icerik=icerik,
                resim=request.FILES.get('resim'),
                kategori='genel',
                stadt=stadt,
                eyalet=eyalet,
                scope='stadt' if stadt else 'eyalet',
                yayinda=False,
            )
            messages.success(request, 'Duyurunuz alındı, inceleme sonrası yayınlanacaktır.')

        if stadt_slug:
            return redirect(f'/{eyalet_slug}/{stadt_slug}/duyurular/')
        return redirect(f'/{eyalet_slug}/duyurular/')

    return render(request, 'duyurular/duyuru_ekle.html', {
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })


def detay(request, pk, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    duyuru = get_object_or_404(Duyuru, pk=pk, yayinda=True)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'duyurular/detay.html', {
        'duyuru':      duyuru,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })
