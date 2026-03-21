"""
Data migration: Mainz ve Mainz-Bingen Stadt kayıtlarını oluşturur,
ardından mevcut tüm içerikleri Mainz'a bağlar.
"""
from django.db import migrations


def seed_mainz(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')

    mainz = Stadt.objects.create(
        name='Mainz',
        slug='mainz',
        typ='kreisfrei',
        lat=49.9929,
        lng=8.2473,
        population=220000,
        auslaenderbehorde_url='https://www.mainz.de/vv/produkte/landes-und-landeshauptstadt/auslaenderamt.php',
        termin_url='https://www.mainz.de/leben-und-arbeit/buergerservice/termine-online-buchen.php',
        beschreibung='Rheinland-Pfalz eyaletinin başkenti. Türk topluluğu için kapsamlı rehber.',
        aktiv=True,
    )

    mainz_bingen = Stadt.objects.create(
        name='Mainz-Bingen',
        slug='mainz-bingen',
        typ='landkreis',
        lat=49.9,
        lng=8.0,
        population=215000,
        aktiv=True,
    )

    # Tüm mevcut içerikleri Mainz'a bağla
    models_to_update = [
        ('rehber', 'Kaynak'),
        ('duyurular', 'Duyuru'),
        ('forum', 'Konu'),
        ('blog', 'BlogYazisi'),
        ('ilan', 'Ilan'),
        ('takvim', 'Etkinlik'),
        ('linkler', 'OnemliLink'),
    ]

    for app_label, model_name in models_to_update:
        Model = apps.get_model(app_label, model_name)
        Model.objects.filter(stadt__isnull=True).update(stadt=mainz, scope='eyalet')

    # Yerler: mevcut sehir alanına göre bağla
    Yer = apps.get_model('yerler', 'Yer')
    Yer.objects.filter(sehir__icontains='mainz', stadt__isnull=True).update(stadt=mainz, scope='stadt')
    # Geri kalanlar da mainz'a bağla (güvenli varsayılan)
    Yer.objects.filter(stadt__isnull=True).update(stadt=mainz, scope='stadt')


def reverse_seed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug__in=['mainz', 'mainz-bingen']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0001_initial'),
        ('rehber', '0004_kaynak_scope_kaynak_stadt'),
        ('duyurular', '0003_duyuru_scope_duyuru_stadt'),
        ('forum', '0002_alter_konu_options_konu_scope_konu_stadt'),
        ('blog', '0003_blogyazisi_scope_blogyazisi_stadt'),
        ('ilan', '0003_ilan_scope_ilan_stadt'),
        ('takvim', '0002_etkinlik_scope_etkinlik_stadt'),
        ('yerler', '0003_yer_scope_yer_stadt_alter_yer_sehir'),
        ('linkler', '0002_onemlilink_scope_onemlilink_stadt'),
    ]

    operations = [
        migrations.RunPython(seed_mainz, reverse_seed),
    ]
