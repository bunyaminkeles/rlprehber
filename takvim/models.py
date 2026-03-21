from django.db import models
from django.db.models import SET_NULL

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'RLP Geneli'),
]

ETKINLIK_TUR = [
    ('resmi_tatil', 'Resmi Tatil'),
    ('paskalya', 'Paskalya'),
    ('okul', 'Okul Takvimi'),
    ('yerel', 'Yerel Etkinlik'),
    ('ozel', 'Özel Gün'),
]

class Etkinlik(models.Model):
    stadt    = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope    = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='eyalet', verbose_name='Kapsam')
    baslik   = models.CharField(max_length=200)
    tarih    = models.DateField()
    bitis    = models.DateField(null=True, blank=True)
    tur      = models.CharField(max_length=20, choices=ETKINLIK_TUR, default='ozel')
    aciklama = models.TextField(blank=True)

    class Meta:
        ordering = ['tarih']
        verbose_name = 'Etkinlik'
        verbose_name_plural = 'Etkinlikler'

    def __str__(self):
        return f"{self.baslik} ({self.tarih})"
