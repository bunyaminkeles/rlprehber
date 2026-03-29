from django.db import migrations


def mainz_linkleri_guncelle(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')

    Yer.objects.filter(id=1).update(
        website='https://mainz.de/vv/oe/auslaenderangelegenheiten'
    )
    Yer.objects.filter(id=20).update(
        website='https://www.hwk.de/'
    )
    Yer.objects.filter(id=35).update(
        website='https://www.mainz.de/vv/oe/verkehrsueberwachungsamt/verkehrsabteilung/kfz-zulassung/kfz-zulassung'
    )


def geri_al(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')

    Yer.objects.filter(id=1).update(
        website='https://www.mainz.de/vv/produkte/landes-und-landeshauptstadt/auslaenderamt.php'
    )
    Yer.objects.filter(id=20).update(
        website='https://www.hwk-rheinhessen.de/'
    )
    Yer.objects.filter(id=35).update(
        website='https://www.mainz.de/vv/produkte/landes-und-landeshauptstadt/kfz-zulassung.php'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0023_seed_hamburg_yerler'),
    ]

    operations = [
        migrations.RunPython(mainz_linkleri_guncelle, geri_al),
    ]
