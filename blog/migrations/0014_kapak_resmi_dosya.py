from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_odak_kelime'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogyazisi',
            name='kapak_resmi_dosya',
            field=models.ImageField(blank=True, null=True, upload_to='blog/kapaklar/', verbose_name='Kapak Resmi (Dosya)'),
        ),
    ]
