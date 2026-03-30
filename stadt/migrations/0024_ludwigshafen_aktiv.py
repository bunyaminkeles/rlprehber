from django.db import migrations


def aktivlestir(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='ludwigshafen').update(aktiv=True)


def geri_al(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='ludwigshafen').update(aktiv=False)


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0023_worms_aktiv'),
    ]

    operations = [
        migrations.RunPython(aktivlestir, geri_al),
    ]
