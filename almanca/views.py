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
    """Bir soruyu göster; sıralı ve rastgele mod desteği."""
    bilgi = engine.konu_bilgi(slug)
    if not bilgi:
        from django.http import Http404
        raise Http404

    thema, tr = bilgi

    # Mod: 'sirali' veya 'rastgele' — GET'ten al, yoksa session'dan, yoksa default rastgele
    mod = request.GET.get('mod') or request.session.get(f'alm_mod_{slug}', 'rastgele')
    request.session[f'alm_mod_{slug}'] = mod

    if request.GET.get('sifirla'):
        request.session.pop(f'alm_gorulmus_{slug}', None)
        request.session.pop(f'alm_dogru_{slug}', None)
        request.session.pop(f'alm_yanlis_{slug}', None)
        request.session.pop(f'alm_index_{slug}', None)
        return redirect(f"{request.path}?mod={mod}")

    gorulmus = request.session.get(f'alm_gorulmus_{slug}', [])
    dogru_sayi = request.session.get(f'alm_dogru_{slug}', 0)
    yanlis_sayi = request.session.get(f'alm_yanlis_{slug}', 0)
    toplam = engine.soru_sayisi(slug)

    if mod == 'sirali':
        index = request.session.get(f'alm_index_{slug}', 0)
        soru = engine.sirali_soru(slug, index)
        gorulmus_sayi = index
    else:
        soru = engine.rastgele_soru(slug, gorulmus)
        gorulmus_sayi = len(gorulmus)

    if soru is None:
        return render(request, 'almanca/bitti.html', {
            'slug': slug,
            'thema': thema,
            'tr': tr,
            'dogru': dogru_sayi,
            'yanlis': yanlis_sayi,
            'toplam': toplam,
            'mod': mod,
        })

    request.session[f'alm_soru_{slug}'] = {
        'uid': soru.uid,
        'dogru_harf': soru.dogru_harf,
        'erklaerung': soru.erklaerung,
        'mod': mod,
    }

    return render(request, 'almanca/quiz.html', {
        'slug': slug,
        'thema': thema,
        'tr': tr,
        'soru': soru,
        'gorulmus': gorulmus_sayi,
        'toplam': toplam,
        'dogru': dogru_sayi,
        'yanlis': yanlis_sayi,
        'mod': mod,
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
    mod = kayit.get('mod', 'rastgele')

    # Görülen soruları takip et (her iki modda da)
    gorulmus = request.session.get(f'alm_gorulmus_{slug}', [])
    if uid not in gorulmus:
        gorulmus.append(uid)
        request.session[f'alm_gorulmus_{slug}'] = gorulmus

    # Sıralı modda index'i ilerlet
    if mod == 'sirali':
        idx = request.session.get(f'alm_index_{slug}', 0)
        request.session[f'alm_index_{slug}'] = idx + 1

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
