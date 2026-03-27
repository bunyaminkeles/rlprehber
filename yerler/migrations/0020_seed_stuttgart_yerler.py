from django.db import migrations

IBADET = [
    {
        'ad': 'DITIB Fatih Camii Stuttgart',
        'adres': 'Rosenbergstraße 10, 70176 Stuttgart',
        'aciklama': 'Stuttgart şehir merkezine yakın konumda bulunan DİTİB\'e bağlı cami ve kültür merkezi.',
        'kapak_resmi': '',
        'website': 'https://www.ditib.de',
        'maps_url': 'https://maps.google.com/?q=DITIB+Fatih+Camii+Stuttgart+Rosenbergstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'Eyüp Sultan Camii Stuttgart',
        'adres': 'Haußmannstraße 9, 70188 Stuttgart',
        'aciklama': 'Stuttgart\'ın doğusunda yer alan Eyüp Sultan Camii, Müslüman topluluğuna ibadet ve kültürel etkinlik hizmetleri sunmaktadır.',
        'kapak_resmi': '',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Eyüp+Sultan+Camii+Stuttgart+Hau%C3%9Fmannstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'IGMG Stuttgart – Böblinger Straße Mescidi',
        'adres': 'Böblinger Straße 97, 70199 Stuttgart',
        'aciklama': 'İslam Toplumu Millî Görüş bünyesinde hizmet veren cami ve kültür merkezi; Kuran kursları ve sosyal etkinlikler düzenlenmektedir.',
        'kapak_resmi': '',
        'website': 'https://www.igmg.org',
        'maps_url': 'https://maps.google.com/?q=IGMG+Stuttgart+B%C3%B6blinger+Stra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'Sehitlik Camii Stuttgart-Zuffenhausen',
        'adres': 'Unterländer Straße 31, 70435 Stuttgart',
        'aciklama': 'Stuttgart-Zuffenhausen semtinde bulunan ve bölge Türk topluluğuna hizmet eden cami; haftalık Cuma namazı ve din eğitimi verilmektedir.',
        'kapak_resmi': '',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Sehitlik+Camii+Stuttgart+Zuffenhausen+Unterl%C3%A4nder+Stra%C3%9Fe',
        'icerik': '',
    },
]

TUV = [
    {
        'ad': 'TÜV SÜD Service-Center Stuttgart-Möhringen',
        'adres': 'Filderstraße 30, 70599 Stuttgart',
        'aciklama': 'TÜV SÜD araç muayene istasyonu; HU/AU periyodik araç muayenesi ve egzoz ölçümü yapılmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.tuvsud.com/de-de/branchen/mobilitaet-und-automotive/hauptuntersuchung',
        'maps_url': 'https://maps.google.com/?q=TÜV+SÜD+Stuttgart+M%C3%B6hringen+Filderstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'DEKRA Automobil Stuttgart-Feuerbach',
        'adres': 'Solitudeallee 60, 70439 Stuttgart',
        'aciklama': 'DEKRA araç muayene merkezi; HU/AU muayenesi, hasar tespiti ve ekspertiz hizmetleri sunulmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.dekra.de/de/hauptuntersuchung-pkw/',
        'maps_url': 'https://maps.google.com/?q=DEKRA+Stuttgart+Feuerbach+Solitudeallee',
        'icerik': '',
    },
    {
        'ad': 'GTÜ Prüfstelle Stuttgart-Ost',
        'adres': 'Ulmer Straße 120, 70188 Stuttgart',
        'aciklama': 'GTÜ bağımsız araç muayene kuruluşu; randevusuz veya uygun randevu ile hızlı HU/AU muayenesi yapılmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.gtue.de',
        'maps_url': 'https://maps.google.com/?q=GTÜ+Stuttgart+Ulmer+Stra%C3%9Fe',
        'icerik': '',
    },
]

SAGLIK = [
    {
        'ad': 'Klinikum Stuttgart – Katharinenhospital',
        'adres': 'Kriegsbergstraße 60, 70174 Stuttgart',
        'aciklama': 'Baden-Württemberg\'in en büyük hastanelerinden biri olan Klinikum Stuttgart, tüm uzmanlık dallarında tedavi hizmeti sunmaktadır.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Stuttgart_-_Katharinenhospital.jpg/1280px-Stuttgart_-_Katharinenhospital.jpg',
        'website': 'https://www.klinikum-stuttgart.de',
        'maps_url': 'https://maps.google.com/?q=Katharinenhospital+Stuttgart+Kriegsbergstra%C3%9Fe',
        'icerik': '<p>Klinikum Stuttgart, Katharinenhospital, Olgahospital ve Bad Cannstatt kliniklerinden oluşan Stuttgart\'ın en büyük hastane grubudur. Yılda 90.000\'den fazla yatan hastaya hizmet vermektedir.</p><h2>Acil Servis</h2><p>7/24 açık acil servis hizmeti sunulmaktadır. Acil olmayan durumlarda önce hausarztınızı veya 116117 hattını aramanız önerilir.</p><div class="info-box"><strong>Adres:</strong> Kriegsbergstraße 60, 70174 Stuttgart</div><div class="info-box"><strong>Telefon:</strong> 0711 278-0</div>',
    },
    {
        'ad': 'Robert-Bosch-Krankenhaus Stuttgart',
        'adres': 'Auerbachstraße 110, 70376 Stuttgart',
        'aciklama': 'Robert Bosch Vakfı\'na ait modern hastane; kardiyoloji, onkoloji ve dahiliye başta olmak üzere birçok uzmanlık alanında ileri düzey tedavi imkânı sunmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.rbk.de',
        'maps_url': 'https://maps.google.com/?q=Robert-Bosch-Krankenhaus+Stuttgart+Auerbachstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'Marienhospital Stuttgart',
        'adres': 'Böheimstraße 37, 70199 Stuttgart',
        'aciklama': 'Katolik vakfına ait Marienhospital, Stuttgart\'ın köklü hastanelerinden biri olup iç hastalıklar, cerrahi ve doğum gibi alanlarda kapsamlı tıbbi hizmet sunmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.marienhospital-stuttgart.de',
        'maps_url': 'https://maps.google.com/?q=Marienhospital+Stuttgart+B%C3%B6heimstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'Diakonie-Klinikum Stuttgart',
        'adres': 'Rosenbergstraße 38, 70176 Stuttgart',
        'aciklama': 'Diyakoni bünyesinde faaliyet gösteren klinik; ortopedi, nöroloji ve dahiliye alanlarında uzmanlaşmış tedavi hizmetleri sunmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.diak-stuttgart.de',
        'maps_url': 'https://maps.google.com/?q=Diakonie-Klinikum+Stuttgart+Rosenbergstra%C3%9Fe',
        'icerik': '',
    },
]

EGITIM = [
    {
        'ad': 'Universität Stuttgart',
        'adres': 'Keplerstraße 7, 70174 Stuttgart',
        'aciklama': 'Baden-Württemberg\'in önde gelen teknik üniversitelerinden biri; mühendislik, mimarlık ve doğa bilimleri alanlarında dünya çapında tanınan araştırma kurumu.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Stuttgart_Universit%C3%A4t_Stadtmitte.jpg/1280px-Stuttgart_Universit%C3%A4t_Stadtmitte.jpg',
        'website': 'https://www.uni-stuttgart.de',
        'maps_url': 'https://maps.google.com/?q=Universität+Stuttgart+Keplerstra%C3%9Fe',
        'icerik': '<p>Universität Stuttgart, 1829 yılında kurulan ve bugün 25.000\'den fazla öğrenciye ev sahipliği yapan köklü bir araştırma üniversitesidir. Mühendislik, fen bilimleri, mimarlık ve şehir planlama alanlarında güçlü programlar sunmaktadır.</p><h2>Uluslararası Öğrenciler</h2><p>Üniversite, uluslararası öğrencilere yönelik kapsamlı destek hizmetleri, danışmanlık ve Almanca dil kursları sunmaktadır. Uluslararası ofis aracılığıyla vize, tanınma ve burs konularında yardım alınabilmektedir.</p><div class="info-box"><strong>Adres:</strong> Keplerstraße 7, 70174 Stuttgart</div><div class="info-box"><strong>Website:</strong> www.uni-stuttgart.de</div>',
    },
    {
        'ad': 'Volkshochschule Stuttgart',
        'adres': 'Rotebühlplatz 28, 70173 Stuttgart',
        'aciklama': 'Stuttgart Halk Yüksekokulu; Almanca dil kursları, mesleki eğitimler, entegrasyon kursları ve kültürel programlar dahil geniş bir kurs yelpazesi sunmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.vhs-stuttgart.de',
        'maps_url': 'https://maps.google.com/?q=Volkshochschule+Stuttgart+Roteb%C3%BChlplatz',
        'icerik': '',
    },
    {
        'ad': 'Universität Hohenheim',
        'adres': 'Schloss Hohenheim 1, 70599 Stuttgart',
        'aciklama': 'Tarım bilimleri, doğa bilimleri ve ekonomi alanlarında uzmanlaşmış; Stuttgart güneyindeki Hohenheim sarayı yerleşkesindeki köklü araştırma üniversitesi.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Schloss_Hohenheim_Stuttgart.jpg/1280px-Schloss_Hohenheim_Stuttgart.jpg',
        'website': 'https://www.uni-hohenheim.de',
        'maps_url': 'https://maps.google.com/?q=Universität+Hohenheim+Stuttgart',
        'icerik': '',
    },
    {
        'ad': 'DHBW Stuttgart',
        'adres': 'Rotebühlplatz 41, 70178 Stuttgart',
        'aciklama': 'Duale Hochschule Baden-Württemberg Stuttgart; iş dünyası ile akademik eğitimi birleştiren çift aşamalı lisans programları sunmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.dhbw-stuttgart.de',
        'maps_url': 'https://maps.google.com/?q=DHBW+Stuttgart+Roteb%C3%BChlplatz',
        'icerik': '',
    },
]

GEZI = [
    {
        'ad': 'Wilhelma – Zoologisch-Botanischer Garten',
        'adres': 'Neckartalstraße 2, 70376 Stuttgart',
        'aciklama': 'Avrupa\'nın tek birleşik zooloji ve botanik bahçesi olan Wilhelma, 11.000\'den fazla hayvan türüne ve nadir bitki koleksiyonlarına ev sahipliği yapmaktadır.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Stuttgart_Wilhelma_001.JPG/1280px-Stuttgart_Wilhelma_001.JPG',
        'website': 'https://www.wilhelma.de',
        'maps_url': 'https://maps.google.com/?q=Wilhelma+Stuttgart+Neckartalstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'Mercedes-Benz Museum Stuttgart',
        'adres': 'Mercedesstraße 100, 70372 Stuttgart',
        'aciklama': 'Otomobil tarihini benzersiz mimarisiyle sunan Mercedes-Benz Müzesi, 130 yılı aşkın tarihe ait 160\'tan fazla aracı sergilemektedir.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Stuttgart_-_Mercedes-Benz_Museum_%28Exterior%29.jpg/1280px-Stuttgart_-_Mercedes-Benz_Museum_%28Exterior%29.jpg',
        'website': 'https://www.mercedes-benz.com/en/art-and-culture/museum/',
        'maps_url': 'https://maps.google.com/?q=Mercedes-Benz+Museum+Stuttgart+Mercedesstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'Stuttgarter Fernsehturm',
        'adres': 'Jahnstraße 369, 70597 Stuttgart',
        'aciklama': 'Dünyanın ilk betonarme televizyon kulesi olan Stuttgart TV Kulesi; şehrin panoramik manzarasını sunan seyir terası ve restoranı ile önemli bir turistik noktadır.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Fernsehturm_Stuttgart_2013.jpg/800px-Fernsehturm_Stuttgart_2013.jpg',
        'website': 'https://www.fernsehturm-stuttgart.de',
        'maps_url': 'https://maps.google.com/?q=Fernsehturm+Stuttgart+Jahnstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'Altes Schloss & Württemberg Devlet Müzesi',
        'adres': 'Schillerplatz 6, 70173 Stuttgart',
        'aciklama': 'Stuttgart\'ın tarihi merkezinde yer alan ortaçağ kalesi ve müzesi; Württemberg tarihi, arkeoloji ve kraliyet ailesi koleksiyonlarını sergilemektedir.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Altes_Schloss_Stuttgart.jpg/1280px-Altes_Schloss_Stuttgart.jpg',
        'website': 'https://www.landesmuseum-stuttgart.de',
        'maps_url': 'https://maps.google.com/?q=Altes+Schloss+Stuttgart+Schillerplatz',
        'icerik': '',
    },
    {
        'ad': 'Schloßplatz & Neues Schloss Stuttgart',
        'adres': 'Schloßplatz 4, 70173 Stuttgart',
        'aciklama': 'Stuttgart\'ın kalbi olan Schloßplatz meydanı ve 18. yüzyıldan kalma Neues Schloss; şehrin buluşma noktası ve kültürel etkinliklerin merkezi.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Stuttgart_Schlossplatz_2013.jpg/1280px-Stuttgart_Schlossplatz_2013.jpg',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Schlossplatz+Stuttgart',
        'icerik': '',
    },
    {
        'ad': 'Porsche Museum Stuttgart-Zuffenhausen',
        'adres': 'Porscheplatz 1, 70435 Stuttgart',
        'aciklama': 'Zuffenhausen\'da konumlanan Porsche Müzesi, 80\'den fazla tarihi araç ile markanın efsanevi yarış ve spor otomobil tarihini gözler önüne sermektedir.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Porsche-Museum_2009.jpg/1280px-Porsche-Museum_2009.jpg',
        'website': 'https://www.porsche.com/germany/aboutporsche/porschemuseum/',
        'maps_url': 'https://maps.google.com/?q=Porsche+Museum+Stuttgart+Zuffenhausen+Porscheplatz',
        'icerik': '',
    },
]

ALISVERIS = [
    {
        'ad': 'Milaneo Stuttgart',
        'adres': 'Mailänder Platz 7, 70173 Stuttgart',
        'aciklama': 'Stuttgart\'ın en büyük alışveriş merkezi olan Milaneo, 200\'den fazla mağaza, restoran ve kafeleriyle şehir merkezinde modern bir alışveriş deneyimi sunmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.milaneo.com',
        'maps_url': 'https://maps.google.com/?q=Milaneo+Stuttgart+Mail%C3%A4nder+Platz',
        'icerik': '',
    },
    {
        'ad': 'Königsbau Passagen Stuttgart',
        'adres': 'Königstraße 28, 70173 Stuttgart',
        'aciklama': 'Tarihi Königsbau binasına entegre edilmiş kapalı çarşı; moda, aksesuar ve gastronomi mağazalarıyla Königstraße\'nin kalbinde yer almaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.koenigsbau-passagen.de',
        'maps_url': 'https://maps.google.com/?q=K%C3%B6nigsbau+Passagen+Stuttgart+K%C3%B6nigstra%C3%9Fe',
        'icerik': '',
    },
    {
        'ad': 'Breuninger Stuttgart',
        'adres': 'Marktstraße 1-3, 70173 Stuttgart',
        'aciklama': 'Stuttgart\'ın köklü premium departmanlı mağazası Breuninger; moda, kozmetik, ev dekorasyonu ve gastronomi alanlarında geniş ürün yelpazesi sunmaktadır.',
        'kapak_resmi': '',
        'website': 'https://www.breuninger.com/de/',
        'maps_url': 'https://maps.google.com/?q=Breuninger+Stuttgart+Marktstra%C3%9Fe',
        'icerik': '',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')
    Yer = apps.get_model('yerler', 'Yer')

    try:
        eyalet = Eyalet.objects.get(kod='BW')
        sehir = Stadt.objects.get(slug='stuttgart')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return

    if not sehir.aktiv:
        sehir.aktiv = True
        sehir.save()

    kategoriler = [
        ('ibadet',    IBADET),
        ('tuv',       TUV),
        ('saglik',    SAGLIK),
        ('egitim',    EGITIM),
        ('gezi',      GEZI),
        ('alisveris', ALISVERIS),
    ]

    for kategori_slug, yerler in kategoriler:
        for veri in yerler:
            Yer.objects.get_or_create(
                ad=veri['ad'],
                stadt=sehir,
                defaults={
                    'eyalet':      eyalet,
                    'scope':       'stadt',
                    'tur':         'yer',
                    'kategori':    kategori_slug,
                    'adres':       veri['adres'],
                    'sehir':       'Stuttgart',
                    'aciklama':    veri['aciklama'],
                    'kapak_resmi': veri.get('kapak_resmi', ''),
                    'website':     veri.get('website', ''),
                    'maps_url':    veri.get('maps_url', ''),
                    'icerik':      veri.get('icerik', ''),
                    'aktif':       True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = (
        [v['ad'] for v in IBADET] +
        [v['ad'] for v in TUV] +
        [v['ad'] for v in SAGLIK] +
        [v['ad'] for v in EGITIM] +
        [v['ad'] for v in GEZI] +
        [v['ad'] for v in ALISVERIS]
    )
    Yer.objects.filter(ad__in=adlar, sehir='Stuttgart').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0019_seed_wiesbaden_yerler'),
        ('stadt', '0010_seed_baskentler'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
