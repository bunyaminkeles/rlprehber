from django.db import migrations

# KdU Köln için resmi kaynak: Stadt Köln Sozialamt
# jobcenter-koeln.de SSL sorunu nedeniyle stadt-koeln.de kullanıldı
KAYNAKLAR = [
    dict(kategori='resmi', baslik='Ausländerbehörde Köln',
         url='https://www.stadt-koeln.de/service/alle-adressen/auslaenderamt',
         ozet='Köln Yabancılar Dairesi; oturma izni, çalışma izni ve yabancı uyruklu diğer işlemler için resmi adres ve iletişim bilgileri.',
         icon='bi-file-earmark-person-fill', sira=1),
    dict(kategori='resmi', baslik='Terminvereinbarung — Köln Online Randevu',
         url='https://www.stadt-koeln.de/service/kontakt/terminvereinbarung-online',
         ozet='Stadt Köln belediye birimlerine online randevu sistemi; Bürgerbüro, Ausländerbehörde ve diğer resmi kurumlar için.',
         icon='bi-calendar-check-fill', sira=2),
    dict(kategori='is', baslik='Jobcenter Köln',
         url='https://jobcenter.digital/koeln',
         ozet='Köln Jobcenter; Bürgergeld başvurusu, iş arama desteği ve sosyal yardım hizmetleri.',
         icon='bi-briefcase-fill', sira=3),
    dict(kategori='is', baslik='Agentur für Arbeit Köln',
         url='https://www.arbeitsagentur.de/vor-ort/koeln',
         ozet='Köln İş ve İşçi Bulma Kurumu; işsizlik sigortası, mesleki rehberlik ve iş ilanları.',
         icon='bi-person-workspace', sira=4),
    dict(kategori='konut', baslik='Köln KdU — Kosten der Unterkunft Bilgisi',
         url='https://www.stadt-koeln.de/service/anliegen/sozialleistungen-wohnen',
         ozet='§ 22 SGB II kapsamında Köln\'de Jobcenter tarafından karşılanan kira tavan değerleri ve konut yardımı bilgisi.',
         icon='bi-house-fill', sira=5),
    dict(kategori='egitim', baslik='VHS Köln — Volkshochschule',
         url='https://www.vhs-koeln.de',
         ozet='Köln Halk Eğitim Merkezi; Almanca entegrasyon kursları, mesleki eğitim ve kültürel etkinlikler.',
         icon='bi-translate', sira=6),
]

URL_DUZELTMELER = {
    'koeln': {
        'auslaenderbehorde_url': 'https://www.stadt-koeln.de/service/alle-adressen/auslaenderamt',
        'termin_url':            'https://www.stadt-koeln.de/service/kontakt/terminvereinbarung-online',
    }
}

YER_URL_DUZELTMELER = [
    # (ad, yeni_website, yeni_maps_url)
    ('Jobcenter Köln',              'https://jobcenter.digital/koeln',                   None),
    ('VHS Köln — Volkshochschule',  'https://www.vhs-koeln.de',                          None),
    ('Ausländerbehörde Köln',       'https://www.stadt-koeln.de/service/alle-adressen/auslaenderamt', None),
]


def seed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')

    try:
        koeln = Stadt.objects.get(slug='koeln')
    except Stadt.DoesNotExist:
        return

    # Kaynaklar ekle
    for d in KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=koeln,
            defaults={**d, 'eyalet': koeln.eyalet, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )

    # Stadt URL düzeltmeleri
    for slug, urls in URL_DUZELTMELER.items():
        Stadt.objects.filter(slug=slug).update(**urls)

    # Yer website URL düzeltmeleri
    for yer_ad, yeni_website, yeni_maps in YER_URL_DUZELTMELER:
        yer_qs = Yer.objects.filter(stadt=koeln, ad=yer_ad)
        update = {}
        if yeni_website is not None:
            update['website'] = yeni_website
        if yeni_maps is not None:
            update['maps_url'] = yeni_maps
        if update:
            yer_qs.update(**update)


def unseed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    basliklar = [d['baslik'] for d in KAYNAKLAR]
    Kaynak.objects.filter(baslik__in=basliklar, stadt__slug='koeln').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0026_seed_hamburg_kaynaklar'),
        ('stadt', '0017_fix_rss_urls'),
        ('yerler', '0001_initial'),
    ]

    operations = [migrations.RunPython(seed, unseed)]
