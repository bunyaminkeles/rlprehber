from django.db import migrations

KAYNAKLAR = [
    # Resmi
    dict(
        kategori='resmi',
        baslik='Ausländerbehörde Berlin',
        url='https://www.berlin.de/einwanderung/',
        ozet='Berlin Yabancılar Dairesi (Landesamt für Einwanderung): oturma izni başvuruları ve uzatmaları için resmi portal.',
        icon='bi-building-fill',
        sira=1,
    ),
    dict(
        kategori='resmi',
        baslik='Bürgeramt Berlin – Online Termin',
        url='https://service.berlin.de/terminvereinbarung/',
        ozet='Anmeldung, pasaport, ehliyet ve diğer vatandaşlık hizmetleri için online randevu sistemi.',
        icon='bi-person-vcard-fill',
        sira=2,
    ),
    # İş
    dict(
        kategori='is',
        baslik='Jobcenter Berlin Friedrichshain-Kreuzberg',
        url='https://www.berlin.de/jobcenter-friedrichshain-kreuzberg/',
        ozet='Bürgergeld başvurusu, iş arama desteği ve mesleki entegrasyon hizmetleri.',
        icon='bi-briefcase-fill',
        sira=1,
    ),
    dict(
        kategori='is',
        baslik='Agentur für Arbeit Berlin Mitte',
        url='https://www.arbeitsagentur.de/vor-ort/berlin-mitte',
        ozet='İşsizlik parası başvurusu, iş ilanları ve kariyer danışmanlığı için resmi istihdam ajansı.',
        icon='bi-briefcase-fill',
        sira=2,
    ),
    # Konut
    dict(
        kategori='konut',
        baslik='Berlin KdU / AV-Wohnen 2026 (PDF)',
        url='https://www.berlin.de/sen/soziales/soziale-sicherung/kosten-der-unterkunft-av-wohnen/flyer-uebernahme-von-wohn--und-heizkosten-_-fragen-und-antworten---stand-2026.pdf',
        ozet='Berlin\'de Bürgergeld / sosyal yardım kapsamında karşılanan kira ve ısınma giderlerine ait güncel (Ocak 2026) soru-cevap kılavuzu.',
        icon='bi-house-fill',
        sira=1,
    ),
    # Eğitim / Almanca
    dict(
        kategori='egitim',
        baslik='VHS Berlin – Deutsch & Integration',
        url='https://www.berlin.de/vhs/kurse/deutsch-integration/',
        ozet='Berlin\'in 12 ilçe halk eğitim merkezinde Almanca ve entegrasyon kursları; başlangıç seviyesinden C1\'e kadar.',
        icon='bi-mortarboard-fill',
        sira=1,
    ),
]


def seed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        sehir = Stadt.objects.get(slug='berlin')
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
    Kaynak.objects.filter(baslik__in=basliklar, stadt__slug='berlin').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('rehber', '0024_bultenabone'),
        ('stadt', '0010_seed_baskentler'),
    ]
    operations = [migrations.RunPython(seed, unseed)]
