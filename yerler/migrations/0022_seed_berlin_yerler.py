from django.db import migrations

IBADET = [
    {
        'ad': 'DİTİB Türk Şehitlik Camii',
        'adres': 'Columbiadamm 128, 10965 Berlin',
        'aciklama': 'Berlin\'in sembolü olan DİTİB Türk Şehitlik Camii, 1.500 kişi kapasitesiyle Almanya\'nın en büyük camilerinden biridir.',
        'kapak_resmi': '',
        'website': 'https://ditib-berlin.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=DITIB+Turk+Sehitlik+Camii+Berlin',
        'icerik': (
            '<p class="lead text-muted">Berlin\'in kalbinde yükselen DİTİB Türk Şehitlik Camii, Alman-Türk mimarisinin eşsiz bir buluşmasıdır.</p>'
            '<h4 class="fw-bold mt-4">Tarihçe</h4>'
            '<p>Türk Şehitliği\'nin içinde yer alan bu caminin temeli 1999 yılında atılmış, inşaatı 2005\'te tamamlanmıştır. '
            'Sultan Abdülaziz döneminden kalma Osmanlı şehitliğine komşu olan cami, 4 katlı yapısında 1.500 kişilik ibadet alanı barındırır.</p>'
            '<h4 class="fw-bold mt-4">Olanaklar</h4>'
            '<ul class="list-group list-group-flush mb-3">'
            '<li class="list-group-item">Kültür ve toplantı merkezi</li>'
            '<li class="list-group-item">Bilgi ve danışmanlık hizmetleri</li>'
            '<li class="list-group-item">Cuma namazı: 1.500 kişi kapasitesi</li>'
            '</ul>'
        ),
    },
    {
        'ad': 'Mevlana Moschee Berlin',
        'adres': 'Skalitzer Str. 132, 10999 Berlin',
        'aciklama': 'Kreuzberg\'in merkezinde yer alan Mevlana Camii, IGMG çatısı altında hizmet vermektedir.',
        'kapak_resmi': '',
        'website': 'https://mevlana-moschee.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Mevlana+Moschee+Berlin+Kreuzberg',
        'icerik': '',
    },
    {
        'ad': 'Berliner Dom',
        'adres': 'Am Lustgarten, 10178 Berlin',
        'aciklama': 'Berlin\'in ihtişamlı protestan katedrali; kupa turu, krypt ziyareti ve konserleriyle açık ziyaretçilere.',
        'kapak_resmi': '',
        'website': 'https://www.berlinerdom.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Berliner+Dom+Berlin',
        'icerik': '',
    },
]

TUV = [
    {
        'ad': 'TÜV Rheinland Berlin-Schöneberg',
        'adres': 'Alboinstraße 56, 12103 Berlin',
        'aciklama': 'Araç muayenesi (HU/AU), teknik inceleme ve sertifikasyon hizmetleri.',
        'kapak_resmi': '',
        'website': 'https://www.tuv.com/germany/de/',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=TUV+Rheinland+Berlin+Schoeneberg',
        'icerik': '',
    },
    {
        'ad': 'DEKRA Automobil Berlin-Charlottenburg',
        'adres': 'Franklinstraße 5-7, 10587 Berlin',
        'aciklama': 'Araç muayenesi (HU/AU), hasar eksperi ve teknik servis hizmetleri.',
        'kapak_resmi': '',
        'website': 'https://www.dekra.de/de/standorte/',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=DEKRA+Berlin+Charlottenburg',
        'icerik': '',
    },
]

SAGLIK = [
    {
        'ad': 'Charité Campus Mitte',
        'adres': 'Philippstraße 10, 10117 Berlin',
        'aciklama': 'Avrupa\'nın en büyük üniversite hastanesi; 7/24 acil servis, tüm branşlarda uzman hekim kadrosu.',
        'kapak_resmi': '',
        'website': 'https://www.charite.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Charite+Campus+Mitte+Berlin',
        'icerik': '',
    },
    {
        'ad': 'Vivantes Klinikum Neukölln',
        'adres': 'Rudower Str. 48, 12351 Berlin',
        'aciklama': 'Büyük kapasiteli Berlin hastanesi; 7/24 acil servis, yetişkin ve çocuk acil birimleri.',
        'kapak_resmi': '',
        'website': 'https://www.vivantes.de/klinikum-neukoelln',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Vivantes+Klinikum+Neukoelln+Berlin',
        'icerik': '',
    },
    {
        'ad': 'Gesundheitszentrum Bergmannstraße',
        'adres': 'Bergmannstraße 5, 10961 Berlin',
        'aciklama': 'Kreuzberg\'de çok branşlı sağlık merkezi; pratisyen, uzman hekimler ve koruyucu sağlık hizmetleri.',
        'kapak_resmi': '',
        'website': 'https://gesundheitszentrum-bergmannstrasse.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Gesundheitszentrum+Bergmannstrasse+Berlin',
        'icerik': '',
    },
]

EGITIM = [
    {
        'ad': 'Humboldt-Universität zu Berlin',
        'adres': 'Unter den Linden 6, 10117 Berlin',
        'aciklama': '1810 kuruluşlu; dünya sıralamalarında öne çıkan köklü Berlin üniversitesi.',
        'kapak_resmi': '',
        'website': 'https://www.hu-berlin.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Humboldt+Universitaet+zu+Berlin',
        'icerik': '',
    },
    {
        'ad': 'Türkische Gemeinde in Deutschland (TGD)',
        'adres': 'Obentrautstr. 72, 10963 Berlin',
        'aciklama': 'Eğitim danışmanlığı, sosyal destek ve entegrasyon projeleriyle Türk toplumuna hizmet.',
        'kapak_resmi': '',
        'website': 'https://tgd.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Turkische+Gemeinde+Deutschland+Berlin',
        'icerik': '',
    },
    {
        'ad': 'VHS Berlin Mitte',
        'adres': 'Linienstraße 162, 10115 Berlin',
        'aciklama': 'Almanca dil kursları, entegrasyon kursları ve mesleki gelişim eğitimleri.',
        'kapak_resmi': '',
        'website': 'https://www.berlin.de/vhs/volkshochschulen/mitte/',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=VHS+Volkshochschule+Berlin+Mitte',
        'icerik': '',
    },
]

GEZI = [
    {
        'ad': 'Brandenburger Tor',
        'adres': 'Pariser Platz 1, 10117 Berlin',
        'aciklama': 'Almanya\'nın sembolü; ücretsiz ziyaret, yakınında Yürüyüş ve Parlamento Çeyreği turu.',
        'kapak_resmi': '',
        'website': 'https://www.visitberlin.de/en/brandenburger-tor',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Brandenburger+Tor+Berlin',
        'icerik': '',
    },
    {
        'ad': 'Reichstag – Alman Parlamentosu',
        'adres': 'Platz der Republik 1, 11011 Berlin',
        'aciklama': 'Norman Foster\'ın cam kubbesiyle yeniden doğan Alman Parlamentosu; ücretsiz kubbe turu (ön kayıt gerekli).',
        'kapak_resmi': '',
        'website': 'https://www.bundestag.de/en/visittheBundestag',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Reichstag+Berlin',
        'icerik': '',
    },
    {
        'ad': 'Jüdisches Museum Berlin',
        'adres': 'Lindenstraße 9, 10969 Berlin',
        'aciklama': 'Daniel Libeskind tasarımlı ikonik mimari; 2000 yıllık Yahudi-Alman tarihini anlatıyor.',
        'kapak_resmi': '',
        'website': 'https://www.jmberlin.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Judisches+Museum+Berlin',
        'icerik': '',
    },
    {
        'ad': 'Berliner Fernsehturm',
        'adres': 'Panoramastraße 1A, 10178 Berlin',
        'aciklama': '368 metre yüksekliğiyle Berlin\'in simgesi; panoramik teras ve döner restoran.',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/2/20/Fernsehturm_Berlin_Alex.JPG',
        'website': 'https://tv-turm.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Berliner+Fernsehturm+Berlin',
        'icerik': '',
    },
]

ALISVERIS = [
    {
        'ad': 'KaDeWe – Kaufhaus des Westens',
        'adres': 'Tauentzienstraße 21-24, 10789 Berlin',
        'aciklama': 'Avrupa anakarasının en büyük mağazası; 60.000 m² alanda lüks alışveriş deneyimi.',
        'kapak_resmi': '',
        'website': 'https://www.kadewe.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=KaDeWe+Berlin',
        'icerik': '',
    },
    {
        'ad': 'Mall of Berlin',
        'adres': 'Leipziger Platz 12, 10117 Berlin',
        'aciklama': "Potsdamer Platz yakınında 270'den fazla mağazayla Berlin'in modern alışveriş merkezi.",
        'kapak_resmi': '',
        'website': 'https://www.mallofberlin.de',
        'maps_url': 'https://www.google.com/maps/search/?api=1&query=Mall+of+Berlin',
        'icerik': '',
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')
    Yer = apps.get_model('yerler', 'Yer')

    try:
        eyalet = Eyalet.objects.get(kod='BE')
        sehir = Stadt.objects.get(slug='berlin')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return

    sehir.aktiv = True
    sehir.save()

    kategoriler = [
        ('ibadet', IBADET),
        ('tuv', TUV),
        ('saglik', SAGLIK),
        ('egitim', EGITIM),
        ('gezi', GEZI),
        ('alisveris', ALISVERIS),
    ]

    for cat_slug, yerler in kategoriler:
        for veri in yerler:
            Yer.objects.get_or_create(
                ad=veri['ad'], stadt=sehir,
                defaults={
                    'eyalet': eyalet, 'scope': 'stadt', 'tur': 'yer', 'kategori': cat_slug,
                    'adres': veri['adres'], 'sehir': 'Berlin', 'aciklama': veri['aciklama'],
                    'kapak_resmi': veri.get('kapak_resmi', ''), 'website': veri.get('website', ''),
                    'maps_url': veri.get('maps_url', ''), 'icerik': veri.get('icerik', ''), 'aktif': True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = [v['ad'] for liste in [IBADET, TUV, SAGLIK, EGITIM, GEZI, ALISVERIS] for v in liste]
    Yer.objects.filter(ad__in=adlar, sehir='Berlin').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0021_seed_mannheim_yerler'),
        ('stadt', '0010_seed_baskentler'),
    ]
    operations = [migrations.RunPython(seed, unseed)]
