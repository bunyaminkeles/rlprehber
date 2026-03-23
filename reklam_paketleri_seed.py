"""
Reklam paketlerini veritabanına ekler (update_or_create, güvenli tekrar çalıştırma).
Kullanım: python reklam_paketleri_seed.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from yerler.models import ReklamPaketi

PAKETLER = [
    {
        'ad': 'Basic',
        'fiyat': '4.90',
        'sure_etiketi': '/ 10 gün',
        'renk': 'secondary',
        'vurgulu': False,
        'sira': 1,
        'ozellikler': (
            'İşletme adı ve adres\n'
            'Kategori rozeti\n'
            'Google Maps linki\n'
            'Platforma giriş fırsatı'
        ),
        'iletisim_notu': '',
    },
    {
        'ad': 'Bronz',
        'fiyat': '9.90',
        'sure_etiketi': '/ 3 hafta',
        'renk': 'warning',
        'vurgulu': False,
        'sira': 2,
        'ozellikler': (
            'Basic paketteki her şey\n'
            'Açıklama metni\n'
            'Telefon numarası\n'
            'Web sitesi linki'
        ),
        'iletisim_notu': '',
    },
    {
        'ad': 'Silver',
        'fiyat': '14.90',
        'sure_etiketi': '/ ay',
        'renk': 'primary',
        'vurgulu': True,
        'sira': 3,
        'ozellikler': (
            'Bronz paketteki her şey\n'
            '3 fotoğraf galerisi\n'
            'WhatsApp butonu\n'
            'Instagram linki\n'
            'Çalışma saatleri'
        ),
        'iletisim_notu': '',
    },
    {
        'ad': 'Gold',
        'fiyat': '59.90',
        'sure_etiketi': '/ 6 ay',
        'renk': 'success',
        'vurgulu': False,
        'sira': 4,
        'ozellikler': (
            'Silver paketteki her şey\n'
            '"Öne Çıkan" rozeti\n'
            'Liste başında görünüm\n'
            '~10 €/ay — %33 tasarruf'
        ),
        'iletisim_notu': '',
    },
    {
        'ad': 'Premium',
        'fiyat': '99.90',
        'sure_etiketi': '/ yıl',
        'renk': 'dark',
        'vurgulu': False,
        'sira': 5,
        'ozellikler': (
            'Gold paketteki her şey\n'
            '1 yıl kesintisiz görünüm\n'
            'Öncelikli destek\n'
            '~8,30 €/ay — %44 tasarruf'
        ),
        'iletisim_notu': (
            'Paket almak veya daha fazla bilgi almak için bizimle iletişime geçin.\n'
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
