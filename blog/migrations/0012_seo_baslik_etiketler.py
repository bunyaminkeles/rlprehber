from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_add_genel_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogyazisi',
            name='seo_baslik',
            field=models.CharField(blank=True, max_length=70, verbose_name='SEO Başlığı (60-70 karakter)'),
        ),
        migrations.AddField(
            model_name='blogyazisi',
            name='etiketler',
            field=models.CharField(blank=True, max_length=200, verbose_name='Etiketler (virgülle ayır)'),
        ),
    ]
