"""
Blog yazılarını veritabanına ekler (get_or_create, güvenli tekrar çalıştırma).
Kullanım: python blog_yazilari_ekle.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import BlogYazisi
from stadt.models import Eyalet

yazar = User.objects.filter(is_superuser=True).first()
rlp = Eyalet.objects.get(slug='rlp')

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
    {
        'baslik': 'RLP\'de Hemşirelik Denkliği: Bilmeniz Gereken Her Şey',
        'slug': 'rlpde-hemsirelik-denkligi-rehberi',
        'kapak_resmi': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&q=80',
        'scope': 'eyalet',
        'ozet': "Türkiye'de hemşire oldunuz, Rheinland-Pfalz'da çalışmak istiyorsunuz. Denklik başvurusu nereye yapılır, hangi belgeler gerekir, stratejik kısayollar nelerdir? İşte eksiksiz rehber.",
        'icerik': '''
<p class="lead">Türkiye'de hemşirelik diploması aldınız. Şimdi Rheinland-Pfalz'da çalışmak istiyorsunuz. Bunun için denklik (Anerkennung) almanız şart. Ama süreç sadece diploma göndermekten ibaret değil. Bilmeniz gereken önemli detaylar var.</p>

<h4>1. Başvuru Nereye Yapılır?</h4>

<p>RLP'de hemşirelik denkliği için tek yetkili kurum Landau'daki <strong>Landesamt für Soziales, Jugend und Versorgung</strong>'dur. Başvuru online değil, posta ile yapılıyor. Resmi formu doldurup ıslak imzanızla birlikte belgelerinizi kuruma göndermeniz gerekiyor.</p>

<p>Önemli bir nokta: kurum dosyayı ancak belgeler eksiksizse incelemeye alıyor. Eksik evrakla göndermek süreci uzatır. Bu yüzden göndermeden önce güvendiğiniz bir kurumla ön kontrol yaptırmanızı öneririz.</p>

<h4>Resmi Başvuru Formu</h4>

<p>Başvuruda kullanmanız gereken resmi form aşağıda görüntülenebilir. Formu indirip doldurun, ıslak imzayla birlikte evraklarınızla posta yoluyla gönderin.</p>

<div class="mb-2">
  <a href="https://lsjv.rlp.de/fileadmin/lsjv/Themen/Gesundheit/Gesundheitsberufe/NA-Heilberufe/AB_Antrag_GB_Pflege.pdf"
     target="_blank" rel="noopener" class="btn btn-primary btn-sm">
    <i class="bi bi-download me-1"></i>Formu İndir (PDF)
  </a>
</div>

<div class="mb-4">
  <iframe
    src="https://docs.google.com/viewer?url=https://lsjv.rlp.de/fileadmin/lsjv/Themen/Gesundheit/Gesundheitsberufe/NA-Heilberufe/AB_Antrag_GB_Pflege.pdf&embedded=true"
    style="width:100%;height:420px;border:1px solid #dee2e6;border-radius:6px"
    allowfullscreen>
  </iframe>
</div>

<h4>2. Gerekli Belgeler</h4>

<ul>
  <li><strong>Kimlik / Pasaport:</strong> Basit fotokopi yeterli.</li>
  <li><strong>Diploma ve Sağlık Bakanlığı Tescili:</strong> Diplomanızın ve Türkiye Sağlık Bakanlığı tescilinin (genellikle diplomanın arkasındaki kaşe) orijinal fotokopisi ve Almanca çevirisi.</li>
  <li><strong>Transkript ve Müfredat:</strong> Okulunuzdan alacağınız; derslerin, ders saatlerinin ve klinik stajların teorik/pratik içeriklerini gösteren detaylı döküm. Orijinal fotokopi ve Almanca çevirisiyle birlikte.</li>
  <li><strong>Çalışma Belgesi ve CV:</strong> Son 5 yılda en az 2 yıl çalıştıysanız nitelikli hizmet belgeniz ve mesleki deneyimlerinizi gösteren tablo şeklinde CV.</li>
</ul>

<div class="info-box">
  <strong>⚠️ Çeviriler Hakkında</strong><br>
  Tüm belgeler yeminli tercüman tarafından çevrilmek zorunda. Almanya'daki yeminli tercümanlara
  <a href="http://www.justiz-dolmetscher.de" target="_blank" rel="noopener">www.justiz-dolmetscher.de</a>
  adresinden ulaşabilirsiniz.
</div>

<h4>3. Maliyetler ve Maddi Destek</h4>

<p>Eyalet Ofisi'nin dosya inceleme harcı <strong>50€ ile 300€</strong> arasında. Ama asıl maliyet buradan gelmiyor. Yüzlerce sayfalık hemşirelik müfredatının yeminli çevirisi çok daha yüksek bir fatura çıkarabiliyor.</p>

<p>Neyse ki bu masraflar için <strong>Anerkennungszuschuss (Denklik Ödeneği)</strong> adında bir destek var. Başvuru detaylarına şuradan ulaşabilirsiniz:<br>
<a href="https://www.anerkennung-in-deutschland.de/html/de/pro/anerkennungszuschuss.php" target="_blank" rel="noopener">anerkennung-in-deutschland.de — Anerkennungszuschuss</a></p>

<div class="info-box">
  <strong>🚨 Kritik Kural</strong><br>
  Destek başvurusunu tercümanla anlaşmadan ve resmi başvuruyu yapmadan <strong>ÖNCE</strong> tamamlamak zorundasınız. Geriye dönük ödeme yapılmıyor.
</div>

<h4>4. Stratejik Kısayol: Eşdeğerlik İncelemesinden Feragat</h4>

<p>Türkiye eğitimi incelendiğinde büyük ihtimalle "kısmen tanınır" sonucu çıkıyor. AB standartlarıyla fark özellikle yaşlı bakımı ve psikiyatri staj saatlerinde oluşuyor. Bu durumda sizden uyum kursu veya sınav isteniyor.</p>

<p>Eğer saatlerinizin uyuşmadığını baştan biliyorsanız akıllı bir seçenek var: başvuru formunda <strong>eşdeğerlik incelemesinden (Gleichwertigkeitsprüfung) feragat edip doğrudan bilgi sınavına veya uyum kursuna girmeyi talep edebilirsiniz.</strong></p>

<p>Bu sayede yüzlerce sayfalık müfredat çevirisi yaptırmanıza gerek kalmıyor. Hem para hem zaman kazanıyorsunuz.</p>

<h4>5. Denklik Gelse de Yetmez: 3 Eksik Parça</h4>

<p>Diploma onayınız gelse bile çalışma ruhsatını (Berufserlaubnis/Urkunde) alabilmek için şu üç şart daha gerekiyor:</p>

<ol class="blog-steps">
  <li>
    <strong>B2 Seviye Almanca</strong><br>
    Resmi ve tanınmış bir B2 dil sertifikası olmadan çalışamazsınız. Goethe, Telc veya ÖSD sertifikaları kabul ediliyor.
  </li>
  <li>
    <strong>Sağlık Raporu</strong><br>
    Mesleği yapmaya bedensel ve ruhsal olarak uygun olduğunuzu gösteren güncel doktor raporu.
  </li>
  <li>
    <strong>Adli Sicil Kaydı</strong><br>
    Hem Türkiye'den hem de Almanya'dan temiz sabıka kaydı gerekiyor.
  </li>
</ol>

<div class="info-box mt-4">
  <strong>🔗 Faydalı Linkler</strong><br>
  <a href="http://www.justiz-dolmetscher.de" target="_blank" rel="noopener">Almanya Yeminli Tercümanlar — justiz-dolmetscher.de</a><br>
  <a href="https://www.anerkennung-in-deutschland.de/html/de/pro/anerkennungszuschuss.php" target="_blank" rel="noopener">Denklik Ödeneği Başvurusu — anerkennung-in-deutschland.de</a>
</div>
'''.strip(),
    },
    {
        'baslik': 'Karfreitag Nedir? Almanya\'da Sessiz Cuma\'nın Anlamı ve Kuralları',
        'slug': 'karfreitag-nedir-almanyada-sessiz-cuma',
        'kapak_resmi': 'https://images.unsplash.com/photo-1455849318743-b2233052fcff?w=1200&q=80',
        'ozet': "Karfreitag (Kutsal Cuma), Almanya'nın en sessiz resmi tatilidir. Müzik yasağı, kapalı dükkanlar ve eyaletten eyalete değişen kurallarla birlikte bu günü nasıl geçirmelisiniz?",
        'icerik': '''
<p class="lead">Almanya'da yaşıyorsanız ya da Paskalya döneminde buradaysanız, Karfreitag'ı (Kutsal Cuma / Kara Cuma) mutlaka duymuşsunuzdur. Bu gün yalnızca bir resmi tatil değil; Almanya'nın en katı sessizlik kurallarının uygulandığı, alışılageldik hayatın durduğu özel bir gündür.</p>

<h3>📅 Karfreitag Ne Zaman?</h3>
<p>Karfreitag, Paskalya Pazarı'ndan (Ostersonntag) iki gün önce, Cuma günü kutlanır. Tarihi her yıl değişir; genellikle Mart sonu ile Nisan ortası arasında gelir.</p>

<h3>✝️ Karfreitag Neden Bu Kadar Önemli?</h3>
<p>Hristiyan inancına göre İsa'nın çarmıha gerildiği gündür. Bu nedenle Almanya'da Karfreitag, <strong>"Stiller Feiertag"</strong> (Sessiz Bayram) olarak tanımlanır. Eğlence yasaklanır, yas tutulur, toplumsal sessizliğe saygı gösterilmesi beklenir.</p>

<h3>🚫 Karfreitag'da Neler Yasak?</h3>
<p>Kurallar eyaletten eyalete farklılık gösterse de genel olarak şunlar geçerlidir:</p>
<ul>
<li><strong>Müzik yasağı:</strong> Diskotekler, barlar ve halka açık alanlarda dans müziği çalmak yasaktır. Canlı müzik etkinlikleri ve konserler büyük ölçüde iptal edilir.</li>
<li><strong>Dans etkinlikleri yasağı:</strong> Çoğu eyalette gece kulüpleri Karfreitag'da kapalı olmak zorundadır.</li>
<li><strong>Spor etkinlikleri kısıtlıdır:</strong> Futbol maçları ve büyük organizasyonlar genellikle bu güne planlanmaz.</li>
<li><strong>Dükkanlar kapalı:</strong> Süpermarketler ve mağazalar tüm Almanya'da kapalıdır.</li>
</ul>

<div class="info-box">
<strong>⚠️ Eyalete Göre Farklılıklar</strong><br>
Bayern (Bavyera) ve Baden-Württemberg gibi muhafazakâr eyaletlerde kurallar çok daha katıdır. Berlin gibi laik eyaletlerde ise bazı istisnalar tanınabilir.
</div>

<h3>✅ Karfreitag'da Neler Yapılabilir?</h3>
<ul>
<li>Kilise ayinlerine katılabilirsiniz — pek çok kilisede özel Karfreitag törenleri düzenlenir.</li>
<li>Doğa yürüyüşleri ve parklar serbesttir.</li>
<li>Restoranlar genellikle açıktır (müzik olmadan).</li>
<li>Toplu taşıma çalışır, ancak seferler azaltılmış olabilir.</li>
</ul>

<h3>🛒 Alışveriş Planı Yapın</h3>
<p>Karfreitag'dan bir gün önce, Perşembe akşamı, tüm ihtiyaçlarınızı karşıladığınızdan emin olun. Süpermarketler, eczaneler ve çoğu hizmet noktası Cuma günü kapalı olacaktır.</p>

<h3>🗓️ Paskalya Haftası Takvimi</h3>
<ul>
<li><strong>Gründonnerstag (Kutsal Perşembe):</strong> Son akşam yemeğini simgeler, bazı eyaletlerde yarı resmi tatil.</li>
<li><strong>Karfreitag (Kara Cuma):</strong> Resmi sessiz tatil — yasaklar geçerli.</li>
<li><strong>Karsamstag (Kutsal Cumartesi):</strong> Hazırlık günü, dükkanlar öğlene kadar açık olabilir.</li>
<li><strong>Ostersonntag (Paskalya Pazarı):</strong> Kutlama günü.</li>
<li><strong>Ostermontag (Paskalya Pazartesi):</strong> Resmi tatil, çoğu işyeri kapalı.</li>
</ul>

<div class="info-box mt-4">
<strong>💡 Kısaca</strong><br>
Karfreitag Almanya'nın en sessiz günüdür. Alışverişinizi önceden yapın, eğlence planı yapmayın ve sessizliğe saygı gösterin. Özellikle Bayern ve Baden-Württemberg'deyseniz kurallar çok daha katı uygulanır.
</div>
'''.strip(),
    },
    {
        'baslik': 'WBS Nedir? Almanya\'da Sosyal Konut Hakkı (Wohnberechtigungsschein) Rehberi',
        'slug': 'wbs-nedir-almanyada-sosyal-konut-hakki-rehberi',
        'kapak_resmi': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&q=80',
        'ozet': "WBS (Wohnberechtigungsschein), Almanya'da düşük gelirli hanelerin sosyal konutlara başvurmasını sağlayan belgedir. Kim alabilir, nasıl başvurulur, hangi avantajlar sağlar?",
        'icerik': '''
<p class="lead">Almanya'da kira fiyatları her yıl artarken, sosyal konut sistemi düşük ve orta gelirli haneler için önemli bir güvence sunuyor. Bu sistemin anahtarı ise <strong>WBS — Wohnberechtigungsschein</strong> (Konut Hakkı Belgesi).</p>

<h3>📄 WBS Nedir?</h3>
<p>WBS, devlet destekli sosyal konutlara (Sozialwohnungen) başvurabilmek için gerekli resmi belgedir. Bu belgeye sahip olanlar, piyasa fiyatının çok altında kira ödeyen sübvansiyonlu dairelere başvurabilir.</p>

<h3>👥 Kim WBS Alabilir?</h3>
<p>WBS gelir sınırına göre verilir. Hanenizdeki kişi sayısına bağlı olarak belirli bir yıllık net gelir eşiğini aşmamanız gerekir. Eyalete göre farklılık gösterse de genel eşikler şöyle:</p>
<ul>
<li><strong>1 kişilik hane:</strong> ~12.000 € / yıl net gelir</li>
<li><strong>2 kişilik hane:</strong> ~18.000 € / yıl</li>
<li><strong>Her ek kişi için:</strong> ~4.100 € eklenir</li>
<li><strong>Her çocuk için:</strong> ek muafiyet tanınır</li>
</ul>

<div class="info-box">
<strong>⚠️ Eyalete Göre Eşikler Farklıdır</strong><br>
Berlin, Hamburg ve Münih gibi büyük şehirlerde gelir eşikleri daha yüksek tutulmuştur. Başvurmadan önce bulunduğunuz eyaletin güncel rakamlarını kontrol edin.
</div>

<h3>📋 Başvuru İçin Gerekli Belgeler</h3>
<ul>
<li>Kimlik veya pasaport</li>
<li>İkamet tescili (Anmeldebestätigung)</li>
<li>Son 3 aylık maaş bordrosu veya gelir belgesi</li>
<li>Hane halkı beyanı (kimlerle yaşadığınızı gösterir)</li>
<li>Oturma izni / Niederlassungserlaubnis (yabancı uyrukluysanız)</li>
</ul>

<h3>🏢 Nereye Başvurulur?</h3>
<p>Başvuru, ikamet ettiğiniz şehrin <strong>Wohnungsamt</strong>'ına (Konut Dairesi) ya da ilgili sosyal hizmetler birimine yapılır. Büyük şehirlerin çoğunda online başvuru da mümkündür.</p>

<h3>⏳ Geçerlilik Süresi</h3>
<p>WBS belgesi genellikle <strong>1 yıl geçerlidir</strong>. Bu süre içinde uygun bir sosyal konut bulamazsanız belgenizi yeniletmeniz gerekir.</p>

<h3>🏠 WBS ile Konut Nasıl Bulunur?</h3>
<ul>
<li>Belediyenin konut listelerini takip edin.</li>
<li>Konut kooperatifleri (Wohnungsbaugesellschaften) genellikle WBS sahiplerine öncelik tanır.</li>
<li><strong>Özel ilanlar:</strong> Bazı ev sahipleri de WBS kabul eden dairelerini Immoscout24, Wohnungsboerse gibi platformlarda yayınlar — filtrelerden "WBS erforderlich" seçeneğini kullanabilirsiniz.</li>
</ul>

<h3>💡 WBS'nin Avantajları</h3>
<ul>
<li>Piyasa kirasının <strong>%30-50 altında</strong> kira ödeyebilirsiniz.</li>
<li>Uzun vadeli kira güvencesi sunar.</li>
<li>Aile ve çocuk sahiplerine ek puan verilir, öncelik tanınır.</li>
</ul>

<div class="info-box mt-4">
<strong>💡 Kısaca</strong><br>
WBS, Almanya'da düşük ve orta gelirli hanelerin uygun fiyatlı konuta erişmesini sağlayan önemli bir belgedir. Gelir sınırını karşılıyorsanız kesinlikle başvurun — özellikle büyük şehirlerde kira yükünü ciddi ölçüde azaltabilir.
</div>
'''.strip(),
    },
]

eklendi = guncellendi = 0
for d in YAZILAR:
    scope = d.get('scope', 'genel')
    eyalet = rlp if scope == 'eyalet' else None
    _, created = BlogYazisi.objects.update_or_create(
        slug=d['slug'],
        defaults={**d, 'yazar': yazar, 'yayinda': True, 'scope': scope, 'eyalet': eyalet},
    )
    if created:
        eklendi += 1
        print(f'  ✓ Eklendi: {d["baslik"]}')
    else:
        guncellendi += 1
        print(f'  ↺ Güncellendi: {d["baslik"]}')

print(f'✅ {eklendi} eklendi, {guncellendi} güncellendi.')
