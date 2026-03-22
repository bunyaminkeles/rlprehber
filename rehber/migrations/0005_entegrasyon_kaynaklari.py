"""
Data migration: Entegrasyon odaklı kaynaklar Rehber/Kaynaklar bölümüne eklenir.

RLP Geneli (eyalet): BAMF, MBE, Antidiskriminierungsstelle, Kindergeld,
  Elterngeld, Mieterbund, Verbraucherzentrale, Make it in Germany, Diploma tanıma

Mainz özel: VHS Mainz, Caritas Mainz Migrationsberatung
Mainz-Bingen özel: VHS Mainz-Bingen, Ausländerbehörde Kreis, Caritas Bingen
"""
from django.db import migrations


EYALET_KAYNAKLAR = [
    # ── Eğitim ───────────────────────────────────────────────────────────────
    dict(
        baslik='BAMF — Integrationskurs Yeri Bul',
        slug='bamf-integrationskurs-bul',
        tip='link',
        url='https://www.bamf.de/SiteGlobals/Functions/WebGIS/DE/WebGIS_Integrationskurs.html',
        kategori='egitim',
        icon='bi-search',
        sira=1,
        yayinda=True,
        scope='eyalet',
        ozet='Bulunduğunuz bölgedeki BAMF onaylı entegrasyon kursu sağlayıcılarını haritadan bulun.',
    ),
    dict(
        baslik='BAMF — Integrationskurs Nedir?',
        slug='bamf-integrationskurs-bilgi',
        tip='link',
        url='https://www.bamf.de/DE/Themen/Integration/ZugewanderteTeilnehmende/Integrationskurse/integrationskurse-node.html',
        kategori='egitim',
        icon='bi-info-circle',
        sira=2,
        yayinda=True,
        scope='eyalet',
        ozet='Entegrasyon kursu hakkı, başvuru süreci ve kurs içeriği — resmi BAMF bilgi sayfası.',
    ),
    # ── Resmi İşlemler ────────────────────────────────────────────────────────
    dict(
        baslik='Migrationsberatung MBE — Danışmanlık Bul',
        slug='mbe-migrationsberatung',
        tip='link',
        url='https://www.bamf.de/DE/Themen/Beratung/MBE/mbe-node.html',
        kategori='resmi',
        icon='bi-people',
        sira=10,
        yayinda=True,
        scope='eyalet',
        ozet='Göçmen yetişkinlere ücretsiz bireysel danışmanlık (Caritas, AWO, Diakonie vb.) — yakınınızdaki merkezi bulun.',
    ),
    dict(
        baslik='Antidiskriminierungsstelle — Ayrımcılık Şikayeti',
        slug='antidiskriminierungsstelle',
        tip='link',
        url='https://www.antidiskriminierungsstelle.de/',
        kategori='resmi',
        icon='bi-shield-check',
        sira=11,
        yayinda=True,
        scope='eyalet',
        ozet='İş, konut veya hizmetlerde ayrımcılığa uğrayanlar için federal danışmanlık ve destek. Ücretsiz.',
    ),
    dict(
        baslik='Kindergeld — Çocuk Yardımı Başvurusu',
        slug='kindergeld-basvuru',
        tip='link',
        url='https://www.arbeitsagentur.de/familie-und-kinder/kindergeld-beantragen',
        kategori='resmi',
        icon='bi-heart',
        sira=12,
        yayinda=True,
        scope='eyalet',
        ozet='Her çocuk için aylık ~250 € Kindergeld yasal hakkınızdır. Online başvuru ve bilgi.',
    ),
    dict(
        baslik='Elterngeld — Doğum Parası Başvurusu',
        slug='elterngeld-basvuru',
        tip='link',
        url='https://www.elterngeld-digital.de/',
        kategori='resmi',
        icon='bi-baby',
        sira=13,
        yayinda=True,
        scope='eyalet',
        ozet='Yeni doğan için ebeveyn yardımı (Elterngeld) dijital başvuru platformu.',
    ),
    dict(
        baslik='Verbraucherzentrale RLP — Tüketici Hakları',
        slug='verbraucherzentrale-rlp',
        tip='link',
        url='https://www.verbraucherzentrale-rlp.de/',
        kategori='gunluk',
        icon='bi-hand-thumbs-up',
        sira=1,
        yayinda=True,
        scope='eyalet',
        ozet='Sözleşme iptalleri, dolandırıcılık, abonelik sorunları — ücretsiz tüketici danışmanlığı.',
    ),
    dict(
        baslik='Mieterbund RLP — Kiracı Hakları',
        slug='mieterbund-rlp',
        tip='link',
        url='https://www.mieterbund-rlp.de/',
        kategori='konut',
        icon='bi-house-check',
        sira=10,
        yayinda=True,
        scope='eyalet',
        ozet='Kira sözleşmesi, tahliye bildirimi ve kira artışı konularında hukuki danışmanlık.',
    ),
    # ── İş & Kariyer ─────────────────────────────────────────────────────────
    dict(
        baslik='Make it in Germany — Türkçe Çalışma Rehberi',
        slug='make-it-in-germany',
        tip='link',
        url='https://www.make-it-in-germany.com/tr/',
        kategori='is',
        icon='bi-briefcase',
        sira=5,
        yayinda=True,
        scope='eyalet',
        ozet='Almanya\'da çalışmak için Türkçe resmi rehber — vize, diploma tanıma, iş başvurusu.',
    ),
    dict(
        baslik='Anerkennung — Yabancı Diploma Tanıma',
        slug='anerkennung-diploma-tanima',
        tip='link',
        url='https://www.anerkennung-in-deutschland.de/',
        kategori='is',
        icon='bi-patch-check',
        sira=6,
        yayinda=True,
        scope='eyalet',
        ozet='Yurt dışında alınan meslek ve üniversite diplomalarının Almanya\'da resmi tanınması.',
    ),
]

MAINZ_KAYNAKLAR = [
    dict(
        baslik='VHS Mainz — Kurs Kayıt',
        slug='vhs-mainz',
        tip='link',
        url='https://www.vhs-mainz.de/',
        kategori='egitim',
        icon='bi-mortarboard',
        sira=3,
        yayinda=True,
        scope='stadt',
        ozet='Mainz Volkshochschule — Almanca, entegrasyon kursu ve yetişkin eğitimi online kayıt.',
    ),
    dict(
        baslik='Caritas Mainz — Göçmen Danışmanlığı',
        slug='caritas-mainz-migrationsberatung',
        tip='link',
        url='https://www.caritas-mainz.de/',
        kategori='resmi',
        icon='bi-people-fill',
        sira=14,
        yayinda=True,
        scope='stadt',
        ozet='Mainz Caritas ücretsiz göçmen danışmanlığı — hukuki, sosyal ve entegrasyon desteği.',
    ),
]

MAINZ_BINGEN_KAYNAKLAR = [
    dict(
        baslik='VHS Mainz-Bingen — Kurs Kayıt',
        slug='vhs-mainz-bingen',
        tip='link',
        url='https://www.vhs-mainz-bingen.de/',
        kategori='egitim',
        icon='bi-mortarboard',
        sira=3,
        yayinda=True,
        scope='stadt',
        ozet='Mainz-Bingen Volkshochschule — BAMF onaylı entegrasyon kursu ve Almanca eğitimi.',
    ),
    dict(
        baslik='Ausländerbehörde Mainz-Bingen — Randevu',
        slug='auslaenderbehorde-mainz-bingen',
        tip='link',
        url='https://www.kreis-mainz-bingen.de/politik-verwaltung/auslaenderbehorde/',
        kategori='resmi',
        icon='bi-building',
        sira=14,
        yayinda=True,
        scope='stadt',
        ozet='Mainz-Bingen ilçesi yabancılar dairesi — randevu ve işlem bilgileri.',
    ),
    dict(
        baslik='Caritas Bingen — Göçmen Danışmanlığı',
        slug='caritas-bingen-migrationsberatung',
        tip='link',
        url='https://www.caritas-mainz.de/',
        kategori='resmi',
        icon='bi-people-fill',
        sira=15,
        yayinda=True,
        scope='stadt',
        ozet='Bingen ve Ingelheim bölgesinde ücretsiz göçmen danışmanlık hizmetleri.',
    ),
]


def ekle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        mainz_bingen = Stadt.objects.get(slug='mainz-bingen')
    except Stadt.DoesNotExist:
        return

    for d in EYALET_KAYNAKLAR:
        Kaynak.objects.get_or_create(slug=d['slug'], defaults=d)

    for d in MAINZ_KAYNAKLAR:
        Kaynak.objects.get_or_create(slug=d['slug'], defaults={**d, 'stadt': mainz})

    for d in MAINZ_BINGEN_KAYNAKLAR:
        Kaynak.objects.get_or_create(slug=d['slug'], defaults={**d, 'stadt': mainz_bingen})


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    tum_sluglar = (
        [d['slug'] for d in EYALET_KAYNAKLAR]
        + [d['slug'] for d in MAINZ_KAYNAKLAR]
        + [d['slug'] for d in MAINZ_BINGEN_KAYNAKLAR]
    )
    Kaynak.objects.filter(slug__in=tum_sluglar).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0004_kaynak_scope_kaynak_stadt'),
        ('stadt', '0006_ayristry_mainz_bingen'),
    ]

    operations = [
        migrations.RunPython(ekle, geri_al),
    ]
