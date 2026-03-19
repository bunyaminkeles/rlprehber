"""
Mainz ve çevresi için temel statik veriyi yükler:
- Yerler (marketler, camiler, TÜV, gezi, resmi kurumlar)
- Önemli linkler
- Rehber sayfaları
- Forum kategorileri

Kullanım: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from yerler.models import Yer
from linkler.models import OnemliLink
from rehber.models import RehberSayfasi
from forum.models import ForumKategori


YERLER = [
    # --- RESMİ KURUMLAR ---
    {
        'ad': 'Ausländerbehörde Mainz',
        'kategori': 'resmi_kurum',
        'adres': 'Valenciaplatz 3, 55118 Mainz',
        'telefon': '+49 6131 12-0',
        'website': 'https://www.mainz.de/leben-in-mainz/buergerservice/auslaenderwesen.php',
        'maps_url': 'https://maps.app.goo.gl/auslaenderbehoerde-mainz',
        'aciklama': 'Oturma izni, çalışma izni ve yabancılar yasası ile ilgili tüm işlemler bu birimde yapılır. Randevu almak için web sitesini ziyaret edin.',
    },
    {
        'ad': 'BAMF — Außenstelle Mainz',
        'kategori': 'resmi_kurum',
        'adres': 'Rheinstraße 97, 55116 Mainz',
        'telefon': '+49 911 943-0',
        'website': 'https://www.bamf.de',
        'maps_url': 'https://maps.app.goo.gl/bamf-mainz',
        'aciklama': 'Federal Göç ve Mülteciler Dairesi. Vatandaşlığa geçiş, entegrasyon kursları ve tanıma işlemleri.',
    },
    {
        'ad': 'Agentur für Arbeit Mainz',
        'kategori': 'resmi_kurum',
        'adres': 'Parcusstraße 2, 55116 Mainz',
        'telefon': '+49 800 4 5555 00',
        'website': 'https://www.arbeitsagentur.de',
        'maps_url': 'https://maps.app.goo.gl/agentur-arbeit-mainz',
        'aciklama': 'İş bulma, işsizlik parası (ALG I), mesleki eğitim ve kariyer danışmanlığı hizmetleri.',
    },
    {
        'ad': 'Jobcenter Mainz',
        'kategori': 'resmi_kurum',
        'adres': 'Isaac-Fulda-Allee 2, 55124 Mainz',
        'telefon': '+49 6131 2536-0',
        'website': 'https://www.jobcenter-mainz.de',
        'maps_url': 'https://maps.app.goo.gl/jobcenter-mainz',
        'aciklama': 'Bürgergeld (eski Hartz IV), konut yardımı ve uzun süreli işsizler için destek hizmetleri.',
    },
    {
        'ad': 'T.C. Frankfurt Başkonsolosluğu',
        'kategori': 'resmi_kurum',
        'adres': 'Friedberger Anlage 1, 60316 Frankfurt am Main',
        'telefon': '+49 69 29 91 58 0',
        'website': 'https://frankfurt.bk.mfa.gov.tr',
        'maps_url': 'https://maps.app.goo.gl/tc-konsolosluk-frankfurt',
        'aciklama': 'Mainz bölgesi için yetkili Türk konsolosluğu. Pasaport yenileme, apostil, nüfus cüzdanı ve e-devlet işlemleri. Randevu zorunlu.',
    },
    {
        'ad': 'Führerscheinstelle Mainz (Ehliyet Birimi)',
        'kategori': 'resmi_kurum',
        'adres': 'Valenciaplatz 3, 55118 Mainz',
        'telefon': '+49 6131 12-0',
        'website': 'https://www.mainz.de/leben-in-mainz/buergerservice/fuehrerschein.php',
        'maps_url': 'https://maps.app.goo.gl/fuhrerscheinstelle-mainz',
        'aciklama': 'Türk ehliyetini Alman ehliyetine dönüştürme, yeni ehliyet başvurusu. Randevu gereklidir.',
    },
    {
        'ad': 'Einwohnermeldeamt Mainz (Anmeldung)',
        'kategori': 'resmi_kurum',
        'adres': 'Stadthaus Rheinufer, Rheinstraße 55, 55116 Mainz',
        'telefon': '+49 6131 12-0',
        'website': 'https://www.mainz.de',
        'maps_url': 'https://maps.app.goo.gl/einwohnermeldeamt-mainz',
        'aciklama': 'İkamet adresi kayıt (Anmeldung) ve adres değişikliği (Ummeldung) işlemleri. Taşınmaktan itibaren 2 hafta içinde yapılması zorunludur.',
    },
    {
        'ad': 'Finanzamt Mainz',
        'kategori': 'resmi_kurum',
        'adres': 'Löwenhofstraße 1, 55116 Mainz',
        'telefon': '+49 6131 488-0',
        'website': 'https://www.finanzamt.rlp.de/mainz',
        'maps_url': 'https://maps.app.goo.gl/finanzamt-mainz',
        'aciklama': 'Vergi numarası (Steuernummer) alma, yıllık vergi beyannamesi (Steuererklärung) işlemleri.',
    },

    # --- TÜV / GTÜ İSTASYONLARI ---
    {
        'ad': 'TÜV Rheinland — Mainz',
        'kategori': 'tuv',
        'adres': 'Binger Straße 44, 55131 Mainz',
        'telefon': '+49 800 8484-000',
        'website': 'https://www.tuv.com',
        'maps_url': 'https://maps.app.goo.gl/tuv-mainz-binger',
        'aciklama': 'Araç muayenesi (HU/AU), teknik inceleme. Muayene için randevu almanız önerilir.',
    },
    {
        'ad': 'DEKRA Mainz',
        'kategori': 'tuv',
        'adres': 'Rheinallee 3, 55116 Mainz',
        'telefon': '+49 800 333-5274',
        'website': 'https://www.dekra.de',
        'maps_url': 'https://maps.app.goo.gl/dekra-mainz',
        'aciklama': 'Araç teknik muayene (HU), hasar tespiti ve değerlendirme.',
    },
    {
        'ad': 'GTÜ Prüfstelle Mainz',
        'kategori': 'tuv',
        'adres': 'Hechtsheimer Straße 12, 55131 Mainz',
        'telefon': '+49 6131 970-0',
        'website': 'https://www.gtue.de',
        'maps_url': 'https://maps.app.goo.gl/gtue-mainz',
        'aciklama': 'Araç muayene istasyonu. TÜV\'e alternatif, genellikle randevu daha kolay bulunur.',
    },

    # --- TÜRK MARKETLERİ ---
    {
        'ad': 'Mavi Market Mainz',
        'kategori': 'turk_market',
        'adres': 'Boppstraße 22, 55118 Mainz',
        'sehir': 'Mainz',
        'aciklama': 'Türk ve Orta Doğu ürünleri, taze sebze-meyve, et ürünleri.',
    },
    {
        'ad': 'Türk Market Mainz-Bretzenheim',
        'kategori': 'turk_market',
        'adres': 'Austraße, 55128 Mainz-Bretzenheim',
        'sehir': 'Mainz',
        'aciklama': 'Türk gıda ürünleri, helal et, bakliyat ve ev ürünleri.',
    },
    {
        'ad': 'Orient Market Bingen am Rhein',
        'kategori': 'turk_market',
        'adres': 'Mainzer Straße, 55411 Bingen am Rhein',
        'sehir': 'Bingen',
        'aciklama': 'Bingen bölgesi için Türk ve Orta Doğu ürünleri.',
    },

    # --- CAMİ / İBADETHANE ---
    {
        'ad': 'DITIB Türkisch-Islamische Gemeinde Mainz',
        'kategori': 'ibadet',
        'adres': 'Boppstraße 20, 55118 Mainz',
        'telefon': '',
        'website': 'https://ditib.de',
        'maps_url': 'https://maps.app.goo.gl/ditib-mainz',
        'aciklama': 'Mainz merkez camii. Cuma namazı, Kuran kursu, cenaze hizmetleri.',
    },
    {
        'ad': 'Islamisches Kulturzentrum Mainz',
        'kategori': 'ibadet',
        'adres': 'Goethestraße 5, 55116 Mainz',
        'sehir': 'Mainz',
        'aciklama': 'Günlük vakit namazları düzenlenmektedir.',
    },
    {
        'ad': 'IGMG Moschee Mainz',
        'kategori': 'ibadet',
        'adres': 'Mainz Bölgesi',
        'sehir': 'Mainz',
        'website': 'https://igmg.org',
        'aciklama': 'Milli Görüş bağlantılı cami ve kültür merkezi.',
    },
    {
        'ad': 'Türkisch-Islamische Gemeinde Bingen',
        'kategori': 'ibadet',
        'adres': 'Bingen am Rhein',
        'sehir': 'Bingen',
        'aciklama': 'Bingen bölgesi Türk-İslam Derneği camii.',
    },

    # --- ALIŞVERİŞ MERKEZLERİ ---
    {
        'ad': 'Römerpassage Mainz',
        'kategori': 'alisveris',
        'adres': 'Schusterstraße 8, 55116 Mainz',
        'website': 'https://www.roemerpassage-mainz.de',
        'maps_url': 'https://maps.app.goo.gl/roemerpassage-mainz',
        'aciklama': 'Mainz şehir merkezindeki en büyük alışveriş merkezi. Zara, H&M, Galeria ve daha fazlası.',
    },
    {
        'ad': 'Einkaufszentrum Zollhafen',
        'kategori': 'alisveris',
        'adres': 'Zollhafen, 55118 Mainz',
        'sehir': 'Mainz',
        'aciklama': 'Yeni gelişim bölgesindeki alışveriş alanı.',
    },
    {
        'ad': 'Huma Shoppingpark (Mainz-Kastel)',
        'kategori': 'alisveris',
        'adres': 'August-Bebel-Straße 3, 65203 Wiesbaden (Mainz-Kastel yakını)',
        'sehir': 'Mainz-Kastel',
        'maps_url': 'https://maps.app.goo.gl/huma-mainz-kastel',
        'aciklama': 'Mainz-Kastel ve Wiesbaden sınırında büyük alışveriş merkezi. Mediamarkt, IKEA yakını.',
    },
    {
        'ad': 'IKEA Wiesbaden (Mainz yakını)',
        'kategori': 'alisveris',
        'adres': 'Wiesbadener Straße 300, 65203 Wiesbaden',
        'website': 'https://www.ikea.com/de/de/stores/wiesbaden/',
        'maps_url': 'https://maps.app.goo.gl/ikea-wiesbaden',
        'aciklama': 'Mainz\'a yakın IKEA. Ev eşyası, mobilya. Otobüs veya araçla kolayca ulaşılabilir.',
    },

    # --- GEZİ & KÜLTÜR ---
    {
        'ad': 'Mainzer Dom (Aziz Martin Katedrali)',
        'kategori': 'gezi',
        'adres': 'Domstraße 3, 55116 Mainz',
        'website': 'https://www.bistum-mainz.de/dom',
        'maps_url': 'https://maps.app.goo.gl/mainzer-dom',
        'aciklama': 'Mainz\'ın simgesi, 1000 yıllık Romanesque katedrali. Ziyaret ücretsiz.',
    },
    {
        'ad': 'Gutenberg Museum',
        'kategori': 'gezi',
        'adres': 'Liebfrauenplatz 5, 55116 Mainz',
        'telefon': '+49 6131 122-640',
        'website': 'https://www.gutenberg-museum.de',
        'maps_url': 'https://maps.app.goo.gl/gutenberg-museum-mainz',
        'aciklama': 'Johannes Gutenberg\'in matbaa icadına adanmış dünya müzesi. Orijinal Gutenberg İncilini görebilirsiniz.',
    },
    {
        'ad': 'Rheinpromenade Mainz',
        'kategori': 'gezi',
        'adres': 'Rheinufer, 55116 Mainz',
        'maps_url': 'https://maps.app.goo.gl/rheinpromenade-mainz',
        'aciklama': 'Ren nehri kıyısında yürüyüş ve bisiklet yolu. Akşamları çok güzel manzara.',
    },
    {
        'ad': 'Zitadelle Mainz',
        'kategori': 'gezi',
        'adres': 'Obentrautstraße 1, 55118 Mainz',
        'maps_url': 'https://maps.app.goo.gl/zitadelle-mainz',
        'aciklama': 'Tarihi kale. Yaz aylarında çeşitli etkinlikler ve festivaller düzenlenir. Manzarası muhteşem.',
    },
    {
        'ad': 'Landesmuseum Mainz',
        'kategori': 'gezi',
        'adres': 'Große Bleiche 49-51, 55116 Mainz',
        'website': 'https://landesmuseum-mainz.de',
        'maps_url': 'https://maps.app.goo.gl/landesmuseum-mainz',
        'aciklama': 'Rheinland-Pfalz eyalet müzesi. Antik Roma döneminden günümüze sanat ve tarih eserleri.',
    },
    {
        'ad': 'Botanischer Garten Mainz',
        'kategori': 'gezi',
        'adres': 'Anselm-Franz-von-Bentzel-Weg 9a, 55128 Mainz',
        'website': 'https://www.botgarten.uni-mainz.de',
        'maps_url': 'https://maps.app.goo.gl/botanischer-garten-mainz',
        'aciklama': 'Johannes Gutenberg Üniversitesi botanik bahçesi. Ücretsiz giriş.',
    },
    {
        'ad': 'Weinberge Nierstein / Oppenheim',
        'kategori': 'gezi',
        'adres': 'Nierstein, Rheinhessen',
        'maps_url': 'https://maps.app.goo.gl/nierstein-weinberge',
        'aciklama': 'Mainz\'ın güneyindeki Rheinhessen bağ bölgesi. Şarap turu ve yürüyüş rotaları.',
    },
    {
        'ad': 'Burg Rheinfels (St. Goar)',
        'kategori': 'gezi',
        'adres': 'Schlossberg 47, 56329 St. Goar',
        'maps_url': 'https://maps.app.goo.gl/burg-rheinfels',
        'aciklama': 'Mainz\'a 1 saat mesafede Ren üzerindeki en büyük kale kalıntısı. Muhteşem manzara.',
    },
]

LINKLER = [
    # --- RESMİ KURUMLAR ---
    {
        'ad': 'Stadt Mainz — Resmi Site',
        'url': 'https://www.mainz.de',
        'kategori': 'resmi',
        'aciklama': 'Mainz Belediyesi resmi web sitesi. Tüm belediye hizmetlerine buradan ulaşılır.',
        'sira': 1,
    },
    {
        'ad': 'Ausländerbehörde Mainz',
        'url': 'https://www.mainz.de/leben-in-mainz/buergerservice/auslaenderwesen.php',
        'kategori': 'resmi',
        'aciklama': 'Oturma izni, çalışma izni ve yabancılar ile ilgili tüm işlemler.',
        'randevu_url': 'https://terminvergabe.mainz.de',
        'sira': 2,
    },
    {
        'ad': 'BAMF — Federal Göç Dairesi',
        'url': 'https://www.bamf.de',
        'kategori': 'resmi',
        'aciklama': 'Entegrasyon kursları, tanıma işlemleri, vatandaşlık bilgileri.',
        'sira': 3,
    },
    {
        'ad': 'T.C. Frankfurt Başkonsolosluğu',
        'url': 'https://frankfurt.bk.mfa.gov.tr',
        'kategori': 'resmi',
        'aciklama': 'Pasaport, nüfus, apostil ve diğer konsolosluk hizmetleri.',
        'randevu_url': 'https://konsolosluk.gov.tr',
        'sira': 4,
    },
    {
        'ad': 'Kreis Mainz-Bingen',
        'url': 'https://www.mainz-bingen.de',
        'kategori': 'resmi',
        'aciklama': 'Mainz-Bingen ilçe yönetimi. Bingen, Ingelheim ve çevre ilçelere ait hizmetler.',
        'sira': 5,
    },
    {
        'ad': 'Verbandsgemeinde Bingen-Rhein',
        'url': 'https://www.verbandsgemeinde-bingen-rhein.de',
        'kategori': 'resmi',
        'aciklama': 'Bingen ve çevre köylere ait yerel yönetim hizmetleri.',
        'sira': 6,
    },

    # --- İLAN PLATFORMLARI ---
    {
        'ad': 'Kleinanzeigen (eski eBay Kleinanzeigen)',
        'url': 'https://www.kleinanzeigen.de/s-mainz/c0',
        'kategori': 'ilan',
        'aciklama': 'Almanya\'nın en büyük ücretsiz ilan platformu. Araç, ev, eşya alım-satım.',
        'sira': 1,
    },
    {
        'ad': 'ImmobilienScout24',
        'url': 'https://www.immobilienscout24.de/Suche/de/rheinland-pfalz/mainz/wohnung-mieten',
        'kategori': 'ilan',
        'aciklama': 'Almanya\'nın en büyük kiralık ev platformu. Mainz ve Mainz-Bingen ilanları.',
        'sira': 2,
    },
    {
        'ad': 'Immonet — Mainz',
        'url': 'https://www.immonet.de/immobiliensuche/mainz.html',
        'kategori': 'ilan',
        'aciklama': 'Kiralık ve satılık ev ilanları.',
        'sira': 3,
    },
    {
        'ad': 'WG-Gesucht (Paylaşımlı Ev)',
        'url': 'https://www.wg-gesucht.de/wg-zimmer-in-Mainz.html',
        'kategori': 'ilan',
        'aciklama': 'WG (paylaşımlı daire) arama platformu. Mainz\'da oda aramak için ideal.',
        'sira': 4,
    },
    {
        'ad': 'Mobile.de — Araç İlanları',
        'url': 'https://www.mobile.de',
        'kategori': 'ilan',
        'aciklama': 'Almanya\'nın en büyük araç alım-satım platformu.',
        'sira': 5,
    },
    {
        'ad': 'AutoScout24',
        'url': 'https://www.autoscout24.de',
        'kategori': 'ilan',
        'aciklama': 'Avrupa genelinde araç alım-satım platformu.',
        'sira': 6,
    },

    # --- İŞ & KARİYER ---
    {
        'ad': 'Agentur für Arbeit — İş Arama',
        'url': 'https://www.arbeitsagentur.de/jobsuche',
        'kategori': 'is',
        'aciklama': 'Resmi Alman iş bulma platformu. ALG I başvurusu, kariyer danışmanlığı.',
        'randevu_url': 'https://www.arbeitsagentur.de/eServices',
        'sira': 1,
    },
    {
        'ad': 'Jobcenter Mainz',
        'url': 'https://www.jobcenter-mainz.de',
        'kategori': 'is',
        'aciklama': 'Bürgergeld başvurusu ve uzun süreli işsizler için destek.',
        'sira': 2,
    },
    {
        'ad': 'Indeed Almanya',
        'url': 'https://de.indeed.com',
        'kategori': 'is',
        'aciklama': 'Geniş kapsamlı iş ilanları platformu.',
        'sira': 3,
    },
    {
        'ad': 'StepStone',
        'url': 'https://www.stepstone.de',
        'kategori': 'is',
        'aciklama': 'Almanya\'da kariyer ve iş ilanları.',
        'sira': 4,
    },
    {
        'ad': 'IHK Rheinhessen (Ticaret Odası)',
        'url': 'https://www.ihk.de/rheinhessen',
        'kategori': 'is',
        'aciklama': 'Esnaf ve girişimciler için ticaret odası. İşletme kurma, mesleki tanıma.',
        'sira': 5,
    },

    # --- EĞİTİM ---
    {
        'ad': 'VHS Mainz (Halk Eğitim Merkezi)',
        'url': 'https://www.vhs-mainz.de',
        'kategori': 'egitim',
        'aciklama': 'Almanca kursları, BAMF entegrasyon kursu, mesleki kurslar ve daha fazlası.',
        'sira': 1,
    },
    {
        'ad': 'Kita-Navigator Mainz (Kreş Kayıt)',
        'url': 'https://kita-navigator.mainz.de',
        'kategori': 'egitim',
        'aciklama': 'Mainz\'daki kreş (Kita) müsaitlik ve başvuru platformu.',
        'sira': 2,
    },
    {
        'ad': 'Johannes Gutenberg Universität Mainz',
        'url': 'https://www.uni-mainz.de',
        'kategori': 'egitim',
        'aciklama': 'Mainz Üniversitesi. Lisans, yüksek lisans ve dil kursları.',
        'sira': 3,
    },
    {
        'ad': 'Hochschule Mainz',
        'url': 'https://www.hs-mainz.de',
        'kategori': 'egitim',
        'aciklama': 'Mainz Uygulamalı Bilimler Üniversitesi.',
        'sira': 4,
    },

    # --- SAĞLIK ---
    {
        'ad': 'Universitätsmedizin Mainz',
        'url': 'https://www.unimedizin-mainz.de',
        'kategori': 'saglik',
        'aciklama': 'Mainz Üniversite Hastanesi. Acil servis ve tüm uzmanlık dalları.',
        'sira': 1,
    },
    {
        'ad': 'Kassenärztliche Vereinigung RLP (Doktor Bul)',
        'url': 'https://www.kv-rlp.de/patienten/arztsuche',
        'kategori': 'saglik',
        'aciklama': 'Mainz ve çevresinde kassenärztlicher (sigortalı) doktor arama.',
        'sira': 2,
    },
    {
        'ad': 'Jameda — Doktor Değerlendirme',
        'url': 'https://www.jameda.de',
        'kategori': 'saglik',
        'aciklama': 'Doktor arama ve değerlendirme platformu.',
        'sira': 3,
    },

    # --- ULAŞIM ---
    {
        'ad': 'MVG — Mainzer Verkehrsgesellschaft',
        'url': 'https://www.mvg-mainz.de',
        'kategori': 'ulasim',
        'aciklama': 'Mainz otobüs ve tramvay. Hat saatleri, bilet satın alma.',
        'sira': 1,
    },
    {
        'ad': 'RNN — Rhein-Nahe Nahverkehr',
        'url': 'https://www.rnn.info',
        'kategori': 'ulasim',
        'aciklama': 'Mainz-Bingen ve çevre ilçelere toplu taşıma.',
        'sira': 2,
    },
    {
        'ad': 'DB — Deutsche Bahn',
        'url': 'https://www.bahn.de',
        'kategori': 'ulasim',
        'aciklama': 'Almanya tren biletleri ve güzergahları.',
        'sira': 3,
    },
    {
        'ad': 'DB Deutschlandticket',
        'url': 'https://www.bahn.de/angebot/regio/deutschlandticket',
        'kategori': 'ulasim',
        'aciklama': '49€ aylık tüm Almanya\'da yerel toplu taşıma aboneliği.',
        'sira': 4,
    },
]

REHBER_SAYFALARI = [
    {
        'baslik': 'Ausländerbehörde — Yabancılar Dairesi',
        'slug': 'auslaenderbehoerde',
        'kategori': 'resmi',
        'icon': 'bi-building',
        'ozet': 'Oturma izni başvurusu, randevu alma ve gerekli belgeler',
        'icerik': '''Ausländerbehörde (Yabancılar Dairesi), Almanya'da yaşayan yabancıların oturma izni ve diğer resmi işlemlerini yürüten kurumdur.

**Adres:** Valenciaplatz 3, 55118 Mainz
**Telefon:** +49 6131 12-0
**Randevu:** Mutlaka önceden randevu alınız — randevusuz kabul yapılmamaktadır.

**Randevu Alma:**
Online randevu için Mainz Belediyesi'nin randevu sistemini kullanın. Yoğun dönemlerde 4-6 hafta öncesinden randevu almanız gerekebilir.

**Genel Olarak Gerekli Belgeler:**
- Geçerli pasaport
- Biyometrik fotoğraf (son 6 ay içinde çekilmiş)
- Anmeldung belgesi (ikamet tescil belgesi)
- İşlem türüne göre ek belgeler (iş sözleşmesi, okul kaydı, sağlık sigortası belgesi vb.)

**Oturma İzni Çeşitleri:**
- Aufenthaltserlaubnis: Geçici oturma izni
- Niederlassungserlaubnis: Süresiz oturma izni (5 yıl sonra başvurulabilir)
- Blaue Karte EU: Yüksek vasıflı çalışanlar için

**Önemli Notlar:**
- Oturma izninizin bitiş tarihinden en az 6 hafta önce yenileme randevusu alın.
- Mevcut oturma izniniz süresi dolmadan randevu aldıysanız, randevu gününe kadar yasal olarak Almanya'da kalabilirsiniz.
- İşlemler Almanca yürütülür; gerekirse tercüman götürebilirsiniz.''',
        'sira': 1,
    },
    {
        'baslik': 'BAMF — Federal Göç ve Mülteciler Dairesi',
        'slug': 'bamf',
        'kategori': 'resmi',
        'icon': 'bi-shield-check',
        'ozet': 'Entegrasyon kursları, tanıma işlemleri ve vatandaşlık',
        'icerik': '''BAMF (Bundesamt für Migration und Flüchtlinge), Almanya'da göç ve entegrasyon süreçlerini yöneten federal kurumdur.

**Web Sitesi:** www.bamf.de
**Mainz Ofisi:** Rheinstraße 97, 55116 Mainz

**Entegrasyon Kursu (Integrationskurs):**
Almanya'ya yeni gelenler için devlet destekli Almanca ve Almanya hakkında genel bilgi kursu. Kurs 700 saat Almanca + 100 saat oryantasyon dersinden oluşur. Katılım bazı durumlarda zorunlu, bazı durumlarda isteğe bağlıdır.

**Kimler Başvurabilir:**
- AB dışından gelen ve oturma iznine sahip kişiler
- Yeni vatandaşlık alanlar
- Uzun süredir Almanya'da olan ama Almanca seviyesi yetersiz olanlar

**Başvuru:**
BAMF web sitesinden ya da yerel Ausländerbehörde aracılığıyla başvurulabilir.

**Yurt Dışı Diploma Tanıma:**
anabin.kmk.org — Türk diplomalarının Alman eşdeğerini öğrenebilirsiniz.
Mesleki tanıma için: www.anerkennung-in-deutschland.de

**Vatandaşlık:**
5 yıl yasal ikamet, yeterli Almanca (B1), ekonomik özgürlük ve entegrasyon koşulları sağlandığında başvuru yapılabilir.''',
        'sira': 2,
    },
    {
        'baslik': 'Agentur für Arbeit & Jobcenter',
        'slug': 'agentur-fuer-arbeit',
        'kategori': 'resmi',
        'icon': 'bi-briefcase',
        'ozet': 'İşsizlik parası, iş arama ve Bürgergeld',
        'icerik': '''**Agentur für Arbeit** kısa süreli işsizlik (ALG I) ve iş bulma hizmetleri sunar.
**Jobcenter** uzun süreli işsizlere Bürgergeld (eski Hartz IV) desteği sağlar.

**Mainz Adresi:** Parcusstraße 2, 55116 Mainz
**Telefon (ücretsiz):** 0800 4 5555 00 (Agentur) | 0800 4 5555 70 (Jobcenter)

**ALG I (Arbeitslosengeld I):**
- En az 12 ay sigortalı çalışmış kişilere ödenir
- Son brüt maaşın %60'ı (çocuğu olanlar %67)
- İş kaybından sonraki 3 gün içinde Agentur'a başvurulmalı

**Bürgergeld (ALG II):**
- Uzun süreli işsizler ya da geliri yetersiz olanlar için
- 2024 itibarıyla tek kişi için ~563€/ay
- Kira yardımı ayrıca ödenir

**İş Arama Platformları:**
- www.arbeitsagentur.de/jobsuche (resmi)
- www.indeed.de
- www.stepstone.de
- www.linkedin.com

**Önemli:** İşsiz kaldığınızda ilk 3 gün içinde başvurmazsanız hak kaybı yaşanabilir.''',
        'sira': 3,
    },
    {
        'baslik': 'Ehliyet — Türk Ehliyetini Almana Dönüştürme',
        'slug': 'ehliyet-donusum',
        'kategori': 'resmi',
        'icon': 'bi-car-front',
        'ozet': 'Türk ehliyetini Alman ehliyetine dönüştürme adımları ve belgeler',
        'icerik': '''Türkiye'de alınan ehliyet, Almanya'da belirli süre kullanılabilir; ancak kalıcı oturum için Alman ehliyetine dönüştürülmesi gerekir.

**Dönüşüm Hakkı:**
Türkiye, AB üyesi olmadığından ehliyet dönüşümü için sınav gerekmektedir. Ancak bazı kategoriler için teorik sınav muafiyeti mümkündür — Führerscheinstelle'ye başvurarak öğrenin.

**Başvuru Yeri:** Führerscheinstelle Mainz
Valenciaplatz 3, 55118 Mainz — Randevu zorunludur.

**Gerekli Belgeler:**
- Geçerli pasaport + fotokopi
- Anmeldung belgesi (ikamet tescil belgesi)
- Mevcut Türk ehliyeti (orijinal + fotokopi)
- Türk ehliyetinin noter onaylı Almanca çevirisi
- Biyometrik fotoğraf (35x45mm)
- Sehsttest (göz testi) belgesi — optisyen veya göz doktorundan
- Erste-Hilfe-Kurs (ilk yardım kursu) sertifikası (genellikle 9 saat)

**Süreç:**
1. Führerscheinstelle'ye randevu al
2. Belgelerini tamamla
3. Başvur, sınav hakkı/muafiyetini öğren
4. Gerekirse teorik ve/veya pratik sınava gir
5. Alman ehliyetini teslim al

**Sürücü Okulları (Fahrschule):**
Mainz'da çeşitli sürücü okulları mevcuttur. Türkçe hizmet veren okullar için forumumuzu inceleyin.

**Not:** Türk ehliyetiyle Almanya'ya ilk geldiğinizde 6 ay kadar geçerlidir. Daimi ikamet sonrası en kısa sürede dönüşüm başlatın.''',
        'sira': 4,
    },
    {
        'baslik': 'Anmeldung — İkamet Tescili',
        'slug': 'anmeldung',
        'kategori': 'resmi',
        'icon': 'bi-house-check',
        'ozet': 'Almanya\'ya taşındığınızda yapılması zorunlu adres kaydı',
        'icerik': '''Anmeldung, Almanya'ya taşınan herkesin yapmak zorunda olduğu ikamet tescil işlemidir. Taşınmadan itibaren **2 hafta** içinde yapılmalıdır.

**Başvuru Yeri (Mainz):**
Einwohnermeldeamt — Stadthaus Rheinufer, Rheinstraße 55, 55116 Mainz
veya herhangi bir Bürgeramt şubesi

**Gerekli Belgeler:**
- Pasaport (orijinal)
- Wohnungsgeberbestätigung: Ev sahibinin imzaladığı ikamet onay belgesi (kiracı olarak taşınıyorsanız ev sahibinden alınır)
- Doldurulmuş Anmeldeformular (belediye web sitesinden indirebilirsiniz)

**Anmeldung Sonrası:**
- Anmeldebestätigung (tescil belgesi) size verilir — bunu saklayın!
- Bu belge: banka hesabı açmak, Ausländerbehörde, Finanzamt ve diğer işlemler için zorunludur.
- Steueridentifikationsnummer (vergi kimlik numarası) 2-4 hafta içinde posta ile gelir.

**Ummeldung (Adres Değişikliği):**
Taşındığınızda yeni adresinizi 2 hafta içinde bildirmeniz gerekir. Aynı ofiste yapılır.

**Abmeldung (Çıkış Kaydı):**
Almanya'dan ayrıldığınızda ya da yurt dışına taşındığınızda yapılır.''',
        'sira': 5,
    },
    {
        'baslik': 'Almanca Çalışma — Kaynaklar ve Kurslar',
        'slug': 'almanca-calisma',
        'kategori': 'almanca',
        'icon': 'bi-translate',
        'ozet': 'Almanca öğrenmek için ücretsiz ve ücretli kaynaklar',
        'icerik': '''Almanca öğrenmek entegrasyonun en kritik adımıdır. Aşağıda hem ücretsiz hem ücretli kaynakları bulabilirsiniz.

**Ücretsiz Kaynaklar:**
- **Deutsche Welle (DW Deutsch):** dw.com/de/deutsch-lernen — Her seviyeye uygun ücretsiz Almanca kursu
- **Duolingo:** Günlük pratik için ideal başlangıç uygulaması
- **Babbel:** Yapılandırılmış dil öğrenimi (kısmen ücretli)
- **Nicos Weg (ARD):** Göçmenler için özel hazırlanmış video dizi ile Almanca
- **YouTube — Easy German:** Günlük konuşma Almancası, altyazılı

**Sınav Hazırlığı:**
- A1, A2, B1, B2, C1, C2 seviyeleri
- Goethe-Institut sınavları: goethe.de
- telc sınavları: telc.net
- Vatandaşlık için minimum B1 gerekir

**Mainz'da Kurslar:**
- **VHS Mainz:** En uygun fiyatlı seçenek — vhs-mainz.de
- **BAMF Entegrasyon Kursu:** Hak sahibiyseniz ücretsiz veya indirimli
- **Goethe-Institut Frankfurt:** Yüksek kaliteli, ücretli
- **Berlitz Mainz:** Yoğun ve özel kurslar

**Pratik İpuçları:**
- Alman komşularınızla Almanca konuşmaya çalışın
- Alışveriş, doktor, market — her fırsatı Almanca pratik için kullanın
- Tandem partner bulun: tandem-city.com
- Yerel kütüphane ücretsiz kitap ve medya sunar''',
        'sira': 1,
    },
    {
        'baslik': 'Sağlık Sigortası — Krankenkasse',
        'slug': 'krankenkasse',
        'kategori': 'saglik',
        'icon': 'bi-heart-pulse',
        'ozet': 'Almanya\'da sağlık sigortası seçimi ve nasıl çalışır',
        'icerik': '''Almanya'da tüm çalışanlar sağlık sigortasına (Krankenkasse) sahip olmak zorundadır.

**Kamu Sigortası (Gesetzliche Krankenversicherung — GKV):**
Maaşın yaklaşık %14.6'sı (işçi + işveren paylaşımlı). Aile üyeleri (eş, çocuklar) çoğunlukla ücretsiz sigortalanır.

**Büyük GKV Sigortacıları:**
- AOK Rheinland-Pfalz/Saarland (www.aok.de)
- TK — Techniker Krankenkasse (www.tk.de)
- Barmer (www.barmer.de)
- DAK Gesundheit (www.dak.de)
- IKK (www.ikk.de)

**Doktor Ziyareti:**
- Aile doktoru (Hausarzt) seçin — her işlem için önce buraya gidin
- Uzman doktora gitmek için genellikle Hausarzt'tan sevk (Überweisung) gerekir
- Acil durumlarda: 112 (ambulans) veya 116 117 (gece/hafta sonu doktor)

**Diş Sağlığı:**
Temel diş tedavileri sigortaya dahildir. Dolgu, çekim vb. ücretsiz. Diş protezi ve estetik için ek ödeme gerekebilir.

**İlaç:**
Reçeteli ilaçlarda 5-10€ katkı payı ödenir. Çocuk ilaçları ücretsizdir.

**Özel Sigorta (PKV):**
Yüksek gelirli çalışanlar ya da serbest meslek sahipleri tercih edebilir. Daha geniş kapsam ama çocuklar ayrıca sigortalanmalı.''',
        'sira': 1,
    },
    {
        'baslik': 'Ulaşım — Mainz\'da Toplu Taşıma',
        'slug': 'ulasim',
        'kategori': 'ulasim',
        'icon': 'bi-bus-front',
        'ozet': 'MVG, RNN ve Deutschlandticket ile şehir içi ve çevre ulaşım',
        'icerik': '''**MVG (Mainzer Verkehrsgesellschaft)**
Mainz şehir içi otobüs ve tramvay işleticisi.
Web: www.mvg-mainz.de | Uygulama: MVG App

**Bilet Türleri:**
- Einzelticket (tek biniş): ~2.50€
- 4er-Karte (4'lü): tasarruflu
- Tageskarte (günlük): ~6€ (tüm gün sınırsız)
- Monatsticket (aylık): ~80€
- **Deutschlandticket: 58€/ay** — tüm Almanya'da yerel ve bölgesel toplu taşıma

**Deutschlandticket:**
En iyi seçenek! Aylık 58€ ile Mainz, Frankfurt, Koblenz ve tüm Almanya'da yerel trenler ve otobüsler. DB uygulamasından ya da MVG'den alınabilir.

**RNN (Rhein-Nahe Nahverkehr)**
Mainz-Bingen, Bingen, Ingelheim ve çevre ilçelere bölgesel otobüs ve tren.
Web: www.rnn.info

**Deutsche Bahn (DB)**
Şehirlerarası tren. Mainz Hauptbahnhof'tan Frankfurt'a ~30 dk, Koblenz'e ~1 saat.

**Bisiklet:**
Mainz bisiklet dostu bir şehirdir. MVGmeinRad bisiklet kiralama sistemi mevcuttur.

**Park:**
Şehir merkezinde ücretli park. P+R (Park and Ride) ile şehir dışına araç bırakıp toplu taşıma kullanabilirsiniz.''',
        'sira': 1,
    },
]

FORUM_KATEGORILER = [
    {'ad': 'Genel Sohbet', 'aciklama': 'Mainz ve çevresinde genel konular, tanışma', 'sira': 1},
    {'ad': 'Resmi İşlemler', 'aciklama': 'Behörde, BAMF, pasaport, ehliyet, Anmeldung sorularınız', 'sira': 2},
    {'ad': 'İş & Kariyer', 'aciklama': 'İş arama, Almanca CV, referans mektupları', 'sira': 3},
    {'ad': 'Konut & Ev', 'aciklama': 'Kiralık ev, WG arama, kira sözleşmesi', 'sira': 4},
    {'ad': 'Araç & Ulaşım', 'aciklama': 'Araç alım-satım, sigorta, ehliyet, TÜV', 'sira': 5},
    {'ad': 'Almanca Öğreniyorum', 'aciklama': 'Dil soruları, kurs önerileri, pratik yapma', 'sira': 6},
    {'ad': 'Çocuk & Aile', 'aciklama': 'Kreş, okul, çocuk hakları', 'sira': 7},
    {'ad': 'Sağlık', 'aciklama': 'Doktor, sigorta, ilaç soruları', 'sira': 8},
    {'ad': 'Gezi & Aktivite', 'aciklama': 'Mainz ve çevresinde gezilecek yerler, etkinlikler', 'sira': 9},
    {'ad': 'İlanlar & Takas', 'aciklama': 'Ücretsiz küçük ilanlar, yardımlaşma', 'sira': 10},
]


class Command(BaseCommand):
    help = 'Temel statik veriyi (yerler, linkler, rehber, forum) veritabanına yükler.'

    def handle(self, *args, **options):
        self._seed_yerler()
        self._seed_linkler()
        self._seed_rehber()
        self._seed_forum()
        self.stdout.write(self.style.SUCCESS('\nTüm seed verisi başarıyla yüklendi.'))

    def _seed_yerler(self):
        self.stdout.write('\nYerler yükleniyor...')
        eklendi = 0
        for veri in YERLER:
            _, created = Yer.objects.get_or_create(
                ad=veri['ad'],
                defaults=veri
            )
            if created:
                eklendi += 1
                self.stdout.write(f'  + {veri["ad"]}')
        self.stdout.write(f'  → {eklendi} yer eklendi.')

    def _seed_linkler(self):
        self.stdout.write('\nLinkler yükleniyor...')
        eklendi = 0
        for veri in LINKLER:
            _, created = OnemliLink.objects.get_or_create(
                ad=veri['ad'],
                defaults=veri
            )
            if created:
                eklendi += 1
                self.stdout.write(f'  + {veri["ad"]}')
        self.stdout.write(f'  → {eklendi} link eklendi.')

    def _seed_rehber(self):
        self.stdout.write('\nRehber sayfaları yükleniyor...')
        eklendi = 0
        for veri in REHBER_SAYFALARI:
            _, created = RehberSayfasi.objects.get_or_create(
                slug=veri['slug'],
                defaults=veri
            )
            if created:
                eklendi += 1
                self.stdout.write(f'  + {veri["baslik"]}')
        self.stdout.write(f'  → {eklendi} rehber sayfası eklendi.')

    def _seed_forum(self):
        self.stdout.write('\nForum kategorileri yükleniyor...')
        eklendi = 0
        for veri in FORUM_KATEGORILER:
            _, created = ForumKategori.objects.get_or_create(
                ad=veri['ad'],
                defaults=veri
            )
            if created:
                eklendi += 1
                self.stdout.write(f'  + {veri["ad"]}')
        self.stdout.write(f'  → {eklendi} forum kategorisi eklendi.')
