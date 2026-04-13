from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.models import User

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'Eyalet Geneli'),
    ('genel', 'Almanya Geneli'),
]

class BlogYazisi(models.Model):
    eyalet        = models.ForeignKey('stadt.Eyalet', null=True, blank=True, on_delete=SET_NULL, related_name='blog_yazilari', verbose_name='Eyalet')
    stadt         = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope         = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='eyalet', verbose_name='Kapsam')
    baslik        = models.CharField(max_length=200)
    seo_baslik    = models.CharField(max_length=70, blank=True, verbose_name='SEO Başlığı (60-70 karakter)')
    odak_kelime   = models.CharField(max_length=100, blank=True, verbose_name='Odak Anahtar Kelime')
    slug          = models.SlugField(unique=True, max_length=220)
    yazar         = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    kapak_resmi   = models.URLField(blank=True, verbose_name='Kapak Resmi URL')
    kapak_resmi_dosya = models.ImageField(upload_to='blog/kapaklar/', blank=True, null=True, verbose_name='Kapak Resmi (Dosya)')
    icerik        = models.TextField()
    ozet          = models.CharField(max_length=300, blank=True)
    etiketler     = models.CharField(max_length=200, blank=True, verbose_name='Etiketler (virgülle ayır)')
    yayinda       = models.BooleanField(default=False)
    olusturulma   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-olusturulma']
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'

    @property
    def canonical_url(self):
        if self.scope == 'stadt' and self.stadt and self.stadt.eyalet:
            return f'/{self.stadt.eyalet.slug}/{self.stadt.slug}/blog/{self.slug}/'
        eyalet_slug = self.eyalet.slug if self.eyalet else 'rlp'
        return f'/{eyalet_slug}/blog/{self.slug}/'

    @property
    def kapak_url(self):
        if self.kapak_resmi_dosya:
            return self.kapak_resmi_dosya.url
        return self.kapak_resmi or ''

    @property
    def etiket_listesi(self):
        return [e.strip() for e in self.etiketler.split(',') if e.strip()]

    def __str__(self):
        return self.baslik
