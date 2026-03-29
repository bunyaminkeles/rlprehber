from django.db import migrations

KOELN_YERLER = [
    # ─── Resmi Kurumlar ───────────────────────────────────────────────────────
    {
        'kategori': 'resmi_kurum',
        'ad': 'Ausländerbehörde Köln',
        'adres': 'Ossendorfweg 35, 50829 Köln',
        'website': 'https://www.stadt-koeln.de/service/suche/detail/auslaenderwesen',
        'maps_url': 'https://maps.google.com/?q=Ossendorfweg+35,+50829+K%C3%B6ln',
    },
    {
        'kategori': 'resmi_kurum',
        'ad': 'Jobcenter Köln',
        'adres': 'Bartholomäus-Schink-Str. 6, 50825 Köln',
        'website': 'https://www.jobcenter-koeln.de',
        'maps_url': 'https://maps.google.com/?q=Bartholomäus-Schink-Str.+6,+50825+K%C3%B6ln',
    },
    {
        'kategori': 'resmi_kurum',
        'ad': 'Agentur für Arbeit Köln',
        'adres': 'Luxemburger Str. 121, 50939 Köln',
        'website': 'https://www.arbeitsagentur.de/vor-ort/koeln',
        'maps_url': 'https://maps.google.com/?q=Luxemburger+Str.+121,+50939+K%C3%B6ln',
    },
    {
        'kategori': 'resmi_kurum',
        'ad': 'Finanzamt Köln-Mitte',
        'adres': 'Breite Str. 3-5, 50667 Köln',
        'website': 'https://www.finanzamt.nrw.de/finanzaemter/koeln-mitte',
        'maps_url': 'https://maps.google.com/?q=Breite+Str.+3,+50667+K%C3%B6ln',
    },
    {
        'kategori': 'resmi_kurum',
        'ad': 'KFZ-Zulassungsstelle Köln',
        'adres': 'Neusser Str. 105, 50670 Köln',
        'website': 'https://www.stadt-koeln.de/service/suche/detail/kfz-zulassungsstelle',
        'maps_url': 'https://maps.google.com/?q=Neusser+Str.+105,+50670+K%C3%B6ln',
    },
    # ─── Sağlık ───────────────────────────────────────────────────────────────
    {
        'kategori': 'saglik',
        'ad': 'Universitätsklinikum Köln (Uniklinik)',
        'adres': 'Kerpener Str. 62, 50937 Köln',
        'website': 'https://www.uk-koeln.de',
        'maps_url': 'https://maps.google.com/?q=Kerpener+Str.+62,+50937+K%C3%B6ln',
    },
    # ─── Eğitim ───────────────────────────────────────────────────────────────
    {
        'kategori': 'egitim',
        'ad': 'Universität zu Köln',
        'adres': 'Albertus-Magnus-Platz, 50923 Köln',
        'website': 'https://www.uni-koeln.de',
        'maps_url': 'https://maps.google.com/?q=Albertus-Magnus-Platz,+50923+K%C3%B6ln',
    },
    {
        'kategori': 'egitim',
        'ad': 'VHS Köln — Volkshochschule',
        'adres': 'Ottoplatz 2, 50679 Köln',
        'website': 'https://www.vhs.koeln.de',
        'maps_url': 'https://maps.google.com/?q=Ottoplatz+2,+50679+K%C3%B6ln',
    },
    # ─── Cami / İbadethane ────────────────────────────────────────────────────
    {
        'kategori': 'ibadet',
        'ad': 'DITIB Zentralmoschee Köln',
        'adres': 'Venloer Str. 160, 50823 Köln',
        'website': 'https://www.zentralmoschee-koeln.de',
        'maps_url': 'https://maps.google.com/?q=Venloer+Str.+160,+50823+K%C3%B6ln',
    },
    # ─── TÜV ──────────────────────────────────────────────────────────────────
    {
        'kategori': 'tuv',
        'ad': 'TÜV Rheinland — Köln',
        'adres': 'Am Grauen Stein 2, 51105 Köln',
        'website': 'https://www.tuv.com/de/tuv-rheinland-gruppe/',
        'maps_url': 'https://maps.google.com/?q=Am+Grauen+Stein+2,+51105+K%C3%B6ln',
    },
    # ─── Alışveriş ────────────────────────────────────────────────────────────
    {
        'kategori': 'alisveris',
        'ad': 'Rhein-Center Köln',
        'adres': 'Aachener Str. 1253, 50858 Köln',
        'website': 'https://www.rheincenter.de',
        'maps_url': 'https://maps.google.com/?q=Aachener+Str.+1253,+50858+K%C3%B6ln',
    },
    # ─── Gezi & Kültür ────────────────────────────────────────────────────────
    {
        'kategori': 'gezi',
        'ad': 'Kölner Dom',
        'adres': 'Domkloster 4, 50667 Köln',
        'website': 'https://www.koelner-dom.de',
        'maps_url': 'https://maps.google.com/?q=Domkloster+4,+50667+K%C3%B6ln',
        'aciklama': "UNESCO Dünya Mirası listesinde yer alan Kölner Dom, Gotik mimarinin en önemli örneklerinden biridir.",
    },
    {
        'kategori': 'gezi',
        'ad': 'Köln Müzesi Kompleksi — Altstadt',
        'adres': 'Roncalliplatz 4, 50667 Köln',
        'website': 'https://www.museenkoeln.de',
        'maps_url': 'https://maps.google.com/?q=Roncalliplatz+4,+50667+K%C3%B6ln',
    },
    # ─── Türk Market ──────────────────────────────────────────────────────────
    {
        'kategori': 'turk_market',
        'ad': 'Türk & Halal Marketler — Köln Ehrenfeld',
        'adres': 'Venloer Str. / Ehrenfeld, 50823 Köln',
        'website': '',
        'maps_url': 'https://maps.google.com/?q=Venloer+Str.,+50823+K%C3%B6ln',
        'aciklama': 'Ehrenfeld mahallesi, Türk marketleri ve helalcileri açısından Köln\'ün en yoğun bölgesidir.',
    },
]


def seed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Yer = apps.get_model('yerler', 'Yer')

    try:
        koeln = Stadt.objects.get(slug='koeln')
    except Stadt.DoesNotExist:
        return

    for veri in KOELN_YERLER:
        Yer.objects.get_or_create(
            stadt=koeln,
            ad=veri['ad'],
            defaults={
                'kategori': veri['kategori'],
                'adres': veri['adres'],
                'website': veri.get('website', ''),
                'maps_url': veri.get('maps_url', ''),
                'aciklama': veri.get('aciklama', ''),
                'sehir': 'Köln',
                'scope': 'stadt',
                'tur': 'yer',
                'aktif': True,
            }
        )

    # RSS URL'sini belediye haber sayfasıyla güncelle
    koeln.rss_duyuru_url = 'https://www.stadt-koeln.de/leben-in-koeln/aktuelles/pressemitteilungen'
    koeln.save(update_fields=['rss_duyuru_url'])


def unseed(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    Yer = apps.get_model('yerler', 'Yer')
    try:
        koeln = Stadt.objects.get(slug='koeln')
        Yer.objects.filter(stadt=koeln, sehir='Köln').delete()
    except Stadt.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0015_update_rss_links'),
        ('yerler', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
