"""
Kullanım:
  python manage.py yer_icerik_yukle /path/to/data.json

JSON formatı:
  {
    "stadt_slug": "berlin",
    "yerler": [
      {
        "id": 117,                     -- varsa günceller, yoksa oluşturur
        "ad": "Berliner Fernsehturm",  -- id yoksa ad ile arar
        "kategori": "gezi",
        "adres": "Alexanderplatz, Berlin",
        "aciklama": "Kısa açıklama...",
        "kapak_resmi": "https://...",
        "wikipedia_url": "https://...",
        "icerik": "<p>HTML içerik...</p>"
      }
    ]
  }
"""
import json
from django.core.management.base import BaseCommand, CommandError
from yerler.models import Yer
from stadt.models import Stadt


class Command(BaseCommand):
    help = 'JSON dosyasından yer içeriklerini yükler / günceller'

    def add_arguments(self, parser):
        parser.add_argument('json_dosya', type=str, help='JSON dosyasının yolu')

    def handle(self, *args, **options):
        dosya = options['json_dosya']
        try:
            with open(dosya, encoding='utf-8') as f:
                veri = json.load(f)
        except FileNotFoundError:
            raise CommandError(f'Dosya bulunamadı: {dosya}')
        except json.JSONDecodeError as e:
            raise CommandError(f'Geçersiz JSON: {e}')

        stadt_slug = veri.get('stadt_slug')
        stadt = None
        if stadt_slug:
            try:
                stadt = Stadt.objects.get(slug=stadt_slug)
            except Stadt.DoesNotExist:
                raise CommandError(f'Şehir bulunamadı: {stadt_slug}')

        ALANLAR = ['ad', 'kategori', 'adres', 'aciklama', 'kapak_resmi', 'wikipedia_url', 'icerik']

        eklendi = guncellendi = 0
        for yer_veri in veri.get('yerler', []):
            yer = None

            if 'id' in yer_veri:
                try:
                    yer = Yer.objects.get(id=yer_veri['id'])
                except Yer.DoesNotExist:
                    pass

            if yer is None and 'ad' in yer_veri:
                yer = Yer.objects.filter(ad=yer_veri['ad']).first()

            if yer is None:
                yer = Yer(tur='yer', aktif=True)
                if stadt:
                    yer.stadt = stadt
                eklendi += 1
                eylem = 'Oluşturuldu'
            else:
                guncellendi += 1
                eylem = 'Güncellendi'

            for alan in ALANLAR:
                if alan in yer_veri:
                    setattr(yer, alan, yer_veri[alan])

            # kapak_resmi verilmişse yüklenmiş fotoğrafı temizle (template kapak_foto'yu önceliklendirir)
            if 'kapak_resmi' in yer_veri and yer_veri['kapak_resmi']:
                yer.kapak_foto = None

            if stadt and not yer.stadt_id:
                yer.stadt = stadt

            yer.save()
            self.stdout.write(f'  ✅ {eylem}: [{yer.id}] {yer.ad}')

        self.stdout.write(self.style.SUCCESS(
            f'\nTamamlandı: {eklendi} eklendi, {guncellendi} güncellendi.'
        ))
