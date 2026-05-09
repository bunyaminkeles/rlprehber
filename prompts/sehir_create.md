# ALMANYALI REHBER — YENİ ŞEHİR OLUŞTURMA PROMPTU (Gemini için)

Sen Kıdemli bir Django Veri Mühendisi ve Araştırmacısın. Bu proje Almanya'daki Türkler için hazırlanmış bir rehber sitesidir (`almanyalirehber.com`). Görevin, aşağıda belirtilen şehir için **tek bir Django migration dosyası** oluşturmaktır.

---

## ŞEHİR BİLGİSİ

```
Şehir adı    : [BURAYA YAZ — Almanca resmi adı, örn: Nürnberg]
Türkçe adı   : [BURAYA YAZ — Türkçe kullanımı, örn: Nürnberg]
Slug         : [BURAYA YAZ — URL'de kullanılacak, Türkçe, küçük harf, tire ile, örn: nuernberg]
Eyalet kodu  : [BURAYA YAZ — aşağıdaki tablodan seç]
```

### Eyalet Kodları (kesin liste — tahmin etme)

| Kod  | Eyalet                  | Dikkat                          |
|------|-------------------------|---------------------------------|
| RLP  | Rheinland-Pfalz         | ⚠️ 'RP' veya 'NRW' YAZMA       |
| NW   | Nordrhein-Westfalen     | ⚠️ 'NRW' veya 'NR' YAZMA       |
| BW   | Baden-Württemberg       |                                 |
| BY   | Bayern                  |                                 |
| HE   | Hessen                  |                                 |
| NI   | Niedersachsen           |                                 |
| SL   | Saarland                |                                 |
| SN   | Sachsen                 |                                 |
| ST   | Sachsen-Anhalt          |                                 |
| TH   | Thüringen               |                                 |
| BB   | Brandenburg             |                                 |
| BE   | Berlin                  |                                 |
| HB   | Bremen                  |                                 |
| HH   | Hamburg                 |                                 |
| MV   | Mecklenburg-Vorpommern  |                                 |
| SH   | Schleswig-Holstein      |                                 |

---

## VERİ ARAŞTIRMASI (ÖNCE BUNLARI BUL)

Google'da araştır, her URL **gerçek ve erişilebilir** olmalı. **ASLA hallüsinasyon yapma.**

### 1. Action Links (3 URL — max 190 karakter!)

| Alan                   | Açıklama                                                  |
|------------------------|-----------------------------------------------------------|
| `termin_url`           | Belediye online randevu sayfası (Bürgeramt / Bürgerbüro)  |
| `auslaenderbehorde_url`| Ausländerbehörde online termin veya iletişim sayfası      |
| `rss_duyuru_url`       | Belediye haber RSS feed'i (yoksa haber ana sayfası)       |

⚠️ **KRİTİK:** URL'leri **percent-encode etme** (ü, ö, ä gibi karakterleri `%C3%BC` yazmak yerine direkt yaz). URLField max_length=200'dür.

### 2. Resmi Kurumlar (5 adet)

Sabit liste — şehre göre adresi araştır:
- Jobcenter [Şehir]
- Ausländerbehörde [Şehir]
- Bürgeramt [Şehir] (merkez şube)
- Agentur für Arbeit [Şehir]
- Finanzamt [Şehir]

### 3. İbadet (3–4 yer)

DITIB camisi öncelikli. IGMG veya DİTİB bünyesindeki camiler. Türk-Müslüman toplumuna hitap eden yerler.

### 4. TÜV (2–3 yer)

TÜV SÜD veya TÜV NORD istasyonları (bölgeye göre hangisi hakimse). Araç muayene (HU/AU) istasyonları.

### 5. Sağlık (3–4 yer)

7/24 acil servis veren hastaneler. Üniversite hastanesi varsa mutlaka ekle.

### 6. Eğitim (3 yer)

- VHS (Volkshochschule) — BAMF onaylı entegrasyon kursları
- Varsa Türkçe dil kursu veren kurum
- Varsa Caritas / Diakonie eğitim merkezi

### 7. Gezi (10 yer)

En önemli 10 turistik yer. Her biri için:
- `aciklama`: Türkçe 1–2 cümle
- `icerik`: Türkçe **3 paragraf** detaylı içerik (paragraflar `\n\n` ile ayrılacak)
- `wikipedia_url`: Almanca Wikipedia linki
- `sira`: 1'den 10'a

### 8. Alışveriş (3–4 yer)

- 1–2 Türk marketi (helal ürünler, Türk gıdası)
- 1–2 büyük AVM (şehrin en merkezi alışveriş merkezi)

---

## ÇIKTI: TEK MIGRATION DOSYASI

Dosya adı: `XXXX_<sehir_slug>_ekosistem.py`

```
XXXX = bir sonraki müsait migration numarası

⚠️ MIGRATION NUMARASINI PROMPT'TAN ALMA — GERÇEK DOSYALARA BAK!
Prompt'taki numara eskimiş olabilir. Şehri üretmeden önce şunu çalıştır:
    ls stadt/migrations/*.py | tail -3
    ls yerler/migrations/*.py | tail -3

Şu an son stad migrasyonu: 0046_merge_0045_erfurt_aktiv_0045_eyalet_nrw_artik_sil
Şu an son yerler migrasyonu: 0046_merge_20260510_0041
→ stad için sonraki: 0047
→ yerler için sonraki: 0047
Bu migration tek dosya olduğu için iki ayrı app'e bölünecek (aşağıya bak)
```

⚠️ **ÖNEMLİ:** Tek şehir için **iki dosya** üretilecek:
- `stadt/migrations/0047_<slug>_aktiv.py` — Stadt güncelleme
- `yerler/migrations/0047_seed_<slug>_yerler.py` — Yer verileri

---

### DOSYA 1: `stadt/migrations/0047_<slug>_aktiv.py`

```python
from django.db import migrations


def update(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    try:
        s = Stadt.objects.get(slug='<SLUG>')
        s.termin_url            = '<TERMIN_URL>'           # max 190 karakter, % encode etme
        s.auslaenderbehorde_url = '<AUSLAENDERBEHORDE_URL>'
        s.rss_duyuru_url        = '<RSS_URL>'
        s.aktiv                 = True
        s.save()
    except Stadt.DoesNotExist:
        pass


def reverse(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    try:
        s = Stadt.objects.get(slug='<SLUG>')
        s.termin_url            = ''
        s.auslaenderbehorde_url = ''
        s.rss_duyuru_url        = ''
        s.aktiv                 = False
        s.save()
    except Stadt.DoesNotExist:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0046_merge_0045_erfurt_aktiv_0045_eyalet_nrw_artik_sil'),
    ]
    operations = [
        migrations.RunPython(update, reverse),
    ]
```

---

### DOSYA 2: `yerler/migrations/0047_seed_<slug>_yerler.py`

```python
from django.db import migrations

RESMI_KURUM = [
    {'ad': 'Jobcenter <Şehir>',          'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': 'https://maps.google.com/?q=...'},
    {'ad': 'Ausländerbehörde <Şehir>',   'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
    {'ad': 'Bürgeramt <Şehir>',          'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
    {'ad': 'Agentur für Arbeit <Şehir>', 'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
    {'ad': 'Finanzamt <Şehir>',          'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
]

IBADET = [
    {'ad': '...', 'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
    # 3–4 adet
]

TUV = [
    {'ad': '...', 'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
    # 2–3 adet
]

SAGLIK = [
    {'ad': '...', 'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
    # 3–4 adet
]

EGITIM = [
    {'ad': '...', 'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
    # 3 adet
]

GEZI = [
    {
        'ad': '...', 'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...',
        'icerik': '<paragraf1>\n\n<paragraf2>\n\n<paragraf3>',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/...', 'sira': 1,
    },
    # 10 adet, sira 1–10
]

ALISVERIS = [
    {'ad': '...', 'adres': '...', 'aciklama': '...', 'website': '...', 'maps_url': '...'},
    # 3–4 adet
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')
    try:
        eyalet = Eyalet.objects.get(kod='<EYALET_KODU>')   # ⚠️ RLP, BY, NW vb. — tahmin etme!
        sehir  = Stadt.objects.get(slug='<SLUG>')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return
    for kategori_slug, veriler in [
        ('resmi_kurum', RESMI_KURUM), ('ibadet', IBADET), ('tuv', TUV),
        ('saglik', SAGLIK), ('egitim', EGITIM), ('gezi', GEZI), ('alisveris', ALISVERIS),
    ]:
        for veri in veriler:
            Yer.objects.get_or_create(
                ad=veri['ad'], stadt=sehir,
                defaults={
                    'eyalet':      eyalet,
                    'scope':       'stadt',
                    'tur':         'yer',
                    'kategori':    kategori_slug,
                    'sehir':       '<Şehir Adı>',          # Almanca resmi adı, örn: 'Nürnberg'
                    'adres':       veri['adres'],
                    'aciklama':    veri['aciklama'],
                    'kapak_resmi': '',
                    'website':     veri.get('website', ''),
                    'maps_url':    veri.get('maps_url', ''),
                    'icerik':      veri.get('icerik', ''),
                    'wikipedia_url': veri.get('wikipedia_url', ''),
                    'sira':        veri.get('sira', 0),
                    'aktif':       True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = [v['ad'] for liste in [RESMI_KURUM, IBADET, TUV, SAGLIK, EGITIM, GEZI, ALISVERIS] for v in liste]
    Yer.objects.filter(ad__in=adlar, sehir='<Şehir Adı>').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0046_merge_20260510_0041'),
        ('stadt',  '0047_<slug>_aktiv'),               # Dosya 1'e bağımlı
    ]
    operations = [migrations.RunPython(seed, unseed)]
```

---

## DOĞRULAMA KURALLARI

1. **HALLÜSINASYON YAPMA.** Her adres, URL ve website gerçek ve doğrulanabilir olmalı.
2. **termin_url max 190 karakter** — percent-encode etme, Unicode karakterleri (ü, ö, ä) direkt yaz.
3. **maps_url formatı:** `https://maps.google.com/?q=Yer+Adı+Şehir` — boşluklar `+` ile.
4. **aciklama:** Türkçe, 1–2 cümle, özlü.
5. **icerik (sadece gezi):** Türkçe, 3 paragraf, `\n\n` ile ayrılmış. Tarihi ve kültürel bilgi ağırlıklı.
6. **eyalet kodu:** Yukarıdaki tablodan kesinlikle doğru kodu yaz. 'RP', 'NRW' gibi yanlış kodlar sessizce hata verir.
7. **slug:** Türkçe yazılış, küçük harf, Almanca özel karakter içermez (ü→ue değil, direkt türkçe sade hali veya yaygın kullanım — örn: münchen→munih, köln→koeln değil koeln de olur).
8. **sira alanı:** Sadece GEZI listesinde kullanılır, 1'den 10'a.

---

## ÇIKTI KURALI

Sadece iki Python dosyasını üret. Açıklama, yorum satırı veya ek bilgi yazma. Doğrulama yaptıktan sonra dosyaları ver.

---

## UYGULAMA ADIMLARI (Gemini çıktısı geldikten sonra)

Gemini iki dosya üretir. Sırayla şunları yap:

### 1. Dosyaları doğru yerlere kaydet

```
mainzer-binger/stadt/migrations/0047_<slug>_aktiv.py         ← Dosya 1
mainzer-binger/yerler/migrations/0047_seed_<slug>_yerler.py  ← Dosya 2
```

### 2. Yerelde test et

```bash
cd /home/bunyamin/Documents/mainzer-binger

# Önce kuru geçiş kontrolü
python manage.py migrate --check

# Uygula
python manage.py migrate
```

Hata yoksa devam et.

### 3. Commit et

```bash
git add stadt/migrations/0047_<slug>_aktiv.py
git add yerler/migrations/0047_seed_<slug>_yerler.py
git commit -m "feat(<slug>): <şehir> şehri ekosistemi ayağa kaldırıldı"
```

### 4. Push ve merge et

```bash
git push origin main
git checkout dev
git merge main -m "merge(main→dev): <şehir> ekosistemi"
git push origin dev
git checkout main
```

### 5. Hetzner'e deploy et

```bash
ssh root@204.168.195.246
cd /var/www/rlprehber
git pull
python manage.py migrate
systemctl restart gunicorn
```

### 6. Prompt dosyalarını güncelle

Her şehirden sonra **bu dosyayı** (`sehir_create.md`) ve `sehir_ayaga_kaldir.txt`'i güncelle:
- `sehir_create.md` içindeki "Şu an son stad migrasyonu" ve "Şu an son yerler migrasyonu" satırlarını yeni numaraya çek
- `sehir_create.md` içindeki dependencies'leri güncelle (0047_<slug>_aktiv → bir sonraki için)
- Her iki prompt dosyasını da commit'e dahil et:

```bash
git add prompts/sehir_create.md
git add prompts/sehir_ayaga_kaldir.txt
```

⚠️ **NEDEN ÖNEMLİ:** Gemini bu dosyadaki numaraları kullanır. Güncellenmezse bir sonraki şehirde migration çakışması çıkar (aynı numara iki ayrı migration'da).
