from django.db import migrations

BASKENTLER = [
    {'eyalet_kod': 'BW', 'name': 'Stuttgart', 'slug': 'stuttgart', 'lat': 48.7775, 'lng': 9.18, 'population': 612663},
    {'eyalet_kod': 'BY', 'name': 'München', 'slug': 'muenchen', 'lat': 48.1375, 'lng': 11.575, 'population': 1505005},
    {'eyalet_kod': 'BE', 'name': 'Berlin', 'slug': 'berlin', 'lat': 52.52, 'lng': 13.405, 'population': 3685265},
    {'eyalet_kod': 'BB', 'name': 'Potsdam', 'slug': 'potsdam', 'lat': 52.40056, 'lng': 13.05917, 'population': 184754},
    {'eyalet_kod': 'HB', 'name': 'Bremen', 'slug': 'bremen', 'lat': 53.07583, 'lng': 8.80722, 'population': 586271},
    {'eyalet_kod': 'HH', 'name': 'Hamburg', 'slug': 'hamburg', 'lat': 53.55, 'lng': 10.0, 'population': 1973896},
    {'eyalet_kod': 'HE', 'name': 'Wiesbaden', 'slug': 'wiesbaden', 'lat': 50.0825, 'lng': 8.24, 'population': 288850},
    {'eyalet_kod': 'MV', 'name': 'Schwerin', 'slug': 'schwerin', 'lat': 53.633, 'lng': 11.417, 'population': 98308},
    {'eyalet_kod': 'NI', 'name': 'Hannover', 'slug': 'hannover', 'lat': 52.367, 'lng': 9.717, 'population': 522131},
    {'eyalet_kod': 'NW', 'name': 'Düsseldorf', 'slug': 'duesseldorf', 'lat': 51.2256, 'lng': 6.7767, 'population': 618685},
    {'eyalet_kod': 'SL', 'name': 'Saarbrücken', 'slug': 'saarbruecken', 'lat': 49.233, 'lng': 7.0, 'population': 182971},
    {'eyalet_kod': 'SN', 'name': 'Dresden', 'slug': 'dresden', 'lat': 51.05, 'lng': 13.74, 'population': 564904},
    {'eyalet_kod': 'ST', 'name': 'Magdeburg', 'slug': 'magdeburg', 'lat': 52.13167, 'lng': 11.63917, 'population': 244329},
    {'eyalet_kod': 'SH', 'name': 'Kiel', 'slug': 'kiel', 'lat': 54.32, 'lng': 10.14, 'population': 252668},
    {'eyalet_kod': 'TH', 'name': 'Erfurt', 'slug': 'erfurt', 'lat': 50.97806, 'lng': 11.02889, 'population': 218793},
]


def seed_baskentler(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')
    for veri in BASKENTLER:
        try:
            eyalet = Eyalet.objects.get(kod=veri['eyalet_kod'])
        except Eyalet.DoesNotExist:
            continue
        Stadt.objects.get_or_create(
            slug=veri['slug'],
            defaults={
                'eyalet': eyalet,
                'name': veri['name'],
                'typ': 'kreisfrei',
                'lat': veri['lat'],
                'lng': veri['lng'],
                'population': veri['population'],
                'aktiv': True,
            }
        )


def unseed_baskentler(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug__in=[v['slug'] for v in BASKENTLER]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0009_seed_icerik_eyalet'),
    ]
    operations = [
        migrations.RunPython(seed_baskentler, unseed_baskentler),
    ]
