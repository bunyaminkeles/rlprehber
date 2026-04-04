"""
Veritabanındaki tüm dış linkleri test eder, kırık olanları raporlar.

Kullanım:
  python manage.py kirik_link_bul
  python manage.py kirik_link_bul --timeout 8
  python manage.py kirik_link_bul --sadece-kirik      # sadece kırıkları yaz
"""
import requests
from django.core.management.base import BaseCommand
from concurrent.futures import ThreadPoolExecutor, as_completed

HEADERS = {'User-Agent': 'Mozilla/5.0 (AlmanyaliRehber LinkChecker/1.0)'}


def _test(url, timeout):
    try:
        r = requests.head(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        if r.status_code == 405:          # HEAD izin vermiyorsa GET dene
            r = requests.get(url, headers=HEADERS, timeout=timeout, stream=True)
        return r.status_code
    except requests.exceptions.SSLError:
        return 'SSL_HATA'
    except requests.exceptions.ConnectionError:
        return 'BAĞLANTI_HATA'
    except requests.exceptions.Timeout:
        return 'ZAMAN_ASIMI'
    except Exception as e:
        return f'HATA:{e}'


def _topla_linkler():
    """Veritabanındaki tüm dış URL'leri kaynak bilgisiyle toplar."""
    linkler = []  # [(url, kaynak_aciklama), ...]

    from rehber.models import Kaynak, Belge
    from yerler.models import Yer
    from stadt.models import Stadt

    for k in Kaynak.objects.filter(yayinda=True, tip='link').exclude(url=''):
        linkler.append((k.url, f'Kaynak #{k.pk}: {k.baslik}'))

    for b in Belge.objects.filter(yayinda=True).exclude(harici_link=''):
        linkler.append((b.harici_link, f'Belge #{b.pk}: {b.baslik}'))

    for y in Yer.objects.filter(aktif=True).exclude(website=''):
        linkler.append((y.website, f'Yer #{y.pk}: {y.ad}'))

    for s in Stadt.objects.filter(aktiv=True):
        if s.termin_url:
            linkler.append((s.termin_url, f'Stadt {s.name}: termin_url'))
        if s.auslaenderbehorde_url:
            linkler.append((s.auslaenderbehorde_url, f'Stadt {s.name}: auslaenderbehorde_url'))
        if s.rss_duyuru_url:
            linkler.append((s.rss_duyuru_url, f'Stadt {s.name}: rss_duyuru_url'))

    # Tekrarlananları kaldır ama kaynağı koru
    seen = {}
    for url, kaynak in linkler:
        if url not in seen:
            seen[url] = kaynak
    return list(seen.items())


class Command(BaseCommand):
    help = 'Veritabanındaki tüm dış linkleri test eder'

    def add_arguments(self, parser):
        parser.add_argument('--timeout',      type=int,  default=10)
        parser.add_argument('--workers',      type=int,  default=10)
        parser.add_argument('--sadece-kirik', action='store_true')

    def handle(self, *args, **options):
        timeout      = options['timeout']
        workers      = options['workers']
        sadece_kirik = options['sadece_kirik']

        linkler = _topla_linkler()
        self.stdout.write(f'\n🔍 {len(linkler)} link test ediliyor (timeout={timeout}s, workers={workers})...\n')

        kirik = []
        tamam = 0

        with ThreadPoolExecutor(max_workers=workers) as ex:
            futures = {ex.submit(_test, url, timeout): (url, kaynak) for url, kaynak in linkler}
            for i, future in enumerate(as_completed(futures), 1):
                url, kaynak = futures[future]
                kod = future.result()
                ok = isinstance(kod, int) and kod < 400

                if ok:
                    tamam += 1
                    if not sadece_kirik:
                        self.stdout.write(self.style.SUCCESS(f'  ✓ {kod}  {url}'))
                else:
                    kirik.append((kod, url, kaynak))
                    self.stdout.write(self.style.ERROR(f'  ✗ {kod}  {url}  [{kaynak}]'))

                if i % 20 == 0:
                    self.stdout.write(f'  ... {i}/{len(linkler)} tamamlandı')

        self.stdout.write('\n' + '─' * 60)
        self.stdout.write(self.style.SUCCESS(f'  ✓ Çalışan : {tamam}'))
        self.stdout.write(self.style.ERROR(  f'  ✗ Kırık   : {len(kirik)}'))

        if kirik:
            self.stdout.write('\n── KIRIK LİNKLER ──────────────────────────────────────')
            for kod, url, kaynak in sorted(kirik, key=lambda x: str(x[0])):
                self.stdout.write(self.style.ERROR(f'  [{kod}] {kaynak}'))
                self.stdout.write(f'         {url}')
