from django.db import migrations


LINKLER = [
    dict(ad='Mainz Jobcenter',                    url='https://www.jobcenter-mainz.de/',                                                       kategori='is',      sira=1, aciklama='İşsizlik yardımı, iş arama desteği ve sosyal yardım başvuruları.'),
    dict(ad='Bundesagentur für Arbeit',            url='https://web.arbeitsagentur.de/',                                                        kategori='is',      sira=2, aciklama='Federal İş Kurumu — ALG I, iş ilanları ve kariyer danışmanlığı.'),
    dict(ad='T.C. Mainz Başkonsolosluğu',          url='https://mainz-bk.mfa.gov.tr/Mission',                                                  kategori='resmi',   sira=1, aciklama='Pasaport, vize, nüfus işlemleri ve konsolosluk hizmetleri.'),
    dict(ad='Mainz Şehir Portalı',                 url='https://www.mainz.de/',                                                                 kategori='resmi',   sira=2, aciklama='Mainz Belediyesi resmi sitesi — haberler, hizmetler, vatandaş işlemleri.'),
    dict(ad='BAMF — Göç ve Mülteci Dairesi',       url='https://www.bamf.de/EN/Startseite/startseite_node.html',                                kategori='resmi',   sira=3, aciklama='Federal Göç ve Mülteciler Dairesi — oturma izni, entegrasyon kursları ve sığınma başvuruları.'),
    dict(ad='Mainz Bürgeramt — Randevu',           url='https://termine-reservieren.de/termine/buergeramt.mainz/',                              kategori='resmi',   sira=4, aciklama='Mainz Vatandaşlık Dairesi online randevu — Anmeldung, pasaport, kimlik işlemleri.'),
    dict(ad='DB — Deutsche Bahn',                  url='https://www.bahn.de',                                                                   kategori='ulasim',  sira=1, aciklama='Almanya tren biletleri ve güzergahları.'),
    dict(ad='FlixBus — Şehirlerarası Otobüs',      url='https://www.flixbus.com/',                                                              kategori='ulasim',  sira=2, aciklama='Avrupa genelinde uygun fiyatlı şehirlerarası otobüs seferleri.'),
    dict(ad='AJet — Uçuş Arama',                   url='https://ajet.com/tr',                                                                   kategori='ulasim',  sira=3, aciklama='Türkiye merkezli havayolu — İstanbul ve diğer şehirlere uçuş arama.'),
    dict(ad='Kleinanzeigen — Mainz',               url='https://www.kleinanzeigen.de/s-mainz/c0',                                               kategori='ilan',    sira=1, aciklama='Mainz bölgesi ücretsiz ilan platformu. Araç, ev, eşya alım-satım.'),
    dict(ad='ImmobilienScout24 — Mainz',           url='https://www.immobilienscout24.de/Suche/de/rheinland-pfalz/mainz/wohnung-mieten',        kategori='ilan',    sira=2, aciklama="Mainz'da kiralık ev ilanları."),
    dict(ad='Immonet — Mainz',                     url='https://www.immonet.de/immobiliensuche/mainz.html',                                     kategori='ilan',    sira=3, aciklama='Mainz kiralık ve satılık ev ilanları.'),
    dict(ad='WG-Gesucht (Paylaşımlı Ev)',          url='https://www.wg-gesucht.de/',                                                            kategori='ilan',    sira=4, aciklama="WG (paylaşımlı daire) arama platformu. Mainz'da oda aramak için ideal."),
    dict(ad='Mobile.de — Araç İlanları',           url='https://www.mobile.de',                                                                 kategori='ilan',    sira=5, aciklama="Almanya'nın en büyük araç alım-satım platformu."),
    dict(ad='AutoScout24',                         url='https://www.autoscout24.de',                                                            kategori='ilan',    sira=6, aciklama='Avrupa genelinde araç alım-satım platformu.'),
    dict(ad='Doctolib — Online Doktor Randevusu',  url='https://www.doctolib.de/',                                                              kategori='saglik',  sira=1, aciklama='Almanya genelinde doktor, uzman ve klinik randevuları için online platform.'),
    dict(ad='IKK Südwest — Sağlık Sigortası',      url='https://www.ikk-suedwest.de/',                                                          kategori='saglik',  sira=2, aciklama='Mainz bölgesinde yaygın sağlık sigortası — üyelik ve hizmetler.'),
    dict(ad='AOK — Sağlık Sigortası',              url='https://www.aok.de/pk/',                                                                kategori='saglik',  sira=3, aciklama="Almanya'nın en büyük kamu sağlık sigortası — bilgi ve üyelik başvurusu."),
    dict(ad='KV RLP — Doktor Arama (Rheinland-Pfalz)', url='https://www.kv-rlp.de/',                                                           kategori='saglik',  sira=4, aciklama='Rheinland-Pfalz Kassenärztliche Vereinigung — bölgedeki aile hekimi ve uzman doktor arama platformu.'),
    dict(ad='BAMF Navi — Entegrasyon Kursu Haritası',  url='https://bamf-navi.bamf.de/de/Themen/Integrationskurse/',                            kategori='egitim',  sira=1, aciklama='BAMF resmi entegrasyon kursu arama aracı — bölgenizdeki Almanca ve oryantasyon kurslarını bulun.'),
]


def seed(apps, schema_editor):
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    for d in LINKLER:
        OnemliLink.objects.get_or_create(url=d['url'], defaults=d)


class Migration(migrations.Migration):
    dependencies = [
        ('linkler', '0004_entegrasyon_linkleri'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
