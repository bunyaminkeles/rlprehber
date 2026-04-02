# Gemini — Gezilecek Yer Blog Promptu

Aşağıdaki metni kopyala, **sadece üstteki şehir ve yer listesini** değiştir, Gemini'ye yapıştır.

---

## KULLANIMM

Şehir ve yerleri doldur:

```
Şehir: Hamburg
Şehir slug: hamburg

Yerler:
1. Hamburger Rathaus (Belediye Sarayı) — Resim: https://commons.wikimedia.org/wiki/File:Hamburg_Rathausmarkt_und_Rathaus.jpg — Kaynak: https://commons.wikimedia.org/wiki/User:Arnoldius

2. St. Michaelis Kirche (Aziz Michael Kilisesi - "Michel") — Resim: https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/St._-_Michaelis_-_Kirche%2C_Heemsen.jpg/640px-St._-_Michaelis_-_Kirche%2C_Heemsen.jpg — Kaynak: https://commons.wikimedia.org/wiki/User:Kiwi05

3. Speicherstadt (Depolar Bölgesi) — Resim: https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Hamburg%2C_Speicherstadt%2C_Wasserschloss_--_2016_--_3265-71.jpg/640px-Hamburg%2C_Speicherstadt%2C_Wasserschloss_--_2016_--_3265-71.jpg — Kaynak: https://www.wikidata.org/wiki/Q34788025
//
4. Elbphilharmonie (Elbe Filarmoni Salonu) — Resim: https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Elbphilharmonie_Eastside_View_With_Sandtorkai_Quay_Magellan_Terraces_Sandtorpark_2022-06-04_16-32.jpg/640px-Elbphilharmonie_Eastside_View_With_Sandtorkai_Quay_Magellan_Terraces_Sandtorpark_2022-06-04_16-32.jpg — Kaynak: https://commons.wikimedia.org/wiki/User:Axel_Tschentscher

5. Alter Elbtunnel (Eski Elbe Tüneli) - Resim: https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Hamburg%2C_Alter_Elbtunnel%2C_S%C3%BCdeingang_--_2025_--_2826.jpg/640px-Hamburg%2C_Alter_Elbtunnel%2C_S%C3%BCdeingang_--_2025_--_2826.jpg - Kaynak: https://www.wikidata.org/wiki/Q34788025

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
