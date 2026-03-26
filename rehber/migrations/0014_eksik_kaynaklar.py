from django.db import migrations

EKLE = [
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'BAMF — Göç ve Mülteci Dairesi',
        'tip': 'link', 'url': 'https://www.bamf.de/TR/Themen/MigrationAufenthalt/migrationaufenthalt-node.html',
        'kategori': 'resmi', 'icon': 'bi-building-fill',
        'ozet': 'Federal Göç ve Mülteci Dairesi — göç, vize ve ikamet bilgileri.',
        'sira': 5,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'BAMF — Integrationskurs Başvuru',
        'tip': 'link', 'url': 'https://www.bamf.de/DE/Themen/Integration/ZugewanderteTeilnehmende/Integrationskurse/integrationskurse-node.html',
        'kategori': 'egitim', 'icon': 'bi-person-check',
        'ozet': 'Entegrasyon kursuna başvuru ve gerekli belgeler.',
        'sira': 5,
    },
]


def ekle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Eyalet = apps.get_model('stadt', 'Eyalet')
    for veri in EKLE:
        if Kaynak.objects.filter(baslik=veri['baslik']).exists():
            continue
        eyalet = Eyalet.objects.filter(slug=veri['eyalet_slug']).first()
        if not eyalet:
            continue
        Kaynak.objects.create(
            eyalet=eyalet, stadt=None, scope=veri['scope'],
            baslik=veri['baslik'], tip=veri['tip'], url=veri['url'],
            kategori=veri['kategori'], icon=veri['icon'],
            ozet=veri['ozet'], sira=veri['sira'], yayinda=True,
        )


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik__in=[v['baslik'] for v in EKLE]).delete()


class Migration(migrations.Migration):
    dependencies = [('rehber', '0013_linkler_birlestir')]
    operations = [migrations.RunPython(ekle, geri_al)]
