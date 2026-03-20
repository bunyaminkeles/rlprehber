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
    # ── Ulaşım
    dict(ad='DB — Deutsche Bahn', url='https://www.bahn.de',
         kategori='ulasim', sira=1,
         aciklama='Almanya tren biletleri ve güzergahları.'),
    dict(ad='FlixBus — Şehirlerarası Otobüs', url='https://www.flixbus.com/',
         kategori='ulasim', sira=2,
         aciklama='Avrupa genelinde uygun fiyatlı şehirlerarası otobüs seferleri.'),
    dict(ad='AJet — Uçuş Arama', url='https://ajet.com/tr',
         kategori='ulasim', sira=3,
         aciklama='Türkiye merkezli havayolu — İstanbul ve diğer şehirlere uçuş arama.'),
    # ── İlan Platformları
    dict(ad='Kleinanzeigen (eski eBay Kleinanzeigen)', url='https://www.kleinanzeigen.de/s-mainz/c0',
         kategori='ilan', sira=1,
         aciklama="Almanya'nın en büyük ücretsiz ilan platformu. Araç, ev, eşya alım-satım."),
    dict(ad='ImmobilienScout24', url='https://www.immobilienscout24.de/Suche/de/rheinland-pfalz/mainz/wohnung-mieten',
         kategori='ilan', sira=2,
         aciklama="Almanya'nın en büyük kiralık ev platformu. Mainz ve Mainz-Bingen ilanları."),
    dict(ad='Immonet — Mainz', url='https://www.immonet.de/immobiliensuche/mainz.html',
         kategori='ilan', sira=3,
         aciklama='Kiralık ve satılık ev ilanları.'),
    dict(ad='WG-Gesucht (Paylaşımlı Ev)', url='https://www.wg-gesucht.de/',
         kategori='ilan', sira=4,
         aciklama="WG (paylaşımlı daire) arama platformu. Mainz'da oda aramak için ideal."),
    dict(ad='Mobile.de — Araç İlanları', url='https://www.mobile.de',
         kategori='ilan', sira=5,
         aciklama="Almanya'nın en büyük araç alım-satım platformu."),
    dict(ad='AutoScout24', url='https://www.autoscout24.de',
         kategori='ilan', sira=6,
         aciklama='Avrupa genelinde araç alım-satım platformu.'),
    dict(ad='Doctolib — Online Doktor Randevusu', url='https://www.doctolib.de/',
         kategori='saglik', sira=1,
         aciklama='Almanya genelinde doktor, uzman ve klinik randevuları için online platform.'),
    dict(ad='IKK Südwest — Sağlık Sigortası', url='https://www.ikk-suedwest.de/',
         kategori='saglik', sira=2,
         aciklama='Mainz bölgesinde yaygın sağlık sigortası — üyelik ve hizmetler.'),
    dict(ad='AOK — Sağlık Sigortası', url='https://www.aok.de/pk/',
         kategori='saglik', sira=3,
         aciklama="Almanya'nın en büyük kamu sağlık sigortası — bilgi ve üyelik başvurusu."),
    dict(ad='KV RLP — Doktor Arama (Rheinland-Pfalz)', url='https://www.kv-rlp.de/',
         kategori='saglik', sira=4,
         aciklama='Rheinland-Pfalz Kassenärztliche Vereinigung — bölgedeki aile hekimi ve uzman doktor arama platformu.'),
]

# ── Rehber Kaynakları (sadece PDF ve randevu linkleri) ───────────
REHBER = [
    dict(baslik='Mainz Bürgeramt — Online Randevu', tip='link',
         url='https://termine-reservieren.de/termine/buergeramt.mainz/',
         kategori='resmi', icon='bi-calendar-check', sira=1, yayinda=True,
         ozet='Anmeldung, pasaport ve kimlik işlemleri için online randevu sistemi.'),
    dict(baslik='Mietbescheinigung — Kira Belgesi (PDF)', tip='link',
         url='https://www.jobcenter-mainz.de/wp-content/uploads/2021/05/Mietbescheinigung.pdf',
         kategori='konut', icon='bi-file-earmark-pdf', sira=1, yayinda=True,
         ozet='Jobcenter Mainz kira belgesi formu — ev sahibine imzalatılır.'),
    dict(baslik='KdU Mainz 2025 — Kira Üst Limitleri (PDF)', tip='link',
         url='https://harald-thome.de/files/pdf/KdU%20New/KdU%20Mainz%20-%2001.01.2025.pdf',
         kategori='konut', icon='bi-file-earmark-text', sira=2, yayinda=True,
         ozet='Mainz Jobcenter tarafından kabul edilen maksimum kira miktarları (01.01.2025).'),
    dict(baslik='KdU Mainz-Bingen 2025 — Uygun Kira Tablosu (PDF)', tip='link',
         url='https://www.mainz-bingen.de/default-wAssets/docs/Familie-Jugend-Asyl-Gesundheit-Soziales/Jobcenter/finanzielle-Leistungen-JobCenter/Sonstiges/Uebersicht-angemessene-KdU-2025.pdf',
         kategori='konut', icon='bi-file-earmark-text', sira=3, yayinda=True,
         ozet='Mainz-Bingen Jobcenter tarafından kabul edilen uygun kira miktarları (2025).'),
    dict(baslik='SCHUFA Datenkopie — Ücretsiz Kredi Raporu', tip='link',
         url='https://www.meineschufa.de/service/datenkopie',
         kategori='resmi', icon='bi-file-person', sira=5, yayinda=True,
         ozet="SCHUFA'dan yılda bir kez ücretsiz alınabilen kişisel kredi ve borç bilgisi raporu."),
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
