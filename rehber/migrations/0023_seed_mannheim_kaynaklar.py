from django.db import migrations

KAYNAKLAR = [
    # resmi
    dict(kategori='resmi', baslik='Mannheim Bürgerservice – Online Randevu',
         url='https://www.mannheim.de/de/service-bieten/buergerdienste/buergerservice',
         ozet='Nüfus, pasaport, kimlik kartı ve diğer resmi işlemler için Mannheim Bürgerbüro online randevu sayfası.',
         icon='bi-calendar-check', sira=1),
    dict(kategori='resmi', baslik='Mannheim Ausländerbehörde – Yabancılar İdaresi',
         url='https://www.mannheim.de/de/service-bieten/buergerdienste/zuwanderung-und-einbuergerung',
         ozet='Oturma izni, vize uzatma ve vatandaşlık işlemleri için Mannheim Yabancılar İdaresi bilgi sayfası.',
         icon='bi-building-fill', sira=2),
    dict(kategori='resmi', baslik='Caritas Mannheim',
         url='https://www.caritas-mannheim.de/',
         ozet='Mannheim Caritas; göçmen danışmanlığı, sosyal yardımlar ve entegrasyon hizmetleri sunan Katolik sosyal kuruluşu.',
         icon='bi-heart-fill', sira=3),

    # is
    dict(kategori='is', baslik='Jobcenter Mannheim',
         url='https://jobcenter-mannheim.de/',
         ozet="İşsizlik yardımı, iş arama desteği ve mesleki entegrasyon hizmetleri için Mannheim Jobcenter'ın resmi sitesi.",
         icon='bi-briefcase-fill', sira=1),
    dict(kategori='is', baslik='Agentur für Arbeit Mannheim',
         url='https://www.arbeitsagentur.de/vor-ort/mannheim',
         ozet='İş bulma, mesleki danışmanlık ve işsizlik sigortası başvuruları için Mannheim İş ve İşçi Bulma Kurumu.',
         icon='bi-building', sira=2),
    dict(kategori='is', baslik='IHK Rhein-Neckar – Sanayi ve Ticaret Odası',
         url='https://www.ihk.de/rhein-neckar/',
         ozet='Mannheim ve Rhein-Neckar bölgesi Sanayi ve Ticaret Odası; girişimcilik, ihracat ve mesleki eğitim desteği.',
         icon='bi-briefcase', sira=3),

    # konut
    dict(kategori='konut', baslik='GBG Wohnen Mannheim',
         url='https://www.gbg-wohnen.de/',
         ozet='Mannheim Belediyesi bünyesindeki konut şirketi. Uygun fiyatlı kiralık daire başvuruları ve boş daire listesi.',
         icon='bi-house-fill', sira=1),
    dict(kategori='konut', baslik='Mannheim Wohngeld – Konut Yardımı',
         url='https://www.mannheim.de/de/service-bieten/soziale-sicherung/wohnen-und-finanzen/wohngeld',
         ozet='Düşük gelirli haneler için kira yardımı (Wohngeld) başvuru bilgileri ve gerekli belgeler.',
         icon='bi-house', sira=2),

    # egitim
    dict(kategori='egitim', baslik='VHS Mannheim – Abendakademie Kurs Kaydı',
         url='https://www.abendakademie-mannheim.de/',
         ozet='Mannheim Halk Eğitim Merkezi kurs programı ve online kayıt sayfası. Dil, mesleki ve kültürel kurslar.',
         icon='bi-mortarboard', sira=1),
    dict(kategori='egitim', baslik='Staatliches Schulamt Mannheim',
         url='https://ma.schulamt-bw.de/',
         ozet='Mannheim Devlet Okul Dairesi; okul kayıt, öğrenci danışmanlığı ve eğitim politikası bilgileri.',
         icon='bi-building', sira=2),
    dict(kategori='egitim', baslik='BAMF Entegrasyon Kursları – Mannheim',
         url='https://www.mannheim.de/de/service-bieten/integration-migration/neuzuwanderung-erstintegration/integrationskurse-berufssprachkurse/integrationskurse',
         ozet="Mannheim'da BAMF onaylı entegrasyon kursları hakkında başvuru ve kayıt bilgileri.",
         icon='bi-book-fill', sira=3),

    # almanca
    dict(kategori='almanca', baslik='VHS Mannheim – Almanca Kursları (DaF/DaZ)',
         url='https://www.abendakademie-mannheim.de/fachbereiche/deutsch-als-fremdsprachezweitsprache/',
         ozet='Mannheim Abendakademie yabancı dil olarak Almanca (DaF/DaZ) kurs programı ve kayıt.',
         icon='bi-translate', sira=1),
    dict(kategori='almanca', baslik='BAMF-NAvI – Entegrasyon Kursu Ara',
         url='https://bamf-navi.bamf.de/de/Themen/Integrationskurse/',
         ozet='Tüm Almanya genelinde yakındaki BAMF onaylı dil ve entegrasyon kurslarını bulma aracı.',
         icon='bi-search', sira=2),
    dict(kategori='almanca', baslik='Kursnet – Bundesagentur für Arbeit',
         url='https://kursnet-finden.arbeitsagentur.de/',
         ozet="Bundesagentur'un ücretsiz eğitim ve dil kursu arama platformu. Mannheim ve çevresi kursları.",
         icon='bi-laptop', sira=3),

    # saglik
    dict(kategori='saglik', baslik='Ärztlicher Bereitschaftsdienst – 116117',
         url='https://www.116117.de/',
         ozet='Acil olmayan durumlarda doktor hattı 116117. Nöbetçi doktor, eczane ve teletıp hizmetlerine yönlendirme.',
         icon='bi-telephone-fill', sira=1),
    dict(kategori='saglik', baslik='Gesundheitsamt Mannheim – Sağlık Dairesi',
         url='https://www.mannheim.de/de/service-bieten/gesundheit',
         ozet='Mannheim Belediyesi Sağlık Dairesi; aşı, infeksiyon kontrol, bebek sağlığı ve çevre sağlığı hizmetleri.',
         icon='bi-heart-pulse', sira=2),
    dict(kategori='saglik', baslik='Universitätsklinikum Mannheim (UMM)',
         url='https://www.umm.de/',
         ozet="Mannheim'ın en büyük hastanesi ve üniversite kliniği. Uzman poliklinik randevuları ve acil servis bilgileri.",
         icon='bi-hospital', sira=3),
]


def seed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        sehir = Stadt.objects.get(slug='mannheim')
    except Stadt.DoesNotExist:
        return

    eyalet = sehir.eyalet

    for d in KAYNAKLAR:
        Kaynak.objects.get_or_create(
            baslik=d['baslik'],
            defaults=dict(
                **d,
                stadt=sehir,
                eyalet=eyalet,
                scope='stadt',
                tip='link',
                yayinda=True,
            ),
        )


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0022_fix_stuttgart_kaynaklar_urls'),
        ('stadt', '0011_seed_mannheim_stadt'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
