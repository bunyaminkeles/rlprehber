from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from stadt.models import Stadt, Eyalet
from yerler.models import Yer
from forum.models import ForumKategori

class Command(BaseCommand):
    help = 'Bir şehri (KdU, Kurumlar, İlan altyapısı) veritabanında sıfırdan, hatasız ve güvenle inşa eder.'

    def add_arguments(self, parser):
        parser.add_argument('stadt_name', type=str, help='İnşa edilecek şehrin adı (Örn: Mainz)')
        parser.add_argument('--eyalet', type=str, default='nrw', help='Bağlı olduğu eyalet slug (Örn: nrw)')

    def handle(self, *args, **options):
        # 1. Girdi Temizliği (Kullanıcı hatasını tolere et)
        stadt_name = options['stadt_name'].strip().title()
        eyalet_slug = options['eyalet'].strip().lower()

        self.stdout.write(f"🚀 [INIT] {stadt_name} ekosistemi ayağa kaldırılıyor...")

        try:
            # 2. Ya Hep Ya Hiç Kuralı (Bozuk veri oluşmasını engeller)
            with transaction.atomic():
                
                eyalet, _ = Eyalet.objects.get_or_create(slug=eyalet_slug, defaults={'isim': eyalet_slug.upper()})

                # ADIM 1: Şehri Yarat veya Getir (Idempotent)
                stadt, created = Stadt.objects.get_or_create(isim=stadt_name)
                if created:
                    stadt.aktiv = True
                    stadt.eyalet = eyalet
                    stadt.slug = stadt_name.lower().replace(' ', '-')
                    stadt.save()
                action = "Yaratıldı" if created else "Zaten Mevcut"
                self.stdout.write(self.style.SUCCESS(f"  ✓ Şehir Kaydı ({stadt_name}): {action}"))

                # ADIM 2: Zorunlu Kurumları Ekle (Jobcenter, Ausländerbehörde vb.)
                kurumlar = ["Jobcenter", "Ausländerbehörde", "Bürgeramt", "Agentur für Arbeit", "Finanzamt"]
                for kurum in kurumlar:
                    Yer.objects.get_or_create(ad=f"{kurum} {stadt_name}", defaults={'kategori': 'resmi_kurum', 'sehir': stadt_name})
                self.stdout.write(self.style.SUCCESS(f"  ✓ Temel Kurumlar ({len(kurumlar)} adet) Bağlandı."))

                # ADIM 3: İlan ve Kategori Altyapısı (Feature Flag ile uyumlu)
                forum_kats = ['Genel Sohbet', 'Resmi İşlemler', 'İş & Kariyer', 'Konut & Ev', 'Araç & Ulaşım']
                for kat in forum_kats:
                    ForumKategori.objects.get_or_create(ad=kat)
                self.stdout.write(self.style.SUCCESS(f"  ✓ Forum Kategorileri Hazır."))

            # Eğer kod buraya ulaştıysa, her şey kusursuz işledi demektir.
            self.stdout.write(self.style.SUCCESS(f"✅ [BİTTİ] {stadt_name} başarıyla ayağa kaldırıldı ve yayına hazır."))

        except Exception as e:
            # İşlem yarıda kesilirse, veritabanını kirletmeden işlemi iptal eder ve uyarır.
            raise CommandError(f"HATA: {stadt_name} inşa edilirken sistem çöktü. İşlemler geri alındı (Rollback). Detay: {str(e)}")