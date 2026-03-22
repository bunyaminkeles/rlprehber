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
    {
        'baslik': 'Almanya\'da Diploma Denkliği (ZAB): Bürokratik Süreci Adım Adım Çözme Rehberi',
        'slug': 'almanyada-diploma-denkligi-zab-rehberi',
        'kapak_resmi': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&q=80',
        'ozet': 'ZAB Zeugnisbewertung nedir, Anabin\'de nasıl kontrol yapılır, belgeler nasıl hazırlanır? Mavi Kart ve nitelikli çalışan vizesi için diploma denkliği sürecinin tam rehberi.',
        'scope': 'eyalet',
        'icerik': '''
<p class="lead">Almanya'da kariyerinize başlamak, nitelikli çalışan vizesi almak veya Mavi Kart (Blaue Karte) başvurusu yapmak istiyorsunuz. Harika bir iş buldunuz ancak sistem önünüze o meşhur engeli çıkardı: <em>"Diplomanızın Almanya'da geçerli olduğunu kanıtlamalısınız."</em></p>

<p>Alman bürokrasisi dışarıdan bakıldığında aşılmaz bir duvar gibi görünebilir. Ancak doğru adımları izlediğinizde, her sürecin aslında belirli kurallara dayanan net bir işleyişi olduğunu göreceksiniz. Bu yazıda, ZAB (Zentralstelle für ausländisches Bildungswesen) üzerinden diploma denklik (<em>Zeugnisbewertung</em>) sürecini en hızlı ve hatasız şekilde nasıl tamamlayacağınızı adım adım anlatıyoruz.</p>

<h4>Adım 1: İlk Kontrol — Anabin Veritabanı</h4>

<p>ZAB'a 200 Euro ödeyip haftalarca beklemeden önce yapmanız gereken çok önemli bir adım var: diplomanızın durumunu Anabin sisteminden kontrol etmek.</p>

<ul>
  <li><strong>Okulunuz Tanınıyor mu?</strong> Mezun olduğunuz üniversite Anabin'de <strong>"H+"</strong> statüsüne sahip olmalıdır.</li>
  <li><strong>Bölümünüz Eşdeğer mi?</strong> Okuduğunuz bölüm sistemde <em>"Entspricht"</em> (Eşdeğer) veya <em>"Gleichwertig"</em> (Denk) olarak geçiyor mu?</li>
</ul>

<p>Eğer her iki sorunun cevabı da evetse ve sistemde tam bir eşleşme bulduysanız, harika bir haberimiz var: çoğu durumda Anabin'den alacağınız PDF çıktıları vize veya Mavi Kart başvurunuz için yeterlidir. Ekstra bir denklik başvurusu yapmanıza gerek kalmaz.</p>

<div class="info-box">
  <strong>⚠️ Ne zaman ZAB zorunlu?</strong><br>
  Durum belirsizse (H+/-), okulunuz listede yoksa veya konsolosluk / yabancılar dairesi sizden özel olarak resmi ZAB belgesi (<em>Zeugnisbewertung</em>) talep ediyorsa süreci başlatma vakti gelmiştir.
</div>

<h4>Adım 2: Belgelerin Doğru Hazırlanması</h4>

<p>ZAB süreci artık tamamen dijital platform ("Mein Portal") üzerinden yürütülüyor. Bu yüzden fiziksel belgelerinizi eksiksiz ve okunur bir şekilde PDF formatında taratmanız hayati önem taşıyor. Türkiye'den alınan diplomalar için genel kurallar şunlardır:</p>

<ul>
  <li><strong>Orijinal Belgeler:</strong> Diplomanızın ve not dökümünüzün (Transkript) orijinal dildeki yüksek çözünürlüklü taramaları.</li>
  <li><strong>Çeviriler:</strong> ZAB genellikle Türkçe, İngilizce ve Fransızca dillerindeki belgeleri doğrudan kabul eder ve yeminli tercüme <strong>istemez</strong>. (Yine de başvuru anında portalın <em>"Länderdokumente"</em> sekmesinden güncel şartları mutlaka teyit edin.)</li>
  <li><strong>Kimlik Belgesi:</strong> Pasaportunuzun veya kimliğinizin taranmış hali.</li>
</ul>

<div class="info-box">
  <strong>💡 Kritik İpucu: İş Sözleşmesi</strong><br>
  Mavi Kart başvurusunda bulunacaksanız ve elinizde şirketle imzaladığınız bir iş sözleşmesi varsa, bunu sisteme <strong>mutlaka</strong> yükleyin. İş sözleşmesi başvurunuza "öncelik" kazandırır ve normalde 3 ay sürebilecek bekleme süresini <strong>2 haftaya</strong> kadar düşürebilir.
</div>

<h4>Adım 3: Başvuru Süreci — "Mein Portal"</h4>

<p>Belgelerimiz hazır olduğuna göre resmi başvuruya geçebiliriz:</p>

<ol class="blog-steps">
  <li>
    <strong>Hesap Oluşturma</strong><br>
    ZAB'ın yeni başvuru portalında (BundID entegrasyonu ile) bir hesap açın.
  </li>
  <li>
    <strong>Eğitim Geçmişi</strong><br>
    Lise eğitiminizden başlayarak üniversiteye kadar olan tüm eğitim bilgilerinizi tarih sırasına göre eksiksiz doldurun.
  </li>
  <li>
    <strong>Evrak Yükleme</strong><br>
    Hazırladığınız PDF dosyalarını sisteme yükleyin. Dosya isimlerinin anlaşılır olmasına dikkat edin.<br>
    <em>Örn: Ahmet_Yilmaz_Diploma_TR.pdf</em>
  </li>
  <li>
    <strong>Ücret Ödemesi</strong><br>
    Başvuruyu tamamladığınızda sistem size bir ödeme bildirimi (<em>Gebührenbescheid</em>) gönderecektir. İlk başvuru ücreti <strong>200 Euro</strong>'dur. Banka havalesinin açıklama kısmına (<em>Verwendungszweck</em>) size verilen referans numarasını <strong>eksiksiz ve doğru</strong> yazdığınızdan emin olun. Aksi takdirde ödemeniz sistemde eşleşmez ve süreciniz aylarca uzayabilir.
  </li>
</ol>

<h4>Adım 4: Bekleme ve Sonuç</h4>

<p>Ödemeniz ZAB'ın sistemine ulaştığı andan itibaren dosyanız "İşlemde" (<em>In Bearbeitung</em>) statüsüne geçer.</p>

<ul>
  <li><strong>Mavi Kart — Öncelikli başvuru:</strong> Genellikle ~2 hafta</li>
  <li><strong>Standart başvuru:</strong> 1 ila 3 ay</li>
</ul>

<p>Süreç tamamlandığında portal üzerinden dijital imzalı bir PDF belgesi alacaksınız. İşte bu belge sizin resmi <em>Zeugnisbewertung</em>'unuzdur. Artık diplomanızın Alman eğitim ve iş dünyasındaki karşılığını kanıtlayan, kariyeriniz boyunca geçerli olacak kalıcı bir belgeye sahipsiniz.</p>

<div class="info-box mt-4">
  <strong>🔗 Faydalı Linkler</strong><br>
  <a href="https://anabin.kmk.org/db/institutionen" target="_blank" rel="noopener">Anabin — Üniversite Arama</a><br>
  <a href="https://zab.kmk.org/de/zeugnisbewertung/antrag" target="_blank" rel="noopener">ZAB — Zeugnisbewertung Başvurusu</a>
</div>

<div class="mt-4 p-4 border rounded" style="background:#f0f5fb; border-color:#2C5F8A !important;">
  <strong>🤖 ZAB'a başvurmanız gerekiyor mu?</strong><br>
  <p class="mb-2 mt-1" style="font-size:0.9rem">Anabin durumunuza göre adım adım öğrenmek için kendi karar aracımızı kullanın:</p>
  <a href="/rlp/rehber/anabin-karar-araci/" class="btn btn-primary btn-sm">
    Anabin Karar Aracı →
  </a>
</div>
'''.strip(),
    },
]

eklendi = guncellendi = 0
for d in YAZILAR:
    _, created = BlogYazisi.objects.update_or_create(
        slug=d['slug'],
        defaults={**d, 'yazar': yazar, 'yayinda': True},
    )
    if created:
        eklendi += 1
        print(f'  ✓ Eklendi: {d["baslik"]}')
    else:
        guncellendi += 1
        print(f'  ↺ Güncellendi: {d["baslik"]}')

print(f'✅ {eklendi} eklendi, {guncellendi} güncellendi.')
