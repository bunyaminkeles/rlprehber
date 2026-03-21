from django.db import models
from django.db.models import SET_NULL

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'RLP Geneli'),
]

KATEGORI_SECENEKLERI = [
    ('belediye', 'Belediye'),
    ('bamf', 'BAMF'),
    ('okul', 'Okul / Kreş'),
    ('is', 'İş & Çalışma'),
    ('genel', 'Genel'),
]

class Duyuru(models.Model):
    stadt       = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope       = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='eyalet', verbose_name='Kapsam')
    baslik      = models.CharField(max_length=300)
    icerik      = models.TextField()
    kategori    = models.CharField(max_length=20, choices=KATEGORI_SECENEKLERI, default='genel')
    kaynak_url  = models.URLField(blank=True)
    yayinda     = models.BooleanField(default=True)
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-olusturulma']
        verbose_name = 'Duyuru'
        verbose_name_plural = 'Duyurular'

    def __str__(self):
        return self.baslik
