from django.db import migrations

KAYNAKLAR = [
    dict(kategori='resmi', baslik='Hamburg Service vor Ort (Bürgerbüro)', url='https://www.hamburg.de/service', ozet='Hamburg\'da nüfus tescili, pasaport, kimlik ve diğer resmi işlemler için Bürgerbüro randevu ve bilgi sayfası.', icon='bi-building-fill', sira=1),
    dict(kategori='resmi', baslik='Ausländerbehörde Hamburg', url='https://www.hamburg.de/auslaenderbehoerde/', ozet='Hamburg Yabancılar Dairesi; oturma izni, çalışma izni ve diğer yabancı uyruklu işlemleri için resmi başvuru sayfası.', icon='bi-file-earmark-person-fill', sira=2),
    dict(kategori='is', baslik='Jobcenter Hamburg', url='https://team-arbeit-hamburg.de/', ozet='Hamburg\'da işsizlik yardımı (Bürgergeld), iş arama desteği ve sosyal hizmetler için Jobcenter.', icon='bi-briefcase-fill', sira=3),
    dict(kategori='is', baslik='Agentur für Arbeit Hamburg', url='https://www.arbeitsagentur.de/vor-ort/hamburg', ozet='Hamburg İş ve İşçi Bulma Kurumu; işsizlik sigortası, mesleki rehberlik ve iş ilanları.', icon='bi-person-workspace', sira=4),
    dict(kategori='konut', baslik='Hamburg KdU Tablosu (PDF)', url='https://www.hamburg.de/resource/blob/46622/65d07f3444e21ac56fdac0c3155897d4/fa-sgbii-22-kdu-00-pdf-data.pdf', ozet='Hamburg Sosyal Yardım Dairesi\'nin § 22 SGB II kapsamındaki güncel kira tavan değerleri (Kosten der Unterkunft) tablosu.', icon='bi-house-fill', sira=5),
    dict(kategori='egitim', baslik='VHS Hamburg – Integrationskurse', url='https://www.vhs-hamburg.de/deutsch/deutsch-lernen-integrationskurse-450', ozet='Hamburg Halk Eğitim Merkezi\'nin devlet onaylı entegrasyon kursları; Almanca dil eğitimi ve oryantasyon modülü.', icon='bi-translate', sira=6),
]


def seed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        sehir = Stadt.objects.get(slug='hamburg')
    except Stadt.DoesNotExist:
        return

    for d in KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'], stadt=sehir,
            defaults={**d, 'eyalet': sehir.eyalet, 'scope': 'stadt', 'tip': 'link', 'yayinda': True}
        )


def unseed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    basliklar = [d['baslik'] for d in KAYNAKLAR]
    Kaynak.objects.filter(baslik__in=basliklar, stadt__slug='hamburg').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('rehber', '0025_seed_berlin_kaynaklar'),
        ('stadt', '0010_seed_baskentler'),
    ]
    operations = [migrations.RunPython(seed, unseed)]
