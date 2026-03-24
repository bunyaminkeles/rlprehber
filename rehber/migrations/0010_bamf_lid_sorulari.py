from django.db import migrations


def ekle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')

    Kaynak.objects.get_or_create(
        slug='bamf-lid-sorulari',
        defaults=dict(
            baslik='Leben in Deutschland — Sınav Soruları (BAMF)',
            tip='link',
            url='https://www.bamf.de/SharedDocs/Anlagen/DE/Integration/Einbuergerung/gesamtfragenkatalog-lebenindeutschland.pdf?__blob=publicationFile&v=23',
            kategori='egitim',
            icon='bi-file-earmark-pdf',
            sira=5,
            yayinda=True,
            scope='eyalet',
            ozet='BAMF resmi vatandaşlık sınavı soru kataloğu — 310 soru ve cevapları (PDF).',
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0009_anabin_widget_kaynak'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
