from django.db import migrations

RESMI_KURUM = [
    {'ad': 'Jobcenter Erfurt', 'adres': 'Magdeburger Allee 148, 99086 Erfurt', 'aciklama': 'Bürgergeld (sosyal yardım) ve uzun süreli işsizler için destek hizmetleri sunar.', 'website': 'https://www.jobcenter-ge.de/Jobcenter/Erfurt/', 'maps_url': 'https://maps.google.com/?q=Jobcenter+Erfurt'},
    {'ad': 'Ausländerbehörde Erfurt', 'adres': 'Bürgermeister-Wagner-Straße 1, 99084 Erfurt', 'aciklama': 'Oturma izni, çalışma izni ve yabancılar yasası ile ilgili tüm işlemler bu birimde yapılır.', 'website': 'https://www.erfurt.de/ef/de/service/buergerservice/auslaender-und-asyl/auslaenderbehoerde/index.html', 'maps_url': 'https://maps.google.com/?q=Ausländerbehörde+Erfurt'},
    {'ad': 'Bürgeramt Erfurt', 'adres': 'Bürgermeister-Wagner-Straße 1, 99084 Erfurt', 'aciklama': 'İkamet adresi kayıt (Anmeldung), pasaport ve kimlik kartı işlemleri için merkezi hizmet noktasıdır.', 'website': 'https://www.erfurt.de/ef/de/service/buergerservice/index.html', 'maps_url': 'https://maps.google.com/?q=Bürgeramt+Erfurt'},
    {'ad': 'Agentur für Arbeit Erfurt', 'adres': 'Max-Reger-Straße 1, 99096 Erfurt', 'aciklama': 'İş bulma, işsizlik parası (ALG I), mesleki eğitim ve kariyer danışmanlığı hizmetleri sunar.', 'website': 'https://www.arbeitsagentur.de/vor-ort/erfurt', 'maps_url': 'https://maps.google.com/?q=Agentur+für+Arbeit+Erfurt'},
    {'ad': 'Finanzamt Erfurt', 'adres': 'Ludwig-Erhard-Allee 9, 99086 Erfurt', 'aciklama': 'Vergi numarası (Steuer-ID), vergi beyannamesi ve diğer vergi işlemleri için yetkili kurumdur.', 'website': 'https://finanzamt.thueringen.de/erfurt', 'maps_url': 'https://maps.google.com/?q=Finanzamt+Erfurt'},
]

IBADET = [
    {'ad': 'DITIB Ulu Camii Erfurt', 'adres': 'Schmidtstedter Str. 34, 99084 Erfurt', 'aciklama': 'Erfurt\'taki DITIB\'e bağlı merkezi cami. Cuma namazı, Kuran kursları ve sosyal etkinlikler düzenlenmektedir.', 'website': 'https://www.ditib.de/', 'maps_url': 'https://maps.google.com/?q=DITIB+Ulu+Camii+Erfurt'},
    {'ad': 'Islamisches Zentrum (IQRA) Erfurt', 'adres': 'Stauffenbergallee 1, 99085 Erfurt', 'aciklama': 'Erfurt İslam Merkezi, ibadet ve kültürel faaliyetler için topluma hizmet vermektedir.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Islamisches+Zentrum+(IQRA)+Erfurt'},
    {'ad': 'VIKZ Moschee Erfurt', 'adres': 'Leipziger Str. 59, 99085 Erfurt', 'aciklama': 'İslam Kültür Merkezleri Birliği\'ne (VIKZ) bağlı cami ve eğitim merkezi.', 'website': '', 'maps_url': 'https://maps.google.com/?q=VIKZ+Moschee+Erfurt'},
]

TUV = [
    {'ad': 'TÜV Thüringen Service-Center Erfurt', 'adres': 'Haarbergstraße 61, 99097 Erfurt', 'aciklama': 'Araç muayenesi (HU/AU), ehliyet sınavları ve diğer teknik kontroller için ana merkez.', 'website': 'https://www.tuev-thueringen.de/', 'maps_url': 'https://maps.google.com/?q=TÜV+Thüringen+Service-Center+Erfurt'},
    {'ad': 'DEKRA Station Erfurt', 'adres': 'Am Urbicher Kreuz 22, 99099 Erfurt', 'aciklama': 'DEKRA\'nın araç muayene ve ekspertiz hizmetleri sunduğu Erfurt istasyonu.', 'website': 'https://www.dekra.de/de/standorte/erfurt/', 'maps_url': 'https://maps.google.com/?q=DEKRA+Station+Erfurt'},
]

SAGLIK = [
    {'ad': 'Helios Klinikum Erfurt', 'adres': 'Nordhäuser Str. 74, 99089 Erfurt', 'aciklama': 'Thüringen eyaletinin en büyük hastanelerinden biri. 24 saat acil servis ve tüm uzmanlık dallarında hizmet vermektedir.', 'website': 'https://www.helios-gesundheit.de/kliniken/erfurt/', 'maps_url': 'https://maps.google.com/?q=Helios+Klinikum+Erfurt'},
    {'ad': 'Katholisches Krankenhaus St. Johann Nepomuk', 'adres': 'Haarbergstraße 72, 99097 Erfurt', 'aciklama': 'Erfurt\'ta hizmet veren önemli bir hastane. Acil servis ve çeşitli tıbbi bölümleri bulunmaktadır.', 'website': 'https://www.kkh-erfurt.de/', 'maps_url': 'https://maps.google.com/?q=Katholisches+Krankenhaus+St.+Johann+Nepomuk+Erfurt'},
    {'ad': 'Kassenärztlicher Notdienst (116 117)', 'adres': 'Am Urbicher Kreuz 1, 99099 Erfurt', 'aciklama': 'Mesai saatleri dışında acil ancak hayati tehlike oluşturmayan durumlar için doktor nöbet hizmeti.', 'website': 'https://www.116117.de', 'maps_url': 'https://maps.google.com/?q=Kassenärztlicher+Notdienst+Erfurt'},
]

EGITIM = [
    {'ad': 'Volkshochschule (VHS) Erfurt', 'adres': 'Schottenstraße 7, 99084 Erfurt', 'aciklama': 'Almanca dil kursları (A1-C2), BAMF entegrasyon kursları ve çeşitli mesleki eğitimler sunan halk eğitim merkezi.', 'website': 'https://www.vhs-erfurt.de/', 'maps_url': 'https://maps.google.com/?q=Volkshochschule+VHS+Erfurt'},
    {'ad': 'Universität Erfurt', 'adres': 'Nordhäuser Str. 63, 99089 Erfurt', 'aciklama': 'Erfurt Üniversitesi, çeşitli lisans ve yüksek lisans programlarının yanı sıra uluslararası öğrenciler için dil kursları da sunmaktadır.', 'website': 'https://www.uni-erfurt.de/', 'maps_url': 'https://maps.google.com/?q=Universität+Erfurt'},
    {'ad': 'Caritasverband für das Bistum Erfurt e.V.', 'adres': 'Wilhelm-Külz-Straße 33, 99084 Erfurt', 'aciklama': 'Göçmenler için danışmanlık, sosyal yardım ve entegrasyon hizmetleri sunan bir yardım kuruluşudur.', 'website': 'https://www.caritas-bistum-erfurt.de/', 'maps_url': 'https://maps.google.com/?q=Caritasverband+für+das+Bistum+Erfurt'},
]

GEZI = [
    {
        'ad': 'Erfurter Dom (Mariendom)', 'adres': 'Domplatz, 99084 Erfurt', 'aciklama': 'Gotik mimarinin bir şaheseri olan ve şehrin siluetine hakim olan görkemli katedral.', 'website': 'https://www.dom-erfurt.de/', 'maps_url': 'https://maps.google.com/?q=Erfurter+Dom',
        'icerik': 'Erfurt Katedrali, ya da resmi adıyla Mariendom, şehrin en önemli simgesi ve Almanya\'nın en etkileyici dini yapılarından biridir. Domberg tepesinde, komşusu Severikirche ile birlikte muhteşem bir mimari ansambl oluşturan katedral, 742 yılına uzanan köklü bir tarihe sahiptir. Bugün gördüğümüz yapı, büyük ölçüde 12. ve 15. yüzyıllar arasında inşa edilmiş Gotik bir şaheserdir.\n\nKatedralin en dikkat çekici özelliklerinden biri, dünyanın en büyük serbest salınımlı ortaçağ çanı olan "Gloriosa"ya ev sahipliği yapmasıdır. 1497 yılında dökülen bu devasa çan, sadece özel günlerde çalınır ve sesi kilometrelerce uzaktan duyulabilir. Katedralin içi, "Wolfram" adı verilen bronz şamdan ve vitray pencereler gibi paha biçilmez sanat eserleriyle doludur.\n\nHer yıl yaz aylarında katedralin önündeki 70 basamaklık dev merdivenler, "DomStufen-Festspiele" adı verilen ünlü açık hava opera ve tiyatro festivali için doğal bir sahneye dönüşür. Bu etkinlik, hem yerel halkın hem de turistlerin büyük ilgisini çeker ve Erfurt\'un kültürel yaşamının zirve noktalarından birini oluşturur.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Erfurter_Dom', 'sira': 1,
    },
    {
        'ad': 'Krämerbrücke', 'adres': 'Krämerbrücke, 99084 Erfurt', 'aciklama': 'Üzerinde hala yaşamın devam ettiği, dükkanlar ve evlerle dolu Avrupa\'nın en uzun ve en ünlü köprüsü.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Krämerbrücke+Erfurt',
        'icerik': 'Krämerbrücke (Tüccarlar Köprüsü), Erfurt\'un en ikonik yapısı ve Floransa\'daki Ponte Vecchio ile birlikte Avrupa\'da üzerinde kesintisiz olarak binaların bulunduğu nadir köprülerden biridir. Gera nehrinin bir kolu olan Breitstrom üzerinde uzanan bu 120 metrelik taş köprü, 1325 yılında inşa edilmiştir ve bugün hala 32 adet yarı ahşap evin yanı sıra el sanatları dükkanlarına, galerilere ve kafelere ev sahipliği yapmaktadır.\n\nKöprünün tarihi, Orta Çağ ticaret yollarının kesişim noktasında bulunan Erfurt\'un zenginliğine dayanır. Başlangıçta baharat, değerli metaller ve ipek gibi lüks mallar satan tüccarların dükkanları burada yer alıyordu. Bugün ise bu tarihi dükkanlarda Thüringen\'e özgü mavi baskı kumaşlar, el yapımı seramikler, mücevherler ve yerel lezzetler bulabilirsiniz. Köprünün atmosferi, sizi adeta zamanda bir yolculuğa çıkarır.\n\nHer yıl Haziran ayında düzenlenen ve on binlerce ziyaretçiyi çeken "Krämerbrückenfest", köprünün ve çevresindeki eski şehrin Orta Çağ ruhunu canlandıran en büyük festivaldir. Müzik, dans, el sanatları pazarları ve tarihi kostümlü gösterilerle dolu bu festival, Erfurt\'u ziyaret etmek için en güzel zamanlardan biridir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Kr%C3%A4merbr%C3%BCcke', 'sira': 2,
    },
    {
        'ad': 'Zitadelle Petersberg', 'adres': 'Petersberg, 99084 Erfurt', 'aciklama': 'Şehre hakim bir tepede yer alan, Avrupa\'nın en büyük ve en iyi korunmuş barok şehir kalelerinden biri.', 'website': 'https://www.zitadelle-petersberg.de/', 'maps_url': 'https://maps.google.com/?q=Zitadelle+Petersberg+Erfurt',
        'icerik': 'Petersberg Kalesi, Erfurt\'un tarihi merkezine tepeden bakan, stratejik bir konumda inşa edilmiş devasa bir barok kaledir. 17. yüzyılda Mainz Elektörlüğü tarafından inşa edilen bu yıldız şeklindeki kale, Avrupa\'da türünün en büyük ve en iyi korunmuş örneklerinden biri olarak kabul edilir. Yüzyıllar boyunca askeri bir üs olarak hizmet vermiş, Napolyon savaşları ve Prusya dönemi gibi birçok tarihi olaya tanıklık etmiştir.\n\nGünümüzde kale, halka açık bir rekreasyon ve kültür alanıdır. Geniş avluları, tarihi binaları ve surları, ziyaretçilere hem tarih hem de muhteşem şehir manzaraları sunar. Kalenin altındaki gizemli dinleme koridorlarını (Horchgänge) rehberli bir turla keşfedebilir veya surlar boyunca yürüyerek Erfurt\'un ve çevresindeki Thüringen manzarasının tadını çıkarabilirsiniz.\n\nKalenin içinde ayrıca çeşitli sergiler, bir ziyaretçi merkezi ve restoranlar bulunmaktadır. Özellikle yaz aylarında düzenlenen etkinlikler, konserler ve festivallerle Petersberg Kalesi, şehrin en canlı noktalarından biri haline gelir. Katedralden kaleye çıkan panoramik asansör, tepeye ulaşımı oldukça kolaylaştırmaktadır.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Zitadelle_Petersberg', 'sira': 3,
    },
    {
        'ad': 'Augustinerkloster (Augustinian Manastırı)', 'adres': 'Augustinerstraße 10, 99084 Erfurt', 'aciklama': 'Reform hareketinin öncüsü Martin Luther\'in 1505-1511 yılları arasında bir keşiş olarak yaşadığı tarihi manastır.', 'website': 'https://www.augustinerkloster.de/', 'maps_url': 'https://maps.google.com/?q=Augustinerkloster+Erfurt',
        'icerik': 'Erfurt\'taki Augustinian Manastırı, sadece mimari güzelliğiyle değil, aynı zamanda dünya tarihini değiştiren bir isme ev sahipliği yapmasıyla da büyük bir öneme sahiptir: Martin Luther. Genç bir hukuk öğrencisi olan Luther, 1505 yılında yaşadığı bir aydınlanma sonrası bu manastıra katılmış ve 1511 yılına kadar burada bir keşiş olarak yaşamıştır. Protestan Reformu\'nun temellerini atan teolojik düşüncelerini büyük ölçüde burada geliştirmiştir.\n\nManastır, İkinci Dünya Savaşı\'nda ağır hasar görmüş olmasına rağmen aslına uygun olarak restore edilmiştir. Bugün ziyaretçiler, Luther\'in yaşadığı hücreyi, dua ettiği kiliseyi ve manastırın kütüphanesini görebilirler. Manastır içindeki "Lutherin Yolu" sergisi, onun Erfurt\'taki yaşamını ve düşünsel gelişimini etkileyici bir şekilde anlatır.\n\nAugustinerkloster, günümüzde sadece bir müze değil, aynı zamanda Protestan topluluğu için önemli bir buluşma, konferans ve konaklama merkezidir. Tarihi atmosferi, sessiz avluları ve etkileyici mimarisiyle manastır, Reformasyon tarihine ilgi duyan herkes için mutlaka görülmesi gereken bir yerdir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Augustinerkloster_(Erfurt)', 'sira': 4,
    },
    {
        'ad': 'Alte Synagoge (Eski Sinagog)', 'adres': 'Waagegasse 8, 99084 Erfurt', 'aciklama': 'Avrupa\'nın en eski ve en iyi korunmuş sinagoglarından biri, paha biçilmez "Erfurt Hazinesi"ne ev sahipliği yapıyor.', 'website': 'https://juedisches-leben.erfurt.de/jl/de/mittelalter/alte_synagoge/index.html', 'maps_url': 'https://maps.google.com/?q=Alte+Synagoge+Erfurt',
        'icerik': 'Erfurt\'un Eski Sinagogu, 11. yüzyıla tarihlenen ve Avrupa\'da temel duvarları bu kadar eski ve sağlam kalmış nadir sinagoglardan biridir. Tarihi şehir merkezinin ortasında, Krämerbrücke\'ye çok yakın bir konumda yer alan bu yapı, Erfurt\'un Orta Çağ\'daki zengin ve canlı Yahudi cemaatinin bir kanıtıdır. 1349\'daki veba salgını sırasında yaşanan bir katliamın ardından sinagog olarak kullanımı sona ermiş, depo ve hatta dans salonu olarak kullanıldığı için yıkımdan kurtulmuştur.\n\n1990\'larda yeniden keşfedilen ve titiz bir restorasyonun ardından 2009\'da müze olarak açılan sinagog, Erfurt\'un Yahudi tarihini gözler önüne serer. Müzenin en değerli parçası, 1998 yılında yapılan bir kazıda bulunan ve "Erfurt Hazinesi" olarak bilinen, 14. yüzyıldan kalma gümüş sikkeler, külçeler ve gotik tarzda yapılmış paha biçilmez bir Yahudi düğün yüzüğünden oluşan koleksiyondur.\n\nEski Sinagog, yakınındaki Orta Çağ Mikve\'si (ritüel banyosu) ve Taş Ev (Steinernes Haus) ile birlikte UNESCO Dünya Mirası Listesi\'nde yer almaktadır. Bu üç yapı, Orta Avrupa\'daki Aşkenaz Yahudi cemaatinin kültürel ve mimari mirasını anlamak için eşsiz bir fırsat sunar.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Alte_Synagoge_(Erfurt)', 'sira': 5,
    },
    {
        'ad': 'Fischmarkt', 'adres': 'Fischmarkt, 99084 Erfurt', 'aciklama': 'Tarihi Belediye Binası (Rathaus) ve zengin tüccar evleriyle çevrili, şehrin en canlı ve güzel meydanlarından biri.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Fischmarkt+Erfurt',
        'icerik': 'Fischmarkt (Balık Pazarı), Erfurt\'un tarihi kalbinin attığı en önemli meydanlardan biridir. Adını bir zamanlar burada kurulan balık pazarından alsa da, bugün meydan siyasi ve sosyal yaşamın merkezidir. Meydan, Rönesans ve Barok dönemlerinden kalma, cepheleri özenle süslenmiş birbirinden güzel binalarla çevrilidir.\n\nMeydana hakim olan en görkemli yapı, Neo-Gotik tarzda inşa edilmiş olan Erfurt Belediye Binası\'dır (Rathaus). Binanın içi, Erfurt ve Thüringen tarihinden sahneleri tasvir eden duvar resimleriyle süslüdür. Meydanın diğer önemli binaları arasında "Zum Breiten Herd" ve "Zum Roten Ochsen" gibi zengin tüccar evleri bulunur. Meydanın ortasındaki Roma tanrısı heykeli ise 1591 yılından kalmadır.\n\nFischmarkt, yıl boyunca çeşitli etkinliklere, pazarlara ve festivallere ev sahipliği yapar. Özellikle Noel zamanında kurulan pazar, meydanı masalsı bir atmosfere büründürür. Çevresindeki çok sayıda kafe ve restoranla Fischmarkt, şehri gezerken mola vermek ve Erfurt\'un canlı atmosferini hissetmek için mükemmel bir noktadır.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Fischmarkt_(Erfurt)', 'sira': 6,
    },
    {
        'ad': 'egapark', 'adres': 'Gothaer Str. 38, 99094 Erfurt', 'aciklama': 'Almanya\'nın en büyük ve en güzel bahçe ve rekreasyon parklarından biri, her yaştan ziyaretçi için aktiviteler sunar.', 'website': 'https://www.egapark-erfurt.de/', 'maps_url': 'https://maps.google.com/?q=egapark+Erfurt',
        'icerik': 'Egapark, 36 hektarlık devasa bir alana yayılan, Thüringen\'in en önemli bahçecilik ve rekreasyon parkıdır. 1961 yılında bir bahçecilik fuarı için kurulan park, o zamandan beri sürekli olarak geliştirilmiş ve bugün Almanya\'nın en güzel parklarından biri olarak kabul edilmektedir. Park, özellikle 2021 yılında düzenlenen Federal Bahçe Fuarı (BUGA) ile tamamen yenilenmiş ve modern bir görünüme kavuşmuştur.\n\nPark, Avrupa\'nın en büyük süs bitkisi yatağı, çeşitli tematik bahçeler, bir Japon bahçesi, bir gül bahçesi ve devasa seralar gibi birçok farklı bölümden oluşur. Özellikle tropik bitkilerin ve kelebeklerin bulunduğu Danakil çöl ve orman evi, ziyaretçilerin en çok ilgi gösterdiği yerlerdendir. Parkın ortasındaki gözlem kulesi, şehre ve parka kuşbakışı bakmak için harika bir fırsat sunar.\n\nÇocuklar için Almanya\'nın en büyük oyun alanı, bir çocuk çiftliği ve su oyun alanları gibi sayısız aktivite mevcuttur. Egapark, sadece bir botanik bahçesi değil, aynı zamanda konserler, festivaller ve eğitim programları ile dolu, tüm aile için tam günlük bir eğlence ve dinlenme merkezidir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Egapark', 'sira': 7,
    },
    {
        'ad': 'Thüringer Zoopark Erfurt', 'adres': 'Am Zoopark 1, 99087 Erfurt', 'aciklama': 'Geniş doğal yaşam alanları ve hayvan çeşitliliği ile Almanya\'nın üçüncü büyük hayvanat bahçesi.', 'website': 'https://www.zoopark-erfurt.de/', 'maps_url': 'https://maps.google.com/?q=Thüringer+Zoopark+Erfurt',
        'icerik': 'Thüringer Zoopark Erfurt, 63 hektarlık geniş bir alana yayılan ve Almanya\'nın en büyük üçüncü hayvanat bahçesidir. Şehrin kuzeyindeki Roter Berg tepesinde yer alan hayvanat bahçesi, hayvanlara geniş ve doğal yaşam alanlarına benzer ortamlar sunmasıyla öne çıkar. Bu sayede ziyaretçiler, hayvanları kafeslerin ardında değil, daha özgür bir şekilde gözlemleme imkanı bulur.\n\nHayvanat bahçesi, dünyanın dört bir yanından yaklaşık 1000 hayvana ev sahipliği yapmaktadır. Özellikle Afrika savanasını andıran geniş alanda serbestçe dolaşan zürafalar, zebralar ve antiloplar büyük ilgi çeker. Aslanlar, filler, gergedanlar ve lemurlar da parkın en popüler sakinleri arasındadır. Ayrıca, yerel ve nadir bulunan evcil hayvan türlerinin korunduğu bir çiftlik bölümü de bulunmaktadır.\n\nThüringer Zoopark, sadece bir eğlence mekanı değil, aynı zamanda türlerin korunması ve çevre eğitimi konularında da aktif bir rol oynar. Geniş oyun alanları, piknik yerleri ve bilgilendirici panolarıyla hayvanat bahçesi, özellikle çocuklu aileler için Erfurt\'ta harika bir gün geçirme alternatifidir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Th%C3%BCringer_Zoopark_Erfurt', 'sira': 8,
    },
    {
        'ad': 'Gedenk- und Bildungsstätte Andreasstraße', 'adres': 'Andreasstraße 37a, 99084 Erfurt', 'aciklama': 'Eski bir Doğu Almanya (DDR) gizli servisi (Stasi) hapishanesi olan ve bugün bir anma ve eğitim merkezine dönüştürülen etkileyici bir müze.', 'website': 'https://www.stiftung-ettersberg.de/andreasstrasse/', 'maps_url': 'https://maps.google.com/?q=Gedenk-+und+Bildungsstätte+Andreasstraße+Erfurt',
        'icerik': 'Andreasstraße Anma ve Eğitim Merkezi, Doğu Almanya\'nın (DDR) karanlık geçmişiyle yüzleşmek için Erfurt\'taki en önemli yerdir. Bu bina, 1952\'den 1989\'a kadar Devlet Güvenlik Bakanlığı (Stasi) tarafından bir gözaltı ve sorgu hapishanesi olarak kullanılmıştır. Binlerce rejim muhalifi, kaçma girişiminde bulunanlar ve "devlet düşmanı" olarak görülen insanlar burada insanlık dışı koşullarda tutulmuş ve sorgulanmıştır.\n\nBugün müze olarak hizmet veren binada, orijinal haliyle korunmuş hücreleri, sorgu odalarını ve tecrit alanlarını gezebilirsiniz. Müzenin kalıcı sergisi, tutukluların hikayelerini, Stasi\'nin acımasız yöntemlerini ve DDR\'deki baskı rejimini multimedya enstalasyonları ve kişisel tanıklıklarla etkileyici bir şekilde anlatır. Ziyaretçiler, totaliter bir devletin bireyler üzerindeki etkisini somut bir şekilde hisseder.\n\nBu merkez aynı zamanda 1989\'da Doğu Almanya\'daki barışçıl devrimin önemli bir sembolüdür. Erfurt halkı, Stasi binasını işgal eden ilk sivil gruplardan biri olmuş ve bu eylem, rejimin çöküşünü hızlandırmıştır. Andreasstraße, sadece bir anma yeri değil, aynı zamanda demokrasi, özgürlük ve insan haklarının önemini vurgulayan bir eğitim merkezidir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Gedenk-_und_Bildungsst%C3%A4tte_Andreasstra%C3%9Fe', 'sira': 9,
    },
    {
        'ad': 'Deutsches Gartenbaumuseum', 'adres': 'Gothaer Str. 50, 99094 Erfurt', 'aciklama': 'egapark içinde yer alan, Almanya\'nın bahçecilik ve peyzaj tarihine adanmış eşsiz bir müze.', 'website': 'https://www.gartenbaumuseum.de/', 'maps_url': 'https://maps.google.com/?q=Deutsches+Gartenbaumuseum+Erfurt',
        'icerik': 'Alman Bahçecilik Müzesi, egapark\'ın tarihi Cyriaksburg kalesinin içinde yer alan, türünün tek örneği bir müzedir. Erfurt, "Çiçek Şehri" olarak bilinir ve bu müze, şehrin bahçecilik ve peyzaj mimarisi alanındaki zengin geleneğini onurlandırır. Müze, bitkilerin insanlık tarihindeki rolünden modern bahçe tasarımına kadar geniş bir yelpazeyi kapsar.\n\nİnteraktif ve modern sergi tasarımı, ziyaretçilere bahçeciliğin bilimsel, kültürel ve sanatsal yönlerini eğlenceli bir şekilde sunar. Bitki genetiği, iklim değişikliğinin bahçeciliğe etkileri ve şehirde tarım gibi güncel konulara odaklanan bölümler özellikle ilgi çekicidir. Müze, sadece uzmanlara değil, aynı zamanda bahçeyle ilgilenen herkese hitap eder.\n\nKalenin tarihi atmosferi ile modern sergi konseptinin birleşimi, müzeye eşsiz bir karakter kazandırır. egapark ziyareti sırasında, bu müzeye de zaman ayırmak, Erfurt\'un neden "Çiçek Şehri" olarak anıldığını daha derinlemesine anlamanızı sağlayacaktır. Müze, hem yetişkinler hem de çocuklar için eğitici ve ilham verici bir deneyim sunar.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Deutsches_Gartenbaumuseum', 'sira': 10,
    },
]

ALISVERIS = [
    {'ad': 'Anger 1', 'adres': 'Anger 1, 99084 Erfurt', 'aciklama': 'Erfurt şehir merkezinin ana alışveriş caddesi Anger üzerinde bulunan en büyük ve en modern alışveriş merkezi.', 'website': 'https://www.anger1erfurt.de/', 'maps_url': 'https://maps.google.com/?q=Anger+1+Erfurt'},
    {'ad': 'Thüringen-Park', 'adres': 'Ermafa-Passage 1, 99091 Erfurt', 'aciklama': 'Şehrin kuzeyinde yer alan, 100\'den fazla mağaza ve büyük bir süpermarket içeren geniş bir alışveriş merkezi.', 'website': 'https://www.thuringen-park.de/', 'maps_url': 'https://maps.google.com/?q=Thüringen-Park+Erfurt'},
    {'ad': 'Sultan Supermarkt', 'adres': 'Magdeburger Allee 120, 99086 Erfurt', 'aciklama': 'Türk ve Orta Doğu ürünleri, helal et, taze sebze-meyve ve bakliyat çeşitleri sunan bir market.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Sultan+Supermarkt+Erfurt'},
    {'ad': 'Pamir Market', 'adres': 'Leipziger Str. 60, 99085 Erfurt', 'aciklama': 'Afgan, İran ve Doğu ürünleri bulabileceğiniz, helal kesim et ve çeşitli gıda malzemeleri sunan bir market.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Pamir+Market+Erfurt'},
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')
    try:
        eyalet = Eyalet.objects.get(kod='TH')
        sehir  = Stadt.objects.get(slug='erfurt')
    except (Eyalet.DoesNotExist, Stadt.DoesNotExist):
        return
    for kategori_slug, veriler in [
        ('resmi_kurum', RESMI_KURUM), ('ibadet', IBADET), ('tuv', TUV),
        ('saglik', SAGLIK), ('egitim', EGITIM), ('gezi', GEZI), ('alisveris', ALISVERIS),
    ]:
        for veri in veriler:
            Yer.objects.get_or_create(
                ad=veri['ad'], stadt=sehir,
                defaults={
                    'eyalet':      eyalet,
                    'scope':       'stadt',
                    'tur':         'yer',
                    'kategori':    kategori_slug,
                    'sehir':       'Erfurt',
                    'adres':       veri['adres'],
                    'aciklama':    veri['aciklama'],
                    'kapak_resmi': '',
                    'website':     veri.get('website', ''),
                    'maps_url':    veri.get('maps_url', ''),
                    'icerik':      veri.get('icerik', ''),
                    'wikipedia_url': veri.get('wikipedia_url', ''),
                    'sira':        veri.get('sira', 0),
                    'aktif':       True,
                }
            )


def unseed(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    adlar = [v['ad'] for liste in [RESMI_KURUM, IBADET, TUV, SAGLIK, EGITIM, GEZI, ALISVERIS] for v in liste]
    Yer.objects.filter(ad__in=adlar, sehir='Erfurt').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0019_seed_wiesbaden_yerler'),
        ('stadt',  '0045_erfurt_aktiv'),
    ]
    operations = [migrations.RunPython(seed, unseed)]