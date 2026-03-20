"""
Blog yazılarını veritabanına ekler (get_or_create, güvenli tekrar çalıştırma).
Kullanım: python blog_yazilari_ekle.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import BlogYazisi

yazar = User.objects.filter(is_superuser=True).first()

YAZILAR = [
    {
        'baslik': 'Zulassungsstelle — Araç Kayıt İşlemleri',
        'slug': 'zulassungsstelle-arac-kayit-islemleri',
        'kapak_resmi': 'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=1200&q=80',
        'ozet': "Almanya'da aracını tescil ettirmek için Zulassungsstelle'de izlemen gereken adımlar: belgeler, ödeme ve plaka takma rehberi.",
        'icerik': '''
<div class="info-box mb-4">
  <strong>📋 Gerekli Belgeler</strong>
  <ul class="mb-0 mt-2">
    <li>Teil 1 — Fahrzeugschein (Ruhsat)</li>
    <li>Teil 2 — Zulassungsbescheinigung (Sahiplik Belgesi)</li>
    <li>Kimlik (Personalausweis veya Reisepass)</li>
    <li>Banka / Kredi Kartı</li>
    <li>eVB Sigorta Numarası</li>
    <li>Eski plakalar (varsa)</li>
    <li>İkamet belgesi (bazı memurlar isteyebilir)</li>
  </ul>
</div>

<ol class="blog-steps">
  <li>
    <strong>Girişi Yap</strong><br>
    Önceden aldığın randevu numarası ya da QR kod ile numaratörden giriş yap. Randevu bilgileri daha önce e-postana gönderildi.
  </li>

  <li>
    <strong>Bekleme Alanına Geç</strong><br>
    Sıra numaranı takip et. Sıra numaran gelen e-postada da mevcut.
  </li>

  <li>
    <strong>Memura Belgelerini Teslim Et</strong><br>
    Sıran geldiğinde ilgili memura git ve şunları teslim et:<br>
    <em>Teil 1 (ruhsat) · Teil 2 (sahiplik belgesi) · Kimlik · Banka/Kredi Kartı · eVB Sigorta Numarası · Eski plakalar (varsa)</em><br>
    Çok elzem değil, ancak bazı memurlar ikamet belgesi de isteyebilir.
  </li>

  <li>
    <strong>Plaka Tercihi</strong><br>
    Memur işlemler sırasında iki soru soracak:<br>
    &bull; Eski plakalarını geri almak istiyor musun, yoksa geri dönüşüme mü gitsin?<br>
    &bull; Özel bir plaka mı olsun, herhangi biri mi? (Özel plaka yaklaşık 10 Euro daha pahalı.)
  </li>

  <li>
    <strong>Bilgileri Onayla ve İmzala</strong><br>
    İşlemler bitince bilgilerinin doğru olduğunu teyit eden bir belge imzalarsın ve kayıt tamamlanır.
  </li>

  <li>
    <strong>Ödeme — Bina İçindeki Bankamatik</strong><br>
    Memur sana bir kart verecek. O kartı bina içindeki bankamatiğe tak. Ekranda ödemen gereken tutar çıkacak — <strong>47,50 Euro</strong> olması lazım. Kartla ya da nakit ödeyebilirsin. Bu, araç kayıt işlem ücretidir.
  </li>

  <li>
    <strong>Makbuzları Al ve Plakacıya Git</strong><br>
    Ödeme sonrası bankamatik sana 2-3 makbuz verecek. Makbuzları al; bina içindeki veya yakınındaki plakacıda plakalarını bastır. Makbuz üzerinde plakan yazar. Plaka basım ücreti <strong>yaklaşık 47,50 Euro</strong>.
  </li>

  <li>
    <strong>Ausgabe / Siegelstelle Ofisine Git</strong><br>
    Plaka ve makbuzlarla birlikte Zulassungsstelle binasının içindeki <em>Ausgabe</em> ya da <em>Siegelstelle</em> ofisine git (genellikle çıkışa yakın olur). Plakalar ile makbuzları teslim et.
  </li>

  <li>
    <strong>Bandrol ve Emisyon Etiketi</strong><br>
    Bandrollü plakalarla birlikte emisyon ölçüm etiketi verilecek.<br>
    &bull; Etiketi arabanın <strong>ön camının sağ alt köşesine</strong> yapıştır.<br>
    &bull; <strong>Çift bandrollü</strong> plaka arka tarafa, <strong>tek bandrollü</strong> ön tarafa takılır.
  </li>
</ol>

<div class="info-box mt-4">
  <strong>💡 Özet Masraf</strong><br>
  Kayıt işlem ücreti: ~47,50 €<br>
  Plaka basım ücreti: ~47,50 €<br>
  Toplam: <strong>~95,00 €</strong> (özel plaka seçilirse +10 €)
</div>
'''.strip(),
    },
]

eklendi = 0
for d in YAZILAR:
    _, created = BlogYazisi.objects.get_or_create(
        slug=d['slug'],
        defaults={**d, 'yazar': yazar, 'yayinda': True},
    )
    if created:
        eklendi += 1
        print(f'  ✓ {d["baslik"]}')

print(f'✅ {eklendi} yeni blog yazısı eklendi.')
