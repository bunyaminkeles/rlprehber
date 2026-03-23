from django.db import models
from django.contrib.auth.models import User


class Konusma(models.Model):
    taraf1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='konusmalar_taraf1')
    taraf2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='konusmalar_taraf2')
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('taraf1', 'taraf2')]
        verbose_name = 'Konuşma'
        verbose_name_plural = 'Konuşmalar'

    def __str__(self):
        return f"{self.taraf1.username} ↔ {self.taraf2.username}"

    def diger_taraf(self, user):
        return self.taraf2 if self.taraf1 == user else self.taraf1

    def son_mesaj(self):
        return self.mesajlar.order_by('-olusturulma').first()

    @classmethod
    def ara(cls, user1, user2):
        """İki kullanıcı arasındaki konuşmayı döndürür, yoksa None."""
        return cls.objects.filter(
            taraf1=user1, taraf2=user2
        ).first() or cls.objects.filter(
            taraf1=user2, taraf2=user1
        ).first()

    @classmethod
    def al_veya_olustur(cls, user1, user2):
        konusma = cls.ara(user1, user2)
        if not konusma:
            konusma = cls.objects.create(taraf1=user1, taraf2=user2)
        return konusma


class Mesaj(models.Model):
    konusma = models.ForeignKey(Konusma, on_delete=models.CASCADE, related_name='mesajlar')
    gonderen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gonderilen_mesajlar')
    icerik = models.TextField()
    okundu = models.BooleanField(default=False)
    olusturulma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['olusturulma']
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'

    def __str__(self):
        return f"{self.gonderen.username}: {self.icerik[:50]}"
