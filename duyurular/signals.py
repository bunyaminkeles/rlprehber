from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
import logging
from .models import Duyuru

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Duyuru)
def duyuru_onay_bildirimi(sender, instance, created, **kwargs):
    logger.warning(f"🔔 [SİNYAL TETİKLENDİ] Duyuru: {instance.baslik} | Yeni mi?: {created}")

    # Duyuru yeni oluşturulduysa ve onay bekliyorsa (yayinda=False)
    if created and not getattr(instance, 'yayinda', True):
        logger.warning("📩 [SİNYAL] Şartlar sağlandı, e-posta gönderimi başlatılıyor...")
        subject = f'[Onay Bekliyor] Yeni Duyuru: {instance.baslik}'
        message = (
            f"Sistemde onayınızı bekleyen yeni bir duyuru eklendi.\n\n"
            f"Başlık: {instance.baslik}\n"
            f"Kullanıcı: {instance.yazar.username if instance.yazar else 'Bilinmiyor'}\n\n"
            f"İncelemek ve yayınlamak için admin paneline gidin:\n"
            f"https://almanyalirehber.com/admin/duyurular/duyuru/{instance.id}/change/"
        )
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'info@almanyalirehber.com'),
                recipient_list=['info@analizus.com'],
                fail_silently=False,
            )
            logger.warning("✅ [SİNYAL] E-posta başarıyla gönderildi!")
        except Exception as e:
            logger.error(f"❌ [SİNYAL HATASI] E-posta gönderilemedi: {e}")