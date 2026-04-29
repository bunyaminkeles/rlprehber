from django.db import migrations

def ileri(apps, schema_editor):
    YerKategori = apps.get_model('yerler', 'YerKategori')
    Yer = apps.get_model('yerler', 'Yer')

    yeni = [
        ('muze',       'Müze',           'yer', 10),
        ('tarihi_yer', 'Tarihi Yer',     'yer', 11),
        ('dini_yapi',  'Dini Yapı',      'yer', 12),
        ('doga',       'Doğa & Park',    'yer', 13),
        ('lezzet',     'Lezzet & Pazar', 'yer', 14),
        ('kultur',     'Kültür & Sanat', 'yer', 15),
    ]
    for slug, ad, tur, sira in yeni:
        YerKategori.objects.get_or_create(slug=slug, defaults={'ad': ad, 'tur': tur, 'sira': sira})

    # Duplikat temizle
    for pk in [284, 282]:
        Yer.objects.filter(pk=pk).delete()

    # Städel Museum kategori düzelt
    Yer.objects.filter(pk=283).update(kategori='muze')

def geri(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [('yerler', '0041_mainz_gutenberg_icerik')]
    operations = [migrations.RunPython(ileri, geri)]
