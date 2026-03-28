from django.db import migrations


def fix_urls(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='mainz').update(
        auslaenderbehorde_url='https://www.mainz.de/vv/oe/auslaenderangelegenheiten',
        termin_url='https://www.mainz.de/verwaltung-und-politik/buergerservice-online/buergeramt-online-terminvereinbarung.php',
    )


def reverse_urls(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='mainz').update(
        auslaenderbehorde_url='https://www.mainz.de/vv/produkte/landes-und-landeshauptstadt/auslaenderamt.php',
        termin_url='https://www.mainz.de/leben-und-arbeit/buergerservice/termine-online-buchen.php',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0011_seed_mannheim_stadt'),
    ]
    operations = [
        migrations.RunPython(fix_urls, reverse_urls),
    ]
