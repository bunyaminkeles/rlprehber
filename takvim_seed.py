"""
Almanya / Rheinland-Pfalz resmi tatilleri ve önemli günleri ekler.
Kullanım: python takvim_seed.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from datetime import date
from takvim.models import Etkinlik

ETKINLIKLER = [
    # 2025
    dict(baslik='Yılbaşı',                    tarih=date(2025, 1,  1),  tur='resmi_tatil', aciklama='Neujahr — Almanya genelinde resmi tatil.'),
    dict(baslik='İyi Cuma (Paskalya)',         tarih=date(2025, 4, 18),  tur='paskalya',    aciklama='Karfreitag — Rheinland-Pfalz resmi tatili.'),
    dict(baslik='Paskalya Pazartesi',          tarih=date(2025, 4, 21),  tur='paskalya',    aciklama='Ostermontag — Almanya genelinde resmi tatil.'),
    dict(baslik='İşçi Bayramı',               tarih=date(2025, 5,  1),  tur='resmi_tatil', aciklama='Tag der Arbeit — Almanya genelinde resmi tatil.'),
    dict(baslik="İsa'nın Göğe Yükselişi",     tarih=date(2025, 5, 29),  tur='resmi_tatil', aciklama='Christi Himmelfahrt — Almanya genelinde resmi tatil.'),
    dict(baslik='Pentikost Pazartesi',         tarih=date(2025, 6,  9),  tur='resmi_tatil', aciklama='Pfingstmontag — Almanya genelinde resmi tatil.'),
    dict(baslik='Corpus Christi',              tarih=date(2025, 6, 19),  tur='resmi_tatil', aciklama='Fronleichnam — Rheinland-Pfalz resmi tatili.'),
    dict(baslik='Alman Birliği Günü',          tarih=date(2025, 10, 3),  tur='resmi_tatil', aciklama='Tag der Deutschen Einheit — Almanya genelinde resmi tatil.'),
    dict(baslik='Azizler Günü',                tarih=date(2025, 11, 1),  tur='resmi_tatil', aciklama='Allerheiligen — Rheinland-Pfalz resmi tatili.'),
    dict(baslik='1. Noel Günü',                tarih=date(2025, 12, 25), tur='resmi_tatil', aciklama='1. Weihnachtstag — Almanya genelinde resmi tatil.'),
    dict(baslik='2. Noel Günü',                tarih=date(2025, 12, 26), tur='resmi_tatil', aciklama='2. Weihnachtstag — Almanya genelinde resmi tatil.'),
    # 2026
    dict(baslik='Yılbaşı',                    tarih=date(2026, 1,  1),  tur='resmi_tatil', aciklama='Neujahr — Almanya genelinde resmi tatil.'),
    dict(baslik='İyi Cuma (Paskalya)',         tarih=date(2026, 4,  3),  tur='paskalya',    aciklama='Karfreitag — Rheinland-Pfalz resmi tatili.'),
    dict(baslik='Paskalya Pazartesi',          tarih=date(2026, 4,  6),  tur='paskalya',    aciklama='Ostermontag — Almanya genelinde resmi tatil.'),
    dict(baslik='İşçi Bayramı',               tarih=date(2026, 5,  1),  tur='resmi_tatil', aciklama='Tag der Arbeit — Almanya genelinde resmi tatil.'),
    dict(baslik="İsa'nın Göğe Yükselişi",     tarih=date(2026, 5, 14),  tur='resmi_tatil', aciklama='Christi Himmelfahrt — Almanya genelinde resmi tatil.'),
    dict(baslik='Pentikost Pazartesi',         tarih=date(2026, 5, 25),  tur='resmi_tatil', aciklama='Pfingstmontag — Almanya genelinde resmi tatil.'),
    dict(baslik='Corpus Christi',              tarih=date(2026, 6,  4),  tur='resmi_tatil', aciklama='Fronleichnam — Rheinland-Pfalz resmi tatili.'),
    dict(baslik='Alman Birliği Günü',          tarih=date(2026, 10, 3),  tur='resmi_tatil', aciklama='Tag der Deutschen Einheit — Almanya genelinde resmi tatil.'),
    dict(baslik='Azizler Günü',                tarih=date(2026, 11, 1),  tur='resmi_tatil', aciklama='Allerheiligen — Rheinland-Pfalz resmi tatili.'),
    dict(baslik='1. Noel Günü',                tarih=date(2026, 12, 25), tur='resmi_tatil', aciklama='1. Weihnachtstag — Almanya genelinde resmi tatil.'),
    dict(baslik='2. Noel Günü',                tarih=date(2026, 12, 26), tur='resmi_tatil', aciklama='2. Weihnachtstag — Almanya genelinde resmi tatil.'),
]

eklendi = 0
for d in ETKINLIKLER:
    _, created = Etkinlik.objects.get_or_create(
        baslik=d['baslik'], tarih=d['tarih'],
        defaults=d,
    )
    if created:
        eklendi += 1
        print(f'  ✓ {d["tarih"]} {d["baslik"]}')

print(f'✅ {eklendi} yeni etkinlik eklendi.')
