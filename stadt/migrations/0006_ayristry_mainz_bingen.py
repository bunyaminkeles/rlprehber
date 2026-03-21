"""
Data migration: Mainz ve Mainz-Bingen içeriklerini ayrıştır.
- Mainz-Bingen'e ait yerler ve kaynaklar doğru şehre taşınır.
- Mainz'e özel linkler scope='stadt' yapılır.
- Gerçekten her iki şehir için geçerli linkler scope='eyalet' kalır.
"""
from django.db import migrations


def ayristir(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Yer = apps.get_model('yerler', 'Yer')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        mainz_bingen = Stadt.objects.get(slug='mainz-bingen')
    except Stadt.DoesNotExist:
        return

    # --- KAYNAKLAR ---
    # KdU Mainz-Bingen → mainz-bingen şehrine taşı
    Kaynak.objects.filter(pk=4).update(stadt=mainz_bingen, scope='stadt')

    # Mainz'e özel kaynaklar scope='stadt' yap (zaten mainz'e bağlı)
    Kaynak.objects.filter(pk__in=[1, 3, 6]).update(scope='stadt')

    # --- YERLER ---
    # Bingen/Ingelheim bölgesindeki yerler → mainz-bingen
    Yer.objects.filter(pk__in=[5, 6, 7, 8]).update(stadt=mainz_bingen, scope='stadt')

    # --- LİNKLER ---
    # Mainz'e özel kurumlar → scope='stadt'
    # [1] Mainz Jobcenter, [4] Mainz Şehir Portalı, [6] Mainz Bürgeramt
    OnemliLink.objects.filter(pk__in=[1, 4, 6]).update(scope='stadt')

    # Geri kalan genel linkler (DB, Kleinanzeigen, AOK, Doctolib vs.) scope='eyalet' kalır


def reverse_ayristir(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Yer = apps.get_model('yerler', 'Yer')

    try:
        mainz = Stadt.objects.get(slug='mainz')
    except Stadt.DoesNotExist:
        return

    Kaynak.objects.filter(pk=4).update(stadt=mainz, scope='eyalet')
    Kaynak.objects.filter(pk__in=[1, 3, 6]).update(scope='eyalet')
    Yer.objects.filter(pk__in=[5, 6, 7, 8]).update(stadt=mainz, scope='stadt')
    OnemliLink.objects.filter(pk__in=[1, 4, 6]).update(scope='eyalet')


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0005_fix_forum_scope'),
        ('linkler', '0002_onemlilink_scope_onemlilink_stadt'),
        ('rehber', '0004_kaynak_scope_kaynak_stadt'),
        ('yerler', '0003_yer_scope_yer_stadt_alter_yer_sehir'),
    ]

    operations = [
        migrations.RunPython(ayristir, reverse_ayristir),
    ]
