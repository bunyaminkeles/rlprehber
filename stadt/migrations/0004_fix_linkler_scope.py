"""
Data migration: Mainz'e bağlı OnemliLink kayıtlarını scope='eyalet'ten
scope='stadt' olarak düzeltir. Linkler/kurumlar şehre özeldir, RLP geneli değil.
"""
from django.db import migrations


def fix_linkler_scope(apps, schema_editor):
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        OnemliLink.objects.filter(stadt=mainz, scope='eyalet').update(scope='stadt')
    except Stadt.DoesNotExist:
        pass


def reverse_fix(apps, schema_editor):
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        OnemliLink.objects.filter(stadt=mainz, scope='stadt').update(scope='eyalet')
    except Stadt.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0003_seed_rlp_staedte'),
        ('linkler', '0002_onemlilink_scope_onemlilink_stadt'),
    ]

    operations = [
        migrations.RunPython(fix_linkler_scope, reverse_fix),
    ]
