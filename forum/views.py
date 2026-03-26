from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import ForumKategori, Konu, Yorum
from accounts.utils import email_dogrulandi_mi, dogrulama_maili_gonder


def liste(request, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    kategoriler_qs = ForumKategori.objects.all()

    if stadt:
        kategoriler = []
        for kat in kategoriler_qs:
            konular = Konu.objects.filter(
                stadt=stadt, scope='stadt', kategori=kat
            ).order_by('-sabitlendi', '-guncelleme')
            kategoriler.append({'kategori': kat, 'konular': konular})
    else:
        kategoriler = [
            {
                'kategori': kat,
                'konular': Konu.objects.filter(
                    scope='eyalet', eyalet__slug=eyalet_slug, kategori=kat
                ).order_by('-sabitlendi', '-guncelleme')
            }
            for kat in kategoriler_qs
        ]

    return render(request, 'forum/liste.html', {
        'kategoriler':  kategoriler,
        'stadt':        stadt,
        'eyalet_slug':  eyalet_slug,
    })


def konu_detay(request, pk, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt
    konu = get_object_or_404(Konu, pk=pk)
    yorumlar = konu.yorumlar.select_related('yazar').all()
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'forum/konu.html', {
        'konu':        konu,
        'yorumlar':    yorumlar,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })


@login_required
def yorum_ekle(request, pk, eyalet_slug='rlp', stadt_slug=None):
    konu = get_object_or_404(Konu, pk=pk)
    if not konu.kapali and request.method == 'POST':
        if not email_dogrulandi_mi(request.user):
            dogrulama_maili_gonder(request, request.user)
            messages.error(request, 'Yorum yapabilmek için e-posta adresinizi doğrulamanız gerekiyor. Doğrulama bağlantısı e-postanıza gönderildi.')
            if stadt_slug:
                return redirect(f'/{eyalet_slug}/{stadt_slug}/forum/konu/{pk}/')
            return redirect(f'/{eyalet_slug}/forum/konu/{pk}/')
        Yorum.objects.create(konu=konu, yazar=request.user, icerik=request.POST['icerik'])
    if stadt_slug:
        return redirect(f'/{eyalet_slug}/{stadt_slug}/forum/konu/{pk}/')
    return redirect(f'/{eyalet_slug}/forum/konu/{pk}/')


@login_required
def konu_ac(request, kategori_pk, eyalet_slug='rlp', stadt_slug=None):
    from stadt.models import Stadt, Eyalet
    kategori = get_object_or_404(ForumKategori, pk=kategori_pk)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if not email_dogrulandi_mi(request.user):
        dogrulama_maili_gonder(request, request.user)
        messages.error(request, 'Konu açabilmek için e-posta adresinizi doğrulamanız gerekiyor. Doğrulama bağlantısı e-postanıza gönderildi.')
        return redirect('account_email')

    if request.method == 'POST':
        eyalet = Eyalet.objects.filter(slug=eyalet_slug).first()
        konu = Konu.objects.create(
            kategori=kategori,
            yazar=request.user,
            baslik=request.POST['baslik'],
            icerik=request.POST['icerik'],
            stadt=stadt,
            eyalet=eyalet,
            scope='stadt' if stadt else 'eyalet',
        )
        messages.success(request, 'Konu açıldı.')
        if stadt_slug:
            return redirect(f'/{eyalet_slug}/{stadt_slug}/forum/konu/{konu.pk}/')
        return redirect(f'/{eyalet_slug}/forum/konu/{konu.pk}/')

    return render(request, 'forum/konu_ac.html', {
        'kategori':    kategori,
        'stadt':       stadt,
        'eyalet_slug': eyalet_slug,
    })
