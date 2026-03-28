from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from rehber.models import BultenAbone

class Command(BaseCommand):
    help = 'Tüm aktif bülten abonelerine e-posta gönderir.'

    def add_arguments(self, parser):
        parser.add_argument('konu', type=str, help='E-postanın konusu')
        parser.add_argument('template_adi', type=str, help='Gönderilecek e-posta şablonunun adı (örn: rehber/email/bulten_icerik.html)')

    def handle(self, *args, **options):
        konu = options['konu']
        template_adi = options['template_adi']
        
        aboneler = BultenAbone.objects.filter(aktif=True)
        if not aboneler:
            self.stdout.write(self.style.WARNING('Gönderilecek aktif abone bulunamadı.'))
            return

        self.stdout.write(f'{len(aboneler)} adet aboneye e-posta gönderimi başlıyor...')

        gonderilen_sayisi = 0
        for abone in aboneler:
            try:
                # E-posta içeriğini hem HTML hem de düz metin olarak hazırlayabilirsiniz.
                # Şimdilik sadece HTML kullanıyoruz.
                html_icerik = render_to_string(template_adi, {'abone': abone})
                
                send_mail(
                    subject=konu,
                    message='',  # Düz metin alternatifi (şimdilik boş)
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[abone.email],
                    html_message=html_icerik,
                    fail_silently=False,
                )
                gonderilen_sayisi += 1
                self.stdout.write(self.style.SUCCESS(f' -> {abone.email} adresine gönderildi.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f' HATA: {abone.email} adresine gönderilemedi: {e}'))

        self.stdout.write(self.style.SUCCESS(f'
Toplam {gonderilen_sayisi} e-posta başarıyla gönderildi.'))
