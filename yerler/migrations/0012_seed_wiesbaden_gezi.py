from django.db import migrations

YERLER = [
    {
        'ad': 'Wiesbaden Şehir Rehberi',
        'adres': 'Wiesbaden, Hessen',
        'aciklama': "Wiesbaden'e yeni taşınacaklar için pratik bir entegrasyon rehberi. Aristokrat şehrin bilinmeyenleri.",
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/MK_36878-82_Wiesbaden_vom_Neroberg.jpg/1920px-MK_36878-82_Wiesbaden_vom_Neroberg.jpg',
        'wikipedia_url': 'https://commons.wikimedia.org/w/index.php?curid=39507522',
        'icerik': """<p>Almanya'nın en şık eyalet başkentlerinden birine, Wiesbaden'e hoş geldiniz. Burası Mainz'ın o hareketli, öğrenci ruhlu dünyasından sadece bir köprü (Theodor-Heuss) uzaklıkta olsa da, nehri geçtiğiniz an hava değişir. Daha vakur, daha düzenli ve biraz daha "ağırbaşlı" bir şehre adım atarsınız.</p>

<h2>1. Şehrin "Altbau" Ruhunu Keşfetmek</h2>
<p>Wiesbaden, II. Dünya Savaşı'ndan mucizevi şekilde sağlam çıkan nadir şehirlerden. Bu da demek oluyor ki, Avrupa'nın o hayal ettiğiniz yüksek tavanlı, geniş pencereli ve tarih kokan Altbau dairelerinde yaşama ihtimaliniz burada çok yüksek.</p>
<div class="info-box"><strong>Tüyo:</strong> Ev ararken Dichterviertel (Şairler Semti) etiketine odaklanın. Sokak isimlerinin hepsi ünlü yazarlardan gelir ve şehrin en prestijli mimarisi buradadır.</div>

<h2>2. "Sıcak Su" Şehrin DNA'sıdır</h2>
<p>Eğer bir Wiesbadenliyseniz, musluğunuzdan akan suyun ötesinde, şehrin altında devasa bir termal ağ olduğunu bilirsiniz.</p>
<div class="info-box"><strong>Alışkanlık:</strong> Cumartesi sabahları merkeze indiğinizde Kochbrunnen meydanındaki o buharlar boşuna tütmez. Burası 66 derece sıcaklıkta mineral fışkıran bir kaynaktır. Wiesbadenliler burayı bir buluşma noktası olarak kullanır.</div>
<div class="info-box"><strong>Önemli:</strong> Eğer gerçek bir "yerel" gibi hissetmek istiyorsanız, kış aylarında Kaiser-Friedrich-Therme'ye gidip o tarihi Roma atmosferinde stres atmak ajandanızın bir parçası olmalı.</div>

<h2>3. Alışverişin ve Sosyalliğin Adresi: Wilhelmstraße</h2>
<p>Frankfurt'un Zeil caddesi ne kadar kaotikse, Wiesbaden'in Wilhelmstraße'si (yerel adıyla "Rue") o kadar zariftir. Burası sadece alışveriş yeri değil, "görünmek ve görmek" yeridir.</p>
<p>Bir Wiesbadener hafta sonu şık giyinir, Kurhaus'un önündeki parkta yürüyüş yapar ve ardından bu cadde üzerindeki kafelerde kahvesini içer. Buradaki yaşam temposu, Alman disiplini ile Akdeniz keyfinin bir karışımıdır.</p>

<h2>4. İş Dünyası: Takım Elbiseli Bir Şehir</h2>
<p>Wiesbaden bir memur ve beyaz yaka şehridir. Federal Kriminal Dairesi (BKA) ve dev sigorta şirketlerinin merkezi burada olduğu için sabah saatlerinde trenden inen binlerce takım elbiseli insan görmeniz normaldir.</p>
<div class="info-box"><strong>Kariyer Notu:</strong> Eğer bilişim, hukuk veya finans sektöründeyseniz, Wiesbaden size Frankfurt'un stresini yaşatmadan global kariyer imkanları sunar.</div>

<h2>5. Yerelin Sırrı: Neroberg</h2>
<p>Eski usul bir fünikülerle (Nerobergbahn) tepesine çıktığınız Neroberg, şehrin balkonudur.</p>
<p>Bir Wiesbadenli buraya sadece manzara için çıkmaz; oradaki Rus Ortodoks Kilisesi'nin altın kubbeleri altında yürüyüş yapar veya yazın ormandaki açık hava havuzunda (Opelbad) yüzer. Burası şehrin gürültüsünden kaçış biletidir.</p>

<h2>6. Ulaşım: Mainz ile Ezeli Rekabet</h2>
<p>Wiesbaden ve Mainz, Ren Nehri'nin iki yakasında birbirine baksa da aralarında tatlı bir rekabet vardır. Bir Wiesbadener için karşı kıyıya geçmek bazen "başka bir eyalete gitmek" (ki öyledir, RLP'den Hessen'e geçersiniz) demektir.</p>
<div class="info-box"><strong>Lojistik:</strong> Frankfurt Havalimanı'na S-Bahn ile sadece 35-40 dakikadasınız. Bu, dünyayla bağınızın hiç kopmaması demek.</div>

<p style="font-size:0.78rem; color:#888; margin-top:2rem;">
  <strong>Fotoğraf kaynağı:</strong> By Martin Kraft – Own work,
  <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener">CC BY-SA 3.0</a>,
  <a href="https://commons.wikimedia.org/w/index.php?curid=39507522" target="_blank" rel="noopener">Wikimedia Commons</a>
</p>""",
    },
    {
        'ad': 'Kurhaus Wiesbaden',
        'adres': 'Kurhausplatz 1, 65189 Wiesbaden',
        'aciklama': "Dostoyevski'nin ilham aldığı, 1907 yılında açılmış neoklasik başyapıt. Dünyanın en güzel kumarhanelerinden Casino Wiesbaden'e ev sahipliği yapar.",
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/8/85/Wiesbaden_BW_2017-04-24_20-51-36.jpg',
        'wikipedia_url': 'https://commons.wikimedia.org/wiki/User:Berthold_Werner',
        'icerik': """<p>Wiesbaden'e adım attığınızda, sizi selamlayan ilk ve en görkemli yapı şüphesiz Kurhaus'tur. 1907 yılında İmparator II. Wilhelm tarafından açılan bu bina, sadece bir "Kür Evi" değil, Avrupa aristokrasisinin, sanatçıların ve hatta imparatorların buluşma noktası olmuştur. Neoklasik mimarisi, devasa sütunları ve heybetli revaklarıyla Kurhaus, Wiesbaden'in lüks ve zarafet dolu geçmişinin yaşayan anıtıdır.</p>

<p>Ancak Kurhaus'un cazibesi sadece dış mimarisiyle sınırlı değildir. Asıl efsane, onun güney kanadında yer alan Casino Wiesbaden'dir. Burası, dünyanın en eski ve en güzel kumarhanelerinden biri kabul edilir.</p>

<h2>Kumarbaz'ın İlham Kaynağı</h2>
<p>Casino Wiesbaden'in halıları üzerinde yürürken, ayak seslerinizin edebiyat tarihine karıştığını hissedebilirsiniz. Ünlü Rus yazar Fyodor Dostoyevski, 19. yüzyılın ortalarında bu salonda defalarca rulet oynamış ve maalesef büyük miktarlarda para kaybetmiştir. İşte bu kayıpların ve yaşadığı o derin tutkunun meyvesi, dünya edebiyatının başyapıtlarından biri olan <em>Kumarbaz</em> romanıdır. Romanın geçtiği kurgusal şehir "Roulettenburg"un arkasında, Dostoyevski'nin Wiesbaden deneyimlerinin olduğu bilinir.</p>

<h2>Sadece Kumar Değil, Bir Deneyim</h2>
<p>Bugün, Casino Wiesbaden sadece şans oyunları meraklılarını değil, tarihi atmosferi solumak isteyenleri de ağırlıyor. Kristal avizeler, ahşap oymalar ve kadife süslemelerle dolu bu salonlara girmek için belirli bir giyim tarzına (ceket-kravat zorunluluğu gibi) uymak gerekiyor. Kumar oynamasanız bile, o tarihi atmosferi görmek, avizelerin ışıltısını hissetmek ve belki de Dostoyevski'nin oturduğu masanın yakınından geçmek, Wiesbaden gezinizin en unutulmaz anlarından biri olacaktır.</p>

<div class="info-box"><strong>Tüyo:</strong> Kurhaus'un hemen arkasındaki geniş parkta (Kurpark) yürüyüş yapın veya binanın önündeki meşhur sütunlu yolda (Kolonnade) fotoğraf çektirin — Wiesbadenli olmanın keyifli bir parçası.</div>""",
    },
    {
        'ad': 'Nerobergbahn',
        'adres': 'Nerotal 1, 65193 Wiesbaden',
        'aciklama': "1888'den beri su ve yerçekimiyle çalışan efsanevi füniküler. Neroberg tepesinden Wiesbaden ve Ren Vadisi'nin nefes kesen manzarası.",
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Wiesbaden_Nerobergbahn_2010-05-01_17.08.21.jpg/1280px-Wiesbaden_Nerobergbahn_2010-05-01_17.08.21.jpg',
        'wikipedia_url': 'https://commons.wikimedia.org/w/index.php?curid=46928652',
        'icerik': """<p>Günümüzde inovasyon dediğimizde aklımıza hemen mikroçipler, yapay zeka ve devasa bataryalar geliyor. Ancak bazen durup geriye bakmak, gerçek dehanın ne kadar zamansız olduğunu anlamamızı sağlar.</p>

<p>Mainz'ın hemen karşısında, Wiesbaden'ın kalbinde, 1888 yılından beri sessizce çalışan bir makine var: Nerobergbahn. Bu sadece bir ulaşım aracı değil; insan zekasının, doğanın kurallarıyla kurduğu en zarif ortaklıklardan biri.</p>

<h2>Su ve Yerçekiminin Kusursuz Dansı</h2>
<p>Nerobergbahn, dünyada hala orijinal su balastı (Wasserballast) sistemiyle çalışan nadir fünikülerlerden biridir.</p>

<div class="info-box"><strong>Yukarıdaki Vagon:</strong> Zirvedeki vagonun tankına yaklaşık 7.000 litreye kadar su doldurulur. Bu ekstra ağırlık, vagonu aşağı doğru çeken bir güç yaratır.</div>
<div class="info-box"><strong>Aşağıdaki Vagon:</strong> Çelik bir halatla üstteki vagona bağlı olan aşağıdaki hafif vagon, yerçekiminin üstteki vagonu aşağı çekmesiyle sessizce yukarı doğru süzülür.</div>
<div class="info-box"><strong>Döngü:</strong> Aşağı inen vagonun suyu boşaltılır, bir pompa yardımıyla tekrar zirveye basılır ve bu zarif dans yeniden başlar.</div>

<p>Bu, sürdürülebilirlik kelimesi icat edilmeden çok önce yaratılmış, sıfır emisyonlu bir başyapıttır.</p>

<h2>Zirvedeki Sığınak: Neroberg</h2>
<div class="info-box"><strong>Altın Kubbeler:</strong> Ağaçların arasından gökyüzüne uzanan Rus Ortodoks Kilisesi (Aziz Elizabeth Kilisesi), altın kubbeleriyle manzaraya bir ressamın fırça darbesi gibi oturur.</div>
<div class="info-box"><strong>Görüş Açısı:</strong> Opelbad'ın üzerinden Wiesbaden'a ve Ren Vadisi'ne baktığınızda, şehrin kaosu yerini sessiz bir düzene bırakır.</div>
<div class="info-box"><strong>Bağlar:</strong> Şehrin içindeki tek üzüm bağı olan Neroberg bağları, doğanın ve insan emeğinin ahengini fısıldar.</div>

<h2>Karmaşayı Reddetmek</h2>
<p>130 yılı aşkın süredir hiçbir dijital güncellemeye, yazılım yamasına veya yeni nesil bataryaya ihtiyaç duymadan aynı kusursuzlukla çalışıyor. Mükemmelliğe, eklenecek bir şey kalmadığında değil, çıkarılacak hiçbir şey kalmadığında ulaşılır.</p>

<p style="font-size:0.78rem; color:#888; margin-top:2rem;">
  <strong>Fotoğraf kaynağı:</strong> By Alexander Hoernigk – Own work,
  <a href="https://creativecommons.org/licenses/by-sa/4.0" target="_blank" rel="noopener">CC BY-SA 4.0</a>,
  <a href="https://commons.wikimedia.org/w/index.php?curid=46928652" target="_blank" rel="noopener">Wikimedia Commons</a>
</p>""",
    },
    {
        'ad': 'Schloss Biebrich',
        'adres': 'Rheingaustraße 182, 65203 Wiesbaden',
        'aciklama': "Nassau Dükleri'nin Ren kıyısındaki Barok sarayı. Statik ve akışkanın, taşın ve suyun 300 yıllık görkemli diyalogu.",
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/a/ab/Schloss_Biebrich_fg01.JPG',
        'wikipedia_url': 'https://commons.wikimedia.org/w/index.php?curid=1506358',
        'icerik': """<p>Bir yapıyı nereye inşa ettiğiniz, ne inşa ettiğinizden daha büyük bir mesaj verir.</p>

<p>Wiesbaden'daki Schloss Biebrich, sıradan bir tepeye veya ormanın derinliklerine saklanmamıştır. O, doğrudan Avrupa'nın en güçlü damarlarından birinin, Ren Nehri'nin tam kıyısına kurulmuştur. Bu bir tesadüf değil, stratejik bir güç gösterisidir.</p>

<h2>İktidarın Geometrisi</h2>
<p>Sarayın Ren Nehri'ne bakan o devasa, simetrik cephesini inceleyin. Barok mimari, estetik bir tercih olmaktan öte, insan aklının kaosa düzen getirme çabasıdır.</p>

<div class="info-box"><strong>Optik Hükümdarlık:</strong> Kusursuz simetri ve merkezdeki dairesel Rotunda, doğanın rastlantısallığına karşı "Burada kuralları insan aklı koyar" der.</div>
<div class="info-box"><strong>Ağ Üzerindeki Düğüm:</strong> 18. yüzyılda Ren Nehri, bugünün fiber optik kabloları gibi ana veri ve ticaret yoluydu. Saray, bu ağın tam üzerine yerleştirilmiş, geçen herkese gücünü yayınlayan devasa bir ana makine gibi işlev görür.</div>

<h2>Arka Bahçedeki Felsefi Evrim</h2>
<p>Ancak asıl deha, binanın arkasına geçtiğinizde başlar. Sarayın devasa parkı (Schlosspark), mimari bir zaman çizelgesidir.</p>
<p>Önceleri tıpkı bina gibi katı, geometrik ve simetrik bir Fransız bahçesi olarak tasarlanmıştı. Ancak zamanla, doğanın kıvrımlarına ve rastlantısallığına saygı duyan İngiliz peyzaj stiline evrildi. Bu geçiş, mutlak kontrolden (Fransız stili) esnek uyuma (İngiliz stili) doğru atılmış felsefi bir adımdır.</p>

<h2>Çıkarılacak Ders</h2>
<p>Schloss Biebrich bize şunu fısıldar: Gerçek kalıcılık, çevrenizdeki akışa (Ren Nehri) direnmekle değil, o akışın hemen kenarında kendi sağlam duruşunuzu (Barok cephe) inşa etmekle mümkündür. Sabitlik ve değişim. Taş ve su. Tasarlanmış en zarif çelişkilerden biri, Ren'in sularına bakarak 300 yıldır aynı mesajı veriyor.</p>

<p style="font-size:0.78rem; color:#888; margin-top:2rem;">
  <strong>Fotoğraf kaynağı:</strong> By Fritz Geller-Grimm – Own work,
  <a href="https://creativecommons.org/licenses/by-sa/2.5" target="_blank" rel="noopener">CC BY-SA 2.5</a>,
  <a href="https://commons.wikimedia.org/w/index.php?curid=1506358" target="_blank" rel="noopener">Wikimedia Commons</a>
</p>""",
    },
    {
        'ad': 'Hessisches Staatstheater Wiesbaden',
        'adres': 'Christian-Zais-Straße 3, 65189 Wiesbaden',
        'aciklama': "Fellner ve Helmer'in 1894'te inşa ettiği Neo-Barok başyapıt. Akustik mühendisliği ve sahneleme sanatının Wiesbaden'daki kusursuz buluşması.",
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/a/ac/Hessisches_Staatstheater_Wiesbaden_2024-10-05_01.jpg',
        'wikipedia_url': 'https://commons.wikimedia.org/w/index.php?curid=155231670',
        'icerik': """<p>Modern dünyada sanal gerçeklik başlıklarıyla veya algoritmalarla insanları başka dünyalara taşımaya çalışıyoruz. Ancak teknoloji ve insan doğasının en saf entegrasyonu, yüz yılı aşkın bir süre önce Wiesbaden'ın merkezinde, Kurhaus'un hemen yanına inşa edildi.</p>

<p>Hessisches Staatstheater bir bina değil, kusursuz bir empati motorudur.</p>

<h2>İllüzyonun Donanımı</h2>
<div class="info-box"><strong>Filtreleme Arayüzü (Foyer):</strong> O görkemli fuaye alanı, sadece beklemek için tasarlanmamıştır. Ziyaretçinin günlük hayatın sıradanlığından sıyrılıp, karşılaşacağı yeni gerçekliğe zihinsel olarak geçiş yapmasını sağlayan bir tampon bölgedir. Altın varaklar ve heykeller, zihni "olağanüstü" olana hazırlar.</div>
<div class="info-box"><strong>Akustik Odak:</strong> Oditoryumun şekli, sesin hiçbir elektronik müdahale olmadan, sadece fizik kurallarıyla en arka sıradaki izleyiciye bile aynı netlikte ulaşmasını sağlar. Bu, teknolojinin görünmez olduğu, saf bir mühendislik zaferidir.</div>

<h2>Boş Tuval ve Gerçekliği Bükmek</h2>
<p>Sahne, en ilkel ve en güçlü kullanıcı arayüzüdür. Üzerinde hiçbir şey yokken perde açıldığında o boşlukta bir evren yaratılır. Işık, ses ve insan hareketi kullanılarak seyircinin zihnine doğrudan bir yazılım yüklenir. Tiyatro, insan duygularını hacklemenin en zarif yoludur.</p>

<h2>Çıkarılacak Ders</h2>
<p>En güçlü tasarımlar, dikkati kendisine çekenler değil, içindeki hikayenin kusursuzca çalışması için görünmez bir platform sağlayanlardır. Yapının tüm o Barok ihtişamı, sadece ortadaki karanlık sahnenin gücünü artırmak için oradadır.</p>

<p style="font-size:0.78rem; color:#888; margin-top:2rem;">
  <strong>Fotoğraf kaynağı:</strong> Leonhard Lenz –
  <a href="https://creativecommons.org/publicdomain/zero/1.0/" target="_blank" rel="noopener">CC0 1.0 Public Domain</a>,
  <a href="https://commons.wikimedia.org/w/index.php?curid=155231670" target="_blank" rel="noopener">Wikimedia Commons</a>
</p>""",
    },
    {
        'ad': "Wiesbaden'da 24 Saat: Güç Noktaları Rotası",
        'adres': 'Wiesbaden, Hessen',
        'aciklama': "Neroberg'den Kurhaus'a, Schloss Biebrich'ten Staatstheater'a — sıradan bir gezi değil, şehrin mimari ve psikolojik güç noktalarını deşifre eden 24 saatlik bir rota.",
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Stadtschloss_Wiesbaden.jpg/1280px-Stadtschloss_Wiesbaden.jpg',
        'wikipedia_url': 'https://commons.wikimedia.org/w/index.php?curid=21806618',
        'icerik': """<p>Sıradan bir şehir rehberi size nereye gideceğinizi, ne yiyeceğinizi ve nerede fotoğraf çektireceğinizi söyler. Biz bunu yapmayacağız.</p>

<p>Wiesbaden, sadece şifalı suları ve tarihi binalarıyla değil; barındırdığı mühendislik, mimari ve psikolojik güç noktalarıyla kusursuz bir "sistemdir". Bu 24 saatlik rota, zihninizi yeniden kalibre edecek bir deşifre sürecidir.</p>

<h2>09:00 | Temel Fizik ve Saflık: Neroberg & Nerobergbahn</h2>
<p>Nerobergbahn'a bindiğinizde sadece bir tepeye çıkmazsınız; 1888'den beri değişmeyen, yerçekimi ve suyun kusursuz denkleminin içine girersiniz. Motor yok, elektrik yok, gürültü yok. Sadece saf, sürtünmesiz bir mantık var.</p>
<div class="info-box"><strong>Zihinsel İndirme:</strong> Hedefinize ulaşmak için doğanın (veya pazarın) kendi ivmesini nasıl kullanabileceğinizi düşünün.</div>

<h2>13:00 | Statik ve Akışkanın Çarpışması: Schloss Biebrich</h2>
<p>Biebrich Sarayı'nın önüne geçin ve nehre doğru bakın. Arkanızda değişime direnen Barok bir taş kütlesi (Saray), önünüzde asla durmayan acımasız bir zaman makinesi (Ren Nehri).</p>
<div class="info-box"><strong>Zihinsel İndirme:</strong> Kendi sarayınızı, değişimin en sert aktığı nehrin tam kenarına, ama kendi kurallarınızla inşa etmelisiniz.</div>

<h2>16:00 | Gizli Gücün Kaynağı: Kochbrunnen</h2>
<p>Şehrin merkezindeki Kochbrunnen'de kısa bir duraklama. Yerin 2000 metre altından 66°C sıcaklıkta yeryüzüne fışkıran bu su, şehrin "bataryasıdır".</p>
<div class="info-box"><strong>Zihinsel İndirme:</strong> Dışarıya sunduğunuz arayüz ne kadar zarif olursa olsun; sisteminizin derinliklerinde sizi besleyen o bitmek bilmez motivasyon kaynağını canlı tutun.</div>

<h2>19:00 | Gerçekliği Bükme Alanı: Hessisches Staatstheater</h2>
<p>Burası bir "Empati Motoru"dur. Işık ve ses frekanslarıyla, oturduğunuz koltukta kalp atışınız ve duygularınız başkaları tarafından yeniden kodlanır.</p>
<div class="info-box"><strong>Zihinsel İndirme:</strong> İnsanların zihnine girmek istiyorsanız, onlara içine girebilecekleri kusursuz bir kurgu, bir bağlam sunun.</div>

<h2>22:00 | Düzen ve Kaosun Sınır Noktası: Kurhaus</h2>
<p>Tarihi Casino'da günü tamamlıyoruz. Bina size "Her şey kontrol altında" der; ama içeride her şeyi şansa bırakırsınız. Dostoyevski'yi delirten, sistemi alt etme arzusudur.</p>
<div class="info-box"><strong>Zihinsel İndirme:</strong> Vizyoner lider, kaosu yok etmeye çalışan değil; o riski kendi kurduğu masada, kendi kurallarıyla oynayabilen kişidir.</div>

<h2>Gerçeklik Yeniden Kodlandı</h2>
<p>Bu 24 saatlik döngü; mekanik sadeliği, stratejik konumlandırmayı, içsel enerjiyi, empatik illüzyonu ve risk yönetimini fiziksel dünyada deneyimlemekti.</p>

<p style="font-size:0.78rem; color:#888; margin-top:2rem;">
  <strong>Fotoğraf kaynağı:</strong> By Martin Kraft – photo.martinkraft.com,
  <a href="https://creativecommons.org/licenses/by-sa/3.0" target="_blank" rel="noopener">CC BY-SA 3.0</a>,
  <a href="https://commons.wikimedia.org/w/index.php?curid=21806618" target="_blank" rel="noopener">Wikimedia Commons</a>
</p>""",
    },
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt = apps.get_model('stadt', 'Stadt')
    Yer = apps.get_model('yerler', 'Yer')
    YerKategori = apps.get_model('yerler', 'YerKategori')

    YerKategori.objects.get_or_create(
        slug='gezi',
        defaults={'ad': 'Gezi & Kültür', 'tur': 'yer', 'sira': 6}
    )

    try:
        eyalet = Eyalet.objects.get(kod='HE')
        wiesbaden = Stadt.objects.get(slug='wiesbaden')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return

    # Wiesbaden pasifse aktif yap
    if not wiesbaden.aktiv:
        wiesbaden.aktiv = True
        wiesbaden.save()

    for veri in YERLER:
        Yer.objects.get_or_create(
            ad=veri['ad'],
            stadt=wiesbaden,
            defaults={
                'eyalet': eyalet,
                'scope': 'stadt',
                'tur': 'yer',
                'kategori': 'gezi',
                'adres': veri['adres'],
                'sehir': 'Wiesbaden',
                'aciklama': veri['aciklama'],
                'kapak_resmi': veri['kapak_resmi'],
                'wikipedia_url': veri['wikipedia_url'],
                'icerik': veri['icerik'],
                'aktif': True,
            }
        )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = [v['ad'] for v in YERLER]
    Yer.objects.filter(ad__in=adlar).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0011_eyalet_fk'),
        ('stadt', '0010_seed_baskentler'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
