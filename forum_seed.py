"""
Forum kategorilerini yükler.
Kullanım: python forum_seed.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from forum.models import ForumKategori

KATEGORILER = [
    dict(ad='Genel Sohbet', aciklama='Mainz ve Bingen hakkında genel konular, tanışma, günlük hayat.', sira=1),
    dict(ad='Konut & Ev Arama', aciklama='Kiralık ev, WG, Anmeldung ve konut ile ilgili sorular.', sira=2),
    dict(ad='İş & Kariyer', aciklama='İş ilanları, CV, mülakat deneyimleri, Jobcenter.', sira=3),
    dict(ad='Resmi İşlemler', aciklama='Ausländerbehörde, Bürgeramt, vize, oturma izni, bürokratik süreçler.', sira=4),
    dict(ad='Ulaşım & Araç', aciklama='Toplu taşıma, araç alım-satım, Zulassungsstelle.', sira=5),
    dict(ad='Sağlık', aciklama='Doktor bulma, sigorta, hastane deneyimleri.', sira=6),
    dict(ad='Gezi & Etkinlik', aciklama='Mainz ve çevresi gezilecek yerler, etkinlikler, tavsiyeler.', sira=7),
    dict(ad='Dil & Entegrasyon', aciklama='Almanca öğrenme, entegrasyon kursları, dil okulu tavsiyeleri.', sira=8),
]

eklendi = 0
for d in KATEGORILER:
    _, created = ForumKategori.objects.get_or_create(
        ad=d['ad'],
        defaults=d,
    )
    if created:
        eklendi += 1
        print(f'  ✓ {d["ad"]}')

print(f'✅ {eklendi} yeni forum kategorisi eklendi.')
