"""
Almanya resmi tatillerini ücretsiz API'den çeker.
API: https://feiertage-api.de — Rheinland-Pfalz (RP) için
Kullanım: python manage.py tatilleri_cek --yil 2026
"""
import requests
from datetime import date
from django.core.management.base import BaseCommand
from takvim.models import Etkinlik

PASKALYA_GUNLERI = {
    'Karfreitag':       'Paskalya Öncesi Cuma',
    'Ostersonntag':     'Paskalya Pazar',
    'Ostermontag':      'Paskalya Pazartesi',
}

TATIL_CEVIRILERI = {
    'Neujahrstag':                  'Yılbaşı',
    'Karfreitag':                   'İyi Cuma (Paskalya)',
    'Ostersonntag':                 'Paskalya Pazar',
    'Ostermontag':                  'Paskalya Pazartesi',
    'Tag der Arbeit':               'İşçi Bayramı',
    'Christi Himmelfahrt':          "İsa'nın Göğe Yükselişi",
    'Pfingstsonntag':               'Pentikost Pazar',
    'Pfingstmontag':                'Pentikost Pazartesi',
    'Fronleichnam':                 'Corpus Christi',
    'Tag der Deutschen Einheit':    'Alman Birliği Günü',
    'Allerheiligen':                'Azizler Günü',
    'Erster Weihnachtstag':         '1. Noel Günü',
    'Zweiter Weihnachtstag':        '2. Noel Günü',
}

TUR_MAP = {
    'Karfreitag':    'paskalya',
    'Ostersonntag':  'paskalya',
    'Ostermontag':   'paskalya',
}


class Command(BaseCommand):
    help = 'Rheinland-Pfalz resmi tatillerini feiertage-api.de üzerinden çeker.'

    def add_arguments(self, parser):
        parser.add_argument('--yil', type=int, default=date.today().year)

    def handle(self, *args, **options):
        yil = options['yil']
        url = f'https://feiertage-api.de/api/?jahr={yil}&nur_land=RP'
        self.stdout.write(f'{yil} yılı tatilleri çekiliyor...')

        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            veri = resp.json()
        except Exception as e:
            self.stderr.write(f'API hatası: {e}')
            return

        eklendi = 0
        for almanca_ad, bilgi in veri.items():
            tarih_str = bilgi.get('datum')
            if not tarih_str:
                continue
            tarih = date.fromisoformat(tarih_str)
            baslik = TATIL_CEVIRILERI.get(almanca_ad, almanca_ad)
            tur    = TUR_MAP.get(almanca_ad, 'resmi_tatil')

            obj, created = Etkinlik.objects.get_or_create(
                baslik=baslik,
                tarih=tarih,
                defaults={'tur': tur, 'aciklama': f'Resmi Almanya tatili — {almanca_ad}'}
            )
            if created:
                eklendi += 1
                self.stdout.write(f'  + {tarih} | {baslik}')

        self.stdout.write(self.style.SUCCESS(f'{eklendi} yeni tatil eklendi ({yil}).'))
