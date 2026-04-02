# Gemini — Gezilecek Yer Blog Promptu

Aşağıdaki metni kopyala, **sadece üstteki şehir ve yer listesini** değiştir, Gemini'ye yapıştır.

---

## KULLANIMM

Şehir ve yerleri doldur:

```
Şehir: Berlin
Şehir slug: berlin

Yerler:
1. Berliner Fernsehturm — Resim: https://upload.wikimedia.org/... — Kaynak: https://commons.wikimedia.org/wiki/User:...
2. Brandenburger Tor — Resim: https://... — Kaynak: https://...
```

Sonra aşağıdaki tam promptu Gemini'ye gönder 👇

---

## GEMİNİ PROMPTU (sabit — değiştirme)

```
Aşağıdaki gezilecek yerler için Türkçe blog içerikleri yaz.

Şehir: [ŞEHİR]
Şehir slug: [SLUG]

Yerler:
[YER LİSTESİ]

Kurallar:
- Her yer için "icerik" alanı HTML formatında olsun (p, h3, h4, ul, li, strong, em, hr tagları)
- "icerik" en az 400 kelime olsun, ilgi çekici ve bilgilendirici yaz
- "aciklama" max 200 karakter, SEO dostu özet cümle
- "kategori" her zaman: gezi
- "adres" alanına o yerin semtini veya meydanını yaz
- "kapak_resmi" alanına o yer için verdiğim Resim linkini yaz
- "wikipedia_url" alanına o yer için verdiğim Kaynak linkini yaz
- Sadece geçerli JSON döndür, başka hiçbir açıklama ekleme

Çıktı formatı:
{
  "stadt_slug": "[SLUG]",
  "yerler": [
    {
      "id": null,
      "ad": "Yer Adı",
      "kategori": "gezi",
      "adres": "Adres, Şehir",
      "aciklama": "Kısa SEO açıklama...",
      "kapak_resmi": "RESİM_URL",
      "wikipedia_url": "KAYNAK_URL",
      "icerik": "<p>İçerik...</p>"
    }
  ]
}
```

---

## SUNUCUYA YÜKLEME

Gemini'nin JSON çıktısını sunucuya yapıştır:

```bash
nano /tmp/veri.json
```

Çalıştır:

```bash
python manage.py yer_icerik_yukle /tmp/veri.json && rm /tmp/veri.json
```

---

## MEVCUT KAYDI GÜNCELLEMEK

DB'deki ID'yi öğrenmek için:

```bash
python manage.py shell -c "from yerler.models import Yer; from stadt.models import Stadt; b=Stadt.objects.get(slug='berlin'); [print(y.id, y.ad) for y in Yer.objects.filter(stadt=b, tur='yer')]"
```

JSON'da `"id": null` yerine o ID'yi yaz, komut günceller.
