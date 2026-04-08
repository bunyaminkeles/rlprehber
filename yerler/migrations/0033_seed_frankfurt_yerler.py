"""
Frankfurt am Main — Önemli Yerler Seed Migrasyonu
Eyalet: Hessen (HE)
"""
from django.db import migrations

RESMI_KURUM = [
    {
        'ad': 'Ausländerbehörde Frankfurt am Main',
        'adres': 'Rebstöcker Straße 4, 60326 Frankfurt am Main',
        'aciklama': 'Frankfurt Yabancılar Dairesi. Oturma ve çalışma izni başvuruları yalnızca online portal üzerinden alınır.',
        'website': 'https://frankfurt.de/auslaenderangelegenheiten',
        'maps_url': 'https://maps.google.com/?q=Rebst%C3%B6cker+Stra%C3%9Fe+4,+60326+Frankfurt+am+Main',
    },
    {
        'ad': 'Jobcenter Frankfurt am Main',
        'adres': 'Gutleutstraße 72–76, 60329 Frankfurt am Main',
        'aciklama': 'Bürgergeld başvurusu, iş arama desteği ve sosyal yardım hizmetleri.',
        'website': 'https://www.jobcenter-frankfurt.de',
        'maps_url': 'https://maps.google.com/?q=Gutleutstra%C3%9Fe+72,+60329+Frankfurt+am+Main',
    },
    {
        'ad': 'Agentur für Arbeit Frankfurt am Main',
        'adres': 'Fischerfeldstraße 10–12, 60311 Frankfurt am Main',
        'aciklama': 'İşsizlik sigortası (ALG I), mesleki rehberlik ve iş ilanları.',
        'website': 'https://www.arbeitsagentur.de/vor-ort/frankfurt-main',
        'maps_url': 'https://maps.google.com/?q=Fischerfeldstra%C3%9Fe+10,+60311+Frankfurt+am+Main',
    },
    {
        'ad': 'Bürgeramt Frankfurt — Innenstadt',
        'adres': 'Zeil 3, 60313 Frankfurt am Main',
        'aciklama': 'Nüfus tescili, kimlik ve pasaport işlemleri. Online randevu zorunludur.',
        'website': 'https://frankfurt.de/service-und-rathaus/service/online-terminvereinbarungen',
        'maps_url': 'https://maps.google.com/?q=Zeil+3,+60313+Frankfurt+am+Main',
    },
    {
        'ad': 'Finanzamt Frankfurt am Main I',
        'adres': 'Gutleutstraße 114–146, 60327 Frankfurt am Main',
        'aciklama': 'Vergi numarası (Steuernummer) alma ve gelir vergisi beyannamesi işlemleri.',
        'website': 'https://www.finanzamt.hessen.de/ffm1',
        'maps_url': 'https://maps.google.com/?q=Gutleutstra%C3%9Fe+114,+60327+Frankfurt+am+Main',
    },
]

IBADET = [
    {
        'ad': 'DITIB Eyüp Sultan Camii Frankfurt',
        'adres': 'Schielestraße 20, 60314 Frankfurt am Main',
        'aciklama': 'Frankfurt\'ın en büyük camilerinden biri. Cuma namazı ve dini etkinlikler düzenlenmektedir.',
        'website': 'https://eyupsuitan-frankfurt.ditib.de',
        'maps_url': 'https://maps.google.com/?q=Schielestr.+20,+60314+Frankfurt+am+Main',
    },
    {
        'ad': 'Fatih Camii Frankfurt',
        'adres': 'Wittelsbacherallee 96, 60316 Frankfurt am Main',
        'aciklama': 'Ostend mahallesinde DITIB bünyesinde hizmet veren cami.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Wittelsbacherallee+96,+60316+Frankfurt+am+Main',
    },
]

TUV = [
    {
        'ad': 'TÜV Hessen — Frankfurt am Main',
        'adres': 'Robert-Bosch-Straße 16, 64293 Darmstadt',
        'aciklama': 'Araç muayenesi için en yakın TÜV Hessen şubesini tuevhessen.de üzerinden aratın. Frankfurt içinde birden fazla nokta mevcuttur.',
        'website': 'https://www.tuevhessen.de',
        'maps_url': 'https://maps.google.com/?q=T%C3%9CV+Hessen+Frankfurt',
    },
]

SAGLIK = [
    {
        'ad': 'Universitätsklinikum Frankfurt (Uniklinik)',
        'adres': 'Theodor-Stern-Kai 7, 60590 Frankfurt am Main',
        'aciklama': 'Hessen\'in en büyük üniversite hastanesi. Acil servis 7/24 hizmet vermektedir.',
        'website': 'https://www.uniklinik-frankfurt.de',
        'maps_url': 'https://maps.google.com/?q=Theodor-Stern-Kai+7,+60590+Frankfurt+am+Main',
    },
    {
        'ad': 'Bürgerhospital Frankfurt',
        'adres': 'Nibelungenallee 37–41, 60318 Frankfurt am Main',
        'aciklama': 'Frankfurt merkezine yakın genel hastane.',
        'website': 'https://www.buergerhospital-ffm.de',
        'maps_url': 'https://maps.google.com/?q=Nibelungenallee+37,+60318+Frankfurt+am+Main',
    },
]

EGITIM = [
    {
        'ad': 'Goethe-Universität Frankfurt am Main',
        'adres': 'Theodor-W.-Adorno-Platz 1, 60629 Frankfurt am Main',
        'aciklama': 'Almanya\'nın önde gelen araştırma üniversitelerinden biri. Lisans, yüksek lisans ve doktora programları.',
        'website': 'https://www.goethe-university-frankfurt.de',
        'maps_url': 'https://maps.google.com/?q=Theodor-W.-Adorno-Platz+1,+60629+Frankfurt+am+Main',
    },
    {
        'ad': 'Frankfurt University of Applied Sciences (Frankfurt UAS)',
        'adres': 'Nibelungenplatz 1, 60318 Frankfurt am Main',
        'aciklama': 'Mühendislik, sosyal bilimler ve sağlık alanlarında uygulamalı üniversite.',
        'website': 'https://www.frankfurt-university.de',
        'maps_url': 'https://maps.google.com/?q=Nibelungenplatz+1,+60318+Frankfurt+am+Main',
    },
    {
        'ad': 'VHS Frankfurt — Volkshochschule',
        'adres': 'Sonnemannstraße 13, 60314 Frankfurt am Main',
        'aciklama': 'Almanca entegrasyon kursları, mesleki eğitim sertifikaları ve kültürel etkinlikler.',
        'website': 'https://www.vhs-frankfurt.de',
        'maps_url': 'https://maps.google.com/?q=Sonnemannstra%C3%9Fe+13,+60314+Frankfurt+am+Main',
    },
]

GEZI = [
    {
        'ad': 'Römerberg — Frankfurt Tarihi Kent Merkezi',
        'adres': 'Römerberg, 60311 Frankfurt am Main',
        'aciklama': 'Frankfurt\'ın simgesi olan ortaçağ meydanı. Römer Belediye Sarayı ve Saalhof burada yer alır.',
        'website': 'https://www.frankfurt-tourismus.de',
        'maps_url': 'https://maps.google.com/?q=R%C3%B6merberg,+60311+Frankfurt+am+Main',
    },
    {
        'ad': 'Städel Museum',
        'adres': 'Schaumainkai 63, 60596 Frankfurt am Main',
        'aciklama': 'Avrupa\'nın önde gelen sanat müzelerinden biri. 700 yıllık resim, heykel ve grafik koleksiyonu.',
        'website': 'https://www.staedelmuseum.de',
        'maps_url': 'https://maps.google.com/?q=Schaumainkai+63,+60596+Frankfurt+am+Main',
    },
    {
        'ad': 'Palmengarten Frankfurt',
        'adres': 'Siesmayerstraße 61, 60323 Frankfurt am Main',
        'aciklama': 'Almanya\'nın en büyük botanik bahçelerinden biri. Tropikal seralar ve açık hava etkinlikleri.',
        'website': 'https://www.palmengarten.de',
        'maps_url': 'https://maps.google.com/?q=Siesmayerstra%C3%9Fe+61,+60323+Frankfurt+am+Main',
    },
]

ALISVERIS = [
    {
        'ad': 'Zeil — Frankfurt Ana Alışveriş Caddesi',
        'adres': 'Zeil, 60313 Frankfurt am Main',
        'aciklama': 'Almanya\'nın en yüksek ciro yapan alışveriş caddelerinden biri. MyZeil AVM ve büyük mağazalar.',
        'website': 'https://www.zeil-frankfurt.de',
        'maps_url': 'https://maps.google.com/?q=Zeil,+60313+Frankfurt+am+Main',
    },
    {
        'ad': 'Berger Straße — Yerel Dükkanlar',
        'adres': 'Berger Straße, 60316 Frankfurt am Main',
        'aciklama': 'Bornheim mahallesinde yerel dükkanlar, kafeler ve pazarların bulunduğu renkli yürüyüş caddesi.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Berger+Stra%C3%9Fe,+60316+Frankfurt+am+Main',
    },
]

TURK_MARKET = [
    {
        'ad': 'Türk Marketleri — Ostend / Bornheim',
        'adres': 'Ostend, 60314 Frankfurt am Main',
        'aciklama': 'Ostend ve Bornheim mahallelerinde yoğunlaşan Türk ve Halal marketler.',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Ostend,+60314+Frankfurt+am+Main',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')

    try:
        eyalet = Eyalet.objects.get(kod='HE')
        sehir  = Stadt.objects.get(slug='frankfurt')
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
        ('turk_market', TURK_MARKET),
    ]:
        for veri in veriler:
            Yer.objects.get_or_create(
                ad=veri['ad'], stadt=sehir,
                defaults={
                    'eyalet':      eyalet,
                    'scope':       'stadt',
                    'tur':         'yer',
                    'kategori':    kategori_slug,
                    'sehir':       'Frankfurt am Main',
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
    adlar = [v['ad'] for liste in [
        RESMI_KURUM, IBADET, TUV, SAGLIK, EGITIM, GEZI, ALISVERIS, TURK_MARKET
    ] for v in liste]
    Yer.objects.filter(ad__in=adlar, sehir='Frankfurt am Main').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0032_urlfield_max_length_500'),
        ('stadt',  '0038_seed_frankfurt'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
