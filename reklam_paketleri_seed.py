"""
Reklam paketlerini veritabanına ekler (update_or_create, güvenli tekrar çalıştırma).
Kullanım: python reklam_paketleri_seed.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from yerler.models import ReklamPaketi

# Eski paketleri temizle (5'ten 3'e geçiş)
ReklamPaketi.objects.filter(ad__in=['Basic', 'Bronz', 'Silver', 'Gold', 'Premium']).delete()

PAKETLER = [
    {
        'ad': 'Temel',
        'aciklama': 'Hızlı başlangıç, risksiz deneyin.',
        'fiyat': '9.90',
        'sure_etiketi': '/ ay',
        'renk': 'secondary',
        'vurgulu': False,
        'sira': 1,
        'ozellikler': (
            'İşletme adı ve adres\n'
            'Kategori rozeti\n'
            'Google Maps linki\n'
            'Açıklama metni\n'
            'Telefon numarası'
        ),
        'iletisim_notu': '',
    },
    {
        'ad': 'Plus',
        'aciklama': 'Müşterilerinize daha fazla ulaşın.',
        'fiyat': '19.90',
        'sure_etiketi': '/ ay',
        'renk': 'primary',
        'vurgulu': True,
        'sira': 2,
        'ozellikler': (
            'Temel paketteki her şey\n'
            '3 fotoğraf galerisi\n'
            'WhatsApp butonu\n'
            'Instagram linki\n'
            'Çalışma saatleri\n'
            'Web sitesi linki'
        ),
        'iletisim_notu': '',
    },
    {
        'ad': 'Pro',
        'aciklama': 'Listenin en üstünde, herkesten önce.',
        'fiyat': '34.90',
        'sure_etiketi': '/ ay',
        'renk': 'warning',
        'vurgulu': False,
        'sira': 3,
        'ozellikler': (
            'Plus paketteki her şey\n'
            '"Öne Çıkan" rozeti\n'
            'Kategori listesinde en üst sıra\n'
            'Öncelikli destek'
        ),
        'iletisim_notu': (
            'Paket almak veya daha fazla bilgi için bizimle iletişime geçin.\n'
            'Ödeme IBAN ile yapılmaktadır.'
        ),
    },
]

eklendi = guncellendi = 0
for p in PAKETLER:
    _, created = ReklamPaketi.objects.update_or_create(
        ad=p['ad'],
        defaults={**p, 'aktif': True},
    )
    if created:
        eklendi += 1
        print(f'  ✓ Eklendi: {p["ad"]}')
    else:
        guncellendi += 1
        print(f'  ↺ Güncellendi: {p["ad"]}')

print(f'✅ {eklendi} eklendi, {guncellendi} güncellendi.')
