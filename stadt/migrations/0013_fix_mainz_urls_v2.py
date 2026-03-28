from django.db import migrations


def fix_urls(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='mainz').update(
        auslaenderbehorde_url='https://antrag-kommunal.service.rlp.de/civ.public/start.html?oe=00.00.MZ.01.33.01.01&mode=cc&cc_key=KontaktAuslaenderbehoerde',
        termin_url='https://termine-reservieren.de/termine/buergeramt.mainz/',
    )


def reverse_urls(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='mainz').update(
        auslaenderbehorde_url='https://www.mainz.de/vv/oe/auslaenderangelegenheiten',
        termin_url='https://www.mainz.de/verwaltung-und-politik/buergerservice-online/buergeramt-online-terminvereinbarung.php',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0012_fix_mainz_urls'),
    ]
    operations = [
        migrations.RunPython(fix_urls, reverse_urls),
    ]
