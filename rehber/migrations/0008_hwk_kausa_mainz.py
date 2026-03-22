"""
Data migration: Handwerkskammer Rheinhessen ve KAUSA RLP — Mainz özel.
Yer (fiziksel adres) + Kaynak + OnemliLink olarak eklenir.
"""
from django.db import migrations


def ekle(apps, schema_editor):
    Kaynak = apps.get_model('rehber', 'Kaynak')
    OnemliLink = apps.get_model('linkler', 'OnemliLink')
    Yer = apps.get_model('yerler', 'Yer')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
    except Stadt.DoesNotExist:
        return

    # ── Yer (fiziksel konum) ──────────────────────────────────────────────
    Yer.objects.get_or_create(
        ad='Handwerkskammer Rheinhessen',
        defaults=dict(
            kategori='resmi_kurum',
            adres='Dagobertstraße 2, 55116 Mainz',
            sehir='Mainz',
            website='https://www.hwk-rheinhessen.de/',
            maps_url='https://maps.google.com/?q=Handwerkskammer+Rheinhessen+Mainz+Dagobertstraße',
            aciklama='Esnaf ve zanaatkârlar odası. Ausbildung, usta belgesi ve göçmen danışmanlığı.',
            icerik=(
                '<p>Handwerkskammer (HWK) Rheinhessen, Mainz ve çevresindeki esnaf, zanaatkâr ve '
                'küçük işletmelerin resmi meslek kuruluşudur.</p>'
                '<h4>Göçmenler İçin Hizmetler</h4>'
                '<ul>'
                '<li>Ausbildung (çıraklık/staj) danışmanlığı ve eşleştirme</li>'
                '<li>Yabancı mesleki belgelerin tanınması</li>'
                '<li>Usta belgesi (Meister) başvuru bilgisi</li>'
                '<li>Kendi işini kurmak isteyenler için rehberlik</li>'
                '</ul>'
                '<h4>KAUSA Servisi</h4>'
                '<p>HWK bünyesindeki <strong>KAUSA RLP</strong> (Koordinierungsstelle Ausbildung und Migration) '
                'göçmen gençleri Ausbildung sürecinde destekler. Ücretsiz ve çok dilli danışmanlık sunar.</p>'
                '<div class="info-box"><strong>📍 Adres:</strong> Dagobertstraße 2, 55116 Mainz<br>'
                '<strong>🌐 KAUSA:</strong> kausa-rlp.de<br>'
                '<strong>📸 Instagram:</strong> @kausa.rlp</div>'
            ),
            aktif=True,
            stadt=mainz,
            scope='stadt',
        ),
    )

    # ── Kaynak ────────────────────────────────────────────────────────────
    kaynaklar = [
        dict(
            baslik='KAUSA RLP — Ausbildung ve Göç Danışmanlığı',
            slug='kausa-rlp',
            tip='link',
            url='https://www.kausa-rlp.de',
            kategori='is',
            icon='bi-tools',
            sira=7,
            yayinda=True,
            scope='stadt',
            ozet='Göçmen gençler için ücretsiz Ausbildung (çıraklık) danışmanlığı — HWK Rheinhessen bünyesinde.',
        ),
        dict(
            baslik='HWK Rheinhessen — Göçmenler İçin',
            slug='hwk-rheinhessen-migranten',
            tip='link',
            url='https://www.hwk.de/migranten',
            kategori='is',
            icon='bi-hammer',
            sira=8,
            yayinda=True,
            scope='stadt',
            ozet='Handwerkskammer — göçmenler için Ausbildung, mesleki tanıma ve kendi işini kurma rehberi.',
        ),
    ]
    for d in kaynaklar:
        Kaynak.objects.get_or_create(slug=d['slug'], defaults={**d, 'stadt': mainz})

    # ── OnemliLink ────────────────────────────────────────────────────────
    linkler = [
        dict(
            ad='KAUSA RLP — Ausbildung Danışmanlığı',
            url='https://www.kausa-rlp.de',
            kategori='is',
            aciklama='Göçmen gençler için ücretsiz Ausbildung danışmanlığı — HWK Rheinhessen.',
            sira=7,
            aktif=True,
            scope='stadt',
        ),
        dict(
            ad='HWK Rheinhessen — Göçmenler',
            url='https://www.hwk.de/migranten',
            kategori='is',
            aciklama='Handwerkskammer — Ausbildung, mesleki tanıma ve girişimcilik desteği.',
            sira=8,
            aktif=True,
            scope='stadt',
        ),
    ]
    for d in linkler:
        OnemliLink.objects.get_or_create(url=d['url'], defaults={**d, 'stadt': mainz})


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0007_zab_portal'),
        ('yerler', '0004_pratik_yerler'),
        ('linkler', '0004_entegrasyon_linkleri'),
        ('stadt', '0006_ayristry_mainz_bingen'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
