"""
Frankfurt am Main şehri tam kurulum: Stadt oluşturma, URL'ler, aktiv=True, Kaynaklar.
Eyalet: Hessen (HE)
"""
from django.db import migrations

FRANKFURT_KAYNAKLAR = [
    {
        'kategori': 'resmi',
        'baslik': 'Ausländerbehörde Frankfurt am Main',
        'url': 'https://frankfurt.de/auslaenderangelegenheiten',
        'ozet': 'Frankfurt Yabancılar Dairesi; oturma izni, çalışma izni ve yabancı uyruklu diğer işlemler için resmi başvuru portalı.',
        'icon': 'bi-file-earmark-person-fill',
        'sira': 1,
    },
    {
        'kategori': 'resmi',
        'baslik': 'Online Termin — Frankfurt Belediyesi',
        'url': 'https://frankfurt.de/service-und-rathaus/service/online-terminvereinbarungen',
        'ozet': 'Bürgeramt, Ausländerbehörde ve diğer belediye birimlerine online randevu alma portalı.',
        'icon': 'bi-calendar-check-fill',
        'sira': 2,
    },
    {
        'kategori': 'is',
        'baslik': 'Jobcenter Frankfurt am Main',
        'url': 'https://www.jobcenter-frankfurt.de',
        'ozet': 'Bürgergeld başvurusu, iş arama desteği ve sosyal yardım hizmetleri.',
        'icon': 'bi-briefcase-fill',
        'sira': 3,
    },
    {
        'kategori': 'is',
        'baslik': 'Agentur für Arbeit Frankfurt am Main',
        'url': 'https://www.arbeitsagentur.de/vor-ort/frankfurt-main',
        'ozet': 'İşsizlik sigortası (ALG I), mesleki rehberlik ve iş ilanları.',
        'icon': 'bi-person-workspace',
        'sira': 4,
    },
    {
        'kategori': 'konut',
        'baslik': 'Frankfurt KdU — Kosten der Unterkunft',
        'url': 'https://frankfurt.de/service-und-rathaus/verwaltung/aemter-und-institutionen/stadtschulamt/bildung-und-betreuung/finanzielle-unterstuetzung/kosten-der-unterkunft',
        'ozet': '§ 22 SGB II kapsamında Frankfurt\'ta Jobcenter tarafından karşılanan kira tavan değerleri.',
        'icon': 'bi-house-fill',
        'sira': 5,
    },
    {
        'kategori': 'egitim',
        'baslik': 'VHS Frankfurt — Volkshochschule',
        'url': 'https://www.vhs-frankfurt.de',
        'ozet': 'Almanca entegrasyon kursları, mesleki eğitim ve kültürel etkinlikler.',
        'icon': 'bi-translate',
        'sira': 6,
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Kaynak = apps.get_model('rehber', 'Kaynak')

    try:
        he = Eyalet.objects.get(kod='HE')
    except Eyalet.DoesNotExist:
        return

    frankfurt, _ = Stadt.objects.get_or_create(
        slug='frankfurt',
        defaults={
            'eyalet': he,
            'name': 'Frankfurt am Main',
            'typ': 'kreisfrei',
            'lat': 50.1109,
            'lng': 8.6821,
            'population': 775000,
            'beschreibung': (
                'Frankfurt am Main, Hessen eyaletinin en büyük şehri ve '
                'Almanya\'nın finans merkezi. Avrupa Merkez Bankası ve Frankfurt '
                'Borsası\'na ev sahipliği yapar.'
            ),
            'termin_url':            'https://frankfurt.de/service-und-rathaus/service/online-terminvereinbarungen',
            'auslaenderbehorde_url': 'https://frankfurt.de/auslaenderangelegenheiten',
            'rss_duyuru_url':        'https://frankfurt.de/aktuelle-meldung',
            'aktiv': True,
        }
    )

    # Mevcut kayıt varsa URL'leri ve aktiv'i güncelle
    Stadt.objects.filter(slug='frankfurt').update(
        termin_url='https://frankfurt.de/service-und-rathaus/service/online-terminvereinbarungen',
        auslaenderbehorde_url='https://frankfurt.de/auslaenderangelegenheiten',
        rss_duyuru_url='https://frankfurt.de/aktuelle-meldung',
        aktiv=True,
    )

    for d in FRANKFURT_KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=frankfurt,
            defaults={**d, 'eyalet': he, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Stadt.objects.filter(slug='frankfurt').update(
        termin_url='',
        auslaenderbehorde_url='',
        rss_duyuru_url='',
        aktiv=False,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0037_eyalet_arma_url'),
        ('rehber', '0035_merge_20260402_0116'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
