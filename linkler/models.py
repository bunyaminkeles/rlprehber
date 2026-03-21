from django.db import models
from django.db.models import SET_NULL

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'RLP Geneli'),
]

LINK_KATEGORI = [
    ('resmi', 'Resmi Kurum'),
    ('ilan', 'İlan Platformu'),
    ('is', 'İş & Kariyer'),
    ('egitim', 'Eğitim'),
    ('saglik', 'Sağlık'),
    ('ulasim', 'Ulaşım'),
    ('haber', 'Haber & Bilgi'),
    ('diger', 'Diğer'),
]

class OnemliLink(models.Model):
    stadt       = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope       = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='eyalet', verbose_name='Kapsam')
    ad          = models.CharField(max_length=200)
    url         = models.URLField()
    kategori    = models.CharField(max_length=20, choices=LINK_KATEGORI)
    aciklama    = models.TextField(blank=True)
    randevu_url = models.URLField(blank=True, help_text='Varsa randevu/iletişim linki')
    aktif       = models.BooleanField(default=True)
    sira        = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['kategori', 'sira', 'ad']
        verbose_name = 'Önemli Link'
        verbose_name_plural = 'Önemli Linkler'

    def __str__(self):
        return self.ad
