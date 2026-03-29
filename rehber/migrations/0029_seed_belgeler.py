from django.db import migrations

FEDERAL_BELGELER = [
    {'baslik': 'Kindergeld Ana Başvuru Formu (KG1)',          'kategori': 'aile',  'harici_link': 'https://www.arbeitsagentur.de/familie-und-kinder/downloads-familie-und-kinder/formulare-kindergeld'},
    {'baslik': 'Elterngeld Başvuru Formu',                    'kategori': 'aile',  'harici_link': 'https://www.elterngeld.net/formulare.html'},
    {'baslik': 'Rundfunkbeitrag (ARD/ZDF) Kayıt Formu',       'kategori': 'konut', 'harici_link': 'https://www.rundfunkbeitrag.de/buergerinnen_und_buerger/formulare/anmelden/index_ger.html'},
    {'baslik': 'Sozialversicherungsausweis Başvurusu',        'kategori': 'is',    'harici_link': 'https://www.deutsche-rentenversicherung.de/DRV/DE/Formulare/formulare_node.html'},
    {'baslik': 'Lohnsteuerhilfeverein — Vergi Beyannamesi',   'kategori': 'is',    'harici_link': 'https://www.vlh.de/'},
    {'baslik': 'Krankenversicherung Üyelik Formu (GKV)',      'kategori': 'genel', 'harici_link': 'https://www.krankenkassenzentrale.de/'},
    {'baslik': 'Ummeldung / Abmeldung (Adres Değişikliği)',   'kategori': 'genel', 'harici_link': 'https://www.ummelden.de/'},
    {'baslik': 'BAföG Öğrenci Bursu Başvurusu',               'kategori': 'is',    'harici_link': 'https://www.bafög.de/de/formulare-253.php'},
    {'baslik': 'Führerschein Umtausch (Ehliyet Dönüşümü)',    'kategori': 'genel', 'harici_link': 'https://www.kba.de/DE/Themen/ZentraleRegister/FAER/Fuehrerscheinumtausch/fuehrerscheinumtausch_node.html'},
]

MAINZ_BELGELER = [
    {'baslik': 'Wohnungsgeberbestätigung (Ev Sahibi Onayı)',         'kategori': 'konut', 'harici_link': 'https://www.mainz.de/vv/medien/internet/Wohnungsgeberbestaetigung.pdf'},
    {'baslik': 'Aufenthaltserlaubnis — Oturum İzni Başvuru Formu',   'kategori': 'vize',  'harici_link': 'https://www.mainz.de/vv/medien/internet/Aufenthaltserlaubnis-Antrag-Erteilung-Verlaengerung.pdf'},
    {'baslik': 'Anmeldung — İkametgah Kayıt Bilgileri',              'kategori': 'genel', 'harici_link': 'https://www.mainz.de/vv/produkte/buergeramt/wohnsitz-als-hauptwohnsitz-anmelden.php'},
    {'baslik': 'Mainz KdU — Kira Tavan Tablosu',                    'kategori': 'konut', 'harici_link': 'https://www.mainz.de/vv/produkte/soziales/kosten-der-unterkunft.php'},
    {'baslik': 'Gewerbeanmeldung — İşyeri Tescil Formu (Mainz)',     'kategori': 'is',    'harici_link': 'https://www.mainz.de/vv/produkte/wirtschaft/gewerbe-anmelden.php'},
]


def seed(apps, schema_editor):
    Belge = apps.get_model('rehber', 'Belge')
    Stadt = apps.get_model('stadt', 'Stadt')

    for d in FEDERAL_BELGELER:
        Belge.objects.get_or_create(
            baslik=d['baslik'],
            stadt=None,
            defaults={
                'kategori':    d['kategori'],
                'harici_link': d['harici_link'],
                'yayinda':     True,
            }
        )

    try:
        mainz = Stadt.objects.get(slug='mainz')
    except Stadt.DoesNotExist:
        return

    for d in MAINZ_BELGELER:
        Belge.objects.get_or_create(
            baslik=d['baslik'],
            stadt=mainz,
            defaults={
                'kategori':    d['kategori'],
                'harici_link': d['harici_link'],
                'yayinda':     True,
            }
        )


def unseed(apps, schema_editor):
    Belge = apps.get_model('rehber', 'Belge')
    federal_basliklar = [d['baslik'] for d in FEDERAL_BELGELER]
    mainz_basliklar   = [d['baslik'] for d in MAINZ_BELGELER]
    Belge.objects.filter(baslik__in=federal_basliklar, stadt__isnull=True).delete()
    Belge.objects.filter(baslik__in=mainz_basliklar,   stadt__slug='mainz').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0028_belge_modeli'),
        ('stadt',  '0018_seed_koeln_stadt'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
