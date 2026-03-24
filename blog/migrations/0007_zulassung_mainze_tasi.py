from django.db import migrations


def tasi(apps, schema_editor):
    BlogYazisi = apps.get_model('blog', 'BlogYazisi')
    Stadt = apps.get_model('stadt', 'Stadt')

    mainz = Stadt.objects.filter(slug='mainz').first()
    if not mainz:
        return

    BlogYazisi.objects.filter(slug='zulassungsstelle-arac-kayit-islemleri').update(
        scope='stadt',
        stadt=mainz,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_kapak_resimleri'),
        ('stadt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(tasi, migrations.RunPython.noop),
    ]
