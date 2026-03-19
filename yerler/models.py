from django.db import models

YER_KATEGORI = [
    ('resmi_kurum', 'Resmi Kurum'),
    ('alisveris', 'Alışveriş Merkezi'),
    ('turk_market', 'Türk Marketi'),
    ('ibadet', 'Cami / İbadethane'),
    ('tuv', 'TÜV / GTÜ İstasyonu'),
    ('saglik', 'Sağlık'),
    ('egitim', 'Eğitim'),
    ('gezi', 'Gezi & Kültür'),
    ('yeme_icme', 'Yeme & İçme'),
    ('diger', 'Diğer'),
]

class Yer(models.Model):
    ad          = models.CharField(max_length=200)
    kategori    = models.CharField(max_length=20, choices=YER_KATEGORI)
    adres       = models.TextField()
    sehir       = models.CharField(max_length=100, default='Mainz')
    telefon     = models.CharField(max_length=50, blank=True)
    website     = models.URLField(blank=True)
    maps_url    = models.URLField(blank=True, help_text='Google Maps linki')
    aciklama    = models.TextField(blank=True)
    aktif       = models.BooleanField(default=True)

    class Meta:
        ordering = ['kategori', 'ad']
        verbose_name = 'Yer'
        verbose_name_plural = 'Yerler'

    def __str__(self):
        return f"{self.ad} ({self.get_kategori_display()})"
