from django.db import migrations


def ekle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.get_or_create(
        slug='anabin-karar-araci',
        defaults=dict(
            baslik='Anabin Karar Aracı — ZAB Gerekli mi?',
            tip='sayfa',
            url='',
            kategori='resmi',
            icon='bi-diagram-3',
            sira=20,
            yayinda=True,
            scope='eyalet',
            ozet='Adım adım sorgulama: Anabin durumuna göre ZAB Zeugnisbewertung başvurusu gerekip gerekmediğini öğren.',
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0008_hwk_kausa_mainz'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
