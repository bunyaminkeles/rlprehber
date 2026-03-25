from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_konu_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='konu',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to='forum/konular/', verbose_name='Resim'),
        ),
        migrations.AddField(
            model_name='yorum',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to='forum/yorumlar/', verbose_name='Resim'),
        ),
    ]
