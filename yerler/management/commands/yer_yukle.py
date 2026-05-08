"""
Kullanım:
  python manage.py yer_yukle yerler.json
  python manage.py yer_yukle yerler.json --guncelle   # mevcut kayıtları da günceller
"""
import json
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from yerler.models import Yer
from stadt.models import Stadt, Eyalet


def _to_html(text):
    if not text or '<' in text:
        return text
    return ''.join(f'<p>{p.strip()}</p>' for p in text.split('\n\n') if p.strip())


class Command(BaseCommand):
    help = 'JSON dosyasından gezilecek yer verilerini içe aktarır'

    def add_arguments(self, parser):
        parser.add_argument('dosya', type=str, help='JSON dosya yolu')
        parser.add_argument('--guncelle', action='store_true', help='Mevcut kayıtları güncelle')

    def handle(self, *args, **options):
        dosya = Path(options['dosya'])
        if not dosya.exists():
            raise CommandError(f'Dosya bulunamadı: {dosya}')

        try:
            veriler = json.loads(dosya.read_text(encoding='utf-8'))
        except json.JSONDecodeError as e:
            raise CommandError(f'JSON hatası: {e}')

        if not isinstance(veriler, list):
            raise CommandError('JSON bir liste ([ ]) olmalı')

        guncelle = options['guncelle']
        eklendi = guncellendi = atlandi = hata = 0

        for i, v in enumerate(veriler, 1):
            try:
                stadt_slug = v.get('stadt', '').strip()
                if not stadt_slug:
                    self.stderr.write(f'[{i}] "stadt" zorunlu, atlandı: {v.get("ad")}')
                    hata += 1
                    continue

                try:
                    stadt = Stadt.objects.get(slug=stadt_slug)
                except Stadt.DoesNotExist:
                    self.stderr.write(f'[{i}] Şehir bulunamadı: {stadt_slug}')
                    hata += 1
                    continue

                ad = v.get('ad', '').strip()
                if not ad:
                    self.stderr.write(f'[{i}] "ad" zorunlu, atlandı')
                    hata += 1
                    continue

                defaults = {
                    'tur':          'yer',
                    'scope':        v.get('scope', 'stadt'),
                    'eyalet':       stadt.eyalet if hasattr(stadt, 'eyalet') else None,
                    'kategori':     v.get('kategori', 'gezi'),
                    'adres':        v.get('adres', ''),
                    'maps_url':     v.get('maps_url', ''),
                    'kapak_resmi':  v.get('kapak_resmi', ''),
                    'website':      v.get('website', ''),
                    'aciklama':     v.get('aciklama', ''),
                    'icerik':       _to_html(v.get('icerik', '')),
                    'wikipedia_url':v.get('wikipedia_url', ''),
                    'sira':         int(v.get('sira', 0)),
                    'aktif':        bool(v.get('aktif', True)),
                }

                obj, created = Yer.objects.get_or_create(
                    ad=ad, stadt=stadt,
                    defaults=defaults,
                )

                if created:
                    eklendi += 1
                    self.stdout.write(self.style.SUCCESS(f'[{i}] Eklendi: {ad}'))
                elif guncelle:
                    for k, val in defaults.items():
                        setattr(obj, k, val)
                    obj.save()
                    guncellendi += 1
                    self.stdout.write(f'[{i}] Güncellendi: {ad}')
                else:
                    atlandi += 1
                    self.stdout.write(f'[{i}] Zaten var (--guncelle ile üzerine yaz): {ad}')

            except Exception as e:
                self.stderr.write(f'[{i}] Hata ({v.get("ad")}): {e}')
                hata += 1

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'Tamamlandı — Eklendi: {eklendi}  Güncellendi: {guncellendi}  '
            f'Atlandı: {atlandi}  Hata: {hata}'
        ))
