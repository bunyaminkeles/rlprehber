from django.db import migrations


def munih_yap(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='muenchen').update(slug='munih')


def geri_al(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='munih').update(slug='muenchen')


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0041_muenchen_action_links'),
    ]
    operations = [
        migrations.RunPython(munih_yap, geri_al),
    ]
