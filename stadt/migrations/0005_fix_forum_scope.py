"""
Data migration: Mainz'e bağlı forum konularını scope='eyalet'ten
scope='stadt' olarak düzeltir.
"""
from django.db import migrations


def fix_forum_scope(apps, schema_editor):
    Konu = apps.get_model('forum', 'Konu')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        Konu.objects.filter(stadt=mainz, scope='eyalet').update(scope='stadt')
    except Stadt.DoesNotExist:
        pass


def reverse_fix(apps, schema_editor):
    Konu = apps.get_model('forum', 'Konu')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        Konu.objects.filter(stadt=mainz, scope='stadt').update(scope='eyalet')
    except Stadt.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0004_fix_linkler_scope'),
        ('forum', '0002_alter_konu_options_konu_scope_konu_stadt'),
    ]

    operations = [
        migrations.RunPython(fix_forum_scope, reverse_fix),
    ]
