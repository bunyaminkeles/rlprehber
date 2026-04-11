from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duyurular', '0008_duyuru_yayin_bitis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duyuru',
            name='scope',
            field=models.CharField(
                choices=[
                    ('stadt', 'Şehre Özel'),
                    ('eyalet', 'RLP Geneli'),
                    ('genel', 'Almanya Geneli'),
                ],
                default='eyalet',
                max_length=10,
                verbose_name='Kapsam',
            ),
        ),
    ]
