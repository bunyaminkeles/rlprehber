import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from . import engine


def liste(request, eyalet_slug='rlp'):
    """Konu seçim sayfası."""
    konular = engine.konu_listesi()
    return render(request, 'almanca/liste.html', {'konular': konular, 'eyalet_slug': eyalet_slug})


def _yanlis_listesi(slug, yanlis_ids, cevaplar):
    result = []
    for uid in yanlis_ids:
        s = engine.soru_by_uid(slug, uid)
        if s:
            cv = cevaplar.get(uid, {})
            result.append({
                'frage': s.frage,
                'dogru_harf': cv.get('dogru_harf', s.dogru_harf),
                'dogru_metin': cv.get('dogru_metin') or s.optionen.get(s.dogru_harf, ''),
                'secilen_harf': cv.get('secilen_harf', ''),
                'secilen_metin': cv.get('secilen_metin') or s.optionen.get(cv.get('secilen_harf', ''), ''),
            })
    return result


def quiz(request, slug, eyalet_slug='rlp'):
    """Bir soruyu göster; sıralı/rastgele mod, navigasyon ve sıfırlama desteği."""
    bilgi = engine.konu_bilgi(slug)
    if not bilgi:
        from django.http import Http404
        raise Http404

    thema, tr = bilgi

    # Mod: 'sirali' veya 'rastgele'
    mod = request.GET.get('mod') or request.session.get(f'alm_mod_{slug}', 'rastgele')
    request.session[f'alm_mod_{slug}'] = mod

    if request.GET.get('sifirla'):
        for k in [f'alm_gorulmus_{slug}', f'alm_dogru_{slug}', f'alm_yanlis_{slug}',
                  f'alm_index_{slug}', f'alm_gecmis_{slug}', f'alm_cevaplar_{slug}',
                  f'alm_yanlis_ids_{slug}', f'alm_soru_{slug}']:
            request.session.pop(k, None)
        return redirect(f"{request.path}?mod={mod}")

    gorulmus   = request.session.get(f'alm_gorulmus_{slug}', [])
    dogru_sayi = request.session.get(f'alm_dogru_{slug}', 0)
    yanlis_sayi = request.session.get(f'alm_yanlis_{slug}', 0)
    toplam     = engine.soru_sayisi(slug)
    gecmis     = request.session.get(f'alm_gecmis_{slug}', [])
    cevaplar   = request.session.get(f'alm_cevaplar_{slug}', {})
    yanlis_ids = request.session.get(f'alm_yanlis_ids_{slug}', [])

    ctx_base = {
        'slug': slug, 'thema': thema, 'tr': tr,
        'gorulmus': len(gorulmus), 'toplam': toplam,
        'dogru': dogru_sayi, 'yanlis': yanlis_sayi,
        'gecmis_sayisi': len(gecmis),
        'yanlis_sorular': _yanlis_listesi(slug, yanlis_ids, cevaplar),
        'mod': mod,
        'eyalet_slug': eyalet_slug,
    }

    # Geçmiş navigasyon: ?goto=N
    goto_str = request.GET.get('goto')
    if goto_str is not None and gecmis:
        try:
            idx = max(0, min(int(goto_str), len(gecmis) - 1))
        except ValueError:
            return redirect(f'/{eyalet_slug}/almanca/{slug}/')

        uid = gecmis[idx]
        soru = engine.soru_by_uid(slug, uid)
        if not soru:
            return redirect(f'/{eyalet_slug}/almanca/{slug}/')

        cv = cevaplar.get(uid, {})
        if not cv:
            request.session[f'alm_soru_{slug}'] = {
                'uid': soru.uid, 'dogru_harf': soru.dogru_harf,
                'erklaerung': soru.erklaerung, 'mod': mod, 'optionen': soru.optionen,
            }
            return render(request, 'almanca/quiz.html', {
                **ctx_base, 'soru': soru, 'already_answered': False, 'mevcut_idx': idx,
            })
        return render(request, 'almanca/quiz.html', {
            **ctx_base, 'soru': soru, 'already_answered': True, 'mevcut_idx': idx,
            'secilen_harf': cv.get('secilen_harf'),
            'dogru_harf_goster': cv.get('dogru_harf', soru.dogru_harf),
        })

    # Cevap vermeden atlama: ?atla=1
    if request.GET.get('atla'):
        kayit = request.session.get(f'alm_soru_{slug}')
        if kayit:
            uid = kayit['uid']
            gorulmus = request.session.get(f'alm_gorulmus_{slug}', [])
            if uid not in gorulmus:
                gorulmus.append(uid)
                request.session[f'alm_gorulmus_{slug}'] = gorulmus
            gecmis = request.session.get(f'alm_gecmis_{slug}', [])
            if uid not in gecmis:
                gecmis.append(uid)
                request.session[f'alm_gecmis_{slug}'] = gecmis
            if mod == 'sirali':
                idx = request.session.get(f'alm_index_{slug}', 0)
                request.session[f'alm_index_{slug}'] = idx + 1
        return redirect(f"{request.path}?mod={mod}")

    # UID ile doğrudan navigasyon: ?uid=<uid>
    uid_param = request.GET.get('uid')
    if uid_param is not None:
        uid_param = uid_param.strip()
        soru = engine.soru_by_uid(slug, uid_param)
        if not soru:
            return redirect(f"{request.path}?mod={mod}")
        if uid_param in cevaplar:
            idx = gecmis.index(uid_param) if uid_param in gecmis else len(gecmis) - 1
            cv = cevaplar[uid_param]
            return render(request, 'almanca/quiz.html', {
                **ctx_base, 'soru': soru, 'already_answered': True, 'mevcut_idx': idx,
                'secilen_harf': cv.get('secilen_harf'),
                'dogru_harf_goster': cv.get('dogru_harf', soru.dogru_harf),
            })
        else:
            request.session[f'alm_soru_{slug}'] = {
                'uid': soru.uid, 'dogru_harf': soru.dogru_harf,
                'erklaerung': soru.erklaerung, 'mod': mod, 'optionen': soru.optionen,
            }
            return render(request, 'almanca/quiz.html', {
                **ctx_base, 'soru': soru, 'already_answered': False,
                'mevcut_idx': len(gecmis),
            })

    # Yeni soru — sıralı veya rastgele mod
    if mod == 'sirali':
        index = request.session.get(f'alm_index_{slug}', 0)
        soru = engine.sirali_soru(slug, index)
        gorulmus_sayi = index
    else:
        soru = engine.rastgele_soru(slug, gorulmus)
        gorulmus_sayi = len(gorulmus)

    if soru is None:
        return render(request, 'almanca/bitti.html', {
            'slug': slug, 'thema': thema, 'tr': tr,
            'dogru': dogru_sayi, 'yanlis': yanlis_sayi, 'toplam': toplam,
            'mod': mod, 'eyalet_slug': eyalet_slug,
            'yanlis_sorular': _yanlis_listesi(slug, yanlis_ids, cevaplar),
        })

    request.session[f'alm_soru_{slug}'] = {
        'uid': soru.uid, 'dogru_harf': soru.dogru_harf,
        'erklaerung': soru.erklaerung, 'mod': mod, 'optionen': soru.optionen,
    }

    return render(request, 'almanca/quiz.html', {
        **ctx_base, 'soru': soru, 'already_answered': False,
        'gorulmus': gorulmus_sayi, 'mevcut_idx': len(gecmis),
    })


def katalog(request, slug, eyalet_slug='rlp'):
    """Tüm soruları sıralı göster: numara, soru, doğru cevap."""
    bilgi = engine.konu_bilgi(slug)
    if not bilgi:
        from django.http import Http404
        raise Http404
    thema, tr = bilgi
    sorular = engine.sirali_sorular(slug)
    return render(request, 'almanca/katalog.html', {
        'slug': slug, 'thema': thema, 'tr': tr,
        'sorular': sorular, 'toplam': len(sorular),
        'son_guncelleme': engine.konu_son_guncelleme(slug),
        'eyalet_slug': eyalet_slug,
    })


@require_POST
def cevapla(request, slug, eyalet_slug='rlp'):
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
    mod        = kayit.get('mod', 'rastgele')
    optionen   = kayit.get('optionen', {})

    gorulmus = request.session.get(f'alm_gorulmus_{slug}', [])
    if uid not in gorulmus:
        gorulmus.append(uid)
        request.session[f'alm_gorulmus_{slug}'] = gorulmus

    if mod == 'sirali':
        idx = request.session.get(f'alm_index_{slug}', 0)
        request.session[f'alm_index_{slug}'] = idx + 1

    gecmis = request.session.get(f'alm_gecmis_{slug}', [])
    if uid not in gecmis:
        gecmis.append(uid)
        request.session[f'alm_gecmis_{slug}'] = gecmis

    cevaplar = request.session.get(f'alm_cevaplar_{slug}', {})
    cevaplar[uid] = {
        'secilen_harf': secilen,
        'dogru_harf': dogru_harf,
        'secilen_metin': optionen.get(secilen, ''),
        'dogru_metin': optionen.get(dogru_harf, ''),
    }
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
