"""
Alışveriş sekmesinden kaldırılanlar: Römerpassage Mainz, IKEA Wiesbaden.
"""
from django.db import migrations

KALDIRILANLAR = [
    'Römerpassage — Alışveriş Merkezi',
    'Römerpassage Mainz',
    'IKEA Wiesbaden',
    'IKEA',
]


def guncelle(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(ad__in=KALDIRILANLAR, kategori='alisveris').update(aktif=False)


def geri_al(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(ad__in=KALDIRILANLAR, kategori='alisveris').update(aktif=True)


class Migration(migrations.Migration):
    dependencies = [('yerler', '0016_egitim_temizlik')]
    operations = [migrations.RunPython(guncelle, geri_al)]
