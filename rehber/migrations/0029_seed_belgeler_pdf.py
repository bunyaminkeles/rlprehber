"""
Belge havuzu — SADECE doğrulanmış, doğrudan indirilebilir PDF dosyalar.
Bilgi sayfaları veya web portalları bu modele EKLENMEMELİDİR.
"""
from django.db import migrations

FEDERAL_BELGELER = [
    {
        'baslik': 'Kindergeld Ana Başvuru Formu (KG1)',
        'kategori': 'aile',
        'harici_link': 'https://www.arbeitsagentur.de/datei/kg1-antrag-kindergeld_ba036550.pdf',
        'ozet': 'Çocuk parası (Kindergeld) için resmi başvuru formu.',
    },
    {
        'baslik': 'SEPA-Lastschriftmandat — Araç Vergisi Otomatik Ödeme',
        'kategori': 'genel',
        'harici_link': 'https://www.zoll.de/SharedDocs/Downloads/DE/FormulareMerkblaetter/Verkehrsteuern/Formular_032021.pdf?__blob=publicationFile',
        'ozet': 'Kfz-Steuer (araç vergisi) için otomatik ödeme talimatı (SEPA) formu.',
    },
]

MAINZ_BELGELER = [
    {
        'baslik': 'Wohnungsgeberbestätigung — Ev Sahibi Onay Belgesi (Mainz)',
        'kategori': 'konut',
        'harici_link': 'https://www.mainz.de/vv/medien/internet/Wohnungsgebende-Bescheinigung-Formular.pdf',
        'ozet': 'Mainz Bürgerbüro için ev sahibinden alınacak ikamet onay formu.',
    },
    {
        'baslik': 'Aufenthaltserlaubnis — Oturum İzni Başvuru Formu (Mainz)',
        'kategori': 'vize',
        'harici_link': 'https://www.mainz.de/vv/medien/internet/Aufenthaltserlaubnis-Antrag-Erteilung-Verlaengerung.pdf',
        'ozet': 'Mainz Ausländerbehörde oturum izni başvurusu ve uzatma formu.',
    },
    {
        'baslik': 'Vollmacht Kfz-Zulassung — Araç Kayıt Vekaletnamesi (Mainz)',
        'kategori': 'genel',
        'harici_link': 'https://www.mainz.de/vv/medien/internet/Zulassungsstelle-Antragstellung-Abholung-Fahrzeugpapiere-Vollmacht.pdf',
        'ozet': 'Mainz araç tescili için başkasına verilebilecek vekaletname formu.',
    },
    {
        'baslik': 'Wohnberechtigungsschein (Sosyal Konut Hak Belgesi) Başvurusu — Mainz',
        'kategori': 'konut',
        'harici_link': 'https://www.wohnbau-mainz.de/fileadmin/Dokumente/Vermietung/Antrag_Wohnberechtigungsschein_web.pdf',
        'ozet': 'Mainz sosyal konut (Sozialwohnung) başvurusu için gereken hak belgesi formu.',
    },
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
                'ozet':        d.get('ozet', ''),
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
                'ozet':        d.get('ozet', ''),
                'yayinda':     True,
            }
        )


def unseed(apps, schema_editor):
    Belge = apps.get_model('rehber', 'Belge')
    federal_basliklar = [d['baslik'] for d in FEDERAL_BELGELER]
    mainz_basliklar   = [d['baslik'] for d in MAINZ_BELGELER]
    Belge.objects.filter(baslik__in=federal_basliklar, stadt__isnull=True).delete()
    Belge.objects.filter(baslik__in=mainz_basliklar, stadt__slug='mainz').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0028_belge_modeli'),
        ('stadt',  '0018_seed_koeln_stadt'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
