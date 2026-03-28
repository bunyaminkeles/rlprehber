from django.db import models


STADT_TYP = [
    ('kreisfrei', 'Kreisfreie Stadt'),
    ('landkreis', 'Landkreis'),
]


class Eyalet(models.Model):
    ad = models.CharField(max_length=100, verbose_name='Eyalet Adı')
    slug = models.SlugField(unique=True, verbose_name='URL Slug')
    kod = models.CharField(max_length=4, unique=True, verbose_name='Kısaltma (BY, NW…)')
    baskent = models.CharField(max_length=100, blank=True, verbose_name='Başkent')
    aktif = models.BooleanField(default=False, verbose_name='Aktif')

    class Meta:
        ordering = ['ad']
        verbose_name = 'Eyalet'
        verbose_name_plural = 'Eyaletler'

    def __str__(self):
        return f'{self.ad} ({self.kod})'


class Stadt(models.Model):
    eyalet = models.ForeignKey(
        Eyalet,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sehirler',
        verbose_name='Eyalet',
    )
    name = models.CharField(max_length=100, verbose_name='Şehir Adı')
    slug = models.SlugField(unique=True, verbose_name='URL Slug')
    typ = models.CharField(max_length=20, choices=STADT_TYP, default='kreisfrei', verbose_name='Tür')
    lat = models.FloatField(null=True, blank=True, verbose_name='Enlem')
    lng = models.FloatField(null=True, blank=True, verbose_name='Boylam')
    population = models.IntegerField(null=True, blank=True, verbose_name='Nüfus')
    auslaenderbehorde_url = models.URLField(blank=True, verbose_name='Ausländerbehörde URL')
    termin_url = models.URLField(blank=True, verbose_name='Randevu URL')
    rss_duyuru_url = models.URLField(blank=True, verbose_name='Belediye RSS / Haber URL')
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
