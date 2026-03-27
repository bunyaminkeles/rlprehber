from django.db import migrations


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        eyalet = Eyalet.objects.get(kod='BW')
    except Eyalet.DoesNotExist:
        return

    Stadt.objects.get_or_create(
        slug='mannheim',
        defaults={
            'eyalet': eyalet,
            'name': 'Mannheim',
            'typ': 'kreisfrei',
            'lat': 49.4883,
            'lng': 8.4660,
            'population': 309370,
            'auslaenderbehorde_url': 'https://www.mannheim.de/de/service-bieten/buergerdienste/zuwanderung-und-einbuergerung',
            'termin_url': 'https://www.mannheim.de/de/service-bieten/buergerdienste/buergerservice',
            'beschreibung': "Baden-Württemberg'in ikinci büyük şehri, Ren ve Neckar nehirlerinin kavşağında.",
            'aktiv': False,
        }
    )


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='mannheim').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0010_seed_baskentler'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
