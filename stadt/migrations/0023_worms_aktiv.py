from django.db import migrations


def aktivlestir(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='worms').update(aktiv=True)


def geri_al(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='worms').update(aktiv=False)


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0022_worms_action_links'),
    ]

    operations = [
        migrations.RunPython(aktivlestir, geri_al),
    ]
