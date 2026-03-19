from django.shortcuts import render, get_object_or_404
from .models import Duyuru

def liste(request):
    kategori = request.GET.get('kategori', '')
    qs = Duyuru.objects.filter(yayinda=True).order_by('-id')
    if kategori:
        qs = qs.filter(kategori=kategori)
    return render(request, 'duyurular/liste.html', {'duyurular': qs[:10], 'secili': kategori})

def detay(request, pk):
    duyuru = get_object_or_404(Duyuru, pk=pk, yayinda=True)
    return render(request, 'duyurular/detay.html', {'duyuru': duyuru})
