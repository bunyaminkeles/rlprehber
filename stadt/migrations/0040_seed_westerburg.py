"""
Westerburg (Westerwald) şehri tam kurulum: Stadt oluşturma, URL'ler, aktiv=True, Kaynaklar.
Eyalet: Rheinland-Pfalz (RLP)
Kreis: Westerwaldkreis
"""
from django.db import migrations

WESTERBURG_KAYNAKLAR = [
    {
        'kategori': 'resmi',
        'baslik': 'Ausländerbehörde Westerwaldkreis (Welcome Center)',
        'url': 'https://www.westerwaldkreis.de/welcome-center-auslaenderbehoerde.html',
        'ozet': 'Westerwaldkreis Yabancılar Dairesi (Montabaur). Oturma izni başvuruları ve yabancı uyruklu işlemler.',
        'icon': 'bi-file-earmark-person-fill',
        'sira': 1,
    },
    {
        'kategori': 'resmi',
        'baslik': 'Online Termin — Bürgerbüro Westerburg',
        'url': 'https://www.terminplaner-online.de/verbandsgemeinde_westerburg/verbandsgemeinde_westerburg/verbandsgemeindeverwaltung/einwohnermeldeamt/',
        'ozet': 'Verbandsgemeinde Westerburg Einwohnermeldeamt online randevu sistemi.',
        'icon': 'bi-calendar-check-fill',
        'sira': 2,
    },
    {
        'kategori': 'is',
        'baslik': 'Jobcenter Westerwaldkreis',
        'url': 'https://www.westerwaldkreis.de/jobcenter.html',
        'ozet': 'Bürgergeld başvurusu ve iş arama desteği için Westerwaldkreis Jobcenter (Montabaur).',
        'icon': 'bi-briefcase-fill',
        'sira': 3,
    },
    {
        'kategori': 'is',
        'baslik': 'Agentur für Arbeit Montabaur',
        'url': 'https://www.arbeitsagentur.de/vor-ort/montabaur',
        'ozet': 'Westerburg bölgesine hizmet veren Montabaur İş Ajansı. ALG I ve mesleki rehberlik.',
        'icon': 'bi-person-workspace',
        'sira': 4,
    },
    {
        'kategori': 'egitim',
        'baslik': 'VHS Westerwaldkreis',
        'url': 'https://www.vhs-westerwald.de',
        'ozet': 'Almanca entegrasyon kursları ve mesleki eğitim programları.',
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

    westerburg, _ = Stadt.objects.get_or_create(
        slug='westerburg',
        defaults={
            'eyalet': rlp,
            'name': 'Westerburg',
            'typ': 'kreisstadt',
            'lat': 50.5566,
            'lng': 7.9781,
            'population': 5600,
            'beschreibung': (
                'Westerburg ist eine Stadt im Westerwaldkreis in Rheinland-Pfalz. '
                'Sie liegt im Oberwesterwald und ist Verwaltungssitz der '
                'Verbandsgemeinde Westerburg.'
            ),
            'termin_url': (
                'https://www.terminplaner-online.de/verbandsgemeinde_westerburg'
                '/verbandsgemeinde_westerburg/verbandsgemeindeverwaltung/einwohnermeldeamt/'
            ),
            'auslaenderbehorde_url': 'https://www.westerwaldkreis.de/welcome-center-auslaenderbehoerde.html',
            'rss_duyuru_url': 'https://www.vg-westerburg.de/',
            'aktiv': True,
        }
    )

    Stadt.objects.filter(slug='westerburg').update(
        termin_url=(
            'https://www.terminplaner-online.de/verbandsgemeinde_westerburg'
            '/verbandsgemeinde_westerburg/verbandsgemeindeverwaltung/einwohnermeldeamt/'
        ),
        auslaenderbehorde_url='https://www.westerwaldkreis.de/welcome-center-auslaenderbehoerde.html',
        rss_duyuru_url='https://www.vg-westerburg.de/',
        aktiv=True,
    )

    for d in WESTERBURG_KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=westerburg,
            defaults={**d, 'eyalet': rlp, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='westerburg').update(
        termin_url='',
        auslaenderbehorde_url='',
        rss_duyuru_url='',
        aktiv=False,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0039_seed_altenkirchen'),
        ('rehber', '0035_merge_20260402_0116'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
