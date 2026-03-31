from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Ilan

@receiver(post_save, sender=Ilan)
def ilan_onay_bildirimi(sender, instance, created, **kwargs):
    # İlan yeni oluşturulduysa ve onay bekliyorsa
    if created and not getattr(instance, 'onaylandi', True):
        subject = f'[Onay Bekliyor] Yeni İlan: {instance.baslik}'
        message = (
            f"Sistemde onayınızı bekleyen yeni bir ilan eklendi.\n\n"
            f"Başlık: {instance.baslik}\n"
            f"Kullanıcı: {instance.sahip.username if instance.sahip else 'Bilinmiyor'}\n\n"
            f"İncelemek ve onaylamak için admin paneline gidin:\n"
            f"https://almanyalirehber.com/admin/ilan/ilan/{instance.id}/change/"
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'info@almanyalirehber.com'),
            recipient_list=['info@analizus.com'],  # E-postanın gönderileceği admin adresi
            fail_silently=True,
        )