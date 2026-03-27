from django.db import migrations


def seed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    # Almanya scope kaynakları yayına al
    Kaynak.objects.filter(scope='almanya', yayinda=False).update(yayinda=True)

    # Wiesbaden kaynakları
    try:
        w = Stadt.objects.get(slug='wiesbaden')
    except Stadt.DoesNotExist:
        return

    he = w.eyalet

    kaynaklar = [
        dict(scope='stadt', kategori='resmi', baslik='Wiesbaden Bürgerbüro — Randevu',
             url='https://dtms.wiesbaden.de/',
             ozet='Wiesbaden Vatandaşlık Dairesi online randevu — Anmeldung, pasaport, kimlik işlemleri.',
             icon='bi-calendar-check', sira=1),
        dict(scope='stadt', kategori='resmi', baslik='Wiesbaden Ausländerbehörde',
             url='https://www.wiesbaden.de/vv/oe/04/33/Auslaenderbehoerde',
             ozet='Wiesbaden Yabancılar Dairesi — oturma izni, vize uzatma ve göç işlemleri.',
             icon='bi-building-fill', sira=2),
        dict(scope='stadt', kategori='resmi', baslik='Caritas Wiesbaden — Göçmen Danışmanlığı',
             url='https://www.caritas-wiesbaden-rheingau-taunus.de/beratung-und-hilfe/migration-und-flucht/migrationsdienst/migrationsdienst',
             ozet='Ücretsiz göçmen danışmanlığı — hukuki, sosyal ve entegrasyon desteği.',
             icon='bi-people-fill', sira=3),
        dict(scope='stadt', kategori='is', baslik='Kommunales Jobcenter Wiesbaden',
             url='https://www1.wiesbaden.de/microsites/kjc/',
             ozet='Wiesbaden Jobcenter — işsizlik yardımı, iş arama ve SGB II desteği.',
             icon='bi-building', sira=1),
        dict(scope='stadt', kategori='is', baslik='Agentur für Arbeit Wiesbaden',
             url='https://www.arbeitsagentur.de/vor-ort/wiesbaden',
             ozet='Wiesbaden İş Bulma Kurumu — iş ilanları, işsizlik parası ve kariyer danışmanlığı.',
             icon='bi-briefcase', sira=2),
        dict(scope='stadt', kategori='is', baslik='HWK Wiesbaden — Göçmenler İçin',
             url='https://www.hwk-wiesbaden.de/',
             ozet='Handwerkskammer Wiesbaden — göçmenler için Ausbildung, mesleki tanıma ve danışmanlık.',
             icon='bi-hammer', sira=3),
        dict(scope='stadt', kategori='egitim', baslik='VHS Wiesbaden — Kurs Kayıt',
             url='https://www.vhs-wiesbaden.de/',
             ozet='Wiesbaden Volkshochschule — Almanca, entegrasyon kursu ve yetişkin eğitimi.',
             icon='bi-mortarboard', sira=1),
        dict(scope='stadt', kategori='konut', baslik='KdU Wiesbaden 2023 — Kira Üst Limitleri (PDF)',
             url='https://harald-thome.de/files/pdf/KdU%20New/KdU%20Wiesbaden%20-%2001.01.2023.pdf',
             ozet='Wiesbaden Jobcenter tarafından kabul edilen maksimum kira miktarları.',
             icon='bi-file-earmark-text', sira=1),
        dict(scope='stadt', kategori='konut', baslik='Wiesbaden — Kira & Isıtma Masrafları Bilgisi',
             url='https://www.wiesbaden.de/leben-in-wiesbaden/arbeit-beruf/kjc/leistungen-lebensunterhalt/miete_und_heizung',
             ozet='Jobcenter Wiesbaden — kabul edilen kira ve ısıtma masraflarına dair resmi bilgi.',
             icon='bi-house-fill', sira=2),
    ]

    for d in kaynaklar:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'],
            defaults=dict(**d, stadt=w, eyalet=he, tip='link', yayinda=True),
        )


class Migration(migrations.Migration):
    dependencies = [
        ('rehber', '0019_scope_almanya'),
        ('stadt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
