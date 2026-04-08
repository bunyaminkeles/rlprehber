"""
Altenkirchen (Westerwald) — Önemli Yerler Seed Migrasyonu
Eyalet: Rheinland-Pfalz (RLP)
"""
from django.db import migrations

RESMI_KURUM = [
    {
        'ad': 'Kreisverwaltung Altenkirchen — Ausländerbehörde',
        'adres': 'Parkstraße 1, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Landkreis Altenkirchen Yabancılar Dairesi. Oturma izni işlemleri için önce telefon veya online randevu alınması zorunludur.',
        'website': 'https://www.kreis-altenkirchen.de/index.php?La=1&object=tx,2333.7762.1&kuo=2&sub=0',
        'maps_url': 'https://maps.google.com/?q=Parkstra%C3%9Fe+1,+57610+Altenkirchen',
    },
    {
        'ad': 'Verbandsgemeindeverwaltung Altenkirchen-Flammersfeld',
        'adres': 'Rathausstraße 13, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Bürgerbüro, nüfus tescili, pasaport ve kimlik işlemleri. Online randevu alınabilir.',
        'website': 'https://www.vg-altenkirchen-flammersfeld.de',
        'maps_url': 'https://maps.google.com/?q=Rathausstra%C3%9Fe+13,+57610+Altenkirchen',
    },
    {
        'ad': 'Agentur für Arbeit Neuwied — Geschäftsstelle Altenkirchen',
        'adres': 'Rathausstraße 13, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Altenkirchen bölgesine hizmet veren İş Ajansı şubesi. ALG I ve iş arama desteği.',
        'website': 'https://www.arbeitsagentur.de/vor-ort/neuwied',
        'maps_url': 'https://maps.google.com/?q=Rathausstra%C3%9Fe+13,+57610+Altenkirchen',
    },
    {
        'ad': 'Finanzamt Altenkirchen',
        'adres': 'Hochstraße 1, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Vergi numarası ve gelir vergisi beyannamesi işlemleri.',
        'website': 'https://www.finanzamt.rlp.de/finanzamt-altenkirchen',
        'maps_url': 'https://maps.google.com/?q=Hochstra%C3%9Fe+1,+57610+Altenkirchen',
    },
]

IBADET = [
    {
        'ad': 'Moschee Altenkirchen — İslam Cemaati',
        'adres': 'Altenkirchen (Westerwald)',
        'aciklama': 'Altenkirchen ve çevresindeki Müslüman cemaat için ibadet mekanı. Detaylı bilgi için yerel İslam dernekleriyle iletişime geçin.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Moschee+Altenkirchen+Westerwald',
    },
]

TUV = [
    {
        'ad': 'TÜV — Altenkirchen bölgesi',
        'adres': 'Altenkirchen (Westerwald)',
        'aciklama': 'En yakın TÜV Rheinland veya DEKRA şubesi için tuv.com veya dekra.de üzerinden "Altenkirchen" aratın.',
        'website': 'https://www.tuv.com/de/tuv-rheinland-gruppe/',
        'maps_url': 'https://maps.google.com/?q=T%C3%9CV+Altenkirchen+Westerwald',
    },
]

SAGLIK = [
    {
        'ad': 'DRK-Krankenhaus Altenkirchen',
        'adres': 'Hochstraße 30, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Landkreis Altenkirchen\'in merkez hastanesi. Dahiliye, cerrahi ve acil servis hizmetleri.',
        'website': 'https://www.drk-kh-altenkirchen.de',
        'maps_url': 'https://maps.google.com/?q=Hochstra%C3%9Fe+30,+57610+Altenkirchen',
    },
]

EGITIM = [
    {
        'ad': 'VHS Landkreis Altenkirchen',
        'adres': 'Parkstraße 1, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Almanca entegrasyon kursları, mesleki eğitim ve yetişkin eğitimi programları.',
        'website': 'https://www.vhs-altenkirchen.de',
        'maps_url': 'https://maps.google.com/?q=Parkstra%C3%9Fe+1,+57610+Altenkirchen',
    },
    {
        'ad': 'Kreisgymnasium Altenkirchen',
        'adres': 'Schulstraße 12, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Landkreis Altenkirchen\'in devlet lisesi.',
        'website': 'https://www.gymnasium-altenkirchen.de',
        'maps_url': 'https://maps.google.com/?q=Schulstra%C3%9Fe+12,+57610+Altenkirchen',
    },
]

GEZI = [
    {
        'ad': 'Westerwaldsteig — Altenkirchen',
        'adres': 'Altenkirchen (Westerwald)',
        'aciklama': 'Almanya\'nın en güzel yürüyüş rotalarından biri. Westerwald\'ın tepe ve ormanlarından geçer.',
        'website': 'https://www.westerwaldsteig.de',
        'maps_url': 'https://maps.google.com/?q=Westerwaldsteig+Altenkirchen',
    },
    {
        'ad': 'Wiedtal — Doğa Yürüyüş Rotası',
        'adres': 'Wied Vadisi, Altenkirchen (Westerwald)',
        'aciklama': 'Kernstadt\'ın hemen güneyinden geçen Wied nehri vadisinde doğa yürüyüşü.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Wied+Altenkirchen+Westerwald',
    },
    {
        'ad': 'Historische Innenstadt Altenkirchen',
        'adres': 'Marktplatz, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Altenkirchen\'in tarihi şehir merkezi ve Marktplatz. Kilise ve geleneksel yapılarla çevrili.',
        'website': 'https://www.altenkirchen.de',
        'maps_url': 'https://maps.google.com/?q=Marktplatz+Altenkirchen+Westerwald',
    },
]

ALISVERIS = [
    {
        'ad': 'Innenstadt Altenkirchen — Alışveriş',
        'adres': 'Rathausstraße / Wilhelmstraße, 57610 Altenkirchen (Westerwald)',
        'aciklama': 'Altenkirchen şehir merkezinde süpermarketler, yerel dükkanlar ve hizmetler.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Innenstadt+Altenkirchen+Westerwald',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')

    try:
        eyalet = Eyalet.objects.get(kod='RLP')
        sehir  = Stadt.objects.get(slug='altenkirchen')
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
                    'sehir':       'Altenkirchen (Westerwald)',
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
    Yer.objects.filter(ad__in=adlar, sehir='Altenkirchen (Westerwald)').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0034_alter_yer_ad'),
        ('stadt',  '0039_seed_altenkirchen'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
