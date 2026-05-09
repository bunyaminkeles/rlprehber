from django.db import migrations


def update(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    try:
        s = Stadt.objects.get(slug='erfurt')
        s.termin_url            = 'https://www.erfurt.de/ef/de/service/buergerservice/buergerservice-online/terminvergabe/index.html'
        s.auslaenderbehorde_url = 'https://www.erfurt.de/ef/de/service/buergerservice/auslaender-und-asyl/auslaenderbehoerde/index.html'
        s.rss_duyuru_url        = 'https://www.erfurt.de/ef/de/service/aktuelles/presse/index.html'
        s.aktiv                 = True
        s.save()
    except Stadt.DoesNotExist:
        pass


def reverse(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    try:
        s = Stadt.objects.get(slug='erfurt')
        s.termin_url            = ''
        s.auslaenderbehorde_url = ''
        s.rss_duyuru_url        = ''
        s.aktiv                 = False
        s.save()
    except Stadt.DoesNotExist:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0010_seed_baskentler'),
    ]
    operations = [
        migrations.RunPython(update, reverse),
    ]