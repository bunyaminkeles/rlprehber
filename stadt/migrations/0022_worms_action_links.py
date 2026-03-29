from django.db import migrations

CITY_DATA = {
    'worms': {
        'termin_url':            'https://termine-reservieren.de/termine/worms/',
        'auslaenderbehorde_url': 'https://www.worms.de/neu-de/buergerservice/online-dienste-auslaenderbehoerde.php',
        'rss_duyuru_url':        'https://www.worms.de/neu-de/aktuelles/rss.php',
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
        ('stadt', '0021_ludwigshafen_action_links'),
    ]
    operations = [
        migrations.RunPython(update_cities, reverse_update),
    ]
