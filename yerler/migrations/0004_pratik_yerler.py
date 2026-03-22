"""
Data migration: Mainz ve Mainz-Bingen için pratik/günlük hayat yerleri eklenir.
Kategoriler: resmi_kurum, saglik, egitim, ibadet, turk_market, alisveris, tuv, yeme_icme
"""
from django.db import migrations


MAINZ_YERLER = [
    # ── Resmi Kurum ──────────────────────────────────────────────────────────
    dict(
        ad='Ausländerbehörde Mainz',
        kategori='resmi_kurum',
        adres='Valenciaplatz 3, 55118 Mainz',
        sehir='Mainz',
        website='https://www.mainz.de/vv/produkte/landes-und-landeshauptstadt/auslaenderamt.php',
        maps_url='https://maps.google.com/?q=Ausländerbehörde+Mainz+Valenciaplatz',
        aciklama='Oturma izni, vize uzatma ve yabancılar hukuku işlemleri.',
        icerik=(
            '<p>Mainz Ausländerbehörde, oturma izni (Aufenthaltserlaubnis), çalışma izni ve Niederlassungserlaubnis '
            'gibi tüm yabancı işlemlerinin yürütüldüğü resmi kurumdur.</p>'
            '<h4>Hangi İşlemler Yapılır?</h4>'
            '<ul>'
            '<li>Aufenthaltserlaubnis (oturma izni) başvurusu ve uzatma</li>'
            '<li>Niederlassungserlaubnis (süresiz oturma izni)</li>'
            '<li>Aile birleşimi başvuruları</li>'
            '<li>Reiseausweis (seyahat belgesi)</li>'
            '<li>EU Freizügigkeitsbescheinigung</li>'
            '</ul>'
            '<h4>Randevu Almak İçin</h4>'
            '<p>Randevu zorunludur. Online randevu sisteminden veya telefonla alınabilir.</p>'
            '<div class="info-box"><strong>📍 Adres:</strong> Valenciaplatz 3, 55118 Mainz<br>'
            '<strong>📞 Tel:</strong> 06131 12-0<br>'
            '<strong>🕐 Saatler:</strong> Randevu ile Pazartesi–Cuma</div>'
        ),
        aktif=True,
    ),
    dict(
        ad='Finanzamt Mainz-Stadt',
        kategori='resmi_kurum',
        adres='Ernst-Ludwig-Straße 14, 55116 Mainz',
        sehir='Mainz',
        maps_url='https://maps.google.com/?q=Finanzamt+Mainz+Ernst-Ludwig-Straße',
        aciklama='Vergi beyannamesi, vergi numarası ve gelir vergisi işlemleri.',
        icerik=(
            '<p>Mainz-Stadt Finanzamt, gelir vergisi (Einkommensteuer), vergi numarası (Steuernummer) ve vergi iadesi '
            'işlemlerini yürüten devlet kurumudur.</p>'
            '<h4>Sık Yapılan İşlemler</h4>'
            '<ul>'
            '<li>Steuernummer (vergi numarası) alma</li>'
            '<li>Steuererklärung (vergi beyannamesi) teslimi</li>'
            '<li>Steuererstattung (vergi iadesi) takibi</li>'
            '<li>Gewerbeanmeldung vergi tescili</li>'
            '</ul>'
            '<h4>ELSTER — Online Vergi</h4>'
            '<p>Vergi beyannamesi <a href="https://www.elster.de" target="_blank">ELSTER</a> sistemi üzerinden '
            'online verilebilir. Ücretsizdir ve belge posta/fiziksel teslim gerekmez.</p>'
            '<div class="info-box"><strong>📍 Adres:</strong> Ernst-Ludwig-Straße 14, 55116 Mainz<br>'
            '<strong>📞 Tel:</strong> 06131 605-0<br>'
            '<strong>🕐 Saatler:</strong> Pazartesi–Cuma 08:00–15:00</div>'
        ),
        aktif=True,
    ),
    # ── Sağlık ───────────────────────────────────────────────────────────────
    dict(
        ad='Universitätsmedizin Mainz (Uniklinik)',
        kategori='saglik',
        adres='Langenbeckstraße 1, 55131 Mainz',
        sehir='Mainz',
        website='https://www.unimedizin-mainz.de/',
        maps_url='https://maps.google.com/?q=Universitätsmedizin+Mainz',
        aciklama='RLP\'nin en büyük üniversite hastanesi. Acil ve tüm uzmanlık branşları.',
        icerik=(
            '<p>Universitätsmedizin Mainz (UMM), Rheinland-Pfalz\'ın en büyük ve en kapsamlı hastanesidir. '
            '60\'tan fazla uzmanlık kliniği ile yaklaşık 1.500 yatak kapasitesine sahiptir.</p>'
            '<h4>Acil Servis (Notaufnahme)</h4>'
            '<p>Acil servise doğrudan gidebilirsiniz, randevu gerekmez. Ambulans için <strong>112</strong>\'yi arayın.</p>'
            '<h4>Uzmanlık Klinikleri</h4>'
            '<p>Kardiyoloji, onkoloji, nöroloji, ortopedi, göz, kulak-burun-boğaz ve daha birçok branşta '
            'hizmet vermektedir. Randevular online veya telefonla alınabilir.</p>'
            '<h4>Tercüman Desteği</h4>'
            '<p>Hastane, ihtiyaç halinde Türkçe dahil birçok dilde tercüman hizmeti sunmaktadır. '
            'Randevu sırasında belirtmeniz yeterlidir.</p>'
            '<div class="info-box"><strong>📍 Adres:</strong> Langenbeckstraße 1, 55131 Mainz<br>'
            '<strong>📞 Acil:</strong> 112 | Hastane: 06131 17-0<br>'
            '<strong>🚌 Ulaşım:</strong> Tram 50/51 — Uniklinik durağı</div>'
        ),
        aktif=True,
    ),
    # ── Eğitim ───────────────────────────────────────────────────────────────
    dict(
        ad='VHS Mainz — Volkshochschule',
        kategori='egitim',
        adres='Raimundistraße 4, 55118 Mainz',
        sehir='Mainz',
        website='https://www.vhs-mainz.de/',
        maps_url='https://maps.google.com/?q=VHS+Mainz+Raimundistraße',
        aciklama='Almanca dil kursları, entegrasyon kursu ve yetişkin eğitimi.',
        icerik=(
            '<p>Mainz Volkshochschule (VHS), Almanca öğrenme, entegrasyon kursu (Integrationskurs) ve '
            'yetişkin eğitimi alanında kapsamlı kurslar sunan belediye eğitim kurumudur.</p>'
            '<h4>Integrationskurs (Entegrasyon Kursu)</h4>'
            '<p>BAMF tarafından finanse edilen ve yasal olarak hak edilen entegrasyon kursları VHS Mainz\'de '
            'verilmektedir. Kurs; Almanca dil eğitimi (A1–B1) ve oryantasyon kursundan oluşur. '
            'Başvuru için BAMF\'ın zulassungs listesini kontrol edin veya doğrudan VHS\'e başvurun.</p>'
            '<h4>Diğer Kurslar</h4>'
            '<ul>'
            '<li>Almanca A1–C2 (tüm seviyeler)</li>'
            '<li>Berufssprache Deutsch (mesleki Almanca)</li>'
            '<li>Telc ve Goethe sertifika hazırlık</li>'
            '<li>Bilgisayar, kariyer ve kültür kursları</li>'
            '</ul>'
            '<div class="info-box"><strong>📍 Adres:</strong> Raimundistraße 4, 55118 Mainz<br>'
            '<strong>📞 Tel:</strong> 06131 122720<br>'
            '<strong>🌐 Online Kayıt:</strong> vhs-mainz.de</div>'
        ),
        aktif=True,
    ),
    # ── İbadet ───────────────────────────────────────────────────────────────
    dict(
        ad='DITIB Türkisch-Islamische Gemeinde Mainz',
        kategori='ibadet',
        adres='Weichselstraße 18, 55131 Mainz',
        sehir='Mainz',
        maps_url='https://maps.google.com/?q=Türkisch-Islamische+Gemeinde+Mainz+Weichselstraße',
        aciklama='Mainz\'deki ana Türk-İslam cemiyeti camisi. DITIB çatısı altında faaliyet gösterir.',
        icerik=(
            '<p>Mainz\'deki Türkisch-Islamische Gemeinde, DITIB (Diyanet İşleri Türk-İslam Birliği) bünyesinde '
            'faaliyet gösteren ve şehrin en büyük Türk toplumu camisidir.</p>'
            '<h4>Hizmetler</h4>'
            '<ul>'
            '<li>Beş vakit ve Cuma namazı</li>'
            '<li>Kuran kursu</li>'
            '<li>Cenaze ve defin hizmetleri koordinasyonu</li>'
            '<li>Dini danışmanlık</li>'
            '</ul>'
            '<div class="info-box"><strong>📍 Adres:</strong> Weichselstraße 18, 55131 Mainz<br>'
            '<strong>🚌 Ulaşım:</strong> Bus 58 veya yürüme mesafesinde Hauptbahnhof\'a</div>'
        ),
        aktif=True,
    ),
    # ── Türk Marketi ─────────────────────────────────────────────────────────
    dict(
        ad='Türk & Halal Marketler — Mainz Neustadt',
        kategori='turk_market',
        adres='Boppstraße / Rheinallee, 55116 Mainz (Neustadt bölgesi)',
        sehir='Mainz',
        maps_url='https://maps.google.com/?q=Türkischer+Supermarkt+Mainz+Neustadt',
        aciklama='Mainz Neustadt bölgesinde yoğunlaşan Türk ve Orta Doğu gıda marketleri.',
        icerik=(
            '<p>Mainz\'de Türk ve Orta Doğu gıda marketleri başta Neustadt olmak üzere birkaç bölgede yer almaktadır. '
            'Helal et, bakliyat, pastane ürünleri, Türk markalı gıdalar ve mevsim sebze-meyve bulunabilir.</p>'
            '<h4>Ne Bulunur?</h4>'
            '<ul>'
            '<li>Helal et ve tavuk</li>'
            '<li>Türk peyniri, zeytin, zeytinyağı</li>'
            '<li>Bakliyat, bulgur, nohut, mercimek</li>'
            '<li>Türk çayı, kahve ve tatlıları</li>'
            '<li>Mevsim sebze ve meyve</li>'
            '</ul>'
            '<h4>İpucu</h4>'
            '<p>Bölgedeki marketlerin büyük çoğunluğu helal sertifikasına sahiptir. '
            'Büyük süpermarketlerde de "Halal" bölümü bulunabilir.</p>'
            '<div class="info-box"><strong>📍 Bölge:</strong> Mainz Neustadt — Boppstraße ve çevresi<br>'
            '<strong>🚌 Ulaşım:</strong> Hauptbahnhof\'tan yürüyüş mesafesi</div>'
        ),
        aktif=True,
    ),
    # ── Alışveriş ─────────────────────────────────────────────────────────────
    dict(
        ad='Römerpassage — Alışveriş Merkezi',
        kategori='alisveris',
        adres='Römerpassage, 55116 Mainz',
        sehir='Mainz',
        website='https://www.roemerpassage.de/',
        maps_url='https://maps.google.com/?q=Römerpassage+Mainz',
        aciklama='Mainz şehir merkezindeki en büyük alışveriş merkezi. 80\'den fazla mağaza.',
        icerik=(
            '<p>Römerpassage, Mainz\'in kalbinde yer alan ve şehrin en büyük kapalı alışveriş merkezi olan '
            'modern bir AVM\'dir. Dom\'a yürüme mesafesindedir.</p>'
            '<h4>Mağazalar</h4>'
            '<p>H&M, C&A, Zara, Deichmann, MediaMarkt, Douglas ve daha pek çok zincir mağazanın yanı sıra '
            'çok sayıda restoran ve kafe barındırmaktadır.</p>'
            '<h4>Ulaşım</h4>'
            '<p>Mainz Hbf\'den yürüyerek 10 dakika, tramvayla 1 durak. Yakın çevrede ücretli otopark mevcuttur.</p>'
            '<div class="info-box"><strong>📍 Adres:</strong> Römerpassage, 55116 Mainz<br>'
            '<strong>🕐 Saatler:</strong> Pazartesi–Cumartesi 09:30–20:00<br>'
            '<strong>🚌 Tram:</strong> 50/51/52 — Dom/Römerpassage durağı</div>'
        ),
        aktif=True,
    ),
    # ── TÜV ─────────────────────────────────────────────────────────────────
    dict(
        ad='TÜV Rheinland — Mainz',
        kategori='tuv',
        adres='Haifa-Allee 2, 55128 Mainz',
        sehir='Mainz',
        website='https://www.tuv.com/',
        maps_url='https://maps.google.com/?q=TÜV+Rheinland+Mainz',
        aciklama='Araç muayenesi (Hauptuntersuchung / HU), ehliyete geçiş sınavları.',
        icerik=(
            '<p>TÜV Rheinland Mainz, araç muayenesi (Hauptuntersuchung – HU) ve AU (egzoz emisyon testi) '
            'hizmetleri sunan resmi teknik muayene kuruluşudur.</p>'
            '<h4>HU — Araç Muayenesi</h4>'
            '<p>Almanya\'da tüm araçların düzenli HU (Hauptuntersuchung) muayenesinden geçmesi yasal zorunluluktur. '
            'Yeni araçlarda ilk 3 yılda bir, ardından her 2 yılda bir yapılmalıdır.</p>'
            '<h4>Randevu</h4>'
            '<p>Online veya telefon ile randevu alınabilir. TÜV yanı sıra bölgede DEKRA ve GTÜ istasyonları da mevcuttur.</p>'
            '<div class="info-box"><strong>📍 Adres:</strong> Haifa-Allee 2, 55128 Mainz<br>'
            '<strong>📞 Tel:</strong> 0800 888 4000<br>'
            '<strong>🌐</strong> tuv.com üzerinden online randevu</div>'
        ),
        aktif=True,
    ),
]

MAINZ_BINGEN_YERLER = [
    # ── Resmi Kurum ──────────────────────────────────────────────────────────
    dict(
        ad='Kreisverwaltung Mainz-Bingen — Ausländerbehörde',
        kategori='resmi_kurum',
        adres='Barbarossastraße 4, 55218 Ingelheim am Rhein',
        sehir='Ingelheim am Rhein',
        website='https://www.kreis-mainz-bingen.de/politik-verwaltung/auslaenderbehorde/',
        maps_url='https://maps.google.com/?q=Kreisverwaltung+Mainz-Bingen+Ingelheim',
        aciklama='Mainz-Bingen ilçesi yabancılar dairesi. Oturma izni, vize uzatma.',
        icerik=(
            '<p>Mainz-Bingen Kreisverwaltung bünyesindeki Ausländerbehörde, ilçe genelinde oturma izni, '
            'yabancı pasaport ve vize işlemlerini yürüten resmi kurumdur. Ana bina Ingelheim am Rhein\'dadır.</p>'
            '<h4>Hangi İşlemler Yapılır?</h4>'
            '<ul>'
            '<li>Aufenthaltserlaubnis başvuru ve uzatma</li>'
            '<li>Niederlassungserlaubnis (süresiz oturma izni)</li>'
            '<li>Aile birleşimi</li>'
            '<li>Duldung (geçici tolerans belgesi)</li>'
            '<li>Reiseausweis für Ausländer</li>'
            '</ul>'
            '<h4>Randevu</h4>'
            '<p>Online randevu için Kreis Mainz-Bingen resmi sitesini ziyaret edin. '
            'Randevusuz kabul genellikle yapılmamaktadır.</p>'
            '<div class="info-box"><strong>📍 Adres:</strong> Barbarossastraße 4, 55218 Ingelheim am Rhein<br>'
            '<strong>📞 Tel:</strong> 06132 787-0<br>'
            '<strong>🚂 Ulaşım:</strong> Ingelheim Bahnhof\'tan ~10 dk yürüyüş</div>'
        ),
        aktif=True,
    ),
    dict(
        ad='Jobcenter Mainz-Bingen',
        kategori='resmi_kurum',
        adres='Bahnhofstraße 16, 55411 Bingen am Rhein',
        sehir='Bingen am Rhein',
        website='https://www.jobcenter-mainz-bingen.de/',
        maps_url='https://maps.google.com/?q=Jobcenter+Mainz-Bingen+Bingen',
        aciklama='İşsizlik yardımı (ALG II / Bürgergeld), iş arama desteği ve sosyal yardım.',
        icerik=(
            '<p>Mainz-Bingen Jobcenter, ilçede ikamet eden ve çalışmayan veya düşük gelirli bireylere '
            'Bürgergeld (eski adıyla ALG II) ve sosyal destek hizmetleri sunar.</p>'
            '<h4>Hangi Destekler Sağlanır?</h4>'
            '<ul>'
            '<li>Bürgergeld (geçim yardımı)</li>'
            '<li>Konut gideri desteği (KdU)</li>'
            '<li>İş arama ve mesleki rehberlik</li>'
            '<li>Eğitim ve nitelendirme destekleri</li>'
            '</ul>'
            '<h4>Başvuru İçin Gerekenler</h4>'
            '<p>Kimlik/pasaport, oturma izni, banka hesap bilgileri, kira sözleşmesi ve gelir belgesi.</p>'
            '<div class="info-box"><strong>📍 Adres:</strong> Bahnhofstraße 16, 55411 Bingen am Rhein<br>'
            '<strong>📞 Tel:</strong> 06721 9810-0<br>'
            '<strong>🚂 Ulaşım:</strong> Bingen Bahnhof\'tan ~5 dk yürüyüş</div>'
        ),
        aktif=True,
    ),
    dict(
        ad='Finanzamt Bingen-Alzey',
        kategori='resmi_kurum',
        adres='Wörthstraße 2-4, 55411 Bingen am Rhein',
        sehir='Bingen am Rhein',
        maps_url='https://maps.google.com/?q=Finanzamt+Bingen+Wörthstraße',
        aciklama='Vergi beyannamesi, vergi numarası ve gelir vergisi işlemleri.',
        icerik=(
            '<p>Bingen-Alzey Finanzamt, Mainz-Bingen ilçesindeki mükellefler için vergi numarası, '
            'beyanname ve vergi iadesi işlemlerini yürüten devlet kurumudur.</p>'
            '<h4>Önemli Bilgiler</h4>'
            '<ul>'
            '<li>Steuernummer (vergi numarası) kaydı</li>'
            '<li>Yıllık Steuererklärung teslimi</li>'
            '<li>Werbungskosten, Kinderfreibetrag gibi indirimler</li>'
            '</ul>'
            '<h4>ELSTER ile Online Beyanname</h4>'
            '<p>Vergi beyannamenizi <a href="https://www.elster.de" target="_blank">elster.de</a> üzerinden '
            'ücretsiz olarak online verebilirsiniz.</p>'
            '<div class="info-box"><strong>📍 Adres:</strong> Wörthstraße 2-4, 55411 Bingen am Rhein<br>'
            '<strong>📞 Tel:</strong> 06721 93-0</div>'
        ),
        aktif=True,
    ),
    # ── Sağlık ───────────────────────────────────────────────────────────────
    dict(
        ad='Nahe-Krankenhaus Bingen',
        kategori='saglik',
        adres='Rochusallee 5, 55411 Bingen am Rhein',
        sehir='Bingen am Rhein',
        website='https://www.nahe-krankenhaus.de/',
        maps_url='https://maps.google.com/?q=Nahe-Krankenhaus+Bingen+Rochusallee',
        aciklama='Bingen\'in ana hastanesi. Acil servis, dahiliye, cerrahi ve doğum bölümleri.',
        icerik=(
            '<p>Nahe-Krankenhaus Bingen, Mainz-Bingen ilçesinin merkez hastanesidir. '
            'Dahiliye, cerrahi, kadın doğum ve acil hizmetleri sunar.</p>'
            '<h4>Acil Servis (Notaufnahme)</h4>'
            '<p>Acil durumda doğrudan hastaneye gidebilir ya da <strong>112</strong> numaralı ambulansı arayabilirsiniz. '
            'Acil olmayan durumlar için önce <strong>116 117</strong> (Bereitschaftsdienst) numarasını arayın.</p>'
            '<h4>Önemli Telefon Numaraları</h4>'
            '<ul>'
            '<li><strong>112</strong> — Ambulans / Acil</li>'
            '<li><strong>116 117</strong> — Gece ve hafta sonu doktor hattı</li>'
            '<li><strong>110</strong> — Polis</li>'
            '</ul>'
            '<div class="info-box"><strong>📍 Adres:</strong> Rochusallee 5, 55411 Bingen am Rhein<br>'
            '<strong>📞 Tel:</strong> 06721 891-0<br>'
            '<strong>📞 Acil:</strong> 112</div>'
        ),
        aktif=True,
    ),
    # ── Eğitim ───────────────────────────────────────────────────────────────
    dict(
        ad='VHS Mainz-Bingen — Volkshochschule',
        kategori='egitim',
        adres='Neugasse 2, 55218 Ingelheim am Rhein',
        sehir='Ingelheim am Rhein',
        website='https://www.vhs-mainz-bingen.de/',
        maps_url='https://maps.google.com/?q=VHS+Mainz-Bingen+Ingelheim',
        aciklama='Almanca dil kursları, entegrasyon kursu (BAMF onaylı) ve yetişkin eğitimi.',
        icerik=(
            '<p>VHS Mainz-Bingen, Mainz-Bingen ilçesinde BAMF onaylı entegrasyon kursları ve Almanca dil '
            'eğitimi sunan bölgenin en kapsamlı halk eğitim merkezidir.</p>'
            '<h4>Integrationskurs — Entegrasyon Kursu</h4>'
            '<p>BAMF tarafından finanse edilen entegrasyon kursları A1 seviyesinden B1 seviyesine kadar '
            'Almanca eğitimi (600 saat) ve oryantasyon kursunu (100 saat) kapsar. '
            'Kurs ücreti BAMF tarafından büyük ölçüde karşılanır.</p>'
            '<h4>Kimler Başvurabilir?</h4>'
            '<ul>'
            '<li>Almanya\'ya yeni gelen göçmenler</li>'
            '<li>Uzun süreli ikamet edenler (koşullara bağlı)</li>'
            '<li>Mülteciler (uygun statüdekiler)</li>'
            '</ul>'
            '<div class="info-box"><strong>📍 Adres:</strong> Neugasse 2, 55218 Ingelheim am Rhein<br>'
            '<strong>📞 Tel:</strong> 06132 7827-0<br>'
            '<strong>🚂 Ulaşım:</strong> Ingelheim Bahnhof yakını</div>'
        ),
        aktif=True,
    ),
    # ── İbadet ───────────────────────────────────────────────────────────────
    dict(
        ad='Türkisch-Islamische Gemeinde Bingen (DITIB)',
        kategori='ibadet',
        adres='Vorstadt 24, 55411 Bingen am Rhein',
        sehir='Bingen am Rhein',
        maps_url='https://maps.google.com/?q=Türkisch-Islamische+Gemeinde+Bingen',
        aciklama='Bingen am Rhein\'daki Türk-İslam Cemaati camisi.',
        icerik=(
            '<p>Bingen am Rhein\'daki Türkisch-Islamische Gemeinde, DITIB bünyesinde faaliyet göstermekte olup '
            'bölgedeki Türk Müslümanlara dinî hizmet sunmaktadır.</p>'
            '<h4>Hizmetler</h4>'
            '<ul>'
            '<li>Beş vakit ve Cuma namazı</li>'
            '<li>Kuran kursu (çocuk ve yetişkin)</li>'
            '<li>Dinî danışmanlık ve rehberlik</li>'
            '<li>Cenaze koordinasyonu</li>'
            '</ul>'
            '<div class="info-box"><strong>📍 Adres:</strong> Vorstadt 24, 55411 Bingen am Rhein<br>'
            '<strong>🚂 Ulaşım:</strong> Bingen Hauptbahnhof yakını</div>'
        ),
        aktif=True,
    ),
    dict(
        ad='İslam Cemaat Merkezi Ingelheim',
        kategori='ibadet',
        adres='Ingelheim am Rhein',
        sehir='Ingelheim am Rhein',
        maps_url='https://maps.google.com/?q=Moschee+Ingelheim+am+Rhein',
        aciklama='Ingelheim am Rhein\'daki cami ve İslam cemaat merkezi.',
        icerik=(
            '<p>Ingelheim am Rhein\'da yaşayan Müslümanlar için yerel cami ve cemaat merkezi. '
            'Cuma namazı ve dinî etkinlikler düzenlenmektedir.</p>'
            '<div class="info-box"><strong>📍 Şehir:</strong> Ingelheim am Rhein<br>'
            '<em>Güncel adres için Google Maps\'te "Moschee Ingelheim" araması yapabilirsiniz.</em></div>'
        ),
        aktif=True,
    ),
    # ── Türk Marketi ─────────────────────────────────────────────────────────
    dict(
        ad='Türk & Halal Marketler — Bingen am Rhein',
        kategori='turk_market',
        adres='Bingen am Rhein — Schloßberg / Vorstadt bölgesi',
        sehir='Bingen am Rhein',
        maps_url='https://maps.google.com/?q=Türkischer+Supermarkt+Bingen+am+Rhein',
        aciklama='Bingen am Rhein\'da Türk ve Orta Doğu gıda ürünleri satan marketler.',
        icerik=(
            '<p>Bingen am Rhein\'da şehir merkezine yakın konumlarda Türk ve Orta Doğu gıdaları sunan '
            'çeşitli marketler bulunmaktadır.</p>'
            '<h4>Ne Bulunur?</h4>'
            '<ul>'
            '<li>Helal et ve tavuk</li>'
            '<li>Türk peyniri, zeytin, bakliyat</li>'
            '<li>Türk çayı, kahve ve tatlıları</li>'
            '<li>Mevsim sebze-meyve</li>'
            '</ul>'
            '<div class="info-box"><strong>📍 Bölge:</strong> Bingen Innenstadt<br>'
            '<strong>🚂 Ulaşım:</strong> Bingen Hauptbahnhof\'a yürüme mesafesi</div>'
        ),
        aktif=True,
    ),
    # ── Alışveriş ─────────────────────────────────────────────────────────────
    dict(
        ad='Bingen Innenstadt — Alışveriş Merkezi',
        kategori='alisveris',
        adres='Basilikastraße / Schloßberg, 55411 Bingen am Rhein',
        sehir='Bingen am Rhein',
        maps_url='https://maps.google.com/?q=Bingen+am+Rhein+Innenstadt+Einkaufen',
        aciklama='Bingen şehir merkezinde alışveriş caddeleri, zincir mağazalar ve yerel dükkanlar.',
        icerik=(
            '<p>Bingen am Rhein\'ın şehir merkezi (Innenstadt), yayalara açık alışveriş caddeleri ile '
            'günlük alışveriş ihtiyaçlarını karşılamak için ideal bir bölgedir.</p>'
            '<h4>Mağaza Türleri</h4>'
            '<ul>'
            '<li>Zincir giyim mağazaları (H&M, C&A, Deichmann vb.)</li>'
            '<li>Süpermarketler (REWE, Lidl, ALDI)</li>'
            '<li>Eczane ve drogheri mağazaları (dm, Rossmann)</li>'
            '<li>Yerel dükkanlar ve kasaplar</li>'
            '</ul>'
            '<h4>Pazar (Wochenmarkt)</h4>'
            '<p>Bingen\'de haftalık açık pazar kurulmaktadır. Taze sebze, meyve ve yerel ürünler satılır.</p>'
            '<div class="info-box"><strong>📍 Bölge:</strong> Bingen Innenstadt — Basilikastraße<br>'
            '<strong>🚂 Ulaşım:</strong> Bingen Hauptbahnhof\'tan ~5 dk yürüyüş</div>'
        ),
        aktif=True,
    ),
    # ── TÜV ─────────────────────────────────────────────────────────────────
    dict(
        ad='GTÜ / TÜV İstasyonu — Bingen am Rhein',
        kategori='tuv',
        adres='Bingen am Rhein',
        sehir='Bingen am Rhein',
        maps_url='https://maps.google.com/?q=TÜV+Bingen+am+Rhein',
        aciklama='Bingen ve Ingelheim bölgesinde araç muayenesi (HU/AU) istasyonları.',
        icerik=(
            '<p>Mainz-Bingen ilçesinde TÜV, GTÜ ve DEKRA gibi teknik muayene kuruluşlarına ait '
            'istasyonlar Bingen ve Ingelheim\'da bulunmaktadır.</p>'
            '<h4>HU — Araç Muayenesi</h4>'
            '<p>Yeni araçlarda ilk 3 yılda bir, ardından her 2 yılda bir HU (Hauptuntersuchung) yaptırmak '
            'yasal zorunluluktur. AU (egzoz testi) genellikle HU ile birlikte yapılır.</p>'
            '<h4>Randevu</h4>'
            '<p>TÜV, GTÜ veya DEKRA\'nın resmi web sitesi üzerinden ya da telefonla randevu alınabilir.</p>'
            '<div class="info-box"><strong>📍 Bölge:</strong> Bingen am Rhein ve Ingelheim am Rhein<br>'
            '<strong>🌐</strong> tuv.com | dekra.de | gtue.de</div>'
        ),
        aktif=True,
    ),
    # ── Yeme & İçme ──────────────────────────────────────────────────────────
    dict(
        ad='Türk & Döner Restoranlar — Bingen / Ingelheim',
        kategori='yeme_icme',
        adres='Bingen am Rhein ve Ingelheim am Rhein merkez',
        sehir='Bingen am Rhein',
        maps_url='https://maps.google.com/?q=Döner+Bingen+am+Rhein',
        aciklama='Bingen ve Ingelheim\'da Türk mutfağı, döner ve kebap restoranları.',
        icerik=(
            '<p>Bingen am Rhein ve Ingelheim am Rhein şehir merkezlerinde Türk restoranları, '
            'döner-kebap dükkanları ve lahmacun salonları bulunmaktadır.</p>'
            '<h4>İpucu</h4>'
            '<p>Google Maps\'te "Türkisches Restaurant Bingen" veya "Döner Ingelheim" aratarak '
            'güncel listeye ve müşteri yorumlarına ulaşabilirsiniz.</p>'
            '<div class="info-box"><strong>📍 Bölge:</strong> Bingen ve Ingelheim şehir merkezleri<br>'
            '<strong>🌐</strong> Google Maps ile güncel listelere bakın</div>'
        ),
        aktif=True,
    ),
]


def ekle(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    Stadt = apps.get_model('stadt', 'Stadt')

    try:
        mainz = Stadt.objects.get(slug='mainz')
        mainz_bingen = Stadt.objects.get(slug='mainz-bingen')
    except Stadt.DoesNotExist:
        return

    for d in MAINZ_YERLER:
        Yer.objects.get_or_create(ad=d['ad'], defaults={**d, 'stadt': mainz, 'scope': 'stadt'})

    for d in MAINZ_BINGEN_YERLER:
        Yer.objects.get_or_create(ad=d['ad'], defaults={**d, 'stadt': mainz_bingen, 'scope': 'stadt'})


def geri_al(apps, schema_editor):
    Yer = apps.get_model('yerler', 'Yer')
    tum_adlar = [d['ad'] for d in MAINZ_YERLER + MAINZ_BINGEN_YERLER]
    Yer.objects.filter(ad__in=tum_adlar).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yerler', '0003_yer_scope_yer_stadt_alter_yer_sehir'),
        ('stadt', '0006_ayristry_mainz_bingen'),
    ]

    operations = [
        migrations.RunPython(ekle, geri_al),
    ]
