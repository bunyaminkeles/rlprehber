from django.db import migrations

KAYNAKLAR = [
    dict(kategori='resmi', baslik='Stuttgart Bürgerbüro — Online Termin',
         url='https://www.stuttgart.de/buergerbuero/',
         ozet='Nüfus tescili, pasaport ve kimlik kartı işlemleri için Stuttgart Bürgerbüro\'ya çevrimiçi randevu alın.',
         icon='bi-calendar-check', sira=1),
    dict(kategori='resmi', baslik='Stuttgart Ausländerbehörde',
         url='https://www.stuttgart.de/auslaenderbehoerde',
         ozet='Oturma izni, çalışma izni ve diğer yabancılar hukuku işlemleri için Stuttgart Yabancılar Dairesi.',
         icon='bi-building-fill', sira=2),
    dict(kategori='resmi', baslik='Caritas Stuttgart — Göçmen Danışmanlığı',
         url='https://www.caritas-stuttgart.de/hilfe-beratung/migration-integration-und-flucht/',
         ozet='Stuttgart\'ta yaşayan göçmenler için ücretsiz danışmanlık, sosyal yardım ve entegrasyon hizmetleri.',
         icon='bi-people-fill', sira=3),
    dict(kategori='resmi', baslik='Stadt Stuttgart — Resmi Portal',
         url='https://www.stuttgart.de',
         ozet='Stuttgart Belediyesi\'nin resmi portalı; tüm idari hizmetler, formlar ve belediye haberleri.',
         icon='bi-globe', sira=4),

    dict(kategori='is', baslik='Jobcenter Stuttgart',
         url='https://www.stuttgart.de/leben/arbeit/jobcenter',
         ozet='Bürgergeld (ALG II) başvurusu, iş bulma desteği ve mesleki yönlendirme hizmetleri.',
         icon='bi-briefcase-fill', sira=1),
    dict(kategori='is', baslik='Agentur für Arbeit Stuttgart',
         url='https://www.arbeitsagentur.de/vor-ort/stuttgart/',
         ozet='İş bulma, mesleki eğitim ve ALG I işlemleri için Stuttgart İş ve Meslek Kurumu.',
         icon='bi-briefcase', sira=2),
    dict(kategori='is', baslik='IHK Region Stuttgart',
         url='https://www.ihk.de/stuttgart/',
         ozet='Ticaret ve sanayi odası; işletme kurma, mesleki sertifikasyon ve danışmanlık hizmetleri.',
         icon='bi-building', sira=3),
    dict(kategori='is', baslik='HWK Region Stuttgart',
         url='https://www.hwk-stuttgart.de',
         ozet='El sanatları odası; esnaf sicil kaydı, ustalık belgesi ve mesleki eğitim danışmanlığı.',
         icon='bi-tools', sira=4),

    dict(kategori='konut', baslik='Stuttgart KdU — Konut Yardımı Sınır Tablosu',
         url='https://www.stuttgart.de/medien/iio/kosten-der-unterkunft.pdf',
         ozet='Jobcenter tarafından karşılanan kira üst sınırlarını gösteren Stuttgart KdU tablosu (PDF).',
         icon='bi-house-fill', sira=1),
    dict(kategori='konut', baslik='SWSG — Stuttgart Konut Şirketi',
         url='https://www.swsg.de',
         ozet='Stuttgart Konut ve Şehir Yapı Şirketi; sosyal konut başvuruları ve kira ilanları.',
         icon='bi-house-door-fill', sira=2),
    dict(kategori='konut', baslik='Mieterverein Stuttgart — Kiracı Derneği',
         url='https://www.mieterverein-stuttgart.de',
         ozet='Kira sözleşmesi, kiracı hakları ve anlaşmazlıklarda ücretsiz hukuki danışmanlık sunan kiracı derneği.',
         icon='bi-file-earmark-text', sira=3),

    dict(kategori='egitim', baslik='VHS Stuttgart — Kurs Kayıt',
         url='https://www.vhs-stuttgart.de/programm/sprachen/deutsch',
         ozet='Stuttgart Halk Yüksekokulu\'nda Almanca, entegrasyon ve mesleki gelişim kurslarına çevrimiçi kayıt.',
         icon='bi-mortarboard', sira=1),
    dict(kategori='egitim', baslik='Staatliches Schulamt Stuttgart',
         url='https://s.schulamt-bw.de/Startseite',
         ozet='Okul kaydı, öğrenci danışmanlığı ve eğitim destek programları için devlet okul dairesi.',
         icon='bi-backpack-fill', sira=2),
    dict(kategori='egitim', baslik='BAMF — Integrationskurs Stuttgart',
         url='https://www.bamf.de/DE/Themen/Integration/ZugewanderteTeilnehmende/Integrationskurse/integrationskurse-node.html',
         ozet='Stuttgart\'ta BAMF onaylı entegrasyon kurslarına başvuru ve kurs sağlayıcısı arama.',
         icon='bi-journal-bookmark-fill', sira=3),

    dict(kategori='almanca', baslik='VHS Stuttgart — Almanca Kursları',
         url='https://www.vhs-stuttgart.de/programm/sprachen/deutsch',
         ozet='A1\'den C1\'e tüm seviyelerde Almanca kursları; hafta içi ve hafta sonu seçenekleri mevcuttur.',
         icon='bi-translate', sira=1),
    dict(kategori='almanca', baslik='BAMF-Navi — Kurs Bulucu',
         url='https://bamf-navi.bamf.de/de/',
         ozet='Stuttgart ve çevresinde BAMF onaylı Almanca ve entegrasyon kursu sağlayıcılarını bulun.',
         icon='bi-compass', sira=2),
    dict(kategori='almanca', baslik='Kursnet — Almanca Kurs Arama',
         url='https://www.arbeitsagentur.de/kursnet',
         ozet='Bundesagentur für Arbeit\'in kurs veritabanı; Stuttgart\'ta Almanca kurslarını listeleyin ve karşılaştırın.',
         icon='bi-search', sira=3),

    dict(kategori='saglik', baslik='Kassenärztlicher Bereitschaftsdienst — 116117',
         url='https://www.116117.de',
         ozet='Acil olmayan tıbbi durumlarda 7/24 hizmet veren nöbetçi hekim hattı; randevu ve doktor yönlendirmesi.',
         icon='bi-telephone-fill', sira=1),
    dict(kategori='saglik', baslik='Gesundheitsamt Stuttgart',
         url='https://www.stuttgart.de/gesundheitsamt',
         ozet='Stuttgart Sağlık Dairesi; aşı, bulaşıcı hastalık kontrolü ve halk sağlığı danışmanlığı hizmetleri.',
         icon='bi-heart-pulse-fill', sira=2),
    dict(kategori='saglik', baslik='Klinikum Stuttgart — Hasta Bilgi Hattı',
         url='https://www.klinikum-stuttgart.de',
         ozet='Stuttgart\'ın en büyük hastane grubu; uzman klinikler, randevu ve poliklinik bilgileri.',
         icon='bi-hospital-fill', sira=3),
]


def seed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        sehir = Stadt.objects.get(slug='stuttgart')
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
        ('rehber', '0020_wiesbaden_ve_almanya_seed'),
        ('stadt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
