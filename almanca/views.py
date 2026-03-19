import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import engine


def liste(request):
    """Konu seçim sayfası."""
    konular = engine.konu_listesi()
    return render(request, 'almanca/liste.html', {'konular': konular})


def quiz(request, thema):
    """Bir soruyu göster; oturum sıfırlama desteği."""
    if request.GET.get('sifirla'):
        request.session.pop(f'alm_gorulmus_{thema}', None)
        request.session.pop(f'alm_dogru_{thema}', None)
        request.session.pop(f'alm_yanlis_{thema}', None)
        return redirect('almanca:quiz', thema=thema)

    gorulmus = request.session.get(f'alm_gorulmus_{thema}', [])
    dogru_sayi = request.session.get(f'alm_dogru_{thema}', 0)
    yanlis_sayi = request.session.get(f'alm_yanlis_{thema}', 0)
    toplam = engine.soru_sayisi(thema)

    soru = engine.rastgele_soru(thema, gorulmus)

    if soru is None:
        return render(request, 'almanca/bitti.html', {
            'thema': thema,
            'tr': engine.KONU_TR.get(thema, thema),
            'dogru': dogru_sayi,
            'yanlis': yanlis_sayi,
            'toplam': toplam,
        })

    # Soruyu session'a kaydet (cevap kontrolü için)
    request.session[f'alm_soru_{thema}'] = {
        'uid': soru.uid,
        'dogru_harf': soru.dogru_harf,
        'erklaerung': soru.erklaerung,
    }

    return render(request, 'almanca/quiz.html', {
        'thema': thema,
        'tr': engine.KONU_TR.get(thema, thema),
        'soru': soru,
        'gorulmus': len(gorulmus),
        'toplam': toplam,
        'dogru': dogru_sayi,
        'yanlis': yanlis_sayi,
    })


@require_POST
def cevapla(request, thema):
    """AJAX: kullanıcının cevabını kontrol et, JSON döndür."""
    veri = json.loads(request.body)
    secilen = veri.get('harf', '').upper()

    kayit = request.session.get(f'alm_soru_{thema}')
    if not kayit:
        return JsonResponse({'hata': 'Oturum bulunamadı.'}, status=400)

    dogru_harf = kayit['dogru_harf']
    erklaerung = kayit['erklaerung']
    uid = kayit['uid']

    gorulmus = request.session.get(f'alm_gorulmus_{thema}', [])
    if uid not in gorulmus:
        gorulmus.append(uid)
        request.session[f'alm_gorulmus_{thema}'] = gorulmus

    if secilen == dogru_harf:
        request.session[f'alm_dogru_{thema}'] = request.session.get(f'alm_dogru_{thema}', 0) + 1
        durum = 'dogru'
    else:
        request.session[f'alm_yanlis_{thema}'] = request.session.get(f'alm_yanlis_{thema}', 0) + 1
        durum = 'yanlis'

    request.session.modified = True

    return JsonResponse({
        'durum': durum,
        'dogru_harf': dogru_harf,
        'erklaerung': erklaerung,
    })
