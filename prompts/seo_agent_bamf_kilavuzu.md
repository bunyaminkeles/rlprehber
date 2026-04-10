# SEO Agent — BAMF Resmi Kılavuzları: Ne Yüklemeli?

Bu belge, Soro-X'e (SEO agent) yüklenecek resmi kaynakların listesini ve öncelik sırasını belirtir.
Amaç: Agent içerik üretirken "kendi yorumunu değil, yasayı" referans alsın.

---

## Öncelik 1 — Mutlaka Yükle

### Familiennachzug (Aile Birleşimi)
- **Kaynak:** bamf.de → Themen → Aufenthalt → Familiennachzug
- **Türkçe adı:** Aile Birleşimi
- **Neden önemli:** Sitenizdeki en yoğun aranan konu. Yanlış bilgi hukuki risk yaratır.
- **İndir:** "Merkblatt Familiennachzug" PDF (Almanca veya Türkçe varsa her ikisi)

### Niederlassungserlaubnis / Daueraufenthalt
- **Kaynak:** bamf.de → Themen → Aufenthalt → Niederlassungserlaubnis
- **Türkçe adı:** Süresiz Oturma İzni
- **Neden önemli:** "Ne zaman kalıcı oturum alırım?" sorusu en çok sorulan 3. soru.

### Einbürgerung (Vatandaşlık)
- **Kaynak:** bamf.de → Themen → Einbürgerung
- **Türkçe adı:** Vatandaşlık Başvurusu
- **Neden önemli:** 2024 reform sonrası kural değişiklikleri var — eski içerik hatalı olabilir.

---

## Öncelik 2 — Yükle (içerik yazılacaksa)

### Integrationskurs (Entegrasyon Kursu)
- **Kaynak:** bamf.de → Themen → Integrationskurse
- **Neden önemli:** Siteye /almanca/ bölümü var, kurs içerikleri için referans.

### Beschäftigung / Arbeitserlaubnis (Çalışma İzni)
- **Kaynak:** bamf.de → Themen → Beschäftigung
- **Neden önemli:** Rehber bölümündeki "İş & Kariyer" kategorisi için.

### Asylverfahren / Duldung
- **Kaynak:** bamf.de → Themen → Asyl
- **Neden önemli:** Bazı kullanıcı segmentleri bu konuda bilgi arıyor.

---

## Öncelik 3 — Opsiyonel (ilgili içerik yazılacaksa)

| Konu | BAMF Bölümü |
|------|-------------|
| Blaue Karte (Mavi Kart) | Qualifizierte Einwanderung → Blaue Karte EU |
| Anerkennungsberatung (Diploma Denkliği) | Themen → Anerkennung |
| Sprachkurs / B1-B2 sınavları | Themen → Integrationskurse → Sprachkurse |
| Lebensunterhalt (Geçim Koşulları) | Aufenthalt → Voraussetzungen |

---

## Yükleme Talimatı (Gemini / Soro-X için)

1. Yukarıdaki PDF'leri BAMF'ın resmi sitesinden indir.
2. Google AI Studio veya Gemini API'de proje oluştururken "Files" bölümüne yükle.
3. System prompt'a şunu ekle:
   > "Yüklenen belgeler resmi BAMF kılavuzlarıdır. İçerik yazarken bu belgelerdeki yasal koşulları,
   > süreleri ve gereksinimleri temel al. Emin olmadığın bilgiyi 'BAMF'a göre...' diye başlatarak
   > belirt. Belgede yer almayan konularda tahmin yürütme, 'güncel bilgi için BAMF.de'yi kontrol
   > edin' yönlendirmesini yap."

---

## Önemli Uyarı

BAMF kılavuzları sık güncellenir. Her 6 ayda bir indirdiğin PDF'in tarihini kontrol et.
Özellikle Einbürgerung ve Familiennachzug kuralları 2024-2025'te değişti.
