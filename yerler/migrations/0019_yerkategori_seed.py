from django.db import migrations


def seed_yerkategoriler(apps, schema_editor):
    YerKategori = apps.get_model('yerler', 'YerKategori')
    for d in [
        dict(slug='resmi_kurum', ad='Resmi Kurumlar', tur='yer', sira=1),
        dict(slug='saglik',      ad='Sağlık',         tur='yer', sira=2),
        dict(slug='egitim',      ad='Eğitim',          tur='yer', sira=3),
    ]:
        YerKategori.objects.get_or_create(slug=d['slug'], defaults=d)


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0018_huma_kaldir'),
    ]

    operations = [
        migrations.RunPython(seed_yerkategoriler, migrations.RunPython.noop),
    ]
