from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from stadt.models import Stadt
from duyurular.models import Duyuru
from ilan.models import Ilan
from takvim.models import Etkinlik
from forum.models import Konu
from ilan.models import SATILIK_KATEGORILER, ARANIYOR_KATEGORILER


def anasayfa(request):
    """Ana sayfa: son forum konuları ve ilanlar widget'ları."""
    sehirler = Stadt.objects.filter(aktiv=True)
    son_konular = (
        Konu.objects
        .select_related('stadt', 'yazar')
        .order_by('-olusturulma')[:8]
    )
    son_satilik = (
        Ilan.objects
        .filter(aktif=True, kategori__in=SATILIK_KATEGORILER)
        .select_related('stadt')
        .order_by('-olusturulma')[:5]
    )
    son_araniyor = (
        Ilan.objects
        .filter(aktif=True, kategori__in=ARANIYOR_KATEGORILER)
        .select_related('stadt')
        .order_by('-olusturulma')[:5]
    )
    return render(request, 'core/anasayfa.html', {
        'sehirler': sehirler,
        'son_konular': son_konular,
        'son_satilik': son_satilik,
        'son_araniyor': son_araniyor,
    })


def hakkinda(request):
    from .models import Oneri
    gonderildi = False
    if request.method == 'POST':
        Oneri.objects.create(
            tur=request.POST.get('tur', 'oneri'),
            ad=request.POST.get('ad', '').strip(),
            eposta=request.POST.get('eposta', '').strip(),
            mesaj=request.POST.get('mesaj', '').strip(),
        )
        gonderildi = True
    return render(request, 'core/hakkinda.html', {'gonderildi': gonderildi})


def iletisim(request):
    return render(request, 'core/iletisim.html')


@login_required
def dashboard(request):
    son_duyurular = Duyuru.objects.filter(yayinda=True).order_by('-olusturulma')[:5]
    yaklasan = Etkinlik.objects.filter(tarih__gte=timezone.now().date()).order_by('tarih')[:5]
    benim_ilanim = Ilan.objects.filter(sahip=request.user).order_by('-olusturulma')[:5]
    return render(request, 'core/dashboard.html', {
        'son_duyurular': son_duyurular,
        'yaklasan': yaklasan,
        'benim_ilanim': benim_ilanim,
    })
