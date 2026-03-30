from django.db import migrations


def guncelle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.filter(baslik='AJet — Uçuş Arama').delete()


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Kaynak.objects.get_or_create(
        baslik='AJet — Uçuş Arama',
        defaults={
            'tip': 'link', 'url': 'https://ajet.com/tr',
            'kategori': 'ulasim', 'icon': 'bi-airplane',
            'scope': 'almanya', 'yayinda': True,
        }
    )


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0032_kirik_link_duzeltmeleri'),
    ]

    operations = [
        migrations.RunPython(guncelle, geri_al),
    ]
