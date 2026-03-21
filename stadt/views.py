from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Stadt
from duyurular.models import Duyuru
from blog.models import BlogYazisi
from ilan.models import Ilan
from takvim.models import Etkinlik
from django.utils import timezone


def home(request, stadt_slug):
    stadt = get_object_or_404(Stadt, slug=stadt_slug, aktiv=True)

    son_duyurular = Duyuru.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        yayinda=True
    ).order_by('-olusturulma')[:4]

    son_yazilar = BlogYazisi.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        yayinda=True
    ).order_by('-olusturulma')[:3]

    son_ilanlar = Ilan.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        aktif=True, onaylandi=True
    ).order_by('-olusturulma')[:4]

    yaklasan = Etkinlik.objects.filter(
        Q(stadt=stadt, scope='stadt') | Q(scope='eyalet'),
        tarih__gte=timezone.now().date()
    ).order_by('tarih')[:3]

    return render(request, 'stadt/home.html', {
        'stadt': stadt,
        'son_duyurular': son_duyurular,
        'son_yazilar': son_yazilar,
        'son_ilanlar': son_ilanlar,
        'yaklasan': yaklasan,
    })
