"""
Mainz Belediyesi ve Türk Konsolosluğu RSS beslemelerinden duyuru çeker.
Kullanım: python manage.py rss_cek
"""
import feedparser
import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from duyurular.models import Duyuru

RSS_KAYNAKLAR = [
    {
        'url':      'https://www.mainz.de/rss/pressemitteilungen.xml',
        'kategori': 'belediye',
        'kaynak':   'Mainz Belediyesi',
    },
    {
        'url':      'https://frankfurt.bk.mfa.gov.tr/haberler/rss',
        'kategori': 'genel',
        'kaynak':   'T.C. Frankfurt Başkonsolosluğu',
    },
]

MAX_HABER = 10  # Her kaynaktan en fazla kaç haber


class Command(BaseCommand):
    help = 'RSS beslemelerinden duyuru çeker ve veritabanına kaydeder.'

    def handle(self, *args, **options):
        toplam = 0
        for kaynak in RSS_KAYNAKLAR:
            self.stdout.write(f"\n{kaynak['kaynak']} RSS çekiliyor...")
            try:
                feed = feedparser.parse(kaynak['url'])
                if feed.bozo and not feed.entries:
                    self.stderr.write(f"  Uyarı: RSS okunamadı — {kaynak['url']}")
                    continue

                for entry in feed.entries[:MAX_HABER]:
                    baslik = entry.get('title', '').strip()[:200]
                    icerik = entry.get('summary', entry.get('description', '')).strip()
                    link   = entry.get('link', '')

                    if not baslik or not icerik:
                        continue

                    _, created = Duyuru.objects.get_or_create(
                        baslik=baslik,
                        defaults={
                            'icerik':     icerik[:2000],
                            'kategori':   kaynak['kategori'],
                            'kaynak_url': link,
                            'yayinda':    True,
                        }
                    )
                    if created:
                        toplam += 1
                        self.stdout.write(f'  + {baslik[:70]}')

            except Exception as e:
                self.stderr.write(f'  Hata ({kaynak["kaynak"]}): {e}')

        self.stdout.write(self.style.SUCCESS(f'\nToplam {toplam} yeni duyuru eklendi.'))
