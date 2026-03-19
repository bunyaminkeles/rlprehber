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
        'baslik': 'Mainz Dom: Bin Yıllık Tarihin Kalbi',
        'slug': 'mainz-dom-bin-yillik-tarihin-kalbi',
        'kapak_resmi': 'https://images.unsplash.com/photo-1577083553180-732d8b4f51aa?w=1200&q=80',
        'ozet': "Mainz'in simgesi, Kutsal Roma İmparatorluğu'nun taç giyme kilisesi: Dom'un 1000 yıllık hikayesi.",
        'icerik': '''
<p>Mainz Dom, Almanya'nın en önemli Romanesk katedrali olarak yaklaşık bin yıldır şehrin kalbinde yükselmektedir. 975 yılında temeli atılan bu muhteşem yapı, Kutsal Roma İmparatorluğu döneminde taç giyme törenleri ve önemli dini ayinlerin merkezi olmuştur.</p>

<img src="https://images.unsplash.com/photo-1577083553180-732d8b4f51aa?w=900&q=80" class="img-fluid rounded my-4" alt="Mainz Dom dış görünüş">

<h4>Mimari Özellikleri</h4>
<p>Dom, altı kulesi ve kırmızı kumtaşından inşa edilmiş görkemli cephesiyle Mainz silüetine hakim olmaktadır. İç mekanda Gotik, Barok ve Romanesk unsurların bir arada bulunması, katedrali adeta bir mimari müzeye dönüştürmektedir.</p>

<div class="info-box">
  <strong>📍 Ziyaret Bilgileri</strong><br>
  Adres: Domstraße, 55116 Mainz<br>
  Giriş: Ücretsiz<br>
  Açık: Her gün 09:00–18:30 (mevsime göre değişir)
</div>

<h4>Tarihsel Önemi</h4>
<p>Dom, yüzyıllar boyunca Mainz Başpiskoposlarının merkezi olmuş; şehrin siyasi ve dini yaşamını şekillendirmiştir. Bugün hâlâ aktif bir kilise olarak hizmet vermekte, aynı zamanda turistlere ve sanatseverlere kapılarını açmaktadır.</p>
'''.strip(),
    },
    {
        'baslik': 'Gutenberg Müzesi: Matbaanın Doğduğu Yer',
        'slug': 'gutenberg-muzesi-matbaanin-dogdugu-yer',
        'kapak_resmi': 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=1200&q=80',
        'ozet': 'Johannes Gutenberg\'in matbaayı icat ettiği şehirde, bu devrimi anlatan dünyaca ünlü müze.',
        'icerik': '''
<p>Mainz, matbaanın mucidi Johannes Gutenberg'in doğduğu ve eserini yarattığı şehirdir. 1900 yılında açılan Gutenberg Müzesi, dünya genelinde baskı ve iletişim tarihinin en önemli koleksiyonlarından birine ev sahipliği yapmaktadır.</p>

<img src="https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=900&q=80" class="img-fluid rounded my-4" alt="Eski kitaplar ve matbaa">

<h4>Müzenin Yıldızı: 42 Satırlı İncil</h4>
<p>Müzenin en değerli eseri, Gutenberg'in yaklaşık 1455 yılında bastığı <em>Gutenberg İncili</em>'dir. Dünyada yalnızca 49 tam nüshası kalan bu incillerden ikisi burada sergilenmekte; özel bir hazinede korunarak ziyaretçilere sunulmaktadır.</p>

<div class="info-box">
  <strong>📍 Ziyaret Bilgileri</strong><br>
  Adres: Liebfrauenplatz 5, 55116 Mainz<br>
  Giriş: 5 € (indirimli 3 €)<br>
  Kapalı: Pazartesi
</div>

<h4>Interaktif Deneyim</h4>
<p>Müzede ziyaretçiler, Gutenberg dönemine ait çalışır durumdaki matbaa makinelerini yakından inceleyebilir ve baskı atölyelerinde deneyim kazanabilir. Çocuklar ve yetişkinler için düzenlenen atölye çalışmaları müzeyi daha da özel kılmaktadır.</p>
'''.strip(),
    },
    {
        'baslik': "Ren Nehri Yürüyüş Yolu: Mainz'in Mavi Şeridi",
        'slug': 'ren-nehri-yuruyus-yolu-mainzin-mavi-seridi',
        'kapak_resmi': 'https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=1200&q=80',
        'ozet': "Mainz'den Ren boyunca uzanan yürüyüş ve bisiklet rotası — şehrin en güzel kaçış noktası.",
        'icerik': '''
<p>Mainz'in batı sınırını çizen Ren Nehri, şehir sakinleri için eşsiz bir doğa ve dinlenme alanı sunar. Nehir boyunca uzanan yürüyüş yolları, bisiklet parkurları ve piknik alanlarıyla Rheinufer, dört mevsim yoğun ilgi görür.</p>

<img src="https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=900&q=80" class="img-fluid rounded my-4" alt="Ren Nehri kıyısı">

<h4>Popüler Rotalar</h4>
<p>Theodor-Heuss-Köprüsü'nden başlayarak güneye doğru uzanan sahil yolu, hem yürüyüş hem de bisiklet için idealdir. Akşam saatlerinde gün batımını izlemek için Winterhafen (Kış Limanı) bölgesi özellikle tercih edilmektedir.</p>

<div class="info-box">
  <strong>🚴 İpucu</strong><br>
  MVGmeinRad bisiklet paylaşım sistemiyle şehir merkezinden Rheinufer'e kolayca ulaşabilirsiniz. İlk 30 dakika ücretsizdir.
</div>

<h4>Etkinlikler ve Festival Alanı</h4>
<p>Yaz aylarında Mainzer Weinmarkt ve çeşitli açık hava festivalleri Ren kıyısında düzenlenir. Kış aylarında ise sis ve sakin bir nehir manzarası, fotoğraf tutkunları için ayrı bir atmosfer yaratır.</p>
'''.strip(),
    },
    {
        'baslik': 'Kurfürstliches Schloss: Barok İhtişamın Gözdesi',
        'slug': 'kurfurstliches-schloss-barok-ihtisamin-gozdesi',
        'kapak_resmi': 'https://images.unsplash.com/photo-1548013146-72479768bada?w=1200&q=80',
        'ozet': "Mainz Seçici Prensleri'nin sarayı — bugün Romalı-Germen Merkez Müzesi'ne ev sahipliği yapıyor.",
        'icerik': '''
<p>Ren Nehri kıyısında yükselen Kurfürstliches Schloss (Seçici Prens Sarayı), 18. yüzyılda Mainz Başpiskoposu ve Seçici Prensi adına inşa edilmiş görkemli bir Barok yapıdır. Bugün bu saray, Römisch-Germanisches Zentralmuseum'a (RGZM) ev sahipliği yapmaktadır.</p>

<img src="https://images.unsplash.com/photo-1548013146-72479768bada?w=900&q=80" class="img-fluid rounded my-4" alt="Barok saray mimarisi">

<h4>RGZM Koleksiyonu</h4>
<p>Roma-Germen Merkez Müzesi, Avrupa'nın prehistorik ve erken tarihsel dönemlerine ait 250.000'den fazla eseri bünyesinde barındırmaktadır. Müze aynı zamanda arkeolojik araştırma merkezi olarak da faaliyet göstermektedir.</p>

<div class="info-box">
  <strong>📍 Ziyaret Bilgileri</strong><br>
  Adres: Ernst-Ludwig-Platz 2, 55116 Mainz<br>
  Giriş: Ücretsiz<br>
  Kapalı: Pazartesi
</div>

<h4>Ren Kıyısındaki Konumu</h4>
<p>Sarayın önünden geçen Rheinufer yürüyüş yolu ve yakınındaki Eiserner Turm (Demir Kule) ile birlikte bu alan, Mainz'in en fotoğraflanmaya değer köşelerinden biri hâline gelmiştir.</p>
'''.strip(),
    },
    {
        'baslik': "St. Stephan Kilisesi: Chagall'ın Mavi Işığı",
        'slug': 'st-stephan-kilisesi-chagallin-mavi-isigi',
        'kapak_resmi': 'https://images.unsplash.com/photo-1519817650390-64a93db51149?w=1200&q=80',
        'ozet': "Marc Chagall'ın efsanevi mavi vitraylarıyla dünyaca tanınan Gotik kilise — barış ve uzlaşının sembolü.",
        'icerik': '''
<p>Mainz'in bir tepesinde konumlanan St. Stephan Kilisesi, Marc Chagall'ın tasarladığı mistik mavi vitraylarıyla dünyaca ünlüdür. Gotik mimarisiyle 14. yüzyılda inşa edilen kilise, 20. yüzyılın en etkileyici sanat eserlerinden birine ev sahipliği yapmaktadır.</p>

<img src="https://images.unsplash.com/photo-1519817650390-64a93db51149?w=900&q=80" class="img-fluid rounded my-4" alt="Mavi vitray ışığı">

<h4>Chagall'ın Barış Penceresi</h4>
<p>Holokost'tan sağ kurtulan Yahudi ressam Marc Chagall, 1978-1985 yılları arasında bu kilisenin pencerelerini Alman-Fransız ve Hristiyan-Yahudi uzlaşısının sembolü olarak tasarlamıştır. Kobalt mavisinin hâkim olduğu vitraylar, içeriye büyülü bir ışık atmosferi katmaktadır.</p>

<div class="info-box">
  <strong>📍 Ziyaret Bilgileri</strong><br>
  Adres: Kleine Weißgasse 12, 55116 Mainz<br>
  Giriş: Ücretsiz (bağış kutusu mevcut)<br>
  Açık: Pazartesi–Cumartesi 10:00–17:00, Pazar 12:00–17:00
</div>

<h4>Neden Ziyaret Edilmeli?</h4>
<p>Güneşli bir öğleden sonra kilisenin içinde vitraylardan süzülen mavi ışığı deneyimlemek, Mainz'deki en unutulmaz anlardan biri olacaktır. Az bilinen ama derinlemesine etkileyici bu mekan, şehrin gizli hazinelerinden biridir.</p>
'''.strip(),
    },
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
