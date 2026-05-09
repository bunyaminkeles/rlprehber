from django.db import migrations

RESMI_KURUM = [
    {'ad': 'Jobcenter Dresden', 'adres': 'Budapester Str. 30, 01069 Dresden', 'aciklama': 'Dresden\'de iş arayanlar ve sosyal yardım (Bürgergeld) için ana başvuru merkezi.', 'website': 'https://www.jobcenter-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Jobcenter+Dresden'},
    {'ad': 'Ausländerbehörde Dresden', 'adres': 'Theaterstraße 11, 01067 Dresden', 'aciklama': 'Oturma izni, aile birleşimi ve diğer yabancılar hukuku konuları için yetkili kurum.', 'website': 'https://www.dresden.de/de/leben/gesellschaft/migration/auslaenderbehoerde.php', 'maps_url': 'https://maps.google.com/?q=Ausländerbehörde+Dresden'},
    {'ad': 'Bürgeramt Dresden, Altstadt', 'adres': 'Theaterstraße 11, 01067 Dresden', 'aciklama': 'Adres kaydı (Anmeldung), kimlik ve pasaport işlemleri için merkezi vatandaşlık ofisi.', 'website': 'https://www.dresden.de/de/rathaus/dienstleistungen/buergerbuero_altstadt_d115.php', 'maps_url': 'https://maps.google.com/?q=Bürgerbüro+Dresden+Theaterstraße'},
    {'ad': 'Agentur für Arbeit Dresden', 'adres': 'Budapester Str. 30, 01069 Dresden', 'aciklama': 'İş bulma, kariyer danışmanlığı ve işsizlik parası (Arbeitslosengeld I) için federal iş bulma kurumu.', 'website': 'https://www.arbeitsagentur.de/vor-ort/dresden', 'maps_url': 'https://maps.google.com/?q=Agentur+für+Arbeit+Dresden'},
    {'ad': 'Finanzamt Dresden-Nord', 'adres': 'Rabenerstraße 1, 01069 Dresden', 'aciklama': 'Vergi beyannameleri, vergi kimlik numarası (Steuer-ID) ve diğer vergi konuları için yetkili vergi dairesi.', 'website': 'https://www.finanzamt.sachsen.de/dresden-nord-4141.html', 'maps_url': 'https://maps.google.com/?q=Finanzamt+Dresden-Nord'},
]

IBADET = [
    {'ad': 'DITIB Fatih Camii Dresden', 'adres': 'Hühndorfer Str. 16, 01157 Dresden', 'aciklama': 'DİTİB\'e bağlı, Dresden\'deki en büyük ve merkezi camilerden biri.', 'website': 'http://www.ditib-dresden.de/', 'maps_url': 'https://maps.google.com/?q=DITIB+Fatih+Camii+Dresden'},
    {'ad': 'Marwa Elsherbiny Kultur- und Bildungszentrum', 'adres': 'Marschnerstraße 2, 01307 Dresden', 'aciklama': 'IGMG\'ye bağlı, kültürel ve dini faaliyetler sunan bir merkez ve cami.', 'website': 'https://mkbzd.de/', 'maps_url': 'https://maps.google.com/?q=Marwa+Elsherbiny+Kultur-+und+Bildungszentrum+Dresden'},
    {'ad': 'Al-Mostafa Moschee', 'adres': 'Wallstraße 1, 01067 Dresden', 'aciklama': 'Dresden merkezine yakın, farklı milletlerden Müslümanların buluştuğu bir ibadet yeri.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Al-Mostafa+Moschee+Dresden'},
]

TUV = [
    {'ad': 'TÜV SÜD Service-Center Dresden-Kaditz', 'adres': 'Kötzschenbroder Str. 129, 01139 Dresden', 'aciklama': 'Araç muayenesi (HU/AU) ve diğer teknik kontroller için TÜV SÜD merkezi.', 'website': 'https://www.tuvsud.com/de-de/store-finder/dresden-kaditz', 'maps_url': 'https://maps.google.com/?q=TÜV+SÜD+Service-Center+Dresden-Kaditz'},
    {'ad': 'TÜV SÜD Service-Center Dresden-Reick', 'adres': 'Hülßestraße 1, 01237 Dresden', 'aciklama': 'Dresden\'in güneyinde bulunan, araç muayenesi ve ehliyet hizmetleri sunan TÜV SÜD şubesi.', 'website': 'https://www.tuvsud.com/de-de/store-finder/dresden-reick', 'maps_url': 'https://maps.google.com/?q=TÜV+SÜD+Service-Center+Dresden-Reick'},
]

SAGLIK = [
    {'ad': 'Universitätsklinikum Carl Gustav Carus Dresden', 'adres': 'Fetscherstraße 74, 01307 Dresden', 'aciklama': 'Dresden\'in en büyük hastanesi ve tıp fakültesi, 7/24 acil servis hizmeti sunar.', 'website': 'https://www.uniklinikum-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Universitätsklinikum+Carl+Gustav+Carus+Dresden'},
    {'ad': 'Städtisches Klinikum Dresden, Standort Friedrichstadt', 'adres': 'Friedrichstraße 41, 01067 Dresden', 'aciklama': 'Şehir merkezine yakın, kapsamlı tıbbi hizmetler ve acil servis sunan belediye hastanesi.', 'website': 'https://www.klinikum-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Städtisches+Klinikum+Dresden+Friedrichstadt'},
    {'ad': 'Krankenhaus St. Joseph-Stift', 'adres': 'Wintergartenstraße 15/17, 01307 Dresden', 'aciklama': 'Acil durumlar için hizmet veren, hasta odaklı yaklaşımıyla bilinen bir hastane.', 'website': 'https://www.joseph-stift.de/', 'maps_url': 'https://maps.google.com/?q=Krankenhaus+St.+Joseph-Stift+Dresden'},
]

EGITIM = [
    {'ad': 'Volkshochschule Dresden e.V.', 'adres': 'Annenstraße 10, 01067 Dresden', 'aciklama': 'BAMF onaylı entegrasyon ve Almanca kursları sunan halk eğitim merkezi.', 'website': 'https://www.vhs-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Volkshochschule+Dresden'},
    {'ad': 'Caritasverband für Dresden e.V.', 'adres': 'Schweriner Str. 21, 01067 Dresden', 'aciklama': 'Göçmenler için danışmanlık, sosyal yardım ve eğitim programları sunan bir yardım kuruluşu.', 'website': 'https://www.caritas-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Caritasverband+für+Dresden'},
    {'ad': 'TUDIAS Dresden', 'adres': 'Freiberger Str. 37, 01067 Dresden', 'aciklama': 'Dresden Teknik Üniversitesi\'ne bağlı, yoğun Almanca dil kursları sunan bir enstitü.', 'website': 'https://www.tudias.de/', 'maps_url': 'https://maps.google.com/?q=TUDIAS+Dresden'},
]

GEZI = [
    {
        'ad': 'Frauenkirche', 'adres': 'Neumarkt, 01067 Dresden', 'aciklama': 'II. Dünya Savaşı\'nda yıkılıp yeniden inşa edilen, barışın ve yeniden doğuşun sembolü olan ikonik Barok kilise.', 'website': 'https://www.frauenkirche-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Frauenkirche+Dresden',
        'icerik': 'Dresden\'in kalbinde yer alan Frauenkirche (Kadınlar Kilisesi), şehrin en ikonik simgelerinden biridir. Orijinal kilise 18. yüzyılda inşa edilmiş, Barok mimarinin en görkemli örneklerinden biri olarak kabul edilmiştir. Ancak, II. Dünya Savaşı\'nın sonlarında, 1945 Dresden Bombardımanı sırasında tamamen yıkılmıştır. Yıkıntıları, savaşın acı bir hatırası olarak on yıllarca yerinde bırakılmıştır.\n\nAlmanya\'nın yeniden birleşmesinden sonra, dünyanın dört bir yanından gelen bağışlarla kilisenin yeniden inşası için bir kampanya başlatıldı. Orijinal planlara sadık kalınarak ve eski taşların birçoğu kullanılarak titiz bir çalışma yürütüldü. Bu yeniden inşa süreci, uluslararası bir uzlaşma ve barış projesi olarak büyük anlam taşıdı ve 2005 yılında tamamlanarak yeniden kutsandı.\n\nBugün Frauenkirche, sadece bir ibadet yeri değil, aynı zamanda umudun, yeniden doğuşun ve barışın güçlü bir sembolüdür. Ziyaretçiler, kilisenin muhteşem iç mekanını keşfedebilir, org konserlerini dinleyebilir ve kubbesine tırmanarak Dresden\'in nefes kesen panoramik manzarasının keyfini çıkarabilirler. Kilise, şehrin trajik geçmişini ve küllerinden yeniden doğuşunu anlatan canlı bir anıt olarak her yıl milyonlarca insanı ağırlamaktadır.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Frauenkirche_(Dresden)', 'sira': 1,
    },
    {
        'ad': 'Zwinger Sarayı', 'adres': 'Sophienstraße, 01067 Dresden', 'aciklama': 'Barok mimarinin başyapıtlarından biri olan, sanat koleksiyonlarına ve müzelere ev sahipliği yapan saray kompleksi.', 'website': 'https://www.der-dresdner-zwinger.de/', 'maps_url': 'https://maps.google.com/?q=Zwinger+Dresden',
        'icerik': 'Dresden\'in en görkemli yapılarından biri olan Zwinger Sarayı, geç Barok döneminin bir mimari şaheseridir. 1709 ile 1732 yılları arasında, Saksonya Elektörü ve Polonya Kralı Güçlü Augustus\'un emriyle inşa edilmiştir. Saray, başlangıçta bir portakal bahçesi (Orangerie) ve festival alanı olarak tasarlanmış, kraliyet koleksiyonlarının sergilendiği bir galeri ve kütüphane olarak hizmet vermiştir.\n\nZwinger, heykeltıraş Balthasar Permoser ve mimar Matthäus Daniel Pöppelmann\'ın ortak çalışmasının bir ürünüdür. Kompleks, geniş bir avluyu çevreleyen galeriler, pavyonlar ve kapılardan oluşur. En dikkat çekici bölümleri arasında, mitolojik figürlerle süslenmiş Nymphenbad (Periler Hamamı) ve tepesinde Herkül heykelinin bulunduğu Kronentor (Taç Kapısı) yer alır. Bu zengin süslemeler ve zarif mimari, sarayı Avrupa\'daki en önemli Barok yapılarından biri yapmaktadır.\n\nGünümüzde Zwinger, dünyaca ünlü üç önemli müzeye ev sahipliği yapmaktadır: Eski Ustalar Resim Galerisi (Gemäldegalerie Alte Meister), Porselen Koleksiyonu (Porzellansammlung) ve Matematik-Fizik Salonu (Mathematisch-Physikalischer Salon). Ziyaretçiler, Raphael\'in "Sistine Madonnası" gibi başyapıtları görebilir, Meissen porseleninin en nadide örneklerini inceleyebilir ve tarihi bilimsel aletlerin dünyasına yolculuk yapabilirler. Zwinger, Dresden\'in sanatsal ve kültürel zenginliğinin kalbi olmaya devam etmektedir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Zwinger_(Dresden)', 'sira': 2,
    },
    {
        'ad': 'Semperoper', 'adres': 'Theaterplatz 2, 01067 Dresden', 'aciklama': 'Dünyaca ünlü akustiği ve görkemli mimarisiyle bilinen, Saksonya Devlet Operası\'na ev sahipliği yapan tarihi opera binası.', 'website': 'https://www.semperoper.de/', 'maps_url': 'https://maps.google.com/?q=Semperoper+Dresden',
        'icerik': 'Dresden\'in Theaterplatz (Tiyatro Meydanı) meydanında görkemli bir şekilde yükselen Semperoper, dünyanın en prestijli opera binalarından biridir. Mimar Gottfried Semper tarafından tasarlanan yapı, ilk olarak 1841\'de açılmıştır. Ancak tarih boyunca iki kez yıkıma uğramıştır: 1869\'da bir yangınla ve 1945\'te II. Dünya Savaşı bombardımanıyla. Her iki felaketten sonra da aslına sadık kalınarak yeniden inşa edilmiştir.\n\nOpera binası, Yüksek Rönesans, Barok ve Klasik Yunan stillerinin bir karışımı olan eklektik mimarisiyle dikkat çeker. Dış cephesi, Goethe, Schiller, Shakespeare ve Molière gibi ünlü sanatçıların heykelleriyle süslenmiştir. İç mekanı ise zengin süslemeleri, kırmızı ve altın renklerin hakim olduğu salonu ve olağanüstü akustiği ile ziyaretçileri büyüler. Semperoper, Richard Wagner ve Richard Strauss gibi bestecilerin birçok önemli eserinin prömiyerine sahne olmuştur.\n\nBugün Semperoper, Saksonya Devlet Operası (Sächsische Staatsoper) ve Saksonya Devlet Orkestrası\'na (Sächsische Staatskapelle) ev sahipliği yapmaktadır. Ziyaretçiler, yıl boyunca sahnelenen opera, bale ve konser performanslarının keyfini çıkarabilir veya rehberli turlara katılarak bu muhteşem yapının tarihini ve mimarisini daha yakından tanıyabilirler. Semperoper, Dresden\'in kültürel yaşamının vazgeçilmez bir parçasıdır.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Semperoper', 'sira': 3,
    },
    {
        'ad': 'Residenzschloss', 'adres': 'Taschenberg 2, 01067 Dresden', 'aciklama': 'Saksonya hükümdarlarının eski ikametgahı olan, günümüzde Yeşil Kasa (Grünes Gewölbe) gibi değerli koleksiyonları barındıran müze kompleksi.', 'website': 'https://www.skd.museum/besuch/residenzschloss/', 'maps_url': 'https://maps.google.com/?q=Residenzschloss+Dresden',
        'icerik': 'Dresden Kraliyet Sarayı (Residenzschloss), şehrin en eski yapılarından biridir ve yaklaşık 400 yıl boyunca Saksonya elektörleri ve krallarının ikametgahı olmuştur. Romanesk bir kaleden başlayarak, yıllar içinde Barok ve Rönesans gibi farklı mimari stillerde genişletilmiştir. Saray, II. Dünya Savaşı\'nda ağır hasar görmüş, ancak uzun bir restorasyon sürecinin ardından eski ihtişamına kavuşturulmuştur.\n\nSaray kompleksi, günümüzde Dresden Devlet Sanat Koleksiyonları\'nın (Staatliche Kunstsammlungen Dresden) bir parçası olarak hizmet vermektedir. İçerisinde, Avrupa\'nın en zengin hazine koleksiyonlarından biri olan Tarihi Yeşil Kasa (Historisches Grünes Gewölbe) ve Yeni Yeşil Kasa (Neues Grünes Gewölbe) gibi dünyaca ünlü müzeleri barındırır. Bu müzelerde, fildişi, gümüş, altın ve değerli taşlardan yapılmış binlerce paha biçilmez eser sergilenmektedir.\n\nZiyaretçiler ayrıca sarayın diğer bölümlerini de keşfedebilirler. Bunlar arasında Türk Odası (Türckische Cammer) ile Osmanlı sanat ve el sanatları koleksiyonu, Silah Galerisi (Rüstkammer) ile tarihi zırh ve silahlar, ve sarayın avlusunda düzenlenen etkinlikler yer alır. Residenzschloss, Saksonya\'nın zengin tarihini ve sanatsal mirasını gözler önüne seren büyüleyici bir mekandır.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Residenzschloss_(Dresden)', 'sira': 4,
    },
    {
        'ad': 'Fürstenzug', 'adres': 'Augustusstraße 1, 01067 Dresden', 'aciklama': 'Yaklaşık 23.000 Meissen porseleni karodan oluşan, Saksonya hükümdarlarının geçit törenini tasvir eden dünyanın en büyük porselen duvar resmi.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Fürstenzug+Dresden',
        'icerik': 'Fürstenzug (Prensler Geçidi), Dresden\'in en etkileyici açık hava sanat eserlerinden biridir. 102 metre uzunluğundaki bu devasa duvar resmi, Stallhof\'un (Ahır Avlusu) dış duvarını süsler. Eser, Saksonya\'yı 1127\'den 1873\'e kadar yöneten Wettin Hanedanı\'nın 35 hükümdarını, atları üzerinde bir geçit töreni halinde tasvir eder. Hükümdarların yanı sıra, bilim adamları, sanatçılar ve askerler gibi dönemin önemli figürleri de resimde yer alır.\n\nResmin orijinali 1870\'lerde sgraffito tekniğiyle yapılmış, ancak hava koşullarına dayanıksız olduğu anlaşılmıştır. Bu nedenle, 1904 ile 1907 yılları arasında, yaklaşık 23.000 adet Meissen porseleni karo kullanılarak yenilenmiştir. Bu porselen karolar sayesinde eser, hava koşullarına karşı son derece dayanıklı hale gelmiş ve hatta 1945 bombardımanından neredeyse hasarsız kurtulmuştur.\n\nBugün Fürstenzug, Dresden\'in en çok fotoğrafı çekilen yerlerinden biridir. Ziyaretçiler, Saksonya tarihinin bu görkemli panoramasını ücretsiz olarak inceleyebilir ve her bir figürün detaylarındaki ustalığa hayran kalabilirler. Resim, şehrin tarihi merkezinde, Frauenkirche ve Residenzschloss gibi diğer önemli yapılara yürüme mesafesindedir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Fürstenzug', 'sira': 5,
    },
    {
        'ad': 'Brühlsche Terrasse', 'adres': 'Georg-Treu-Platz 1, 01067 Dresden', 'aciklama': '"Avrupa\'nın Balkonu" olarak bilinen, Elbe Nehri kıyısında muhteşem manzaralar sunan tarihi teras.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Brühlsche+Terrasse+Dresden',
        'icerik': 'Brühl Terası (Brühlsche Terrasse), Dresden\'in tarihi merkezinde, Elbe Nehri boyunca uzanan muhteşem bir gezinti yoludur. 19. yüzyılda "Avrupa\'nın Balkonu" olarak adlandırılan bu teras, şehrin en güzel manzaralarından birini sunar. Teras, aslen şehrin surlarının bir parçası olarak inşa edilmiş, daha sonra Kont Heinrich von Brühl tarafından özel bir zevk bahçesine dönüştürülmüştür. 1814 yılında halka açılmıştır.\n\nTeras boyunca yürürken, Elbe Nehri\'nin, karşı kıyıdaki Neustadt bölgesinin ve Augustus Köprüsü\'nün büyüleyici manzaralarını seyredebilirsiniz. Teras aynı zamanda Dresden Sanat Akademisi (Kunstakademie) ve Albertinum Müzesi gibi önemli mimari yapılara da ev sahipliği yapmaktadır. Heykeller, çeşmeler ve özenle düzenlenmiş bahçeler, terasın atmosferine zarafet katmaktadır.\n\nBrühl Terası, hem yerel halk hem de turistler için popüler bir buluşma ve dinlenme noktasıdır. Güneşli bir günde bir kafede oturmak, nehir trafiğini izlemek veya sadece tarihi atmosferin tadını çıkarmak için mükemmel bir yerdir. Teras, Dresden\'in tarihi dokusunu ve doğal güzelliğini bir arada deneyimlemek için eşsiz bir fırsat sunar.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Brühlsche_Terrasse', 'sira': 6,
    },
    {
        'ad': 'Gemäldegalerie Alte Meister', 'adres': 'Theaterplatz 1, 01067 Dresden', 'aciklama': 'Zwinger Sarayı\'nda yer alan, Raphael\'in "Sistine Madonnası" gibi dünyaca ünlü eserlere ev sahipliği yapan sanat müzesi.', 'website': 'https://gemaeldegalerie.skd.museum/', 'maps_url': 'https://maps.google.com/?q=Gemäldegalerie+Alte+Meister+Dresden',
        'icerik': 'Eski Ustalar Resim Galerisi (Gemäldegalerie Alte Meister), Zwinger Sarayı\'nın Semper Galerisi\'nde yer alan, dünyanın en önemli sanat müzelerinden biridir. Koleksiyonun temelleri, 16. yüzyılda Saksonya elektörleri tarafından atılmıştır. Müze, özellikle İtalyan Rönesansı ve Hollanda Altın Çağı\'na ait başyapıtlarıyla ünlüdür.\n\nGalerinin en ünlü eseri, şüphesiz Raphael\'in "Sistine Madonnası"dır. Bu ikonik tablo, her yıl dünyanın dört bir yanından sanatseverleri Dresden\'e çekmektedir. Koleksiyonda ayrıca Giorgione, Titian, Rembrandt, Rubens, Vermeer ve Canaletto gibi ustaların paha biçilmez eserleri de bulunmaktadır. Müze, 15. yüzyıldan 18. yüzyıla kadar Avrupa resim sanatının gelişimini gözler önüne seren zengin bir panorama sunar.\n\nZiyaretçiler, bu sanat hazinesini keşfederken Batı sanat tarihinin en önemli dönemlerine tanıklık etme fırsatı bulurlar. Galerinin görkemli salonları ve eserlerin etkileyici sunumu, unutulmaz bir sanat deneyimi yaşatır. Gemäldegalerie Alte Meister, Dresden\'e yapılan bir gezinin olmazsa olmaz duraklarından biridir ve sanat tutkunları için adeta bir cennettir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Gemäldegalerie_Alte_Meister', 'sira': 7,
    },
    {
        'ad': 'Großer Garten', 'adres': 'Hauptallee 8, 01219 Dresden', 'aciklama': 'Dresden\'in en büyük parkı olan, içinde saray, botanik bahçesi ve minyatür demiryolu bulunan popüler bir dinlenme alanı.', 'website': 'https://www.grosser-garten-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Großer+Garten+Dresden',
        'icerik': 'Großer Garten (Büyük Bahçe), Dresden\'in merkezinde yer alan ve şehrin akciğerleri olarak kabul edilen devasa bir parktır. 1676 yılında Barok tarzda bir bahçe olarak tasarlanan park, bugün hem tarihi hem de doğal güzellikleri bir arada sunan popüler bir rekreasyon alanıdır. Yaklaşık 1.8 kilometrekarelik bir alana yayılan park, geniş çayırları, göletleri ve yaşlı ağaçlarıyla huzurlu bir sığınak sunar.\n\nParkın kalbinde, 1680 yılında inşa edilen Erken Barok tarzındaki Sommerpalais (Yazlık Saray) yer alır. Parkın içinde ayrıca Dresden Botanik Bahçesi ve Dresden Hayvanat Bahçesi gibi önemli kurumlar da bulunmaktadır. Parkın en sevilen özelliklerinden biri de, 1950\'den beri hizmet veren ve parkın içinde 5.6 kilometrelik bir tur atan minyatür demiryolu Parkeisenbahn\'dır.\n\nGroßer Garten, spor yapmak, piknik yapmak, yürüyüşe çıkmak veya sadece doğanın tadını çıkarmak isteyenler için mükemmel bir yerdir. Yıl boyunca çeşitli konserler, festivaller ve açık hava etkinliklerine ev sahipliği yapar. Şehrin gürültüsünden kaçmak ve dinlenmek için ideal bir ortam sunan bu yeşil vaha, Dresden halkının ve ziyaretçilerin vazgeçilmezidir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Großer_Garten_(Dresden)', 'sira': 8,
    },
    {
        'ad': 'Pfunds Molkerei', 'adres': 'Bautzner Str. 79, 01099 Dresden', 'aciklama': 'Guinness Rekorlar Kitabı\'na "Dünyanın En Güzel Süt Dükkanı" olarak giren, elle boyanmış Villeroy & Boch karolarıyla kaplı tarihi dükkan.', 'website': 'https://www.pfunds.de/', 'maps_url': 'https://maps.google.com/?q=Pfunds+Molkerei+Dresden',
        'icerik': 'Dresden\'in Neustadt bölgesinde yer alan Pfunds Molkerei, sıradan bir süt dükkanından çok daha fazlasıdır. 1880 yılında Pfund kardeşler tarafından kurulan bu dükkan, 1998 yılında Guinness Rekorlar Kitabı tarafından "Dünyanın En Güzel Süt Dükkanı" olarak tescillenmiştir. Bu unvanı, dükkanın duvarlarını, tavanını ve tezgahını kaplayan 247 metrekarelik el boyaması Villeroy & Boch karolarına borçludur.\n\nİçeri adım attığınızda, kendinizi adeta bir sanat galerisinde hissedersiniz. Neo-Rönesans tarzındaki karolar, melekler, çocuklar, mitolojik figürler ve pastoral sahneler gibi çeşitli motiflerle süslenmiştir. Bu görsel şölen, 19. yüzyıl sonu estetiğini ve işçiliğini yansıtan büyüleyici bir atmosfer yaratır. Dükkan, II. Dünya Savaşı bombardımanından şans eseri kurtulmuş ve orijinal haliyle günümüze ulaşmıştır.\n\nZiyaretçiler, bu eşsiz dükkanda sadece tarihi atmosferin tadını çıkarmakla kalmaz, aynı zamanda çeşitli süt ürünleri, peynirler, yerel spesiyaliteler ve hediyelik eşyalar da satın alabilirler. Üst katta yer alan restoranda ise geleneksel Saksonya yemeklerini ve taze süt ürünlerini tadabilirsiniz. Pfunds Molkerei, Dresden\'in gizli kalmış hazinelerinden biridir ve kesinlikle görülmeye değerdir.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Pfunds_Molkerei', 'sira': 9,
    },
    {
        'ad': 'Kunsthofpassage', 'adres': 'Görlitzer Str. 21-25, 01099 Dresden', 'aciklama': 'Neustadt bölgesinde yer alan, yaratıcı ve ilginç tasarımlara sahip binalardan oluşan bir dizi avlu. Özellikle "Yağmur Oluğu Orkestrası" ile ünlüdür.', 'website': 'https://www.kunsthof-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Kunsthofpassage+Dresden',
        'icerik': 'Dresden\'in bohem ve alternatif yaşam tarzıyla bilinen Äußere Neustadt (Dış Yeni Şehir) bölgesinde saklı bir mücevher olan Kunsthofpassage, birbiriyle bağlantılı beş avludan oluşan sanatsal bir komplekstir. Sanatçılar, tasarımcılar ve mimarlar tarafından yaratılan bu geçit, binaların cephelerini birer tuval olarak kullanarak yaratıcılığın sınırlarını zorlar. Her avlunun kendine özgü bir teması ve atmosferi vardır.\n\nEn ünlü avlu, şüphesiz "Elementler Avlusu"dur (Hof der Elemente). Bu avludaki mavi binanın cephesi, karmaşık bir oluk ve boru sistemiyle donatılmıştır. Yağmur yağdığında, bu sistem adeta bir müzik aletine dönüşür ve suyun akışıyla melodik sesler çıkarır. Diğer avlular arasında "Işık Avlusu" (Hof des Lichts), "Metamorfozlar Avlusu" (Hof der Metamorphosen) ve "Mitolojik Yaratıklar Avlusu" (Hof der Fabelwesen) bulunur.\n\nKunsthofpassage, sadece ilginç mimarisiyle değil, aynı zamanda içinde barındırdığı küçük butikler, sanat galerileri, kafeler ve atölyelerle de canlı bir mekandır. Ziyaretçiler, bu dar geçitlerde dolaşırken beklenmedik sanat eserleriyle karşılaşabilir ve Dresden\'in yaratıcı ruhunu en saf haliyle deneyimleyebilirler. Burası, standart turistik rotaların dışına çıkmak isteyenler için keşfedilmeyi bekleyen bir harikalar diyarıdır.',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Kunsthofpassage', 'sira': 10,
    },
]

ALISVERIS = [
    {'ad': 'Altmarkt-Galerie Dresden', 'adres': 'Webergasse 1, 01067 Dresden', 'aciklama': 'Dresden\'in kalbinde, 200\'den fazla mağaza ve restorana ev sahipliği yapan modern bir alışveriş merkezi.', 'website': 'https://www.altmarkt-galerie-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Altmarkt-Galerie+Dresden'},
    {'ad': 'Centrum-Galerie Dresden', 'adres': 'Prager Str. 15, 01069 Dresden', 'aciklama': 'Prager Strasse üzerinde yer alan, popüler markaları ve geniş bir yeme-içme alanını bir araya getiren büyük bir AVM.', 'website': 'https://www.centrum-galerie-dresden.de/', 'maps_url': 'https://maps.google.com/?q=Centrum-Galerie+Dresden'},
    {'ad': 'Saray Market', 'adres': 'Kesselsdorfer Str. 23, 01159 Dresden', 'aciklama': 'Helal et ürünleri, taze sebze-meyve ve çeşitli Türk gıda ürünlerini bulabileceğiniz bir market.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Saray+Market+Dresden'},
    {'ad': 'Gazi-Market', 'adres': 'Wernerstraße 35, 01159 Dresden', 'aciklama': 'Türk ve Ortadoğu mutfağına yönelik geniş ürün yelpazesi sunan bir diğer popüler market.', 'website': '', 'maps_url': 'https://maps.google.com/?q=Gazi-Market+Dresden'},
]


def seed(apps, schema_editor):
    Eyalet = apps.get_model('stadt', 'Eyalet')
    Stadt  = apps.get_model('stadt', 'Stadt')
    Yer    = apps.get_model('yerler', 'Yer')
    try:
        eyalet = Eyalet.objects.get(kod='SN')
        sehir  = Stadt.objects.get(slug='dresden')
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
                    'sehir':       'Dresden',
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
    Yer.objects.filter(ad__in=adlar, sehir='Dresden').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('yerler', '0046_merge_20260510_0041'),
        ('stadt',  '0047_dresden_aktiv'),
    ]
    operations = [migrations.RunPython(seed, unseed)]