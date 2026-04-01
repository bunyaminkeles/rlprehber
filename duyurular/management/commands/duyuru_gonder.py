from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Tüm kayıtlı kullanıcılara belirli bir duyuruyu e-posta ile gönderir.'

    def add_arguments(self, parser):
        parser.add_argument('konu', type=str, help='E-posta konusu')
        parser.add_argument('duyuru_url', type=str, help='Duyurunun tam URL\'si')
        parser.add_argument(
            '--template',
            type=str,
            default='rehber/email/duyuru_bildirim.html',
            help='Kullanılacak e-posta şablonu (varsayılan: rehber/email/duyuru_bildirim.html)',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='E-posta göndermeden kaç kişiye gönderileceğini gösterir',
        )

    def handle(self, *args, **options):
        konu = options['konu']
        duyuru_url = options['duyuru_url']
        template_adi = options['template']
        dry_run = options['dry_run']

        kullanicilar = User.objects.filter(is_active=True).exclude(email='')
        toplam = kullanicilar.count()

        if toplam == 0:
            self.stdout.write(self.style.WARNING('E-posta gönderilecek aktif kullanıcı bulunamadı.'))
            return

        if dry_run:
            self.stdout.write(self.style.WARNING(f'[DRY RUN] {toplam} kullanıcıya gönderilecek. Gerçek gönderim yapılmadı.'))
            return

        self.stdout.write(f'{toplam} kullanıcıya e-posta gönderimi başlıyor...')

        gonderilen = 0
        for kullanici in kullanicilar:
            try:
                html_icerik = render_to_string(template_adi, {
                    'konu': konu,
                    'kullanici_adi': kullanici.first_name or kullanici.username,
                    'duyuru_url': duyuru_url,
                })
                send_mail(
                    subject=konu,
                    message=(
                        f'Merhaba,\n\n'
                        f'Duyuruya buradan ulaşabilirsiniz: {duyuru_url}\n\n'
                        f'Almanyalı Rehber\ninfo@analizus.com'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[kullanici.email],
                    html_message=html_icerik,
                    fail_silently=False,
                )
                gonderilen += 1
                self.stdout.write(self.style.SUCCESS(f'  -> {kullanici.email}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'  HATA [{kullanici.email}]: {e}'))

        self.stdout.write(self.style.SUCCESS(f'\nToplam {gonderilen}/{toplam} e-posta başarıyla gönderildi.'))
