"""
Alışveriş sekmesinden HUMA Shoppingpark Mainz-Kastel kaldırıldı.
"""
from django.db import migrations

KALDIRILANLAR = [
    'HUMA Shoppingpark Mainz-Kastel',
    'HUMA Shoppingpark',
]


def guncelle(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(ad__in=KALDIRILANLAR, kategori='alisveris').update(aktif=False)


def geri_al(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(ad__in=KALDIRILANLAR, kategori='alisveris').update(aktif=True)


class Migration(migrations.Migration):
    dependencies = [('yerler', '0017_alisveris_temizlik')]
    operations = [migrations.RunPython(guncelle, geri_al)]
