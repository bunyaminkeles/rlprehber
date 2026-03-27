"""
Eğitim sekmesinden VHS Mainz fiziksel kurum kaydı kaldırıldı.
"""
from django.db import migrations


def guncelle(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(ad='VHS Mainz — Volkshochschule', kategori='egitim').update(aktif=False)


def geri_al(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(ad='VHS Mainz — Volkshochschule', kategori='egitim').update(aktif=True)


class Migration(migrations.Migration):
    dependencies = [('yerler', '0015_resmi_kurum_temizlik')]
    operations = [migrations.RunPython(guncelle, geri_al)]
