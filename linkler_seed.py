"""
Temel linkleri ve rehber kaynaklarını yükler.
Kullanım: python linkler_seed.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from linkler.models import OnemliLink
from rehber.models import Kaynak

# ── Önemli Linkler ───────────────────────────────────────────────
LINKLER = [
    dict(ad='Mainz Jobcenter', url='https://www.jobcenter-mainz.de/',
         kategori='is', sira=1,
         aciklama='İşsizlik yardımı, iş arama desteği ve sosyal yardım başvuruları.'),
    dict(ad='Bundesagentur für Arbeit', url='https://web.arbeitsagentur.de/',
         kategori='is', sira=2,
         aciklama='Federal İş Kurumu — ALG I, iş ilanları ve kariyer danışmanlığı.'),
    dict(ad='T.C. Mainz Başkonsolosluğu', url='https://mainz-bk.mfa.gov.tr/Mission',
         kategori='resmi', sira=1,
         aciklama='Pasaport, vize, nüfus işlemleri ve konsolosluk hizmetleri.'),
    dict(ad='Mainz Şehir Portalı', url='https://www.mainz.de/',
         kategori='resmi', sira=2,
         aciklama='Mainz Belediyesi resmi sitesi — haberler, hizmetler, vatandaş işlemleri.'),
    dict(ad='BAMF — Göç ve Mülteci Dairesi', url='https://www.bamf.de/EN/Startseite/startseite_node.html',
         kategori='resmi', sira=3,
         aciklama='Federal Göç ve Mülteciler Dairesi — oturma izni, entegrasyon kursları ve sığınma başvuruları.'),
    dict(ad='Mainz Bürgeramt — Randevu', url='https://termine-reservieren.de/termine/buergeramt.mainz/',
         kategori='resmi', sira=4,
         aciklama='Mainz Vatandaşlık Dairesi online randevu — Anmeldung, pasaport, kimlik işlemleri.'),
    dict(ad='Mietbescheinigung — Kira Belgesi (PDF)', url='https://www.jobcenter-mainz.de/wp-content/uploads/2021/05/Mietbescheinigung.pdf',
         kategori='is', sira=3,
         aciklama='Jobcenter Mainz için kira belgesi formu — ev sahibine imzalatılır.'),
    dict(ad='KdU Mainz 2025 — Kira Üst Limitleri (PDF)', url='https://harald-thome.de/files/pdf/KdU%20New/KdU%20Mainz%20-%2001.01.2025.pdf',
         kategori='is', sira=4,
         aciklama='Mainz Jobcenter tarafından kabul edilen maksimum kira miktarları (01.01.2025).'),
]

# ── Rehber Kaynakları ────────────────────────────────────────────
REHBER = [
    dict(baslik='Mainz Jobcenter', tip='link', url='https://www.jobcenter-mainz.de/',
         kategori='is', icon='bi-briefcase', sira=1, yayinda=True,
         ozet='İşsizlik yardımı ve iş arama desteği için başvuru noktası.'),
    dict(baslik='Bundesagentur für Arbeit (İş Kurumu)', tip='link',
         url='https://web.arbeitsagentur.de/',
         kategori='is', icon='bi-building', sira=2, yayinda=True,
         ozet='ALG I, iş ilanları ve kariyer danışmanlığı için Federal İş Kurumu.'),
    dict(baslik='T.C. Mainz Başkonsolosluğu', tip='link',
         url='https://mainz-bk.mfa.gov.tr/Mission',
         kategori='resmi', icon='bi-flag', sira=1, yayinda=True,
         ozet='Pasaport, vize, nüfus işlemleri ve tüm konsolosluk hizmetleri.'),
    dict(baslik='Mainz Belediyesi (mainz.de)', tip='link', url='https://www.mainz.de/',
         kategori='resmi', icon='bi-building-fill', sira=2, yayinda=True,
         ozet='Mainz şehir portalı — belediye hizmetleri, haberler ve duyurular.'),
    dict(baslik='BAMF — Göç ve Mülteci Dairesi', tip='link',
         url='https://www.bamf.de/EN/Startseite/startseite_node.html',
         kategori='resmi', icon='bi-shield-check', sira=3, yayinda=True,
         ozet='Oturma izni, entegrasyon kursları ve sığınma başvuruları için resmi daire.'),
    dict(baslik='Mainz Bürgeramt — Online Randevu', tip='link',
         url='https://termine-reservieren.de/termine/buergeramt.mainz/',
         kategori='resmi', icon='bi-calendar-check', sira=4, yayinda=True,
         ozet='Anmeldung, pasaport ve kimlik işlemleri için online randevu sistemi.'),
    dict(baslik='Mietbescheinigung — Kira Belgesi (PDF)', tip='link',
         url='https://www.jobcenter-mainz.de/wp-content/uploads/2021/05/Mietbescheinigung.pdf',
         kategori='konut', icon='bi-file-earmark-pdf', sira=1, yayinda=True,
         ozet='Jobcenter Mainz kira belgesi formu — ev sahibine imzalatılır.'),
    dict(baslik='KdU Mainz 2025 — Kira Üst Limitleri (PDF)', tip='link',
         url='https://harald-thome.de/files/pdf/KdU%20New/KdU%20Mainz%20-%2001.01.2025.pdf',
         kategori='konut', icon='bi-file-earmark-text', sira=2, yayinda=True,
         ozet='Mainz Jobcenter tarafından kabul edilen maksimum kira miktarları (01.01.2025).'),
]

eklendi = 0
for d in LINKLER:
    _, created = OnemliLink.objects.get_or_create(url=d['url'], defaults=d)
    if created:
        eklendi += 1
        print(f'  ✓ Link: {d["ad"]}')

for d in REHBER:
    _, created = Kaynak.objects.get_or_create(url=d['url'], defaults=d)
    if created:
        eklendi += 1
        print(f'  ✓ Rehber: {d["baslik"]}')

print(f'✅ {eklendi} yeni kayıt eklendi.')
