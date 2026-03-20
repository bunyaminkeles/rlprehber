from django.db import models
from django.contrib.auth.models import User

class ForumKategori(models.Model):
    ad       = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True)
    sira     = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sira']
        verbose_name = 'Forum Kategorisi'
        verbose_name_plural = 'Forum Kategorileri'

    def __str__(self):
        return self.ad

class Konu(models.Model):
    kategori    = models.ForeignKey(ForumKategori, on_delete=models.CASCADE, related_name='konular')
    yazar       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    baslik      = models.CharField(max_length=200)
    icerik      = models.TextField()
    sabitlendi  = models.BooleanField(default=False)
    kapali      = models.BooleanField(default=False)
    olusturulma = models.DateTimeField(auto_now_add=True)
    guncelleme  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-sabitlendi', '-olusturulma']
        verbose_name = 'Konu'
        verbose_name_plural = 'Konular'

    def __str__(self):
        return self.baslik

class Yorum(models.Model):
    konu        = models.ForeignKey(Konu, on_delete=models.CASCADE, related_name='yorumlar')
    yazar       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    icerik      = models.TextField()
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['olusturulma']
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return f"{self.konu.baslik} - {self.yazar}"
