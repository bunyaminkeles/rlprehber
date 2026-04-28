from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
import json
from .models import Profil # noqa
from ilan.models import Ilan
from takvim.models import Etkinlik
from duyurular.models import Duyuru
from forum.models import Konu
from blog.models import BlogYazisi

@login_required
def dashboard(request):
    from stadt.models import Stadt
    profil, _ = Profil.objects.get_or_create(kullanici=request.user)

    # Kullanıcının profil şehriyle eşleştir, bulamazsa Mainz, o da yoksa ilk aktif şehir
    stadt = None
    if profil.sehir:
        stadt = Stadt.objects.select_related('eyalet').filter(name__iexact=profil.sehir, aktiv=True).first()
    if not stadt:
        stadt = Stadt.objects.select_related('eyalet').filter(slug='mainz', aktiv=True).first()
    if not stadt:
        stadt = Stadt.objects.select_related('eyalet').filter(aktiv=True).first()

    bugun = timezone.now().date()
    duyuru_sayisi   = Duyuru.objects.filter(yayinda=True).count()
    etkinlik_sayisi = Etkinlik.objects.filter(tarih__gte=bugun).count()
    ilan_sayisi     = Ilan.objects.filter(sahip=request.user, aktif=True).count()

    son_duyurular   = Duyuru.objects.filter(yayinda=True).order_by('-olusturulma')[:5]
    yaklasan        = Etkinlik.objects.filter(tarih__gte=bugun).order_by('tarih')[:5]
    benim_ilanim    = Ilan.objects.filter(sahip=request.user).order_by('-olusturulma')[:5]
    son_konular     = Konu.objects.select_related('yazar', 'kategori').order_by('-guncelleme')[:5]
    son_bloglar     = BlogYazisi.objects.filter(yayinda=True).order_by('-olusturulma')[:3]
    benim_konularim = Konu.objects.filter(yazar=request.user).count()
    eyalet_slug     = stadt.eyalet.slug if stadt and stadt.eyalet else 'rlp'
    return render(request, 'core/dashboard.html', {
        'profil': profil,
        'stadt': stadt,
        'eyalet_slug': eyalet_slug,
        'duyuru_sayisi': duyuru_sayisi,
        'etkinlik_sayisi': etkinlik_sayisi,
        'ilan_sayisi': ilan_sayisi,
        'son_duyurular': son_duyurular,
        'yaklasan': yaklasan,
        'benim_ilanim': benim_ilanim,
        'son_konular': son_konular,
        'son_bloglar': son_bloglar,
        'benim_konularim': benim_konularim,
    })

@login_required
def profil(request):
    from stadt.models import Stadt
    p, _ = Profil.objects.get_or_create(kullanici=request.user)
    if request.method == 'POST':
        p.biyografi       = request.POST.get('biyografi', '')
        p.sehir           = request.POST.get('sehir', '')
        p.biyografi_gizli = 'biyografi_gizli' in request.POST
        p.sehir_gizli     = 'sehir_gizli' in request.POST
        p.save()
        return redirect('accounts:dashboard')
    sehirler = Stadt.objects.filter(aktiv=True).order_by('name')
    sehir_adlari = list(sehirler.values_list('name', flat=True))
    return render(request, 'accounts/profil.html', {
        'profil': p,
        'sehirler': sehirler,
        'sehir_adlari': sehir_adlari,
    })


def kullanici_listesi(request):
    q = request.GET.get('q', '').strip()
    kullanicilar = User.objects.filter(is_active=True).select_related('profil').order_by('username')
    if q:
        kullanicilar = kullanicilar.filter(username__icontains=q)
    return render(request, 'accounts/kullanici_listesi.html', {
        'kullanicilar': kullanicilar,
        'q': q,
    })


def kullanici_profil(request, kullanici_adi):
    hedef = get_object_or_404(User, username=kullanici_adi, is_active=True)
    profil, _ = Profil.objects.get_or_create(kullanici=hedef)
    return render(request, 'accounts/kullanici_profil.html', {
        'hedef': hedef,
        'profil': profil,
    })


@login_required
@require_POST
def toggle_task_completion(request):
    """
    Kullanıcının profilindeki görev tamamlama durumunu günceller.
    """
    try:
        data = json.loads(request.body)
        task_slug = data.get('task_slug')
        is_completed = data.get('is_completed')

        if not task_slug or is_completed is None:
            return JsonResponse({'success': False, 'message': 'Eksik veri.'}, status=400)

        profile = request.user.profil
        if is_completed and task_slug not in profile.completed_tasks:
            profile.completed_tasks.append(task_slug)
        elif not is_completed and task_slug in profile.completed_tasks:
            profile.completed_tasks.remove(task_slug)
        profile.save()
        return JsonResponse({'success': True, 'completed_tasks': profile.completed_tasks})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Geçersiz JSON.'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)
