from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import Konusma, Mesaj
from accounts.utils import email_dogrulandi_mi


@login_required
def gelen_kutusu(request):
    konusmalar = Konusma.objects.filter(
        Q(taraf1=request.user) | Q(taraf2=request.user)
    ).prefetch_related('mesajlar').order_by('-olusturulma')

    # Her konuşma için okunmamış mesaj sayısı
    konusma_listesi = []
    for k in konusmalar:
        okunmamis = k.mesajlar.filter(okundu=False).exclude(gonderen=request.user).count()
        konusma_listesi.append({
            'konusma': k,
            'diger': k.diger_taraf(request.user),
            'son_mesaj': k.son_mesaj(),
            'okunmamis': okunmamis,
        })

    return render(request, 'mesajlar/gelen_kutusu.html', {
        'konusma_listesi': konusma_listesi,
    })


@login_required
def konusma_detay(request, pk):
    konusma = get_object_or_404(
        Konusma, pk=pk
    )
    # Sadece konuşmanın tarafları görebilir
    if request.user not in (konusma.taraf1, konusma.taraf2):
        messages.error(request, 'Bu konuşmaya erişim izniniz yok.')
        return redirect('mesajlar:gelen_kutusu')

    # Okunmamış mesajları okundu olarak işaretle
    konusma.mesajlar.filter(okundu=False).exclude(gonderen=request.user).update(okundu=True)

    if request.method == 'POST':
        if not email_dogrulandi_mi(request.user):
            messages.error(request, 'Mesaj göndermek için e-posta adresinizi doğrulamanız gerekiyor.')
            return redirect('mesajlar:konusma', pk=pk)
        icerik = request.POST.get('icerik', '').strip()
        if icerik:
            Mesaj.objects.create(konusma=konusma, gonderen=request.user, icerik=icerik)
        return redirect('mesajlar:konusma', pk=pk)

    diger = konusma.diger_taraf(request.user)
    return render(request, 'mesajlar/konusma.html', {
        'konusma': konusma,
        'mesajlar': konusma.mesajlar.all(),
        'diger': diger,
    })


@login_required
def mesaj_baslat(request, kullanici_adi):
    if not email_dogrulandi_mi(request.user):
        messages.error(request, 'Mesaj göndermek için e-posta adresinizi doğrulamanız gerekiyor.')
        return redirect('account_email')

    alici = get_object_or_404(User, username=kullanici_adi)
    if alici == request.user:
        messages.error(request, 'Kendinize mesaj gönderemezsiniz.')
        return redirect('mesajlar:gelen_kutusu')

    konusma = Konusma.al_veya_olustur(request.user, alici)
    return redirect('mesajlar:konusma', pk=konusma.pk)


def okunmamis_sayi(user):
    """Navbar badge için okunmamış mesaj sayısı."""
    if not user.is_authenticated:
        return 0
    return Mesaj.objects.filter(
        konusma__in=Konusma.objects.filter(Q(taraf1=user) | Q(taraf2=user)),
        okundu=False
    ).exclude(gonderen=user).count()


@login_required
def mesajlar_api(request, pk):
    """AJAX polling: son_id'den büyük yeni mesajları JSON olarak döndür."""
    from django.http import JsonResponse
    konusma = get_object_or_404(Konusma, pk=pk)
    if request.user not in (konusma.taraf1, konusma.taraf2):
        return JsonResponse({'hata': 'Erişim yok'}, status=403)

    son_id = int(request.GET.get('son_id', 0))
    yeni = konusma.mesajlar.filter(pk__gt=son_id).values(
        'pk', 'icerik', 'olusturulma', 'gonderen__username', 'okundu'
    )
    # Gelen mesajları okundu yap
    konusma.mesajlar.filter(pk__gt=son_id, okundu=False).exclude(gonderen=request.user).update(okundu=True)

    return JsonResponse({
        'mesajlar': [
            {
                'pk': m['pk'],
                'icerik': m['icerik'],
                'zaman': m['olusturulma'].strftime('%H:%M'),
                'gonderen': m['gonderen__username'],
                'benim': m['gonderen__username'] == request.user.username,
            }
            for m in yeni
        ]
    })
