"""
Belediye RSS URL'lerini gerçek feedparser-uyumlu endpoint'lerle günceller.

Test sonuçları (2026-03-29):
  Mainz       : https://www.mainz.de/?sp%3Aout=rss          → 23 entry ✓
  Wiesbaden   : https://www.wiesbaden.de/?sp%3Aout=rss      → 16 entry ✓
  Mannheim    : https://www.mannheim.de/de/rss/nachrichten   → 50 entry ✓
  Berlin      : Çalışan RSS bulunamadı — temizlendi
  Hamburg     : Çalışan RSS bulunamadı — temizlendi
  Stuttgart   : RSS yalnızca servis kategorileri içeriyor — temizlendi
  Mainz-Bingen: Çalışan RSS bulunamadı — temizlendi
  Köln        : Çalışan RSS bulunamadı — temizlendi
"""

from django.db import migrations

RSS_GUNCELLEMELER = {
    'mainz':         'https://www.mainz.de/?sp%3Aout=rss',
    'wiesbaden':     'https://www.wiesbaden.de/?sp%3Aout=rss',
    'mannheim':      'https://www.mannheim.de/de/rss/nachrichten',
    # Çalışan RSS bulunamayan şehirler — boşaltılıyor
    'berlin':        '',
    'hamburg':       '',
    'stuttgart':     '',
    'mainz-bingen':  '',
    'koeln':         '',
}


def forward(apps, schema_editor):
    Stadt = apps.get_model('stadt', 'Stadt')
    for slug, url in RSS_GUNCELLEMELER.items():
        Stadt.objects.filter(slug=slug).update(rss_duyuru_url=url)


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('stadt', '0016_seed_koeln_yerler'),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]
