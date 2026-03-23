from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import ForumKategori, Konu, Yorum
from accounts.utils import email_dogrulandi_mi


def liste(request, stadt_slug=None):
    from stadt.models import Stadt
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    # Kategoriler eyalet geneli — her şehirde aynı
    kategoriler_qs = ForumKategori.objects.all()

    if stadt:
        # Sadece o şehre özel konular
        kategoriler = []
        for kat in kategoriler_qs:
            konular = Konu.objects.filter(
                stadt=stadt, scope='stadt', kategori=kat
            ).order_by('-sabitlendi', '-guncelleme')
            kategoriler.append({'kategori': kat, 'konular': konular})
    else:
        # RLP geneli — sadece eyalet scope
        kategoriler = [
            {'kategori': kat, 'konular': Konu.objects.filter(scope='eyalet', kategori=kat).order_by('-sabitlendi', '-guncelleme')}
            for kat in kategoriler_qs
        ]

    return render(request, 'forum/liste.html', {
        'kategoriler': kategoriler,
        'stadt': stadt,
    })


def konu_detay(request, pk, stadt_slug=None):
    from stadt.models import Stadt
    konu = get_object_or_404(Konu, pk=pk)
    yorumlar = konu.yorumlar.select_related('yazar').all()
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None
    return render(request, 'forum/konu.html', {
        'konu': konu,
        'yorumlar': yorumlar,
        'stadt': stadt,
    })


@login_required
def yorum_ekle(request, pk, stadt_slug=None):
    konu = get_object_or_404(Konu, pk=pk)
    if not konu.kapali and request.method == 'POST':
        if not email_dogrulandi_mi(request.user):
            messages.error(request, 'Yorum yapabilmek için e-posta adresinizi doğrulamanız gerekiyor.')
            if stadt_slug:
                return redirect('forum:konu', pk=pk, stadt_slug=stadt_slug)
            return redirect('forum:konu', pk=pk)
        Yorum.objects.create(konu=konu, yazar=request.user, icerik=request.POST['icerik'])
    if stadt_slug:
        return redirect('forum:konu', pk=pk, stadt_slug=stadt_slug)
    return redirect('forum:konu', pk=pk)


@login_required
def konu_ac(request, kategori_pk, stadt_slug=None):
    from stadt.models import Stadt
    kategori = get_object_or_404(ForumKategori, pk=kategori_pk)
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True) if stadt_slug else None

    if request.method == 'POST':
        if not email_dogrulandi_mi(request.user):
            messages.error(request, 'Konu açabilmek için e-posta adresinizi doğrulamanız gerekiyor.')
            return redirect('account_email')
        konu = Konu.objects.create(
            kategori=kategori,
            yazar=request.user,
            baslik=request.POST['baslik'],
            icerik=request.POST['icerik'],
            stadt=stadt,
            scope='stadt' if stadt else 'eyalet',
        )
        messages.success(request, 'Konu açıldı.')
        if stadt_slug:
            return redirect('forum:konu', pk=konu.pk, stadt_slug=stadt_slug)
        return redirect('forum:konu', pk=konu.pk)

    return render(request, 'forum/konu_ac.html', {
        'kategori': kategori,
        'stadt': stadt,
    })
