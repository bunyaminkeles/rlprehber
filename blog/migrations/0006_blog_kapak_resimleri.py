from django.db import migrations


def ekle(apps, schema_editor):
    BlogYazisi = apps.get_model('blog', 'BlogYazisi')

    BlogYazisi.objects.filter(slug='wohnberechtigungsschein-wbs-nedir-nasil-alinir').update(
        kapak_resmi='https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&q=80',
    )

    BlogYazisi.objects.filter(slug='helau-mainz-karnavali-nedir').update(
        kapak_resmi='https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?w=1200&q=80',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_helau_karneval_yazisi'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
