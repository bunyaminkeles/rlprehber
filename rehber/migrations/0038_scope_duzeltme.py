"""
Yanlış scope atamalarını düzelt:
1. T.C. Mainz Başkonsolosluğu: scope='genel'/'almanya' → scope='eyalet', eyalet=RLP
   (RLP geneli için, tüm Almanya değil)
2. Köln kaynakları: scope='eyalet', eyalet=None → scope='stadt', stadt=Köln
   (eyalet bağlantısız kalınca hiçbir şehirde görünmüyordu)
"""
from django.db import migrations


KOLN_BASLIKLAR = [
    'Köln Kundenzentrum — Online Terminvereinbarung',
    'T.C. Köln Başkonsolosluğu',
    'Köln Şehir Portalı',
    'Köln Bürgeramt — Randevu',
    'Ausländerbehörde Köln',
    'Terminvereinbarung — Köln Online Randevu',
    'Kleinanzeigen — Köln',
    'ImmobilienScout24 — Köln',
    'Immonet — Köln',
    'Jobcenter Köln',
    'KV Nordrhein — Doktor Arama (NRW)',
]


def duzelt(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')
    Eyalet = apps.get_model('stadt', 'Eyalet')

    try:
        rlp = Eyalet.objects.get(slug='rlp')
    except Eyalet.DoesNotExist:
        rlp = None

    # 1. T.C. Mainz Başkonsolosluğu — scope=genel/almanya → eyalet=RLP
    if rlp:
        Kaynak.objects.filter(
            baslik='T.C. Mainz Başkonsolosluğu',
            scope__in=['genel', 'almanya'],
        ).update(scope='eyalet', eyalet=rlp, stadt=None)

    # 2. Köln kaynakları — scope=eyalet, eyalet=None → scope=stadt, stadt=Köln
    try:
        koln = Stadt.objects.get(slug='koln')
    except Stadt.DoesNotExist:
        try:
            koln = Stadt.objects.get(name__icontains='Köln')
        except Stadt.DoesNotExist:
            koln = None

    if koln:
        Kaynak.objects.filter(
            baslik__in=KOLN_BASLIKLAR,
            scope='eyalet',
            eyalet=None,
        ).update(scope='stadt', stadt=koln, eyalet=koln.eyalet)


def geri_al(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0037_onemlilink_to_kaynak'),
        ('stadt', '0006_ayristry_mainz_bingen'),
    ]

    operations = [
        migrations.RunPython(duzelt, geri_al),
    ]
