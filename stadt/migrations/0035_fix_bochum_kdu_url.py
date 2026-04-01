from django.db import migrations


def fix(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt  = apps.get_model('stadt', 'Stadt')
    try:
        bochum = Stadt.objects.get(slug='bochum')
    except Stadt.DoesNotExist:
        return
    Kaynak.objects.filter(stadt=bochum, baslik='Bochum KdU — Kosten der Unterkunft').update(
        url='https://jobcenter-bochum.de/geld-wohnen/wohnung-heizung'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0034_fix_bochum_kaynaklar'),
    ]

    operations = [
        migrations.RunPython(fix, migrations.RunPython.noop),
    ]
