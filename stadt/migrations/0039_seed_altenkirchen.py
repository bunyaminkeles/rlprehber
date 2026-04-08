"""
Altenkirchen (Westerwald) şehri tam kurulum: Stadt oluşturma, URL'ler, aktiv=True, Kaynaklar.
Eyalet: Rheinland-Pfalz (RLP)
Kreis: Landkreis Altenkirchen (Westerwald)
"""
from django.db import migrations

ALTENKIRCHEN_KAYNAKLAR = [
    {
        'kategori': 'resmi',
        'baslik': 'Ausländerbehörde Landkreis Altenkirchen',
        'url': 'https://www.kreis-altenkirchen.de/index.php?La=1&object=tx,2333.7762.1&kuo=2&sub=0',
        'ozet': 'Landkreis Altenkirchen Yabancılar Dairesi; oturma izni ve çalışma izni online başvuru portalı.',
        'icon': 'bi-file-earmark-person-fill',
        'sira': 1,
    },
    {
        'kategori': 'resmi',
        'baslik': 'Online Termin — Bürgerbüro Altenkirchen',
        'url': 'https://www.terminplaner-online.de/verbandsgemeinde_altenkirchen-flammersfeld/verbandsgemeinde_altenkirchen-flammersfeld/rathaus_altenkirchen/buergerbuero/',
        'ozet': 'Verbandsgemeinde Altenkirchen-Flammersfeld Bürgerbüro online randevu sistemi.',
        'icon': 'bi-calendar-check-fill',
        'sira': 2,
    },
    {
        'kategori': 'is',
        'baslik': 'Jobcenter Landkreis Altenkirchen',
        'url': 'https://www.kreis-altenkirchen.de/INTERNET/Bürgerservice/',
        'ozet': 'Bürgergeld başvurusu ve iş arama desteği için Landkreis Altenkirchen bünyesindeki Jobcenter.',
        'icon': 'bi-briefcase-fill',
        'sira': 3,
    },
    {
        'kategori': 'is',
        'baslik': 'Agentur für Arbeit — Neuwied (Altenkirchen bölgesi)',
        'url': 'https://www.arbeitsagentur.de/vor-ort/neuwied',
        'ozet': 'Altenkirchen bölgesine hizmet veren Neuwied İş Ajansı. ALG I ve mesleki rehberlik.',
        'icon': 'bi-person-workspace',
        'sira': 4,
    },
    {
        'kategori': 'egitim',
        'baslik': 'VHS Landkreis Altenkirchen',
        'url': 'https://www.vhs-altenkirchen.de',
        'ozet': 'Almanca entegrasyon kursları ve mesleki eğitim.',
        'icon': 'bi-translate',
        'sira': 5,
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Kaynak = apps.get_model('rehber', 'Kaynak')

    try:
        rlp = Eyalet.objects.get(kod='RLP')
    except Eyalet.DoesNotExist:
        return

    altenkirchen, _ = Stadt.objects.get_or_create(
        slug='altenkirchen',
        defaults={
            'eyalet': rlp,
            'name': 'Altenkirchen (Westerwald)',
            'typ': 'kreisstadt',
            'lat': 50.6866,
            'lng': 7.6474,
            'population': 6500,
            'beschreibung': (
                'Altenkirchen liegt im Nordwesten des Westerwaldes im Naturraum '
                'Altenkirchener Hochfläche. Es befindet sich an der Einmündung des '
                'Erbachs in die direkt südlich der Kernstadt vorbeifließende Wied.'
            ),
            'termin_url': (
                'https://www.terminplaner-online.de/verbandsgemeinde_altenkirchen-flammersfeld'
                '/verbandsgemeinde_altenkirchen-flammersfeld/rathaus_altenkirchen/buergerbuero/'
            ),
            'auslaenderbehorde_url': 'https://www.kreis-altenkirchen.de/index.php?La=1&object=tx,2333.7762.1&kuo=2&sub=0',
            'rss_duyuru_url': 'https://www.vg-altenkirchen-flammersfeld.de/aktuell/pressemeldungen',
            'aktiv': True,
        }
    )

    Stadt.objects.filter(slug='altenkirchen').update(
        termin_url=(
            'https://www.terminplaner-online.de/verbandsgemeinde_altenkirchen-flammersfeld'
            '/verbandsgemeinde_altenkirchen-flammersfeld/rathaus_altenkirchen/buergerbuero/'
        ),
        auslaenderbehorde_url='https://www.kreis-altenkirchen.de/index.php?La=1&object=tx,2333.7762.1&kuo=2&sub=0',
        rss_duyuru_url='https://www.vg-altenkirchen-flammersfeld.de/aktuell/pressemeldungen',
        aktiv=True,
    )

    for d in ALTENKIRCHEN_KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=altenkirchen,
            defaults={**d, 'eyalet': rlp, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='altenkirchen').update(
        termin_url='',
        auslaenderbehorde_url='',
        rss_duyuru_url='',
        aktiv=False,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0038_seed_frankfurt'),
        ('rehber', '0035_merge_20260402_0116'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
