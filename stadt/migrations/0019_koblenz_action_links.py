from django.db import migrations

CITY_DATA = {
    'koblenz': {
        'termin_url':            'https://www.koblenz.de/rathaus/verwaltung/buergerservice/buergertermine/',
        'auslaenderbehorde_url': 'https://www.koblenz.de/buergerservice/abteilungen/RLP:department:345950/auslaenderangelegenheiten/',
        'rss_duyuru_url':        'https://www.presseportal.de/rss/r/Koblenz.rss2',
    },
}


def update_cities(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    for slug, data in CITY_DATA.items():
        try:
            sehir = Stadt.objects.get(slug=slug)
            sehir.termin_url            = data['termin_url']
            sehir.auslaenderbehorde_url = data['auslaenderbehorde_url']
            sehir.rss_duyuru_url        = data['rss_duyuru_url']
            sehir.save()
        except Stadt.DoesNotExist:
            continue


def reverse_update(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0018_seed_koeln_stadt'),
    ]

    operations = [
        migrations.RunPython(update_cities, reverse_update),
    ]
