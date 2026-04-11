from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from .models import Duyuru
from accounts.utils import email_dogrulandi_mi, dogrulama_maili_gonder


def _kapsam_filtresi(stadt, eyalet_slug):
    almanya_geneli = Q(scope='genel')
    if stadt:
        return Q(stadt=stadt, scope='stadt') | Q(scope='eyalet', eyalet__slug=eyalet_slug) | almanya_geneli
    return Q(scope='eyalet', eyalet__slug=eyalet_slug) | almanya_geneli


def _form_context():
    from stadt.models import Eyalet, Stadt
    eyaletler = Eyalet.objects.filter(aktif=True).order_by('ad')
    sehirler  = Stadt.objects.filter(aktiv=True).select_related('eyalet').order_by('name')
    return eyaletler, sehirler


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    bugun = timezone.localdate()
    temel = Duyuru.objects.filter(_kapsam_filtresi(stadt, eyalet_slug), yayinda=True, yayin_bitis__gte=bugun)

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


def liste_almanya(request):
    bugun = timezone.localdate()
    temel = Duyuru.objects.filter(yayinda=True, yayin_bitis__gte=bugun)

    konsolosluk = temel.filter(kaynak_tipi='konsolosluk').order_by('-olusturulma')[:20]
    kullanici   = temel.filter(kaynak_tipi='kullanici').order_by('-olusturulma')[:20]

    return render(request, 'duyurular/liste.html', {
        'konsolosluk': konsolosluk,
        'belediye':    [],
        'kullanici':   kullanici,
        'stadt':       None,
        'eyalet_slug': None,
        'almanya_geneli': True,
    })


def _duyuru_ekle_post(request, geri_url, varsayilan_eyalet_slug=None, varsayilan_stadt=None):
    from stadt.models import Eyalet, Stadt
    baslik      = request.POST.get('baslik', '').strip()
    icerik      = request.POST.get('icerik', '').strip()
    yayin_bitis = request.POST.get('yayin_bitis', '').strip()
    scope       = request.POST.get('scope', 'genel')

    if scope not in ('genel', 'eyalet', 'stadt'):
        scope = 'genel'

    if not baslik or not icerik:
        messages.error(request, 'Başlık ve içerik zorunludur.')
        return False
    if not yayin_bitis:
        messages.error(request, 'Yayın bitiş tarihi zorunludur.')
        return False
    if scope == 'stadt' and not request.POST.get('stadt_id'):
        messages.error(request, 'Şehre özel duyuru için şehir seçiniz.')
        return False
    if scope == 'eyalet' and not request.POST.get('eyalet_id'):
        messages.error(request, 'Eyalet geneli duyuru için eyalet seçiniz.')
        return False

    eyalet = None
    stadt  = None
    if scope == 'stadt':
        stadt  = Stadt.objects.filter(pk=request.POST.get('stadt_id'), aktiv=True).first()
        eyalet = stadt.eyalet if stadt else None
    elif scope == 'eyalet':
        eyalet = Eyalet.objects.filter(pk=request.POST.get('eyalet_id'), aktif=True).first()

    Duyuru.objects.create(
        yazar=request.user,
        kaynak_tipi='kullanici',
        baslik=baslik,
        icerik=icerik,
        resim=request.FILES.get('resim'),
        kategori='genel',
        scope=scope,
        eyalet=eyalet,
        stadt=stadt,
        yayinda=False,
        yayin_bitis=yayin_bitis,
    )
    messages.success(request, 'Duyurunuz alındı, inceleme sonrası yayınlanacaktır.')
    return True


@login_required
def duyuru_ekle(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt_ctx = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if not email_dogrulandi_mi(request.user):
        dogrulama_maili_gonder(request, request.user)
        messages.error(request, 'Duyuru eklemek için e-posta adresinizi doğrulamanız gerekiyor. Doğrulama bağlantısı e-postanıza gönderildi.')
        return redirect('account_email')

    if stadt_slug:
        geri_url = f'/{eyalet_slug}/{stadt_slug}/duyurular/'
    else:
        geri_url = f'/{eyalet_slug}/duyurular/'

    if request.method == 'POST':
        if _duyuru_ekle_post(request, geri_url):
            return redirect(geri_url)

    eyaletler, sehirler = _form_context()
    return render(request, 'duyurular/duyuru_ekle.html', {
        'stadt':               stadt_ctx,
        'eyalet_slug':         eyalet_slug,
        'geri_url':            geri_url,
        'eyaletler':           eyaletler,
        'sehirler':            sehirler,
        'varsayilan_scope':    'stadt' if stadt_slug else 'eyalet' if eyalet_slug else 'genel',
        'varsayilan_eyalet_id': stadt_ctx.eyalet_id if stadt_ctx else None,
        'varsayilan_stadt_id':  stadt_ctx.pk if stadt_ctx else None,
    })


@login_required
def duyuru_ekle_almanya(request):
    if not email_dogrulandi_mi(request.user):
        dogrulama_maili_gonder(request, request.user)
        messages.error(request, 'Duyuru eklemek için e-posta adresinizi doğrulamanız gerekiyor. Doğrulama bağlantısı e-postanıza gönderildi.')
        return redirect('account_email')

    geri_url = '/almanya/duyurular/'
    if request.method == 'POST':
        if _duyuru_ekle_post(request, geri_url):
            return redirect(geri_url)

    eyaletler, sehirler = _form_context()
    return render(request, 'duyurular/duyuru_ekle.html', {
        'stadt':              None,
        'eyalet_slug':        None,
        'geri_url':           geri_url,
        'eyaletler':          eyaletler,
        'sehirler':           sehirler,
        'varsayilan_scope':   'genel',
        'varsayilan_eyalet_id': None,
        'varsayilan_stadt_id':  None,
        'almanya_geneli':     True,
    })


def detay(request, pk, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    bugun = timezone.localdate()
    duyuru = get_object_or_404(Duyuru, pk=pk, yayinda=True, yayin_bitis__gte=bugun)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'duyurular/detay.html', {
        'duyuru':      duyuru,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })
