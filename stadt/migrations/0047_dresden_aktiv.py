from django.db import migrations


def update(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    try:
        s = Stadt.objects.get(slug='dresden')
        s.termin_url            = 'https://www.dresden.de/de/rathaus/dienstleistungen/online-terminvergabe_d115.php'
        s.auslaenderbehorde_url = 'https://www.dresden.de/de/leben/gesellschaft/migration/auslaenderbehoerde.php'
        s.rss_duyuru_url        = 'https://www.dresden.de/de/rathaus/aktuelles/pressemitteilungen/rss.php?rubrik=0'
        s.aktiv                 = True
        s.save()
    except Stadt.DoesNotExist:
        pass


def reverse(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    try:
        s = Stadt.objects.get(slug='dresden')
        s.termin_url            = ''
        s.auslaenderbehorde_url = ''
        s.rss_duyuru_url        = ''
        s.aktiv                 = False
        s.save()
    except Stadt.DoesNotExist:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0046_merge_0045_erfurt_aktiv_0045_eyalet_nrw_artik_sil'),
    ]
    operations = [
        migrations.RunPython(update, reverse),
    ]