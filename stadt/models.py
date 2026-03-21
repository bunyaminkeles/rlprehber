from django.db import models


STADT_TYP = [
    ('kreisfrei', 'Kreisfreie Stadt'),
    ('landkreis', 'Landkreis'),
]


class Stadt(models.Model):
    name = models.CharField(max_length=100, verbose_name='Şehir Adı')
    slug = models.SlugField(unique=True, verbose_name='URL Slug')
    typ = models.CharField(max_length=20, choices=STADT_TYP, default='kreisfrei', verbose_name='Tür')
    lat = models.FloatField(null=True, blank=True, verbose_name='Enlem')
    lng = models.FloatField(null=True, blank=True, verbose_name='Boylam')
    population = models.IntegerField(null=True, blank=True, verbose_name='Nüfus')
    auslaenderbehorde_url = models.URLField(blank=True, verbose_name='Ausländerbehörde URL')
    termin_url = models.URLField(blank=True, verbose_name='Randevu URL')
    beschreibung = models.TextField(blank=True, verbose_name='Açıklama')
    aktiv = models.BooleanField(default=False, verbose_name='Aktif')

    class Meta:
        ordering = ['name']
        verbose_name = 'Şehir'
        verbose_name_plural = 'Şehirler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('stadt:home', kwargs={'stadt_slug': self.slug})
