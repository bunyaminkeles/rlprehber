from django.db import migrations


def ekle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    OnemliLink = apps.get_model('linkler', 'OnemliLink')

    Kaynak.objects.get_or_create(
        slug='zab-zeugnisbewertung',
        defaults=dict(
            baslik='ZAB — Yabancı Diploma Değerlendirmesi',
            tip='link',
            url='https://zab.kmk.org/de/zeugnisbewertung/antrag',
            kategori='resmi',
            icon='bi-file-earmark-check',
            sira=15,
            yayinda=True,
            scope='eyalet',
            ozet='KMK Zentralstelle — yabancı okul ve üniversite diplomaları için resmi Zeugnisbewertung başvurusu.',
        ),
    )

    OnemliLink.objects.get_or_create(
        url='https://zab.kmk.org/de/zeugnisbewertung/antrag',
        defaults=dict(
            ad='ZAB — Yabancı Diploma Değerlendirmesi',
            kategori='resmi',
            aciklama='KMK Zentralstelle — yabancı okul ve üniversite diplomaları için resmi Zeugnisbewertung başvurusu.',
            sira=16,
            aktif=True,
            scope='eyalet',
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0006_kirik_linkleri_sil'),
        ('linkler', '0004_entegrasyon_linkleri'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
