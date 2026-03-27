"""
Almanya resmi tatillerini eyalet bazında ücretsiz API'den çeker.
API: https://feiertage-api.de
Kullanım: python manage.py tatilleri_cek --yil 2026
"""
import requests
from datetime import date
from django.core.management.base import BaseCommand
from takvim.models import Etkinlik

# Eyalet slug → API kodu
EYALET_API_KODLARI = {
    'rlp': 'RP',
    'be':  'BE',
    'by':  'BY',
    'hh':  'HH',
    'he':  'HE',
    'nw':  'NW',
    'bw':  'BW',
    'ni':  'NI',
    'hb':  'HB',
    'sn':  'SN',
    'sl':  'SL',
    'sh':  'SH',
    'st':  'ST',
    'th':  'TH',
    'bb':  'BB',
    'mv':  'MV',
}

TATIL_CEVIRILERI = {
    'Neujahrstag':               'Yılbaşı',
    'Karfreitag':                'İyi Cuma (Paskalya)',
    'Ostersonntag':              'Paskalya Pazar',
    'Ostermontag':               'Paskalya Pazartesi',
    'Tag der Arbeit':            'İşçi Bayramı',
    'Christi Himmelfahrt':       "İsa'nın Göğe Yükselişi",
    'Pfingstsonntag':            'Pentikost Pazar',
    'Pfingstmontag':             'Pentikost Pazartesi',
    'Fronleichnam':              'Corpus Christi',
    'Tag der Deutschen Einheit': 'Alman Birliği Günü',
    'Allerheiligen':             'Azizler Günü',
    'Erster Weihnachtstag':      '1. Noel Günü',
    'Zweiter Weihnachtstag':     '2. Noel Günü',
    'Reformationstag':           'Reformasyon Günü',
    'Buß- und Bettag':           'Tövbe ve Dua Günü',
    'Mariä Himmelfahrt':         'Meryem Ana Göğe Yükseliş',
    'Heilige Drei Könige':       'Üç Bilge Adam Günü',
    'Internationaler Frauentag': 'Dünya Kadınlar Günü',
    'Weltkindertag':             'Dünya Çocuklar Günü',
}

TUR_MAP = {
    'Karfreitag':   'paskalya',
    'Ostersonntag': 'paskalya',
    'Ostermontag':  'paskalya',
}


class Command(BaseCommand):
    help = 'Tüm eyaletler için resmi tatilleri feiertage-api.de üzerinden çeker.'

    def add_arguments(self, parser):
        parser.add_argument('--yil', type=int, default=date.today().year)
        parser.add_argument('--eyalet', type=str, default=None,
                            help='Sadece belirli eyalet (rlp, be, by ...)')

    def handle(self, *args, **options):
        from stadt.models import Eyalet
        yil = options['yil']
        sadece = options.get('eyalet')

        eyaletler = Eyalet.objects.all()
        if sadece:
            eyaletler = eyaletler.filter(slug=sadece)

        toplam = 0
        for eyalet in eyaletler:
            api_kodu = EYALET_API_KODLARI.get(eyalet.slug)
            if not api_kodu:
                self.stdout.write(f'  ⚠ {eyalet.slug} için API kodu yok, atlanıyor.')
                continue

            url = f'https://feiertage-api.de/api/?jahr={yil}&nur_land={api_kodu}'
            self.stdout.write(f'\n{eyalet.ad} ({api_kodu}) — {yil} yılı çekiliyor...')

            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                veri = resp.json()
            except Exception as e:
                self.stderr.write(f'  API hatası ({eyalet.slug}): {e}')
                continue

            eklendi = 0
            for almanca_ad, bilgi in veri.items():
                tarih_str = bilgi.get('datum')
                if not tarih_str:
                    continue
                tarih  = date.fromisoformat(tarih_str)
                baslik = TATIL_CEVIRILERI.get(almanca_ad, almanca_ad)
                tur    = TUR_MAP.get(almanca_ad, 'resmi_tatil')

                obj, created = Etkinlik.objects.get_or_create(
                    baslik=baslik,
                    tarih=tarih,
                    eyalet=eyalet,
                    defaults={
                        'tur':      tur,
                        'scope':    'eyalet',
                        'aciklama': f'Resmi tatil — {almanca_ad}',
                    }
                )
                if created:
                    eklendi += 1
                    self.stdout.write(f'  + {tarih} | {baslik}')

            toplam += eklendi
            self.stdout.write(f'  → {eklendi} yeni tatil eklendi.')

        self.stdout.write(self.style.SUCCESS(f'\nToplam {toplam} tatil eklendi ({yil}).'))
