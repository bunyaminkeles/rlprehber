from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_seo_baslik_etiketler'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogyazisi',
            name='odak_kelime',
            field=models.CharField(blank=True, max_length=100, verbose_name='Odak Anahtar Kelime'),
        ),
    ]
