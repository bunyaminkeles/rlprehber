"""
Linkler app'indeki benzersiz OnemliLink kayıtlarını Kaynak'a taşır.
Mükerrer olanlar atlanır (zaten Kaynak'ta var).
"""
from django.db import migrations


YENI_KAYNAKLAR = [
    # ── Resmi ────────────────────────────────────────────────────────────────
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'T.C. Mainz Başkonsolosluğu',
        'tip': 'link', 'url': 'https://mainz-bk.mfa.gov.tr/Mission',
        'kategori': 'resmi', 'icon': 'bi-flag',
        'ozet': 'Türk vatandaşları için konsolosluk hizmetleri.',
        'sira': 50,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'Mainz Şehir Portalı',
        'tip': 'link', 'url': 'https://www.mainz.de/',
        'kategori': 'resmi', 'icon': 'bi-building-fill',
        'ozet': 'Mainz Belediyesi resmi web sitesi.',
        'sira': 51,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'Mainz Ausländerbehörde — Online Randevu',
        'tip': 'link', 'url': 'https://www.mainz.de/vv/produkte/landes-und-landeshauptstadt/auslaenderamt.php',
        'kategori': 'resmi', 'icon': 'bi-calendar-check',
        'ozet': 'Yabancılar dairesi online randevu sistemi.',
        'sira': 52,
    },
    {
        'scope': 'stadt', 'eyalet_slug': 'rlp', 'stadt_slug': 'mainz-bingen',
        'baslik': 'Kreis Mainz-Bingen Portalı',
        'tip': 'link', 'url': 'https://www.kreis-mainz-bingen.de/',
        'kategori': 'resmi', 'icon': 'bi-building',
        'ozet': 'Mainz-Bingen ilçesi resmi web sitesi.',
        'sira': 53,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'Antidiskriminierungsstelle des Bundes',
        'tip': 'link', 'url': 'https://www.antidiskriminierungsstelle.de/',
        'kategori': 'resmi', 'icon': 'bi-shield-check',
        'ozet': 'Federal Ayrımcılık Karşıtı Kurum — şikayet ve danışmanlık.',
        'sira': 54,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'Verbraucherzentrale Rheinland-Pfalz',
        'tip': 'link', 'url': 'https://www.verbraucherzentrale-rlp.de/',
        'kategori': 'resmi', 'icon': 'bi-person-check',
        'ozet': 'Tüketici hakları danışmanlığı — RLP.',
        'sira': 55,
    },
    # ── İş & Kariyer ─────────────────────────────────────────────────────────
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'Bundesagentur für Arbeit',
        'tip': 'link', 'url': 'https://web.arbeitsagentur.de/',
        'kategori': 'is', 'icon': 'bi-briefcase-fill',
        'ozet': 'Federal İş Ajansı — iş arama, işsizlik yardımı.',
        'sira': 50,
    },
    {
        'scope': 'stadt', 'eyalet_slug': 'rlp', 'stadt_slug': 'mainz',
        'baslik': 'Mainz Jobcenter',
        'tip': 'link', 'url': 'https://www.jobcenter-mainz.de/',
        'kategori': 'is', 'icon': 'bi-building',
        'ozet': 'Mainz Jobcenter — işsizlik yardımı ve iş arama desteği.',
        'sira': 51,
    },
    {
        'scope': 'stadt', 'eyalet_slug': 'rlp', 'stadt_slug': 'mainz-bingen',
        'baslik': 'Jobcenter Mainz-Bingen',
        'tip': 'link', 'url': 'https://www.jobcenter-mainz-bingen.de/',
        'kategori': 'is', 'icon': 'bi-building',
        'ozet': 'Mainz-Bingen Jobcenter — işsizlik yardımı ve iş arama desteği.',
        'sira': 52,
    },
    # ── Eğitim ───────────────────────────────────────────────────────────────
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'BAMF Navi — Entegrasyon Kursu Haritası',
        'tip': 'link', 'url': 'https://bamf-navi.bamf.de/de/Themen/Integrationskurse/',
        'kategori': 'egitim', 'icon': 'bi-map',
        'ozet': 'Yakınındaki entegrasyon kurslarını bul.',
        'sira': 50,
    },
    # ── Sağlık ───────────────────────────────────────────────────────────────
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'Doctolib — Online Doktor Randevusu',
        'tip': 'link', 'url': 'https://www.doctolib.de/',
        'kategori': 'saglik', 'icon': 'bi-calendar-heart',
        'ozet': 'Online doktor randevusu — doktor bul ve randevu al.',
        'sira': 50,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'KV RLP — Doktor Arama',
        'tip': 'link', 'url': 'https://www.kv-rlp.de/',
        'kategori': 'saglik', 'icon': 'bi-search-heart',
        'ozet': 'Rheinland-Pfalz\'ta doktor arama platformu.',
        'sira': 51,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'AOK — Sağlık Sigortası',
        'tip': 'link', 'url': 'https://www.aok.de/pk/',
        'kategori': 'saglik', 'icon': 'bi-heart-pulse',
        'ozet': 'AOK sağlık sigortası bilgi ve başvuru.',
        'sira': 52,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'IKK Südwest — Sağlık Sigortası',
        'tip': 'link', 'url': 'https://www.ikk-suedwest.de/',
        'kategori': 'saglik', 'icon': 'bi-heart-pulse',
        'ozet': 'IKK Südwest sağlık sigortası.',
        'sira': 53,
    },
    # ── Ulaşım ───────────────────────────────────────────────────────────────
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'DB — Deutsche Bahn',
        'tip': 'link', 'url': 'https://www.bahn.de',
        'kategori': 'ulasim', 'icon': 'bi-train-front',
        'ozet': 'Tren bileti ve sefer sorgusu.',
        'sira': 10,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'FlixBus — Şehirlerarası Otobüs',
        'tip': 'link', 'url': 'https://www.flixbus.com/',
        'kategori': 'ulasim', 'icon': 'bi-bus-front',
        'ozet': 'Avrupa genelinde şehirlerarası otobüs.',
        'sira': 11,
    },
    {
        'scope': 'eyalet', 'eyalet_slug': 'rlp', 'stadt_slug': None,
        'baslik': 'AJet — Uçuş Arama',
        'tip': 'link', 'url': 'https://ajet.com/tr',
        'kategori': 'ulasim', 'icon': 'bi-airplane',
        'ozet': 'Uygun fiyatlı uçuş arama.',
        'sira': 12,
    },
]


def ekle_kaynaklar(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')

    for veri in YENI_KAYNAKLAR:
        eyalet = Eyalet.objects.filter(slug=veri['eyalet_slug']).first()
        if not eyalet:
            continue
        stadt = Stadt.objects.filter(slug=veri['stadt_slug']).first() if veri['stadt_slug'] else None

        if Kaynak.objects.filter(baslik=veri['baslik']).exists():
            continue  # mükerrer

        Kaynak.objects.create(
            eyalet=eyalet,
            stadt=stadt,
            scope=veri['scope'],
            baslik=veri['baslik'],
            tip=veri['tip'],
            url=veri['url'],
            kategori=veri['kategori'],
            icon=veri['icon'],
            ozet=veri['ozet'],
            sira=veri['sira'],
            yayinda=True,
        )


def geri_al(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    basliklar = [v['baslik'] for v in YENI_KAYNAKLAR]
    Kaynak.objects.filter(baslik__in=basliklar).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0012_eyalet_fk'),
        ('stadt',  '0010_seed_baskentler'),
    ]

    operations = [
        migrations.RunPython(ekle_kaynaklar, geri_al),
    ]
