from django.db import migrations

RESMI_KURUM = [
    {'ad': 'Jobcenter Hannover',          'adres': 'Vahrenwalder Str. 245, 30179 Hannover', 'aciklama': 'Hannover Jobcenter, işsizlik yardımı ve iş arama desteği sunan başlıca sosyal hizmet kuruluşudur.', 'website': 'https://www.jobcenter-hannover.de/', 'maps_url': 'https://maps.google.com/?q=Jobcenter+Hannover+Vahrenwalder+Str+245'},
    {'ad': 'Ausländerbehörde Hannover',   'adres': 'Hamburger Allee 25, 30161 Hannover',   'aciklama': 'Hannover Yabancılar Dairesi, oturma izni, vize uzatma ve vatandaşlık işlemlerini yürüten resmi kurumdur.',          'website': 'https://auslaenderbehoerdeonline.hannover-stadt.de/', 'maps_url': 'https://maps.google.com/?q=Ausländerbehörde+Hannover+Hamburger+Allee+25'},
    {'ad': 'Bürgeramt Hannover (Mitte)',  'adres': 'Trammplatz 2, 30159 Hannover',          'aciklama': 'Hannover Merkez Bürgeramt, nüfus cüzdanı, pasaport ve anmeldeung gibi temel belediye hizmetlerini sunmaktadır.',    'website': 'https://www.hannover.de/', 'maps_url': 'https://maps.google.com/?q=Bürgeramt+Hannover+Trammplatz+2'},
    {'ad': 'Agentur für Arbeit Hannover', 'adres': 'Brühlstr. 12, 30169 Hannover',          'aciklama': 'Hannover İş ve Meslek Kurumu, işsizlik sigortası, meslek danışmanlığı ve iş ilanları konusunda hizmet vermektedir.', 'website': 'https://www.arbeitsagentur.de/', 'maps_url': 'https://maps.google.com/?q=Agentur+für+Arbeit+Hannover+Brühlstr+12'},
    {'ad': 'Finanzamt Hannover',          'adres': 'Schiffgraben 4, 30159 Hannover',        'aciklama': 'Hannover Vergi Dairesi, gelir vergisi beyannamesi ve vergi numarası işlemlerinin yürütüldüğü resmi kurumdur.',         'website': 'https://www.hannover.de/', 'maps_url': 'https://maps.google.com/?q=Finanzamt+Hannover+Schiffgraben+4'},
]

IBADET = [
    {'ad': 'DITIB Türkisch-Islamische Gemeinde zu Hannover (Merkez Camii)', 'adres': 'Stiftstraße 10, 30159 Hannover',    'aciklama': 'Hannover\'in merkez DITIB camisi olup Türk-İslam toplumunun en büyük buluşma ve ibadet merkezidir. Cuma namazlarında bin\'i aşkın Müslüman\'ı ağırlayan camide Türkçe ve Almanca hizmetler verilmektedir.', 'website': 'https://www.ditib-hannover.de/', 'maps_url': 'https://maps.google.com/?q=Stiftstraße+10+30159+Hannover'},
    {'ad': 'DITIB İlim ve İrfan Camii (Bothfeld-Vahrenheide)',             'adres': 'Leipziger Str. 112, 30179 Hannover', 'aciklama': 'Hannover\'in kuzey semti Bothfeld-Vahrenheide\'de hizmet veren bu DITIB camisi, bölgenin Türk-Müslüman toplumuna ibadet ve sosyal etkinlik merkezi olarak hizmet vermektedir.',                              'website': 'https://www.ditib-hannover.de/', 'maps_url': 'https://maps.google.com/?q=Leipziger+Str.+112+30179+Hannover'},
    {'ad': 'IGMG Hannover Merkez – Ayasofya Camii',                        'adres': 'Weidendamm 9, 30167 Hannover',      'aciklama': '1982\'den bu yana Hannover Müslüman topluluğunun önemli bir merkezi olan Ayasofya Camii, kubbeli ve minareli mimarisiyle bölgenin köklü İslam ibadethanelerinden biridir.',                                        'website': 'https://www.igmghannover.de/', 'maps_url': 'https://maps.google.com/?q=Weidendamm+9+30167+Hannover'},
]

TUV = [
    {'ad': 'TÜV NORD Station Hannover-Döhren',         'adres': 'Thurnithistraße 11, 30519 Hannover',  'aciklama': 'Hannover\'in güney bölgesinde yer alan TÜV NORD istasyonu; araç muayenesi (HU), egzoz testi (AU) ve hasar tespiti hizmetleri sunmaktadır.',              'website': 'https://www.tuev-nord.de/', 'maps_url': 'https://maps.google.com/?q=Thurnithistraße+11+30519+Hannover'},
    {'ad': 'TÜV NORD Station Hannover-Bornum (Linden)', 'adres': 'Bornumer Str. 148, 30453 Hannover',  'aciklama': 'Hannover\'in batı yakasında yer alan TÜV NORD Bornum istasyonu, araç muayenesi ve teknik denetim hizmetlerini sunmaktadır.',                            'website': 'https://www.tuev-nord.de/', 'maps_url': 'https://maps.google.com/?q=Bornumer+Str.+148+30453+Hannover'},
    {'ad': 'TÜV NORD Station Hannover-Anderten',        'adres': 'Hägenstraße 4a, 30559 Hannover',     'aciklama': 'Hannover\'in doğu ilçesinde konumlanan Anderten TÜV NORD istasyonu, Hauptuntersuchung ve diğer araç teknik muayene hizmetleri sunmaktadır.',             'website': 'https://www.tuev-nord.de/', 'maps_url': 'https://maps.google.com/?q=Hägenstraße+4a+30559+Hannover'},
]

SAGLIK = [
    {'ad': 'Medizinische Hochschule Hannover (MHH)',  'adres': 'Carl-Neuberg-Straße 1, 30625 Hannover',   'aciklama': 'Almanya\'nın en büyük üniversite hastanelerinden biri olan MHH, 1.520 yatak kapasitesiyle yılda yaklaşık 56.000 hastaya hizmet vermektedir. 24 saat açık merkezi acil servisi mevcuttur.',          'website': 'https://www.mhh.de/', 'maps_url': 'https://maps.google.com/?q=Carl-Neuberg-Straße+1+30625+Hannover'},
    {'ad': 'KRH Klinikum Siloah',                    'adres': 'Stadionbrücke 4, 30459 Hannover',          'aciklama': 'Hannover Bölge Klinik Ağı\'nın önemli hastanelerinden biri olan Klinikum Siloah, 24 saat acil servis hizmeti vermekte olup geniş bir tıbbi hizmet yelpazesi sunmaktadır.',                          'website': 'https://siloah.krh.de/', 'maps_url': 'https://maps.google.com/?q=Stadionbrücke+4+30459+Hannover'},
    {'ad': 'Diakovere Henriettenstift Hannover',     'adres': 'Marienstraße 72-90, 30171 Hannover',       'aciklama': 'Hannover\'in köklü hastanelerinden biri olan Henriettenstift, ortopedi ve travmatoloji alanındaki uzmanlığıyla öne çıkmaktadır. Poliklinik hizmetleri hafta içi ve hafta sonu sunulmaktadır.',       'website': 'https://www.diakovere.de/', 'maps_url': 'https://maps.google.com/?q=Marienstraße+72+30171+Hannover'},
    {'ad': 'KRH Klinikum Region Hannover',           'adres': 'Roesebeckstr. 15, 30449 Hannover',         'aciklama': 'KRH, Hannover bölgesindeki birden fazla hastaneyi yöneten sağlık grubudur. Bölgede 24 saat acil hizmet veren birden fazla şubesi bulunmaktadır.',                                                      'website': 'https://www.krh.de/', 'maps_url': 'https://maps.google.com/?q=KRH+Klinikum+Region+Hannover'},
]

EGITIM = [
    {'ad': 'VHS Hannover (Volkshochschule)',              'adres': 'Burgstraße 14, 30159 Hannover',      'aciklama': 'Hannover Halk Yüksekokulu, BAMF onaylı entegrasyon kursları, A1\'den B2\'ye Almanca dil kursları ve Türkçe dil kursları sunmaktadır.',                                                         'website': 'https://www.vhs-hannover.de/', 'maps_url': 'https://maps.google.com/?q=VHS+Hannover+Burgstraße+14'},
    {'ad': 'VHS Hannover – Entegrasyon Kursları',         'adres': 'Burgstraße 14, 30159 Hannover',      'aciklama': 'VHS Hannover, BAMF tarafından yetkilendirilmiş entegrasyon kursları sunmaktadır. Bu kurslar B1 seviyesinde Almanca öğrenmeyi ve Almanya\'daki toplumsal yaşama entegrasyonu desteklemektedir.',   'website': 'https://www.vhs-hannover.de/vhs-programm/deutsch-integration/integrationskurse', 'maps_url': 'https://maps.google.com/?q=VHS+Hannover+Burgstraße+14'},
    {'ad': 'Hannover DITIB Türk Eğitim Merkezi',          'adres': 'Stiftstraße 10, 30159 Hannover',     'aciklama': 'DITIB bünyesinde faaliyet gösteren Türkçe dil kursları ve kültürel eğitim programları, Türk kökenli ailelerin çocuklarının anadillerini korumalarına destek vermektedir.',                      'website': 'https://www.ditib-hannover.de/', 'maps_url': 'https://maps.google.com/?q=Stiftstraße+10+30159+Hannover'},
]

ALISVERIS = [
    {'ad': 'Sitar Lebensmittel-Markt',    'adres': 'Melanchthonstraße 47, 30165 Hannover', 'aciklama': 'Hannover Nordstadt\'ta taze helal ürünler ve Türk ile Doğu mutfağı malzemeleri sunan önde gelen Türk marketi; geniş meyve-sebze yelpazesi ve organik ürünleriyle öne çıkmaktadır.',  'website': 'https://www.sitarmarkt.de/', 'maps_url': 'https://maps.google.com/?q=Melanchthonstraße+47+30165+Hannover'},
    {'ad': 'Divan Market',                'adres': 'Goethestraße 6, 30159 Hannover',       'aciklama': 'Hannover şehir merkezinde Steintor yakınlarında konumlanan Divan Market, taze meyve-sebze, Türk baharatları, çay çeşitleri ve geleneksel Türk gıda ürünleriyle geniş bir müşteri kitlesine hizmet vermektedir.', 'website': 'http://www.divan-market.de/', 'maps_url': 'https://maps.google.com/?q=Goethestraße+6+30159+Hannover'},
    {'ad': 'Ernst-August-Galerie (AVM)',  'adres': 'Ernst-August-Platz 2, 30159 Hannover', 'aciklama': 'Hannover Hauptbahnhof\'un hemen karşısında yer alan Ernst-August-Galerie, 100\'den fazla mağaza ve restoran barındıran şehrin en merkezi alışveriş merkezidir.',                          'website': 'https://www.ernst-august-galerie.de/', 'maps_url': 'https://maps.google.com/?q=Ernst-August-Platz+2+30159+Hannover'},
    {'ad': 'Galeria Hannover (Kröpcke)', 'adres': 'Georgstraße 32, 30159 Hannover',        'aciklama': 'Hannover\'in işlek Kröpcke meydanı yakınında yer alan Galeria, çok katlı yapısıyla giyim, elektronik, ev eşyaları ve gıda gibi geniş bir ürün yelpazesi sunmaktadır.',                   'website': 'https://www.galeria.de/', 'maps_url': 'https://maps.google.com/?q=Georgstraße+32+30159+Hannover'},
]

GEZI = [
    {'ad': 'Herrenhäuser Gärten',                     'adres': 'Herrenhäuser Straße 3c, 30419 Hannover',  'aciklama': 'Avrupa\'nın en önemli Barok bahçelerinden biri olan Herrenhäuser Gärten, dört ayrı bahçe bölümünden oluşan muhteşem bir yeşil alan kompleksidir.',                           'website': 'https://herrenhaeuser-gaerten.hannover.de/', 'maps_url': 'https://maps.google.com/?q=Herrenhäuser+Gärten+Hannover'},
    {'ad': 'Neues Rathaus (Yeni Belediye Binası)',     'adres': 'Platz der Menschenrechte 1, 30159 Hannover', 'aciklama': '1901-1913 yılları arasında inşa edilen Neues Rathaus, Neo-Rönesans mimarisinin görkemli bir örneği olup 97,7 metrelik kubbesiyle şehrin siluetine hakimdir.',                 'website': 'https://www.hannover.de', 'maps_url': 'https://maps.google.com/?q=Neues+Rathaus+Hannover'},
    {'ad': 'Maschsee',                                'adres': 'Rudolf-von-Bennigsen-Ufer, 30173 Hannover', 'aciklama': '78 hektarlık yüzey alanı ve 6 kilometrelik sahil şeridiyle Hannover\'in en gözde rekreasyon alanıdır. Yaz aylarında yelken, kano ve plaj etkinlikleri düzenlenmektedir.',  'website': 'https://www.hannover.de', 'maps_url': 'https://maps.google.com/?q=Maschsee+Hannover'},
    {'ad': 'Erlebniszoo Hannover',                    'adres': 'Adenauerallee 1, 30175 Hannover',           'aciklama': 'Birbirinden farklı tema dünyalarına bölünmüş yenilikçi tasarımıyla Almanya\'nın en çok ziyaret edilen hayvanat bahçelerinden biri; 2.400\'den fazla hayvan barındırmaktadır.',  'website': 'https://www.zoo-hannover.de/', 'maps_url': 'https://maps.google.com/?q=Erlebniszoo+Hannover+Adenauerallee+1'},
    {'ad': 'Marktkirche St. Georgii et Jacobi',       'adres': 'Hanns-Lilje-Platz 2, 30159 Hannover',       'aciklama': '14. yüzyılda inşa edilen Marktkirche, Kuzey Almanya tuğla Gotiği üslubunun en önemli örneklerinden olup 97 metrelik kulesiyle eski şehrin sembolüdür.',                      'website': 'https://www.marktkirche-hannover.de/', 'maps_url': 'https://maps.google.com/?q=Marktkirche+Hannover+Hanns-Lilje-Platz'},
    {'ad': 'Leineschloss (Niedersächsischer Landtag)', 'adres': 'Hannah-Arendt-Platz 1, 30159 Hannover',    'aciklama': '1637\'de inşa edilen Leineschloss, 19. yüzyılda Hannover Krallığı\'nın sarayıydı; bugün Aşağı Saksonya Eyalet Parlamentosu\'na ev sahipliği yapmaktadır.',                     'website': 'https://www.landtag-niedersachsen.de/', 'maps_url': 'https://maps.google.com/?q=Leineschloss+Hannover+Hannah-Arendt-Platz'},
    {'ad': 'Sprengel Museum Hannover',                'adres': 'Kurt-Schwitters-Platz 1, 30169 Hannover',   'aciklama': '1979\'da açılan Sprengel Museum, Max Ernst, Paul Klee ve Kurt Schwitters\'e ait 4.000\'den fazla eserle Almanya\'nın önde gelen modern sanat müzelerinden biridir.',             'website': 'https://www.sprengel-museum.de/', 'maps_url': 'https://maps.google.com/?q=Sprengel+Museum+Hannover+Kurt-Schwitters-Platz'},
    {'ad': 'Nanas (Niki de Saint Phalle Heykelleri)', 'adres': 'Leibnizufer, 30159 Hannover',               'aciklama': '1974\'te Leibnizufer kıyısına yerleştirilen üç renkli dev heykel, Hannover\'in en tanınmış sembollerinden biridir. Sanatçı Niki de Saint Phalle\'nin 5 metreyi aşan bu figürleri şehrin ikonuna dönüşmüştür.', 'website': 'https://www.visit-hannover.com', 'maps_url': 'https://maps.google.com/?q=Nanas+Leibnizufer+Hannover'},
    {'ad': 'Aegidienkirche (Savaş Anıtı)',            'adres': 'Aegidienkirchhof 1, 30159 Hannover',         'aciklama': '14. yüzyıldan kalma ve 1943\'te yıkılan Aegidienkirche, bugün savaş kurbanlarına adanmış bir anıt olarak yıkıntı hâlinde bırakılmıştır. Her yıl 6 Ağustos\'ta Hiroşima anması düzenlenmektedir.', 'website': 'https://www.visit-hannover.com', 'maps_url': 'https://maps.google.com/?q=Aegidienkirche+Hannover'},
    {'ad': 'Niedersächsisches Landesmuseum Hannover', 'adres': 'Willy-Brandt-Allee 5, 30169 Hannover',      'aciklama': 'Aşağı Saksonya\'nın en büyük eyalet müzesi; prehistorya, doğa tarihi ve güzel sanatlar koleksiyonlarını tek çatı altında barındırmaktadır. Rubens\'ten Rembrandt\'a uzanan koleksiyon ve mamut fosili öne çıkmaktadır.', 'website': 'https://landesmuseum-hannover.de/', 'maps_url': 'https://maps.google.com/?q=Landesmuseum+Hannover+Willy-Brandt-Allee'},
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')
    try:
        eyalet = Eyalet.objects.get(kod='NI')
        sehir  = Stadt.objects.get(slug='hannover')
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
                    'eyalet': eyalet, 'scope': 'stadt', 'tur': 'yer',
                    'kategori': kategori_slug, 'sehir': 'Hannover',
                    'adres': veri['adres'], 'aciklama': veri['aciklama'],
                    'kapak_resmi': '', 'website': veri.get('website', ''),
                    'maps_url': veri.get('maps_url', ''), 'icerik': '',
                    'aktif': True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = [v['ad'] for liste in [RESMI_KURUM, IBADET, TUV, SAGLIK, EGITIM, GEZI, ALISVERIS] for v in liste]
    Yer.objects.filter(ad__in=adlar, sehir='Hannover').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0043_seed_muenchen_yerler'),
        ('stadt',  '0043_hannover_action_links_aktiv'),
    ]
    operations = [migrations.RunPython(seed, unseed)]
