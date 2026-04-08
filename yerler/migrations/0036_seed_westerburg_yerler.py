"""
Westerburg (Westerwald) — Önemli Yerler Seed Migrasyonu
Eyalet: Rheinland-Pfalz (RLP) | Kreis: Westerwaldkreis
"""
from django.db import migrations

RESMI_KURUM = [
    {
        'ad': 'Verbandsgemeindeverwaltung Westerburg',
        'adres': 'Neumarkt 1, 56457 Westerburg',
        'aciklama': 'Bürgerbüro, nüfus tescili, pasaport ve kimlik işlemleri. Online randevu alınabilir.',
        'website': 'https://www.vg-westerburg.de',
        'maps_url': 'https://maps.google.com/?q=Neumarkt+1,+56457+Westerburg',
    },
    {
        'ad': 'Kreisverwaltung Westerwaldkreis — Ausländerbehörde',
        'adres': 'Peter-Altmeier-Platz 1, 56410 Montabaur',
        'aciklama': 'Westerwaldkreis Yabancılar Dairesi (Welcome Center). Oturma izni için randevu zorunludur.',
        'website': 'https://www.westerwaldkreis.de/welcome-center-auslaenderbehoerde.html',
        'maps_url': 'https://maps.google.com/?q=Peter-Altmeier-Platz+1,+56410+Montabaur',
    },
    {
        'ad': 'Jobcenter Westerwaldkreis',
        'adres': 'Bahnhofstraße 1, 56410 Montabaur',
        'aciklama': 'Bürgergeld başvurusu, iş arama desteği ve sosyal yardım hizmetleri.',
        'website': 'https://www.westerwaldkreis.de/jobcenter.html',
        'maps_url': 'https://maps.google.com/?q=Bahnhofstra%C3%9Fe+1,+56410+Montabaur',
    },
    {
        'ad': 'Agentur für Arbeit Montabaur',
        'adres': 'Koblenzer Straße 2, 56410 Montabaur',
        'aciklama': 'Westerburg bölgesine hizmet veren İş Ajansı. ALG I ve mesleki rehberlik.',
        'website': 'https://www.arbeitsagentur.de/vor-ort/montabaur',
        'maps_url': 'https://maps.google.com/?q=Koblenzer+Stra%C3%9Fe+2,+56410+Montabaur',
    },
]

IBADET = [
    {
        'ad': 'İslam Cemaati — Westerburg / Westerwaldkreis',
        'adres': 'Westerwaldkreis',
        'aciklama': 'Westerburg çevresindeki Müslüman cemaat için ibadet mekanı. Detaylı bilgi için Westerwaldkreis İslam dernekleriyle iletişime geçin.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Moschee+Westerwaldkreis',
    },
]

TUV = [
    {
        'ad': 'TÜV / DEKRA — Montabaur bölgesi',
        'adres': 'Westerwaldkreis',
        'aciklama': 'En yakın araç muayene noktası için tuv.com veya dekra.de üzerinden "Montabaur" veya "Westerburg" aratın.',
        'website': 'https://www.tuv.com/de/tuv-rheinland-gruppe/',
        'maps_url': 'https://maps.google.com/?q=T%C3%9CV+Montabaur+Westerwald',
    },
]

SAGLIK = [
    {
        'ad': 'Marienhaus Klinikum Bendorf-Neuwied-Waldbreitbach',
        'adres': 'Klarastraße 22, 56170 Bendorf',
        'aciklama': 'Westerburg bölgesine yakın genel hastane. Dahiliye ve cerrahi hizmetleri.',
        'website': 'https://www.marienhaus-klinikum.de',
        'maps_url': 'https://maps.google.com/?q=Klarastra%C3%9Fe+22,+56170+Bendorf',
    },
    {
        'ad': 'Gemeinschaftspraxis — Westerburg Merkez',
        'adres': 'Westerburg (Westerwald)',
        'aciklama': 'Westerburg şehir merkezindeki aile hekimi ve uzman muayenehaneleri için Jameda.de üzerinden arama yapabilirsiniz.',
        'website': 'https://www.jameda.de',
        'maps_url': 'https://maps.google.com/?q=%C3%84rzte+Westerburg+Westerwald',
    },
]

EGITIM = [
    {
        'ad': 'VHS Westerwaldkreis — Westerburg',
        'adres': 'Westerwaldkreis',
        'aciklama': 'Almanca entegrasyon kursları ve mesleki eğitim. Kurs programı için vhs-westerwald.de adresini ziyaret edin.',
        'website': 'https://www.vhs-westerwald.de',
        'maps_url': 'https://maps.google.com/?q=VHS+Westerwaldkreis',
    },
    {
        'ad': 'Realschule plus und Gymnasium Westerburg',
        'adres': 'Im Weiherfeld 1, 56457 Westerburg',
        'aciklama': 'Westerburg\'un devlet okulu. İlkokul sonrası eğitim için bölgenin ana okulu.',
        'website': 'https://www.rsg-westerburg.de',
        'maps_url': 'https://maps.google.com/?q=Im+Weiherfeld+1,+56457+Westerburg',
    },
]

GEZI = [
    {
        'ad': 'Burg Westerburg (Westerburger Schloss)',
        'adres': 'Schloßstraße, 56457 Westerburg',
        'aciklama': 'Westerburg\'un simgesi olan tarihi şato. Oberwesterwald\'ın panorama manzarasını sunar.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Burg+Westerburg+56457',
    },
    {
        'ad': 'Westerwaldsteig — Westerburg güzergahı',
        'adres': 'Westerburg (Westerwald)',
        'aciklama': '235 km\'lik Westerwaldsteig yürüyüş rotasının Westerburg güzergahı. Orman ve tepe manzaraları.',
        'website': 'https://www.westerwaldsteig.de',
        'maps_url': 'https://maps.google.com/?q=Westerwaldsteig+Westerburg',
    },
]

ALISVERIS = [
    {
        'ad': 'Innenstadt Westerburg — Yerel Alışveriş',
        'adres': 'Neumarkt, 56457 Westerburg',
        'aciklama': 'Westerburg şehir merkezinde süpermarketler, fırınlar ve yerel dükkanlar.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Neumarkt+Westerburg',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')

    try:
        eyalet = Eyalet.objects.get(kod='RLP')
        sehir  = Stadt.objects.get(slug='westerburg')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return

    for kategori_slug, veriler in [
        ('resmi_kurum', RESMI_KURUM),
        ('ibadet',      IBADET),
        ('tuv',         TUV),
        ('saglik',      SAGLIK),
        ('egitim',      EGITIM),
        ('gezi',        GEZI),
        ('alisveris',   ALISVERIS),
    ]:
        for veri in veriler:
            Yer.objects.get_or_create(
                ad=veri['ad'], stadt=sehir,
                defaults={
                    'eyalet':      eyalet,
                    'scope':       'stadt',
                    'tur':         'yer',
                    'kategori':    kategori_slug,
                    'sehir':       'Westerburg',
                    'adres':       veri['adres'],
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
    adlar = [v['ad'] for liste in [
        RESMI_KURUM, IBADET, TUV, SAGLIK, EGITIM, GEZI, ALISVERIS
    ] for v in liste]
    Yer.objects.filter(ad__in=adlar, sehir='Westerburg').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0035_seed_altenkirchen_yerler'),
        ('stadt',  '0040_seed_westerburg'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
