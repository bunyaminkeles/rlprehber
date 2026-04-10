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
    randevu_url = models.URLField(blank=True, verbose_name='Randevu Linki', help_text='Varsa randevu/iletişim linki')
    sira        = models.PositiveIntegerField(default=0)
    yayinda     = models.BooleanField(default=True)
    guncelleme  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['kategori', 'sira']
        verbose_name = 'Kaynak'
        verbose_name_plural = 'Kaynaklar'

    def __str__(self):
        return self.baslik


BELGE_KATEGORI = [
    ('aile',   'Aile & Çocuk'),
    ('konut',  'Konut & Kira'),
    ('vize',   'Vize & Oturum'),
    ('is',     'İş & Eğitim'),
    ('genel',  'Genel'),
]

class Belge(models.Model):
    baslik       = models.CharField(max_length=300, verbose_name='Başlık')
    dosya        = models.FileField(upload_to='belgeler/pdf/', blank=True, null=True, verbose_name='Dosya (PDF/DOCX)')
    harici_link  = models.URLField(blank=True, null=True, verbose_name='Harici Link', help_text='Dosya bizde değilse resmi kurumun linki')
    kategori     = models.CharField(max_length=10, choices=BELGE_KATEGORI, default='genel', verbose_name='Kategori')
    stadt        = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir', help_text='Boşsa Federal (Tüm Almanya)')
    ozet         = models.CharField(max_length=300, blank=True, verbose_name='Kısa Açıklama')
    sira         = models.PositiveIntegerField(default=0, verbose_name='Sıra')
    yayinda      = models.BooleanField(default=True, verbose_name='Yayında')
    olusturulma  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['kategori', 'sira', 'baslik']
        verbose_name = 'Belge'
        verbose_name_plural = 'Belgeler'

    def __str__(self):
        return self.baslik

    @property
    def kapsam(self):
        return self.stadt.name if self.stadt else 'Federal'

    @property
    def indirme_url(self):
        if self.dosya:
            return self.dosya.url
        return self.harici_link or '#'

    @property
    def dosya_uzantisi(self):
        if self.dosya:
            name = self.dosya.name.lower()
            if name.endswith('.pdf'):
                return 'pdf'
            if name.endswith('.docx') or name.endswith('.doc'):
                return 'docx'
        return 'link'


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
