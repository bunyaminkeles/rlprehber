from django.db import models
from django.db.models import SET_NULL

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'Eyalet Geneli'),
    ('almanya', 'Tüm Almanya'),
]

KAYNAK_KATEGORI = [
    ('resmi', 'Resmi İşlemler & Kurumlar'),
    ('ilan', 'İlan Platformları'),
    ('is', 'İş & Kariyer'),
    ('konut', 'Konut'),
    ('egitim', 'Eğitim'),
    ('saglik', 'Sağlık'),
    ('ulasim', 'Ulaşım'),
    ('almanca', 'Almanca Öğrenimi'),
    ('gunluk', 'Günlük Yaşam'),
    ('gezi', 'Gezi & Kültür'),
    ('haber', 'Haber & Bilgi'),
    ('diger', 'Diğer'),
]

KAYNAK_TIPI = [
    ('sayfa', 'Dahili Sayfa'),
    ('link', 'Harici Link'),
]

class Kaynak(models.Model):
    eyalet      = models.ForeignKey('stadt.Eyalet', null=True, blank=True, on_delete=SET_NULL, related_name='kaynaklar', verbose_name='Eyalet')
    stadt       = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope       = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='eyalet', verbose_name='Kapsam')
    baslik      = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=220, unique=True, blank=True, null=True, help_text='Sadece dahili sayfalar için kullanılır.')
    tip         = models.CharField(max_length=10, choices=KAYNAK_TIPI, default='sayfa')
    url         = models.URLField(blank=True, help_text='Sadece harici linkler için kullanılır.')
    kategori    = models.CharField(max_length=20, choices=KAYNAK_KATEGORI)
    icerik      = models.TextField(blank=True, help_text='Sadece dahili sayfalar için kullanılır.')
    ozet        = models.CharField(max_length=300, blank=True)
    icon        = models.CharField(max_length=50, default='bi-info-circle')
    sira        = models.PositiveIntegerField(default=0)
    yayinda     = models.BooleanField(default=True)
    guncelleme  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['kategori', 'sira']
        verbose_name = 'Kaynak'
        verbose_name_plural = 'Kaynaklar'

    def __str__(self):
        return self.baslik


class BultenAbone(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-posta")
    kayit_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")
    aktif = models.BooleanField(default=True, verbose_name="Aktif")

    class Meta:
        verbose_name = "Bülten Abonesi"
        verbose_name_plural = "Bülten Aboneleri"
        ordering = ['-kayit_tarihi']

    def __str__(self):
        return self.email
