from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'RLP Geneli'),
]

class BlogYazisi(models.Model):
    stadt         = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope         = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='eyalet', verbose_name='Kapsam')
    baslik        = models.CharField(max_length=200)
    slug          = models.SlugField(unique=True, max_length=220)
    yazar         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    kapak_resmi   = models.URLField(blank=True, verbose_name='Kapak Resmi URL')
    icerik        = models.TextField()
    ozet          = models.CharField(max_length=300, blank=True)
    yayinda       = models.BooleanField(default=False)
    olusturulma   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-olusturulma']
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'

    def __str__(self):
        return self.baslik
