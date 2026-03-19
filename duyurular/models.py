from django.db import models

KATEGORI_SECENEKLERI = [
    ('belediye', 'Belediye'),
    ('bamf', 'BAMF'),
    ('okul', 'Okul / Kreş'),
    ('is', 'İş & Çalışma'),
    ('genel', 'Genel'),
]

class Duyuru(models.Model):
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
