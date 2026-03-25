from django.db import migrations


PAKETLER = [
    dict(ad='Temel',  aciklama='Hızlı başlangıç, risksiz deneyin.',       fiyat='9.90',  sure_etiketi='/ ay', renk='secondary', vurgulu=False, sira=1,
         ozellikler='İşletme adı ve adres\nKategori rozeti\nGoogle Maps linki\nAçıklama metni\nTelefon numarası', iletisim_notu=''),
    dict(ad='Plus',   aciklama='Müşterilerinize daha fazla ulaşın.',       fiyat='19.90', sure_etiketi='/ ay', renk='primary',   vurgulu=True,  sira=2,
         ozellikler='Temel paketteki her şey\n3 fotoğraf galerisi\nWhatsApp butonu\nInstagram linki\nÇalışma saatleri\nWeb sitesi linki', iletisim_notu=''),
    dict(ad='Pro',    aciklama='Listenin en üstünde, herkesten önce.',     fiyat='34.90', sure_etiketi='/ ay', renk='warning',   vurgulu=False, sira=3,
         ozellikler='Plus paketteki her şey\n"Öne Çıkan" rozeti\nKategori listesinde en üst sıra\nÖncelikli destek',
         iletisim_notu='Paket almak veya daha fazla bilgi için bizimle iletişime geçin.\nÖdeme IBAN ile yapılmaktadır.'),
]


def seed(apps, schema_editor):
    ReklamPaketi = apps.get_model('yerler', 'ReklamPaketi')
    # Eski isimli paketleri temizle
    ReklamPaketi.objects.filter(ad__in=['Basic', 'Bronz', 'Silver', 'Gold', 'Premium']).delete()
    for p in PAKETLER:
        ReklamPaketi.objects.update_or_create(ad=p['ad'], defaults={**p, 'aktif': True})


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0009_merge_0007'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
