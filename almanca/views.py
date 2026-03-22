import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import engine


def liste(request):
    """Konu seçim sayfası."""
    konular = engine.konu_listesi()
    return render(request, 'almanca/liste.html', {'konular': konular})


def _yanlis_listesi(slug, yanlis_ids, cevaplar):
    result = []
    for uid in yanlis_ids:
        s = engine.soru_by_uid(slug, uid)
        if s:
            cv = cevaplar.get(uid, {})
            result.append({
                'frage': s.frage,
                'dogru_harf': s.dogru_harf,
                'dogru_metin': s.optionen.get(s.dogru_harf, ''),
                'secilen_harf': cv.get('secilen_harf', ''),
                'secilen_metin': s.optionen.get(cv.get('secilen_harf', ''), ''),
            })
    return result


def quiz(request, slug):
    """Bir soruyu göster; navigasyon ve sıfırlama desteği."""
    bilgi = engine.konu_bilgi(slug)
    if not bilgi:
        from django.http import Http404
        raise Http404

    thema, tr = bilgi

    if request.GET.get('sifirla'):
        for k in [f'alm_gorulmus_{slug}', f'alm_dogru_{slug}', f'alm_yanlis_{slug}',
                  f'alm_gecmis_{slug}', f'alm_cevaplar_{slug}', f'alm_yanlis_ids_{slug}',
                  f'alm_soru_{slug}']:
            request.session.pop(k, None)
        return redirect('almanca:quiz', slug=slug)

    gorulmus      = request.session.get(f'alm_gorulmus_{slug}', [])
    dogru_sayi    = request.session.get(f'alm_dogru_{slug}', 0)
    yanlis_sayi   = request.session.get(f'alm_yanlis_{slug}', 0)
    toplam        = engine.soru_sayisi(slug)
    gecmis        = request.session.get(f'alm_gecmis_{slug}', [])
    cevaplar      = request.session.get(f'alm_cevaplar_{slug}', {})
    yanlis_ids    = request.session.get(f'alm_yanlis_ids_{slug}', [])

    goto_str = request.GET.get('goto')

    if goto_str is not None and gecmis:
        # Geçmişteki bir soruya git (zaten cevaplanmış)
        try:
            idx = max(0, min(int(goto_str), len(gecmis) - 1))
        except ValueError:
            return redirect('almanca:quiz', slug=slug)

        uid = gecmis[idx]
        soru = engine.soru_by_uid(slug, uid)
        if not soru:
            return redirect('almanca:quiz', slug=slug)

        cv = cevaplar.get(uid, {})
        return render(request, 'almanca/quiz.html', {
            'slug': slug, 'thema': thema, 'tr': tr, 'soru': soru,
            'gorulmus': len(gorulmus), 'toplam': toplam,
            'dogru': dogru_sayi, 'yanlis': yanlis_sayi,
            'already_answered': True,
            'secilen_harf': cv.get('secilen_harf'),
            'dogru_harf_goster': cv.get('dogru_harf', soru.dogru_harf),
            'mevcut_idx': idx,
            'gecmis_sayisi': len(gecmis),
            'yanlis_sorular': _yanlis_listesi(slug, yanlis_ids, cevaplar),
        })

    # Yeni soru
    soru = engine.rastgele_soru(slug, gorulmus)

    if soru is None:
        return render(request, 'almanca/bitti.html', {
            'slug': slug, 'thema': thema, 'tr': tr,
            'dogru': dogru_sayi, 'yanlis': yanlis_sayi, 'toplam': toplam,
        })

    request.session[f'alm_soru_{slug}'] = {
        'uid': soru.uid,
        'dogru_harf': soru.dogru_harf,
        'erklaerung': soru.erklaerung,
    }

    return render(request, 'almanca/quiz.html', {
        'slug': slug, 'thema': thema, 'tr': tr, 'soru': soru,
        'gorulmus': len(gorulmus), 'toplam': toplam,
        'dogru': dogru_sayi, 'yanlis': yanlis_sayi,
        'already_answered': False,
        'mevcut_idx': len(gecmis),
        'gecmis_sayisi': len(gecmis),
        'yanlis_sorular': _yanlis_listesi(slug, yanlis_ids, cevaplar),
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
    uid        = kayit['uid']

    # Görülmüş listesi
    gorulmus = request.session.get(f'alm_gorulmus_{slug}', [])
    if uid not in gorulmus:
        gorulmus.append(uid)
        request.session[f'alm_gorulmus_{slug}'] = gorulmus

    # Sıralı geçmiş
    gecmis = request.session.get(f'alm_gecmis_{slug}', [])
    if uid not in gecmis:
        gecmis.append(uid)
        request.session[f'alm_gecmis_{slug}'] = gecmis

    # Cevap kaydı
    cevaplar = request.session.get(f'alm_cevaplar_{slug}', {})
    cevaplar[uid] = {'secilen_harf': secilen, 'dogru_harf': dogru_harf}
    request.session[f'alm_cevaplar_{slug}'] = cevaplar

    if secilen == dogru_harf:
        request.session[f'alm_dogru_{slug}'] = request.session.get(f'alm_dogru_{slug}', 0) + 1
        durum = 'dogru'
    else:
        request.session[f'alm_yanlis_{slug}'] = request.session.get(f'alm_yanlis_{slug}', 0) + 1
        durum = 'yanlis'
        yanlis_ids = request.session.get(f'alm_yanlis_ids_{slug}', [])
        if uid not in yanlis_ids:
            yanlis_ids.append(uid)
            request.session[f'alm_yanlis_ids_{slug}'] = yanlis_ids

    request.session.modified = True

    return JsonResponse({
        'durum': durum,
        'dogru_harf': dogru_harf,
        'erklaerung': erklaerung,
        'gecmis_idx': len(gecmis) - 1,
    })
