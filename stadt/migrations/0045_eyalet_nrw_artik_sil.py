from django.db import migrations


def sil(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Eyalet.objects.filter(kod='', slug='nrw').delete()


def geri_al(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('stadt', '0044_eyalet_arma_url_eksikler'),
    ]
    operations = [
        migrations.RunPython(sil, geri_al),
    ]
