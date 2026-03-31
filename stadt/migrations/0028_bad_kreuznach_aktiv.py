from django.db import migrations


def aktivlestir(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='bad-kreuznach').update(aktiv=True)


def geri_al(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='bad-kreuznach').update(aktiv=False)


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0027_bad_kreuznach_seed'),
    ]

    operations = [
        migrations.RunPython(aktivlestir, geri_al),
    ]
