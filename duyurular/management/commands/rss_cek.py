"""
Mainz Belediyesi, T.C. Dışişleri ve Mainz Konsolosluğu'ndan duyuru çeker.
Kullanım: python manage.py rss_cek
"""
import feedparser
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from duyurular.models import Duyuru

RSS_KAYNAKLAR = [
    {
        'url':      'https://www.mainz.de/pressemeldungen/?sp%3Aout=rss',
        'kategori': 'belediye',
        'kaynak':   'Mainz Belediyesi',
    },
    {
        'url':      'https://www.mfa.gov.tr/rss.tr.mfa',
        'kategori': 'genel',
        'kaynak':   'T.C. Dışişleri Bakanlığı',
    },
]

SCRAPE_KAYNAKLAR = [
    {
        'url':        'https://mainz-bk.mfa.gov.tr/Mission/Announcements',
        'kategori':   'genel',
        'kaynak':     'T.C. Mainz Başkonsolosluğu',
        'link_base':  'https://mainz-bk.mfa.gov.tr',
        'link_match': '/Mission/ShowAnnouncement/',
    },
]

MAX_HABER = 15
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; MainzerBingerBot/1.0)',
    'Accept-Language': 'de-DE,de;q=0.9,tr;q=0.8,en;q=0.7',
}

# Bu başlıklar navigasyon öğesi — duyuru sayılmasın
NAV_BLACKLIST = {
    'generalkonsulat', 'mitteilungen', 'informationen', 'konsularische dienste',
    'tüm duyurular', 'randevu iptali', 'vize ön başvuru', 'randevu sorgulama',
    'ehemalige generalkonsuln', 'yabancılar için vize',
    'türk vatandaşları için', 'die botschaft',
}


def _temizle_baslik(text: str) -> str:
    """Başlıklardaki kurumsal imza artıklarını temizler."""
    import re
    # "Türkisches Generalkonsulat  Mainz12.03.2024" gibi artıkları kaldır
    text = re.sub(r'Türkisches Generalkonsulat\s+Mainz\s*[\d.]*', '', text)
    return text.strip()


def _is_nav_item(text: str) -> bool:
    """Kısa veya bilinen navigasyon metinlerini filtrele."""
    t = text.strip().lower()
    if len(t) < 15:
        return True
    for kw in NAV_BLACKLIST:
        if t.startswith(kw):
            return True
    return False


class Command(BaseCommand):
    help = 'RSS beslemelerinden ve Mainz Konsolosluğu sitesinden duyuru çeker.'

    def add_arguments(self, parser):
        parser.add_argument('--sadece-rss', action='store_true',
                            help='Sadece RSS kaynaklarını çek, scraping yapma')
        parser.add_argument('--temizle', action='store_true',
                            help='Navigasyon öğelerini veritabanından sil')

    def handle(self, *args, **options):
        if options.get('temizle'):
            self._temizle()
            return

        toplam = 0

        self.stdout.write(self.style.MIGRATE_HEADING('\n=== RSS Beslemeleri ==='))
        for kaynak in RSS_KAYNAKLAR:
            toplam += self._rss_isle(kaynak)

        if not options.get('sadece_rss'):
            self.stdout.write(self.style.MIGRATE_HEADING('\n=== Web Scraping ==='))
            for kaynak in SCRAPE_KAYNAKLAR:
                toplam += self._scrape_isle(kaynak)

        self.stdout.write(self.style.SUCCESS(f'\n✅ Toplam {toplam} yeni duyuru eklendi.'))
        self._eskiyi_temizle()

    # ------------------------------------------------------------------ #
    def _eskiyi_temizle(self):
        """Her kategoride en fazla 10 duyuru bırak, gerisini sil."""
        from duyurular.models import Duyuru
        kategoriler = Duyuru.objects.values_list('kategori', flat=True).distinct()
        silindi = 0
        for kat in kategoriler:
            sakla = Duyuru.objects.filter(kategori=kat).order_by('-id').values_list('id', flat=True)[:10]
            fazla = Duyuru.objects.filter(kategori=kat).exclude(id__in=list(sakla))
            sayi = fazla.count()
            if sayi:
                fazla.delete()
                silindi += sayi
        if silindi:
            self.stdout.write(f'🗑  {silindi} eski duyuru silindi.')

    # ------------------------------------------------------------------ #
    def _temizle(self):
        """Navigasyon öğesi olarak hatalı eklenen girişleri sil."""
        silindi = 0
        for d in Duyuru.objects.all():
            if _is_nav_item(d.baslik):
                self.stdout.write(f'  - Siliniyor: {d.baslik}')
                d.delete()
                silindi += 1
        self.stdout.write(self.style.SUCCESS(f'✅ {silindi} hatalı giriş silindi.'))

    # ------------------------------------------------------------------ #
    def _rss_isle(self, kaynak):
        self.stdout.write(f"\n▶ {kaynak['kaynak']}")
        eklendi = 0
        try:
            # feedparser URL ile çekince bazen bozo hatası veriyor;
            # önce requests ile alıp içeriği parse et
            resp = requests.get(kaynak['url'], headers=HEADERS, timeout=15)
            resp.raise_for_status()
            feed = feedparser.parse(resp.content)

            if not feed.entries:
                self.stdout.write('  (duyuru bulunamadı)')
                return 0

            for entry in feed.entries[:MAX_HABER]:
                baslik = entry.get('title', '').strip()[:200]
                icerik = (
                    entry.get('summary', '')
                    or entry.get('description', '')
                    or entry.get('content', [{}])[0].get('value', '')
                ).strip()
                link = entry.get('link', '')

                if not baslik or _is_nav_item(baslik):
                    continue
                if not icerik:
                    icerik = baslik

                _, created = Duyuru.objects.get_or_create(
                    baslik=baslik,
                    defaults={
                        'icerik':     icerik[:3000],
                        'kategori':   kaynak['kategori'],
                        'kaynak_url': link,
                        'yayinda':    True,
                    }
                )
                if created:
                    eklendi += 1
                    self.stdout.write(f'  + {baslik[:80]}')

        except requests.RequestException as e:
            self.stderr.write(f'  ✗ Bağlantı hatası: {e}')
        except Exception as e:
            self.stderr.write(f'  ✗ Hata: {e}')

        if eklendi == 0:
            self.stdout.write('  (yeni duyuru yok)')
        return eklendi

    # ------------------------------------------------------------------ #
    def _scrape_isle(self, kaynak):
        self.stdout.write(f"\n▶ {kaynak['kaynak']}")
        eklendi = 0
        try:
            resp = requests.get(kaynak['url'], headers=HEADERS, timeout=15)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, 'html.parser')

            # Belirli link pattern varsa onu kullan (örn. /Mission/ShowAnnouncement/)
            link_match = kaynak.get('link_match', '')
            if link_match:
                candidates = [
                    a for a in soup.find_all('a', href=True)
                    if link_match in a.get('href', '')
                ]
            else:
                candidates = (
                    soup.select('div.haberList li')
                    or soup.select('.news-list li')
                    or soup.select('ul.haberler li')
                    or [
                        a for a in soup.find_all('a', href=True)
                        if any(kw in a.get('href', '')
                               for kw in ['/Announcement', '/Haber', '/Detail'])
                    ]
                )

            sayac = 0
            for item in candidates:
                if sayac >= MAX_HABER:
                    break

                baslik = _temizle_baslik(item.get_text(strip=True))[:200]
                if not baslik or _is_nav_item(baslik):
                    continue

                a_tag = item if item.name == 'a' else item.find('a')
                href = a_tag.get('href', '') if a_tag else ''
                if href and not href.startswith('http'):
                    href = kaynak['link_base'].rstrip('/') + '/' + href.lstrip('/')

                p = item.find('p')
                icerik = p.get_text(strip=True) if p else baslik

                _, created = Duyuru.objects.get_or_create(
                    baslik=baslik,
                    defaults={
                        'icerik':     icerik[:3000],
                        'kategori':   kaynak['kategori'],
                        'kaynak_url': href,
                        'yayinda':    True,
                    }
                )
                if created:
                    eklendi += 1
                    sayac += 1
                    self.stdout.write(f'  + {baslik[:80]}')

        except requests.RequestException as e:
            self.stderr.write(f'  ✗ Bağlantı hatası: {e}')
        except Exception as e:
            self.stderr.write(f'  ✗ Hata: {e}')

        if eklendi == 0:
            self.stdout.write('  (yeni duyuru yok)')
        return eklendi
