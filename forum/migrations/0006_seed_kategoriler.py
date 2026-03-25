from django.db import migrations


KATEGORILER = [
    dict(ad='Genel Sohbet',       aciklama='Mainz ve Bingen hakkında genel konular, tanışma, günlük hayat.', sira=1),
    dict(ad='Konut & Ev Arama',   aciklama='Kiralık ev, WG, Anmeldung ve konut ile ilgili sorular.',         sira=2),
    dict(ad='İş & Kariyer',       aciklama='İş ilanları, CV, mülakat deneyimleri, Jobcenter.',               sira=3),
    dict(ad='Resmi İşlemler',     aciklama='Ausländerbehörde, Bürgeramt, vize, oturma izni, bürokratik süreçler.', sira=4),
    dict(ad='Ulaşım & Araç',      aciklama='Toplu taşıma, araç alım-satım, Zulassungsstelle.',               sira=5),
    dict(ad='Sağlık',             aciklama='Doktor bulma, sigorta, hastane deneyimleri.',                    sira=6),
    dict(ad='Gezi & Etkinlik',    aciklama='Mainz ve çevresi gezilecek yerler, etkinlikler, tavsiyeler.',    sira=7),
    dict(ad='Dil & Entegrasyon',  aciklama='Almanca öğrenme, entegrasyon kursları, dil okulu tavsiyeleri.',  sira=8),
]


def seed(apps, schema_editor):
    ForumKategori = apps.get_model('forum', 'ForumKategori')
    for d in KATEGORILER:
        ForumKategori.objects.get_or_create(ad=d['ad'], defaults=d)


class Migration(migrations.Migration):
    dependencies = [
        ('forum', '0005_remove_konu_resim_remove_yorum_resim'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
