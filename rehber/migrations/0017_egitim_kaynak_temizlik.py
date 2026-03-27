"""
Eğitim sekmesinden kaldırılan Kaynak kayıtları:
- BAMF — Integrationskurs Nedir?
- BAMF — Integrationskurs Başvuru
- VHS Mainz — Kurs Kayıt
"""
from django.db import migrations

KALDIRILANLAR = [
    'BAMF — Integrationskurs Nedir?',
    'BAMF — Integrationskurs Başvuru',
    'VHS Mainz — Kurs Kayıt',
]


def guncelle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=KALDIRILANLAR).update(yayinda=False)


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=KALDIRILANLAR).update(yayinda=True)


class Migration(migrations.Migration):
    dependencies = [('rehber', '0016_resmi_kaynak_temizlik')]
    operations = [migrations.RunPython(guncelle, geri_al)]
