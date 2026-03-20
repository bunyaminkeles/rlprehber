from django.shortcuts import render, get_object_or_404
from .models import Yer, YER_KATEGORI

def liste(request):
    kategori = request.GET.get('kategori', '')
    kategoriler = {}
    for k, v in YER_KATEGORI:
        if kategori and k != kategori:
            continue
        yerler = Yer.objects.filter(aktif=True, kategori=k)
        if yerler.exists():
            kategoriler[k] = {'ad': v, 'yerler': yerler}
    return render(request, 'yerler/liste.html', {
        'kategoriler': kategoriler,
        'secili': kategori,
        'tum_kategoriler': YER_KATEGORI,
    })

def detay(request, pk):
    yer = get_object_or_404(Yer, pk=pk, aktif=True)
    return render(request, 'yerler/detay.html', {'yer': yer})
