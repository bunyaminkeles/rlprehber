"""
Kırık link düzeltmeleri — link checker raporu 2026-03-30
"""
from django.db import migrations

KAYNAK_GUNCELLEMELER = [
    # Stuttgart KdU 404 → yeni resmi PDF
    {
        'eski_baslik': 'Stuttgart KdU — Konut Yardımı Sınır Tablosu',
        'yeni': {
            'url':    'https://www.stuttgart.de/medien/ibs/21-anlage-zur-feststellung-der-angemessenen-kosten-der-unterkunft-und-heizung.pdf',
            'baslik': 'Stuttgart KdU — Angemessene Kosten der Unterkunft (PDF)',
            'ozet':   'Jobcenter Stuttgart tarafından § 22 SGB II kapsamında kabul edilen kira tavan değerleri tablosu.',
        },
    },
    # Köln KdU 404 → jobcenterkoeln.de 2026 PDF
    {
        'eski_baslik': 'Köln KdU — Kosten der Unterkunft Bilgisi',
        'yeni': {
            'url':    'https://www.jobcenterkoeln.de/wp-content/uploads/2026/02/JC_Uebersicht-Mietrichtwert-2026.pdf',
            'baslik': 'Köln KdU — Mietrichtwerte 2026 (PDF)',
            'ozet':   'Jobcenter Köln tarafından yayımlanan 2026 yılı kira üst limitleri ve Bürgergeld konut yardımı tablosu.',
        },
    },
    # Köln Bürgeramt randevu 404 → güncel URL
    {
        'eski_baslik': 'Köln Bürgeramt — Online Randevu',
        'yeni': {
            'url':    'https://www.stadt-koeln.de/artikel/06415/index.html',
            'baslik': 'Köln Kundenzentrum — Online Terminvereinbarung',
            'ozet':   'Stadt Köln Kundenzentrum\'larına online randevu sistemi; pasaport, kimlik, nüfus tescili ve diğer resmi işlemler.',
        },
    },
    # Mannheim Wohngeld 404 → mannheim.de/sosiales yeni URL
    {
        'eski_baslik': 'Mannheim Wohngeld – Konut Yardımı',
        'yeni': {
            'url':    'https://www.mannheim.de/de/service-bieten/soziales/wohngeld',
            'baslik': 'Mannheim Wohngeld — Konut Yardımı',
            'ozet':   'Düşük gelirli haneler için kira yardımı (Wohngeld) başvuru bilgileri ve gerekli belgeler.',
        },
    },
    # Mainz-Bingen Jobcenter SSL hatası → mainz-bingen.de resmi sayfası
    {
        'eski_baslik': 'Jobcenter Mainz-Bingen',
        'yeni': {
            'url':    'https://www.mainz-bingen.de/de/Jobcenter/',
            'ozet':   'Mainz-Bingen Jobcenter; Bürgergeld başvurusu, iş arama desteği ve sosyal yardım hizmetleri.',
        },
    },
    # Wiesbaden Kommunales Jobcenter DNS hatası → wiesbaden.de
    {
        'eski_baslik': 'Kommunales Jobcenter Wiesbaden',
        'yeni': {
            'url':    'https://www.wiesbaden.de/leben-in-wiesbaden/arbeit-beruf/kjc/',
            'ozet':   'Wiesbaden Kommunales Jobcenter; Bürgergeld başvurusu, iş danışmanlığı ve sosyal yardım hizmetleri.',
        },
    },
    # Mannheim Kursnet DNS hatası → arbeitsagentur.de/kursnet yeni URL
    {
        'eski_baslik': 'Kursnet – Bundesagentur für Arbeit',
        'yeni': {
            'url':    'https://www.arbeitsagentur.de/kursnet',
            'baslik': 'KURSNET — Bundesagentur für Arbeit',
            'ozet':   'Bundesagentur\'un ücretsiz eğitim ve dil kursu arama platformu. Mannheim ve çevresi kursları.',
        },
    },
]

BELGE_GUNCELLEMELER = [
    # SEPA-Lastschriftmandat 404 → zoll.de güncel URL
    {
        'eski_baslik': 'SEPA-Lastschriftmandat — Araç Vergisi Otomatik Ödeme',
        'yeni': {
            'harici_link': 'https://www.zoll.de/SharedDocs/Downloads/DE/FormulareMerkblaetter/Verkehrsteuern/merkblatt_sepa_ausfuellhilfe.pdf?__blob=publicationFile&v=3',
            'ozet': 'Kfz-Steuer (araç vergisi) için otomatik ödeme talimatı (SEPA) formu ve doldurma kılavuzu.',
        },
    },
]


def guncelle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Belge  = apps.get_model('rehber', 'Belge')

    for g in KAYNAK_GUNCELLEMELER:
        qs = Kaynak.objects.filter(baslik=g['eski_baslik'])
        if qs.exists():
            qs.update(**g['yeni'])

    for g in BELGE_GUNCELLEMELER:
        qs = Belge.objects.filter(baslik=g['eski_baslik'])
        if qs.exists():
            qs.update(**g['yeni'])


def geri_al(apps, schema_editor):
    pass  # geri alma gerekmiyor — eski URL'ler zaten kırıktı


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0031_kdu_hamburg_worms_trier_mannheim'),
    ]

    operations = [
        migrations.RunPython(guncelle, geri_al),
    ]
