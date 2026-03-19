from django.shortcuts import render
from .models import OnemliLink, LINK_KATEGORI

def liste(request):
    kategori = request.GET.get('kategori', '')
    kategoriler = {}
    for k, v in LINK_KATEGORI:
        linkler = OnemliLink.objects.filter(aktif=True, kategori=k)
        if linkler.exists():
            kategoriler[k] = {'ad': v, 'linkler': linkler}
    return render(request, 'linkler/liste.html', {
        'kategoriler': kategoriler,
        'tum_kategoriler': LINK_KATEGORI,
    })
