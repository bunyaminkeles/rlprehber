from django.db import migrations


KAYNAKLAR = [
    dict(baslik='Mainz Bürgeramt — Online Randevu',       tip='link', url='https://termine-reservieren.de/termine/buergeramt.mainz/',                                                                                                                   kategori='resmi',   icon='bi-calendar-check',       sira=1, yayinda=True, ozet='Anmeldung, pasaport ve kimlik işlemleri için online randevu sistemi.'),
    dict(baslik='Mietbescheinigung — Kira Belgesi (PDF)', tip='link', url='https://www.jobcenter-mainz.de/wp-content/uploads/2021/05/Mietbescheinigung.pdf',                                                                                            kategori='konut',   icon='bi-file-earmark-pdf',     sira=1, yayinda=True, ozet='Jobcenter Mainz kira belgesi formu — ev sahibine imzalatılır.'),
    dict(baslik='KdU Mainz 2025 — Kira Üst Limitleri (PDF)', tip='link', url='https://harald-thome.de/files/pdf/KdU%20New/KdU%20Mainz%20-%2001.01.2025.pdf',                                                                                          kategori='konut',   icon='bi-file-earmark-text',    sira=2, yayinda=True, ozet='Mainz Jobcenter tarafından kabul edilen maksimum kira miktarları (01.01.2025).'),
    dict(baslik='KdU Mainz-Bingen 2025 — Uygun Kira Tablosu (PDF)', tip='link', url='https://www.mainz-bingen.de/default-wAssets/docs/Familie-Jugend-Asyl-Gesundheit-Soziales/Jobcenter/finanzielle-Leistungen-JobCenter/Sonstiges/Uebersicht-angemessene-KdU-2025.pdf', kategori='konut', icon='bi-file-earmark-text', sira=3, yayinda=True, ozet='Mainz-Bingen Jobcenter tarafından kabul edilen uygun kira miktarları (2025).'),
    dict(baslik='SCHUFA Datenkopie — Ücretsiz Kredi Raporu', tip='link', url='https://www.meineschufa.de/service/datenkopie',                                                                                                                           kategori='resmi',   icon='bi-file-person',          sira=5, yayinda=True, ozet="SCHUFA'dan yılda bir kez ücretsiz alınabilen kişisel kredi ve borç bilgisi raporu."),
    dict(baslik='Almanca Kurs Haritası',                  tip='link', url='https://bamf-navi.bamf.de/de/Themen/Integrationskurse/?coord=443065.5539144&kursart=1&',                                                                                     kategori='almanca', icon='bi-map',                   sira=1, yayinda=True, ozet='BAMF entegrasyon kursları haritası — yakınınızdaki Almanca kurslarını bulun.'),
]


def seed(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    for d in KAYNAKLAR:
        Kaynak.objects.get_or_create(url=d['url'], defaults=d)


class Migration(migrations.Migration):
    dependencies = [
        ('rehber', '0010_bamf_lid_sorulari'),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
