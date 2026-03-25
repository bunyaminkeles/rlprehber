from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Duyuru
from accounts.utils import email_dogrulandi_mi


def _kapsam_filtresi(stadt):
    if stadt:
        return Q(stadt=stadt, scope='stadt') | Q(scope='eyalet')
    return Q(scope='eyalet')


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    temel = Duyuru.objects.filter(_kapsam_filtresi(stadt), yayinda=True)

    konsolosluk = temel.filter(kaynak_tipi='konsolosluk').order_by('-olusturulma')[:20]
    belediye    = temel.filter(kaynak_tipi='belediye').order_by('-olusturulma')[:20] if stadt else []
    kullanici   = temel.filter(kaynak_tipi='kullanici').order_by('-olusturulma')[:20]

    return render(request, 'duyurular/liste.html', {
        'konsolosluk': konsolosluk,
        'belediye':    belediye,
        'kullanici':   kullanici,
        'stadt':       stadt,
    })


@login_required
def duyuru_ekle(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if request.method == 'POST':
        if not email_dogrulandi_mi(request.user):
            messages.error(request, 'Duyuru eklemek için e-posta adresinizi doğrulamanız gerekiyor.')
            return redirect('account_email')

        baslik = request.POST.get('baslik', '').strip()
        icerik = request.POST.get('icerik', '').strip()
        if not baslik or not icerik:
            messages.error(request, 'Başlık ve içerik zorunludur.')
        else:
            Duyuru.objects.create(
                yazar=request.user,
                kaynak_tipi='kullanici',
                baslik=baslik,
                icerik=icerik,
                resim=request.FILES.get('resim'),
                kategori='genel',
                stadt=stadt,
                scope='stadt' if stadt else 'eyalet',
                yayinda=False,
            )
            messages.success(request, 'Duyurunuz alındı, inceleme sonrası yayınlanacaktır.')
        if stadt_slug:
            return redirect('duyurular:liste', stadt_slug=stadt_slug)
        return redirect('duyurular:liste')

    return render(request, 'duyurular/duyuru_ekle.html', {'stadt': stadt})


def detay(request, pk, stadt_slug=None):
    from stadt.models import Stadt
    duyuru = get_object_or_404(Duyuru, pk=pk, yayinda=True)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'duyurular/detay.html', {
        'duyuru': duyuru,
        'stadt': stadt,
    })
