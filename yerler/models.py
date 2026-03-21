from django.db import models
from django.db.models import SET_NULL

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'RLP Geneli'),
]

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
    stadt           = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope           = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='stadt', verbose_name='Kapsam')
    ad              = models.CharField(max_length=200)
    kategori        = models.CharField(max_length=20, choices=YER_KATEGORI)
    adres           = models.TextField()
    sehir           = models.CharField(max_length=100, default='Mainz', help_text='Eski alan - migration sonrası kullanılmayacak')
    telefon         = models.CharField(max_length=50, blank=True)
    website         = models.URLField(blank=True)
    maps_url        = models.URLField(blank=True, help_text='Google Maps linki')
    aciklama        = models.TextField(blank=True)
    kapak_resmi     = models.URLField(blank=True, verbose_name='Kapak Resmi URL')
    icerik          = models.TextField(blank=True, verbose_name='Blog İçeriği (HTML)')
    wikipedia_url   = models.URLField(blank=True, verbose_name='Wikipedia Kaynak URL')
    aktif           = models.BooleanField(default=True)

    class Meta:
        ordering = ['kategori', 'ad']
        verbose_name = 'Yer'
        verbose_name_plural = 'Yerler'

    def __str__(self):
        return f"{self.ad} ({self.get_kategori_display()})"
