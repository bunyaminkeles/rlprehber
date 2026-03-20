import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import engine


def liste(request):
    """Konu seçim sayfası."""
    konular = engine.konu_listesi()
    return render(request, 'almanca/liste.html', {'konular': konular})


def quiz(request, slug):
    """Bir soruyu göster; oturum sıfırlama desteği."""
    bilgi = engine.konu_bilgi(slug)
    if not bilgi:
        from django.http import Http404
        raise Http404

    thema, tr = bilgi

    if request.GET.get('sifirla'):
        request.session.pop(f'alm_gorulmus_{slug}', None)
        request.session.pop(f'alm_dogru_{slug}', None)
        request.session.pop(f'alm_yanlis_{slug}', None)
        return redirect('almanca:quiz', slug=slug)

    gorulmus = request.session.get(f'alm_gorulmus_{slug}', [])
    dogru_sayi = request.session.get(f'alm_dogru_{slug}', 0)
    yanlis_sayi = request.session.get(f'alm_yanlis_{slug}', 0)
    toplam = engine.soru_sayisi(slug)

    soru = engine.rastgele_soru(slug, gorulmus)

    if soru is None:
        return render(request, 'almanca/bitti.html', {
            'slug': slug,
            'thema': thema,
            'tr': tr,
            'dogru': dogru_sayi,
            'yanlis': yanlis_sayi,
            'toplam': toplam,
        })

    request.session[f'alm_soru_{slug}'] = {
        'uid': soru.uid,
        'dogru_harf': soru.dogru_harf,
        'erklaerung': soru.erklaerung,
    }

    return render(request, 'almanca/quiz.html', {
        'slug': slug,
        'thema': thema,
        'tr': tr,
        'soru': soru,
        'gorulmus': len(gorulmus),
        'toplam': toplam,
        'dogru': dogru_sayi,
        'yanlis': yanlis_sayi,
    })


@require_POST
def cevapla(request, slug):
    """AJAX: kullanıcının cevabını kontrol et, JSON döndür."""
    if not engine.konu_bilgi(slug):
        from django.http import Http404
        raise Http404

    veri = json.loads(request.body)
    secilen = veri.get('harf', '').upper()

    kayit = request.session.get(f'alm_soru_{slug}')
    if not kayit:
        return JsonResponse({'hata': 'Oturum bulunamadı.'}, status=400)

    dogru_harf = kayit['dogru_harf']
    erklaerung = kayit['erklaerung']
    uid = kayit['uid']

    gorulmus = request.session.get(f'alm_gorulmus_{slug}', [])
    if uid not in gorulmus:
        gorulmus.append(uid)
        request.session[f'alm_gorulmus_{slug}'] = gorulmus

    if secilen == dogru_harf:
        request.session[f'alm_dogru_{slug}'] = request.session.get(f'alm_dogru_{slug}', 0) + 1
        durum = 'dogru'
    else:
        request.session[f'alm_yanlis_{slug}'] = request.session.get(f'alm_yanlis_{slug}', 0) + 1
        durum = 'yanlis'

    request.session.modified = True

    return JsonResponse({
        'durum': durum,
        'dogru_harf': dogru_harf,
        'erklaerung': erklaerung,
    })
