"""
Data migration: Entegrasyon odaklı linkler eklenir.

RLP Geneli (eyalet):
- BAMF Integrationskurs, Migrationsberatung MBE, Antidiskriminierungsstelle,
  Familienkasse (Kindergeld), Mieterschutzbund, Verbraucherzentrale RLP,
  Berufsberatung, SCHUFA

Mainz özel:
- VHS Mainz, Caritas Mainz Migrationsberatung, Ausländerbehörde termin

Mainz-Bingen özel:
- VHS Mainz-Bingen, Ausländerbehörde Kreis randevu
"""
from django.db import migrations


EYALET_LINKLER = [
    # ── Eğitim ───────────────────────────────────────────────────────────────
    dict(
        ad='BAMF — Integrationskurs Kurs Yeri Bul',
        url='https://www.bamf.de/SiteGlobals/Functions/WebGIS/DE/WebGIS_Integrationskurs.html',
        kategori='egitim',
        aciklama='Bulunduğunuz bölgedeki BAMF onaylı entegrasyon kursu sağlayıcılarını haritadan bulun.',
        sira=1,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    dict(
        ad='BAMF — Integrationskurs Bilgi ve Başvuru',
        url='https://www.bamf.de/DE/Themen/Integration/ZugewanderteTeilnehmende/Integrationskurse/integrationskurse-node.html',
        kategori='egitim',
        aciklama='Entegrasyon kursu nedir, kimler katılabilir, nasıl başvurulur — resmi BAMF bilgi sayfası.',
        sira=2,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    # ── Resmi ─────────────────────────────────────────────────────────────────
    dict(
        ad='Migrationsberatung MBE — Danışmanlık Bul',
        url='https://www.bamf.de/DE/Themen/Beratung/MBE/mbe-node.html',
        kategori='resmi',
        aciklama='Göçmen yetişkinlere ücretsiz bireysel danışmanlık sunan MBE merkezlerini bulun (Caritas, AWO, Diakonie vb.).',
        sira=5,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    dict(
        ad='Antidiskriminierungsstelle des Bundes',
        url='https://www.antidiskriminierungsstelle.de/',
        kategori='resmi',
        aciklama='İş, konut veya hizmetlerde ayrımcılığa uğrayanlar için federal danışmanlık ve destek hattı. Ücretsiz.',
        sira=6,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    dict(
        ad='Familienkasse — Kindergeld Başvurusu',
        url='https://www.arbeitsagentur.de/familie-und-kinder/kindergeld-beantragen',
        kategori='resmi',
        aciklama='Çocuk yardımı (Kindergeld) başvurusu. Her çocuk için aylık ~250 € — yasal hak.',
        sira=7,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    dict(
        ad='Elterngeld — Doğum Parası Başvurusu',
        url='https://www.elterngeld-digital.de/',
        kategori='resmi',
        aciklama='Yeni doğan bebek için ebeveyn yardımı (Elterngeld) online başvuru platformu.',
        sira=8,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    # ── Konut ─────────────────────────────────────────────────────────────────
    dict(
        ad='Mieterbund RLP — Kiracı Hakları',
        url='https://www.mieterbund-rlp.de/',
        kategori='resmi',
        aciklama='Rheinland-Pfalz kiracı hakları derneği. Kira sözleşmesi, tahliye ve hukuki danışmanlık.',
        sira=9,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    # ── Günlük Yaşam ─────────────────────────────────────────────────────────
    dict(
        ad='Verbraucherzentrale Rheinland-Pfalz',
        url='https://www.verbraucherzentrale-rlp.de/',
        kategori='resmi',
        aciklama='Tüketici hakları, sözleşme iptalleri, finansal dolandırıcılık — ücretsiz danışmanlık.',
        sira=10,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    # ── İş ───────────────────────────────────────────────────────────────────
    dict(
        ad='Make it in Germany — Çalışma Rehberi',
        url='https://www.make-it-in-germany.com/tr/',
        kategori='is',
        aciklama='Almanya\'da çalışmak isteyen göçmenler için Türkçe resmi rehber — vize, tanınma, iş başvurusu.',
        sira=3,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
    dict(
        ad='Anerkennung — Yabancı Diploma Tanıma',
        url='https://www.anerkennung-in-deutschland.de/',
        kategori='is',
        aciklama='Yurt dışında alınan meslek ve üniversite diplomalarının Almanya\'da tanınması için resmi platform.',
        sira=4,
        aktif=True,
        scope='eyalet',
        stadt=None,
    ),
]

MAINZ_LINKLER = [
    dict(
        ad='VHS Mainz — Kurs Kayıt',
        url='https://www.vhs-mainz.de/',
        kategori='egitim',
        aciklama='Mainz Volkshochschule — Almanca, entegrasyon kursu ve yetişkin eğitimi online kayıt.',
        sira=3,
        aktif=True,
        scope='stadt',
    ),
    dict(
        ad='Caritas Mainz — Migrationsberatung',
        url='https://www.caritas-mainz.de/',
        kategori='resmi',
        aciklama='Mainz Caritas göçmen danışmanlık merkezi — ücretsiz hukuki, sosyal ve entegrasyon danışmanlığı.',
        sira=11,
        aktif=True,
        scope='stadt',
    ),
    dict(
        ad='Mainz Ausländerbehörde — Online Randevu',
        url='https://www.mainz.de/vv/produkte/landes-und-landeshauptstadt/auslaenderamt.php',
        kategori='resmi',
        aciklama='Mainz yabancılar dairesi online randevu ve işlem bilgileri.',
        sira=12,
        aktif=True,
        scope='stadt',
    ),
]

MAINZ_BINGEN_LINKLER = [
    dict(
        ad='VHS Mainz-Bingen — Kurs Kayıt',
        url='https://www.vhs-mainz-bingen.de/',
        kategori='egitim',
        aciklama='Mainz-Bingen Volkshochschule — BAMF onaylı entegrasyon kursu ve Almanca eğitimi.',
        sira=3,
        aktif=True,
        scope='stadt',
    ),
    dict(
        ad='Ausländerbehörde Mainz-Bingen — Randevu',
        url='https://www.kreis-mainz-bingen.de/politik-verwaltung/auslaenderbehorde/',
        kategori='resmi',
        aciklama='Mainz-Bingen ilçesi yabancılar dairesi randevu ve bilgi sayfası.',
        sira=11,
        aktif=True,
        scope='stadt',
    ),
    dict(
        ad='Caritas Bingen — Migrationsberatung',
        url='https://www.caritas-mainz.de/',
        kategori='resmi',
        aciklama='Bingen ve Ingelheim bölgesinde göçmen danışmanlık hizmetleri — Caritas.',
        sira=12,
        aktif=True,
        scope='stadt',
    ),
]


def ekle(apps, schema_editor):
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        mainz_bingen = Stadt.objects.get(slug='mainz-bingen')
    except Stadt.DoesNotExist:
        return

    for d in EYALET_LINKLER:
        OnemliLink.objects.get_or_create(url=d['url'], defaults=d)

    for d in MAINZ_LINKLER:
        OnemliLink.objects.get_or_create(url=d['url'], defaults={**d, 'stadt': mainz})

    for d in MAINZ_BINGEN_LINKLER:
        OnemliLink.objects.get_or_create(url=d['url'], defaults={**d, 'stadt': mainz_bingen})


def geri_al(apps, schema_editor):
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    tum_url = (
        [d['url'] for d in EYALET_LINKLER]
        + [d['url'] for d in MAINZ_LINKLER]
        + [d['url'] for d in MAINZ_BINGEN_LINKLER]
    )
    OnemliLink.objects.filter(url__in=tum_url).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('linkler', '0003_mainz_bingen_linkler'),
        ('stadt', '0006_ayristry_mainz_bingen'),
    ]

    operations = [
        migrations.RunPython(ekle, geri_al),
    ]
