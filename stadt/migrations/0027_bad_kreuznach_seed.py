from django.db import migrations


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    try:
        eyalet = Eyalet.objects.get(kod='RLP')
    except Eyalet.DoesNotExist:
        return

    sehir, _ = Stadt.objects.get_or_create(
        slug='bad-kreuznach',
        defaults={
            'eyalet':      eyalet,
            'name':        'Bad Kreuznach',
            'typ':         'kreisfrei',
            'lat':         49.8412,
            'lng':         7.8680,
            'population':  41000,
            'beschreibung': 'Nahe nehri kıyısında kaplıcalarıyla ünlü, Rheinland-Pfalz\'ın tarihi şehri.',
            'aktiv':       False,
        }
    )

    sehir.termin_url            = 'https://termine-reservieren.de/termine/svkh/select2?md=2'
    sehir.auslaenderbehorde_url = 'https://www.kreis-badkreuznach.de/kreisverwaltung/organisation/informationen-aus-amt-10-der-kreisverwaltung-bad-kreuznach-auslaenderamt/servicepoint-der-auslaenderbehoerde/'
    sehir.rss_duyuru_url        = 'https://www.bad-kreuznach.de/buergerservice/buergerapp/aktuelles-rss-feed/'
    sehir.save()


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='bad-kreuznach').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0026_trier_aktiv'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
