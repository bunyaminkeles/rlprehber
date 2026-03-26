from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.sites.models import Site
from allauth.account.models import EmailAddress, EmailConfirmationHMAC


class Command(BaseCommand):
    help = 'Doğrulanmamış kullanıcılara hatırlatma maili gönderir'

    def handle(self, *args, **kwargs):
        site = Site.objects.get_current()
        base_url = f'https://{site.domain}'

        bekleyenler = EmailAddress.objects.filter(verified=False, primary=True).select_related('user')
        toplam = bekleyenler.count()
        gonderilen = 0

        for email_address in bekleyenler:
            try:
                confirmation = EmailConfirmationHMAC(email_address)
                link = f'{base_url}/accounts/confirm-email/{confirmation.key}/'

                send_mail(
                    subject='Almanyalı Rehber — E-posta adresinizi doğrulamayı unutmayın',
                    message=(
                        f'Merhaba {email_address.user.username},\n\n'
                        'Forum, ilan ve duyuru gibi özelliklerden yararlanmak için '
                        'e-posta adresinizi doğrulamanız gerekiyor.\n\n'
                        f'Doğrulama bağlantısı:\n{link}\n\n'
                        'Almanyalı Rehber'
                    ),
                    from_email=None,
                    recipient_list=[email_address.email],
                )
                gonderilen += 1
                self.stdout.write(f'  ✓ {email_address.email}')
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'  ✗ {email_address.email}: {e}'))

        self.stdout.write(self.style.SUCCESS(f'\n{gonderilen}/{toplam} mail gönderildi.'))
