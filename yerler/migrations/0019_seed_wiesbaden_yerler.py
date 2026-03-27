from django.db import migrations

IBADET = [
    {
        'ad': 'DITIB Fatih Camii Wiesbaden',
        'adres': 'Schiersteiner Str. 6, 65187 Wiesbaden',
        'aciklama': 'Wiesbaden\'ın en büyük camii. DITIB bünyesinde faaliyet göstermekte olup Türkçe ve Almanca Kuran kursları, cenaze hizmetleri ve sosyal etkinlikler düzenlenmektedir.',
        'website': 'https://wiesbaden.ditib.de',
        'maps_url': 'https://maps.google.com/?q=DITIB+Fatih+Camii+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'IGMG Mevlana Camii Wiesbaden',
        'adres': 'Eltviller Str. 14, 65203 Wiesbaden',
        'aciklama': 'İslam Toplumu Millî Görüş (IGMG) bünyesindeki Mevlana Camii. Cuma namazı, Kuran eğitimi ve gençlik programları sunulmaktadır.',
        'website': 'https://www.igmg.org',
        'maps_url': 'https://maps.google.com/?q=IGMG+Mevlana+Camii+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Eyüp Sultan Camii Wiesbaden',
        'adres': 'Mainzer Str. 97, 65189 Wiesbaden',
        'aciklama': 'Wiesbaden merkezine yakın konumda hizmet veren camii. Beş vakit namaz, Kuran kursları ve dini danışmanlık hizmetleri mevcuttur.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Eyüp+Sultan+Camii+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Wiesbaden Alevi Kültür Merkezi',
        'adres': 'Wiesbaden, Hessen',
        'aciklama': 'Alevi Bektaşi topluluğuna hizmet veren kültür merkezi. Cem törenleri, saz-semah etkinlikleri ve kültürel programlar düzenlenmektedir.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Alevi+Kültür+Merkezi+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
]

TUV = [
    {
        'ad': 'TÜV Hessen — Wiesbaden Prüfstelle',
        'adres': 'Abraham-Lincoln-Str. 38-42, 65189 Wiesbaden',
        'aciklama': 'TÜV Hessen\'in Wiesbaden merkez muayene istasyonu. Araç muayenesi (HU/AU), ehliyet sınavları ve teknik kontroller için randevu alınabilir.',
        'website': 'https://www.tuev-hessen.de',
        'maps_url': 'https://maps.google.com/?q=TÜV+Hessen+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'DEKRA Wiesbaden',
        'adres': 'Aarauer Str. 2, 65187 Wiesbaden',
        'aciklama': 'DEKRA araç muayene ve teknik hizmetler merkezi. HU (Hauptuntersuchung), AU (Abgasuntersuchung) ve araç değerleme hizmetleri sunulmaktadır.',
        'website': 'https://www.dekra.de',
        'maps_url': 'https://maps.google.com/?q=DEKRA+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'GTÜ Prüfstelle Wiesbaden',
        'adres': 'Wiesbaden, Hessen',
        'aciklama': 'GTÜ (Gesellschaft für Technische Überwachung) muayene istasyonu. TÜV ve DEKRA\'ya alternatif olarak araç periyodik muayenesi yapılmaktadır.',
        'website': 'https://www.gtue.de',
        'maps_url': 'https://maps.google.com/?q=GTÜ+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
]

SAGLIK = [
    {
        'ad': 'HSK — Helios Dr. Horst Schmidt Kliniken',
        'adres': 'Ludwig-Erhard-Str. 100, 65199 Wiesbaden',
        'aciklama': 'Wiesbaden\'ın en büyük hastanesi. Acil servis, tüm uzmanlık klinikleri ve yoğun bakım birimleriyle 24 saat hizmet vermektedir.',
        'website': 'https://www.helios-gesundheit.de/kliniken/wiesbaden/',
        'maps_url': 'https://maps.google.com/?q=HSK+Helios+Wiesbaden',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/HSK_Wiesbaden.jpg/1280px-HSK_Wiesbaden.jpg',
        'icerik': """<p>Wiesbaden'ın kalbi sayılan HSK (Helios Dr. Horst Schmidt Kliniken), Hessen eyaletinin en kapsamlı hastanelerinden biridir. Acil bir durumda veya uzman hekim arayışında olduğunuzda ilk başvuracağınız adres burasıdır.</p>

<h2>Acil Servis</h2>
<p>Hastane acil servisi 7/24 açıktır. Hayatı tehdit eden durumlarda 112 (Notruf) aranmalıdır.</p>
<div class="info-box"><strong>Adres:</strong> Ludwig-Erhard-Str. 100, 65199 Wiesbaden — Acil giriş ayrı bir kapıdan yapılmaktadır, tabelaları takip edin.</div>

<h2>Başlıca Klinikler</h2>
<div class="info-box"><strong>Kardiyoloji:</strong> Kalp hastalıkları ve kateter laboratuvarı.</div>
<div class="info-box"><strong>Nöroloji:</strong> İnme merkezi (Stroke Unit) — bölgedeki en hızlı müdahale kapasitesine sahip.</div>
<div class="info-box"><strong>Çocuk Kliniği:</strong> Çocuk acil ve pediatri bölümü aynı kampüste.</div>
<div class="info-box"><strong>Doğum:</strong> Kadın doğum kliniği — doğum öncesi randevu için web sitesinden kayıt yapılabilir.</div>

<h2>Pratik Bilgiler</h2>
<div class="info-box"><strong>Ulaşım:</strong> Otobüs hatları: 14, 18, 27 — "HSK" durağında inin.</div>
<div class="info-box"><strong>Tercüman:</strong> Hastane bünyesinde telefon tercümanlık hizmeti mevcuttur, Türkçe dahil.</div>
<div class="info-box"><strong>Randevu:</strong> Poliklinik randevuları için web sitesinden veya 0611 43-0 numarasından ulaşabilirsiniz.</div>""",
    },
    {
        'ad': 'Ärztlicher Bereitschaftsdienst — 116 117',
        'adres': 'Telefonla erişim: 116 117',
        'aciklama': 'Hafta sonu ve gece saatlerinde acil olmayan sağlık sorunları için KV Hessen\'in doktor nöbet hattı. Türkçe tercüman talepli arama yapılabilir.',
        'website': 'https://www.116117.de',
        'maps_url': '',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Gesundheitsamt Wiesbaden',
        'adres': 'Konradinerallee 11, 65189 Wiesbaden',
        'aciklama': 'Wiesbaden Sağlık Dairesi. Aşı, bulaşıcı hastalık bildirimi, çocuk sağlığı taramaları ve göçmen sağlık hizmetleri için başvuru noktası.',
        'website': 'https://www.wiesbaden.de/gesundheitsamt',
        'maps_url': 'https://maps.google.com/?q=Gesundheitsamt+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Zahnklinik — Universitätsklinikum Frankfurt (Yakın)',
        'adres': 'Theodor-Stern-Kai 7, 60590 Frankfurt am Main',
        'aciklama': 'Wiesbaden\'da acil diş kliniği sınırlıdır. Frankfurt Üniversite Diş Kliniği, Wiesbaden\'a S-Bahn ile 35 dakika uzaklıkta acil diş hizmetleri sunar.',
        'website': 'https://www.kgu.de/zahnmedizin',
        'maps_url': 'https://maps.google.com/?q=Zahnklinik+Frankfurt+Universitätsklinikum',
        'kapak_resmi': '',
        'icerik': '',
    },
]

EGITIM = [
    {
        'ad': 'VHS Wiesbaden — Volkshochschule',
        'adres': 'Alcide-De-Gasperi-Str. 4, 65197 Wiesbaden',
        'aciklama': 'Wiesbaden Halk Eğitim Merkezi. Almanca dil kursları (A1–C2), BAMF entegrasyon kursları, mesleki eğitim ve genel kültür programları sunmaktadır.',
        'website': 'https://www.vhs-wiesbaden.de',
        'maps_url': 'https://maps.google.com/?q=VHS+Wiesbaden',
        'kapak_resmi': '',
        'icerik': """<p>Wiesbaden'a yeni taşındıysanız ilk durağınız VHS (Volkshochschule) olmalı. Burada hem Almanca öğrenebilir, hem mesleki sertifikalar alabilir, hem de şehirdeki Türk topluluğuyla bağlantı kurabilirsiniz.</p>

<h2>Almanca Kursları</h2>
<div class="info-box"><strong>Seviyeler:</strong> A1'den C2'ye tüm seviyelerde grup dersleri. Kayıt döneminde erken başvurmak önerilir — popüler saatler hızlı dolar.</div>
<div class="info-box"><strong>BAMF Entegrasyon Kursu:</strong> VHS Wiesbaden yetkili BAMF kursu sağlayıcısıdır. Berechtigungsschein (yetki belgesi) ile ücretsiz veya indirimli katılım mümkündür.</div>
<div class="info-box"><strong>Deutschtest für Zuwanderer (DTZ):</strong> B1 sınav merkezi olarak VHS, göçmenlik belgesi için gerekli sınavı da düzenlemektedir.</div>

<h2>Diğer Eğitimler</h2>
<div class="info-box"><strong>Bilgisayar & Dijital:</strong> MS Office, temel bilgisayar kullanımı, internet güvenliği gibi pratik dersler.</div>
<div class="info-box"><strong>Sağlık & Spor:</strong> Yoga, pilates ve sağlıklı yaşam kursları da programda yer almaktadır.</div>

<h2>Kayıt</h2>
<p>Online kayıt: <a href="https://www.vhs-wiesbaden.de" target="_blank" rel="noopener">vhs-wiesbaden.de</a> — Telefon: 0611 31-4040</p>""",
    },
    {
        'ad': 'Hochschule RheinMain',
        'adres': 'Kurt-Schumacher-Ring 18, 65197 Wiesbaden',
        'aciklama': 'Wiesbaden\'ın uygulamalı bilimler üniversitesi. Mühendislik, işletme, tasarım ve sosyal bilimler alanlarında Almanca ve İngilizce lisans/yüksek lisans programları.',
        'website': 'https://www.hs-rm.de',
        'maps_url': 'https://maps.google.com/?q=Hochschule+RheinMain+Wiesbaden',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Hochschule_RheinMain_Kurt-Schumacher-Ring.jpg/1280px-Hochschule_RheinMain_Kurt-Schumacher-Ring.jpg',
        'icerik': '',
    },
    {
        'ad': 'Schulamt Wiesbaden — Okul Kayıt',
        'adres': 'Friedrichstr. 35, 65185 Wiesbaden',
        'aciklama': 'Wiesbaden Hessen Okul Dairesi. Yeni taşınan aileler için çocuk okul kaydı, okul türü danışmanlığı ve özel eğitim ihtiyaçları konularında rehberlik.',
        'website': 'https://ssa.hessen.de/wiesbaden',
        'maps_url': 'https://maps.google.com/?q=Schulamt+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'BAMF Integrationskurs Beratung — Wiesbaden',
        'adres': 'Wiesbaden, Hessen',
        'aciklama': 'BAMF entegrasyon kursu danışmanlığı. Yeni gelenler için kurs hakkı ve yükümlülüğü, ücretsiz kurs başvurusu ve yakın kurs merkezleri hakkında bilgi.',
        'website': 'https://bamf-navi.bamf.de',
        'maps_url': '',
        'kapak_resmi': '',
        'icerik': '',
    },
]

ALISVERIS = [
    {
        'ad': 'Mauritius Galerie Wiesbaden',
        'adres': 'Kirchgasse 38, 65185 Wiesbaden',
        'aciklama': 'Wiesbaden şehir merkezindeki alışveriş merkezi. 60\'tan fazla mağaza, restoranlar ve hizmet noktalarıyla hafta içi ve hafta sonu açık.',
        'website': 'https://www.mauritius-galerie.de',
        'maps_url': 'https://maps.google.com/?q=Mauritius+Galerie+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Nerotal-Passage Wiesbaden',
        'adres': 'Nerotal 1a, 65193 Wiesbaden',
        'aciklama': 'Wiesbaden\'ın köklü alışveriş pasajı. Butikler, kafe ve hizmet mağazalarıyla merkeze yakın konumda yer almaktadır.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Nerotal-Passage+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
    {
        'ad': 'Forum am Marktplatz Wiesbaden',
        'adres': 'Marktplatz 6, 65183 Wiesbaden',
        'aciklama': 'Wiesbaden Marktplatz\'ın hemen yanındaki alışveriş ve hizmet kompleksi. Moda mağazaları, süpermarket ve restoranlar bir arada.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Forum+am+Marktplatz+Wiesbaden',
        'kapak_resmi': '',
        'icerik': '',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')
    Yer = apps.get_model('yerler', 'Yer')

    try:
        eyalet = Eyalet.objects.get(kod='HE')
        wiesbaden = Stadt.objects.get(slug='wiesbaden')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return

    kategoriler = [
        ('ibadet', IBADET),
        ('tuv', TUV),
        ('saglik', SAGLIK),
        ('egitim', EGITIM),
        ('alisveris', ALISVERIS),
    ]

    for kategori_slug, yerler in kategoriler:
        for veri in yerler:
            Yer.objects.get_or_create(
                ad=veri['ad'],
                stadt=wiesbaden,
                defaults={
                    'eyalet': eyalet,
                    'scope': 'stadt',
                    'tur': 'yer',
                    'kategori': kategori_slug,
                    'adres': veri['adres'],
                    'sehir': 'Wiesbaden',
                    'aciklama': veri['aciklama'],
                    'kapak_resmi': veri.get('kapak_resmi', ''),
                    'website': veri.get('website', ''),
                    'maps_url': veri.get('maps_url', ''),
                    'icerik': veri.get('icerik', ''),
                    'aktif': True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = (
        [v['ad'] for v in IBADET] +
        [v['ad'] for v in TUV] +
        [v['ad'] for v in SAGLIK] +
        [v['ad'] for v in EGITIM] +
        [v['ad'] for v in ALISVERIS]
    )
    Yer.objects.filter(ad__in=adlar, sehir='Wiesbaden').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0019_yerkategori_seed'),
        ('stadt', '0010_seed_baskentler'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
