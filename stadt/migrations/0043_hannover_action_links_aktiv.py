from django.db import migrations


def update(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    try:
        s = Stadt.objects.get(slug='hannover')
        s.termin_url            = 'https://www.hannover.de/Leben-in-der-Region-Hannover/B%C3%BCrger-Service/B%C3%BCrger-Service-in-der-Landeshauptstadt-Hannover/Termine-bei-Beh%C3%B6rden-buchen/Terminvereinbarung-in-den-B%C3%BCrger%C3%A4mtern'
        s.auslaenderbehorde_url = 'https://auslaenderbehoerdeonline.hannover-stadt.de/'
        s.rss_duyuru_url        = 'https://e-government.hannover-stadt.de/lhhsimwebre.nsf/RSSUebersicht.xsp'
        s.aktiv                 = True
        s.save()
    except Stadt.DoesNotExist:
        pass


def reverse(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    try:
        s = Stadt.objects.get(slug='hannover')
        s.termin_url            = ''
        s.auslaenderbehorde_url = ''
        s.rss_duyuru_url        = ''
        s.aktiv                 = False
        s.save()
    except Stadt.DoesNotExist:
        pass


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0042_muenchen_slug_munih'),
    ]
    operations = [
        migrations.RunPython(update, reverse),
    ]
