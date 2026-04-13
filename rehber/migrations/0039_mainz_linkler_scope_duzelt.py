"""
Mainz'a özel linklerin scope'unu URL bazlı düzelt.
OnemliLink → Kaynak migrasyon sırasında bazı Mainz linkleri
yanlış scope ile (eyalet/genel) taşınmış olabilir.
"""
from django.db import migrations


# URL → (scope, stad_slug) eşleşmesi
MAINZ_LINKLER = [
    'https://www.mainz.de/',
    'https://termine-reservieren.de/termine/buergeramt.mainz/',
    'https://www.jobcenter-mainz.de/',
    'https://www.auslaenderbehoerde.mainz.de/',
    'https://www.mainz.de/microsite/auslaenderbehoerde/',
    'https://www.caritas-bistum-mainz.de/',
]


def duzelt(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
    except Stadt.DoesNotExist:
        return

    # URL'ye göre eşleş, scope yanlışsa düzelt
    Kaynak.objects.filter(
        url__in=MAINZ_LINKLER,
    ).exclude(
        scope='stadt', stadt=mainz,
    ).update(scope='stadt', stadt=mainz, eyalet=mainz.eyalet)

    # Başlığa göre de yakala (URL farklı olabilir)
    MAINZ_BASLIKLAR = [
        'Mainz Şehir Portalı',
        'Mainz Bürgeramt — Online Randevu',
        'Mainz Bürgeramt — Randevu',
        'Mainz Ausländerbehörde — Online Randevu',
        'Mainz Jobcenter',
    ]
    Kaynak.objects.filter(
        baslik__in=MAINZ_BASLIKLAR,
    ).exclude(
        scope='stadt', stadt=mainz,
    ).update(scope='stadt', stadt=mainz, eyalet=mainz.eyalet)


def geri_al(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0038_scope_duzeltme'),
        ('stadt', '0006_ayristry_mainz_bingen'),
    ]

    operations = [
        migrations.RunPython(duzelt, geri_al),
    ]
