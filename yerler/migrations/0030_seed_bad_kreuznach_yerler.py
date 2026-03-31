from django.db import migrations

RESMI_KURUM = [
    {
        'ad': 'Rathaus Bad Kreuznach (Bürgerbüro)',
        'adres': 'Kornmarkt 5, 55543 Bad Kreuznach',
        'aciklama': 'Şehir belediyesi ve vatandaş hizmetleri merkezi. Adres tescili, kimlik/pasaport başvurusu.',
        'website': 'https://www.bad-kreuznach.de',
        'maps_url': 'https://www.google.com/maps/search/Rathaus+Bad+Kreuznach+Kornmarkt+5',
    },
    {
        'ad': 'Kreisverwaltung Bad Kreuznach',
        'adres': 'Salinenstraße 47, 55543 Bad Kreuznach',
        'aciklama': 'İlçe idare binası. Yabancılar Dairesi (Ausländerbehörde) zemin katta hizmet vermektedir.',
        'website': 'https://www.kreis-badkreuznach.de',
        'maps_url': 'https://www.google.com/maps/search/Kreisverwaltung+Bad+Kreuznach+Salinenstrasse+47',
    },
    {
        'ad': 'Ausländerbehörde Bad Kreuznach',
        'adres': 'Salinenstraße 47 (Zemin Kat), 55543 Bad Kreuznach',
        'aciklama': 'Yabancılar Dairesi. Pzt–Cum 08:00–12:00, Perş ayrıca 14:00–18:00. Tel: 0671/803-1399.',
        'website': 'https://www.kreis-badkreuznach.de/kreisverwaltung/organisation/informationen-aus-amt-10-der-kreisverwaltung-bad-kreuznach-auslaenderamt/servicepoint-der-auslaenderbehoerde/',
        'maps_url': 'https://www.google.com/maps/search/Ausländerbehörde+Bad+Kreuznach+Salinenstrasse+47',
    },
    {
        'ad': 'Finanzamt Bad Kreuznach',
        'adres': 'Ringstraße 10, 55543 Bad Kreuznach',
        'aciklama': 'Vergi dairesi.',
        'website': 'https://fa-bad-kreuznach.rlp.de/',
        'maps_url': 'https://www.google.com/maps/search/Finanzamt+Bad+Kreuznach+Ringstrasse+10',
    },
    {
        'ad': 'Agentur für Arbeit Bad Kreuznach',
        'adres': 'Bosenheimer Straße 16/26, 55543 Bad Kreuznach',
        'aciklama': 'İş kurumu. İşsizlik yardımı, iş arama ve mesleki danışmanlık hizmetleri.',
        'website': 'https://www.arbeitsagentur.de/vor-ort/bad-kreuznach',
        'maps_url': 'https://www.google.com/maps/search/Agentur+für+Arbeit+Bad+Kreuznach',
    },
    {
        'ad': 'Jobcenter Bad Kreuznach',
        'adres': 'Viktoriastraße 36, 55543 Bad Kreuznach',
        'aciklama': 'SGB II kapsamında işsizlik yardımı ve sosyal destek hizmetleri.',
        'website': 'https://jobcenter-badkreuznach.de',
        'maps_url': 'https://www.google.com/maps/search/Jobcenter+Bad+Kreuznach+Viktoriastrasse+36',
    },
]

IBADET = [
    {
        'ad': 'DITIB Bad Kreuznach Merkez Camii',
        'adres': 'Mühlenstraße 78, 55543 Bad Kreuznach',
        'aciklama': 'Bad Kreuznach\'ın en büyük Türk camii, DITIB bünyesinde.',
        'website': 'https://ditib-kh.de/',
        'maps_url': 'https://www.google.com/maps/search/DITIB+Bad+Kreuznach+Mühlenstraße+78',
    },
    {
        'ad': 'Al-Hijra Moschee',
        'adres': 'Nikolaus-Otto-Straße 13, 55543 Bad Kreuznach',
        'aciklama': 'Bad Kreuznach\'daki diğer cami.',
        'website': 'https://alhijra.de/',
        'maps_url': 'https://www.google.com/maps/search/Al-Hijra+Moschee+Bad+Kreuznach',
    },
]

TUV = [
    {
        'ad': 'DEKRA Automobil Bad Kreuznach',
        'adres': 'Mainzer Straße 10, 55545 Bad Kreuznach',
        'aciklama': 'Araç muayene istasyonu (HU/AU).',
        'website': 'https://www.dekra.de/de/bad-kreuznach/',
        'maps_url': 'https://www.google.com/maps/search/DEKRA+Bad+Kreuznach+Mainzer+Strasse+10',
    },
    {
        'ad': 'TÜV SÜD Auto Partner Bad Kreuznach',
        'adres': 'Planiger Straße, Gebäude 66N, 55543 Bad Kreuznach',
        'aciklama': 'TÜV araç muayene istasyonu.',
        'website': 'https://www.tuvsud.com/de-de/standorte/europe/germany/bad-kreuznach/planiger-str-gebaeude-66n',
        'maps_url': 'https://www.google.com/maps/search/TÜV+SÜD+Bad+Kreuznach+Planiger+Strasse',
    },
]

SAGLIK = [
    {
        'ad': 'Diakonie Kliniken Bad Kreuznach',
        'adres': 'Mannheimer Straße 166, 55543 Bad Kreuznach',
        'aciklama': 'Bad Kreuznach\'ın ana hastanesi.',
        'website': 'https://www.diakoniekliniken.de/badkreuznach',
        'maps_url': 'https://www.google.com/maps/search/Diakonie+Kliniken+Bad+Kreuznach',
    },
    {
        'ad': 'Drei-Burgen-Klinik Bad Kreuznach',
        'adres': 'Bad Kreuznach',
        'aciklama': 'Kardiyoloji ve rehabilitasyon kliniği.',
        'website': 'https://www.drei-burgen-klinik.de/',
        'maps_url': 'https://www.google.com/maps/search/Drei-Burgen-Klinik+Bad+Kreuznach',
    },
]

EGITIM = [
    {
        'ad': 'VHS Bad Kreuznach',
        'adres': 'Wilhelmstraße 7–11, 55543 Bad Kreuznach',
        'aciklama': 'Halk eğitim merkezi. Almanca dil kursları, entegrasyon kursları ve mesleki eğitimler.',
        'website': 'https://vhs-bad-kreuznach.de/',
        'maps_url': 'https://www.google.com/maps/search/VHS+Bad+Kreuznach+Wilhelmstrasse',
    },
    {
        'ad': 'KVHS Kreis Bad Kreuznach',
        'adres': 'Bad Kreuznach',
        'aciklama': 'İlçe halk eğitim merkezi. Çevre ilçelere yönelik kurslar.',
        'website': 'https://www.kvhs-kh.de/',
        'maps_url': 'https://www.google.com/maps/search/KVHS+Bad+Kreuznach',
    },
]

GEZI = [
    {
        'ad': 'Alte Nahebrücke (Köprü Evleri)',
        'adres': 'Nahe Nehri, Bad Kreuznach Merkez',
        'aciklama': 'Üzerinde evler bulunan tarihi köprü. Bad Kreuznach\'ın simgesi.',
        'website': '',
        'maps_url': 'https://www.google.com/maps/search/Alte+Nahebrücke+Bad+Kreuznach',
    },
    {
        'ad': 'Kurpark Bad Kreuznach',
        'adres': 'Bad Kreuznach Merkez',
        'aciklama': 'Termal kaplıca şehrinin tarihi parkı. Yürüyüş ve dinlenme alanı.',
        'website': '',
        'maps_url': 'https://www.google.com/maps/search/Kurpark+Bad+Kreuznach',
    },
    {
        'ad': 'Salinental',
        'adres': 'Bad Kreuznach – Bad Münster am Stein arası',
        'aciklama': "Avrupa'nın en büyük açık hava inhalatoryumu. 1,1 km uzunluğunda tuz duvarları.",
        'website': '',
        'maps_url': 'https://www.google.com/maps/search/Salinental+Bad+Kreuznach',
    },
    {
        'ad': 'Kauzenburg',
        'adres': 'Bad Kreuznach tepesi',
        'aciklama': 'Şehre hâkim tarihi kale kalıntıları.',
        'website': '',
        'maps_url': 'https://www.google.com/maps/search/Kauzenburg+Bad+Kreuznach',
    },
]

ALISVERIS = [
    {
        'ad': 'KM-Frischdienst (Türk Market)',
        'adres': 'Bosenheimer Straße 127a, 55543 Bad Kreuznach',
        'aciklama': 'Türk ve Orta Doğu ürünleri sunan market.',
        'website': 'https://km-frischdienst.de/',
        'maps_url': 'https://www.google.com/maps/search/KM+Frischdienst+Bad+Kreuznach+Bosenheimer+Strasse',
    },
    {
        'ad': 'GALERIA Bad Kreuznach',
        'adres': 'Mannheimer Straße 152, 55543 Bad Kreuznach',
        'aciklama': 'Büyük alışveriş merkezi.',
        'website': 'https://www.galeria.de/filialen/l/bad-kreuznach/mannheimer-strasse-152/001512',
        'maps_url': 'https://www.google.com/maps/search/Galeria+Bad+Kreuznach+Mannheimer+Strasse+152',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')
    try:
        eyalet = Eyalet.objects.get(kod='RLP')
        sehir  = Stadt.objects.get(slug='bad-kreuznach')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return
    for kategori_slug, veriler in [
        ('resmi_kurum', RESMI_KURUM),
        ('ibadet',      IBADET),
        ('tuv',         TUV),
        ('saglik',      SAGLIK),
        ('egitim',      EGITIM),
        ('gezi',        GEZI),
        ('alisveris',   ALISVERIS),
    ]:
        for veri in veriler:
            Yer.objects.get_or_create(
                ad=veri['ad'], stadt=sehir,
                defaults={
                    'eyalet':      eyalet,
                    'scope':       'stadt',
                    'tur':         'yer',
                    'kategori':    kategori_slug,
                    'sehir':       'Bad Kreuznach',
                    'adres':       veri['adres'],
                    'aciklama':    veri['aciklama'],
                    'kapak_resmi': veri.get('kapak_resmi', ''),
                    'website':     veri.get('website', ''),
                    'maps_url':    veri.get('maps_url', ''),
                    'icerik':      veri.get('icerik', ''),
                    'aktif':       True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = [v['ad'] for liste in [RESMI_KURUM, IBADET, TUV, SAGLIK, EGITIM, GEZI, ALISVERIS] for v in liste]
    Yer.objects.filter(ad__in=adlar, sehir='Bad Kreuznach').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0029_seed_trier_yerler'),
        ('stadt',  '0028_bad_kreuznach_aktiv'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
