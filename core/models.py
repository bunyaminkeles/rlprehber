from django.db import models


ONERI_TUR = [
    ('oneri', 'Öneri'),
    ('hata', 'Hata Bildirimi'),
    ('icerik', 'İçerik Talebi'),
    ('diger', 'Diğer'),
]


class Oneri(models.Model):
    tur         = models.CharField(max_length=20, choices=ONERI_TUR, default='oneri', verbose_name='Tür')
    ad          = models.CharField(max_length=100, blank=True, verbose_name='Ad Soyad')
    eposta      = models.EmailField(blank=True, verbose_name='E-posta')
    mesaj       = models.TextField(verbose_name='Mesaj')
    olusturulma = models.DateTimeField(auto_now_add=True)
    okundu      = models.BooleanField(default=False, verbose_name='Okundu')

    class Meta:
        ordering = ['-olusturulma']
        verbose_name = 'Öneri'
        verbose_name_plural = 'Öneriler'

    def __str__(self):
        return f'{self.get_tur_display()} — {self.ad or "Anonim"} ({self.olusturulma:%d.%m.%Y})'
