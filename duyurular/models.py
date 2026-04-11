from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'RLP Geneli'),
    ('genel', 'Almanya Geneli'),
]

KATEGORI_SECENEKLERI = [
    ('belediye', 'Belediye'),
    ('bamf', 'BAMF'),
    ('okul', 'Okul / Kreş'),
    ('is', 'İş & Çalışma'),
    ('genel', 'Genel'),
]

KAYNAK_TIPI = [
    ('konsolosluk', 'T.C. Konsolosluk'),
    ('belediye', 'Belediye'),
    ('kullanici', 'Kullanıcı'),
]

class Duyuru(models.Model):
    eyalet      = models.ForeignKey('stadt.Eyalet', null=True, blank=True, on_delete=SET_NULL, related_name='duyurular', verbose_name='Eyalet')
    stadt       = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope       = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='eyalet', verbose_name='Kapsam')
    yazar       = models.ForeignKey(User, null=True, blank=True, on_delete=SET_NULL, verbose_name='Yazar')
    kaynak_tipi = models.CharField(max_length=15, choices=KAYNAK_TIPI, default='belediye', verbose_name='Kaynak Tipi')
    baslik      = models.CharField(max_length=300)
    icerik      = models.TextField()
    kategori    = models.CharField(max_length=20, choices=KATEGORI_SECENEKLERI, default='genel')
    resim       = models.ImageField(upload_to='duyurular/', blank=True, null=True, verbose_name='Resim')
    kaynak_url  = models.URLField(blank=True, max_length=500)
    yayinda     = models.BooleanField(default=True)
    yayin_bitis = models.DateField(null=True, verbose_name='Yayın Bitiş Tarihi')
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-olusturulma']
        verbose_name = 'Duyuru'
        verbose_name_plural = 'Duyurular'

    def __str__(self):
        return self.baslik
