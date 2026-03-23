"""
Gezi & Kültür yerlerini ekler.
Kullanım: python yerler_seed.py
"""
import os, django, hashlib
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from yerler.models import Yer


def wiki_img(filename, width=1280):
    h = hashlib.md5(filename.encode()).hexdigest()
    return f'https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{filename}/{width}px-{filename}'


YERLER = [
    {
        'ad': 'Mainz Katedrali (Mainzer Dom)',
        'kategori': 'gezi',
        'adres': 'Domstraße 3',
        'sehir': 'Mainz',
        'website': 'https://bistummainz.de/mainzer-dom/start/index.html',
        'maps_url': 'https://maps.google.com/?q=Mainzer+Dom',
        'kapak_resmi': wiki_img('Mainz_Dom_BW_2012-08-18_16-18-12.JPG'),
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Mainzer_Dom',
        'icerik': (
            '<p>Mainz Katedrali, şehrin silüetine yön veren bu 1000 yıllık devasa yapı, Romanesk mimarisinin '
            'Almanya\'daki en iyi örneklerinden biridir. Kırmızı kumtaşından yapılmış kuleleriyle büyüleyici bir görünüme sahiptir.</p>'
            '<h4>Tarihçe</h4>'
            '<p>975 yılında temeli atılan katedral, Kutsal Roma İmparatorluğu döneminde taç giyme törenlerine ve önemli dini '
            'ayinlere ev sahipliği yapmıştır. Bugün hâlâ aktif bir kilise olarak hizmet vermektedir.</p>'
            '<h4>Mimari</h4>'
            '<p>Altı kulesi ve kırmızı kumtaşından inşa edilmiş cephesiyle Mainz\'in en tanımlayıcı yapısıdır. '
            'İç mekânda Romanesk, Gotik ve Barok unsurlar bir arada bulunur.</p>'
            '<div class="info-box"><strong>📍 Ziyaret Bilgileri</strong><br>Giriş: Ücretsiz<br>Açık: Her gün 09:00–18:30</div>'
        ),
    },
    {
        'ad': 'Gutenberg Müzesi',
        'kategori': 'gezi',
        'adres': 'Liebfrauenplatz 5',
        'sehir': 'Mainz',
        'website': 'https://www.gutenberg-museum.de/',
        'maps_url': 'https://maps.google.com/?q=Gutenberg+Museum+Mainz',
        'kapak_resmi': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Tore_am_Gutenberg-Museum,_Liebfrauenplatz,_Mainz.jpg/1280px-Tore_am_Gutenberg-Museum,_Liebfrauenplatz,_Mainz.jpg',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Gutenberg-Museum',
        'icerik': (
            '<p>Matbaanın mucidi Johannes Gutenberg\'in doğduğu şehirde yer alan bu müzede, dünyada geriye kalan '
            'nadir orijinal Gutenberg İncillerinden ikisini kendi gözlerinizle görebilirsiniz.</p>'
            '<h4>42 Satırlı İncil</h4>'
            '<p>Müzenin en değerli eseri, Gutenberg\'in yaklaşık 1455 yılında bastığı <em>Gutenberg İncili</em>\'dir. '
            'Dünyada yalnızca 49 tam nüshası kalan bu incillerden ikisi özel bir hazinede korunarak sergilenmektedir.</p>'
            '<h4>İnteraktif Deneyim</h4>'
            '<p>Ziyaretçiler çalışır durumdaki matbaa makinelerini yakından inceleyebilir ve baskı atölyelerinde deneyim kazanabilir.</p>'
            '<div class="info-box"><strong>📍 Ziyaret Bilgileri</strong><br>Giriş: 5 € (indirimli 3 €)<br>Kapalı: Pazartesi</div>'
        ),
    },
    {
        'ad': 'Kirschgarten (Eski Şehir Meydanı)',
        'kategori': 'gezi',
        'adres': 'Kirschgarten',
        'sehir': 'Mainz',
        'maps_url': 'https://maps.google.com/?q=Kirschgarten+Mainz',
        'kapak_resmi': wiki_img('Am_Kirschgarten_30_(Mainz).JPG'),
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Kirschgarten_(Mainz)',
        'icerik': (
            '<p>Mainz Altstadt (Eski Şehir) bölgesinde yer alan, Arnavut kaldırımlı sokakları ve geleneksel ahşap iskeletli '
            '(Fachwerkhaus) evleriyle meşhur, çok şirin bir meydandır.</p>'
            '<h4>Fachwerkhaus Mimarisi</h4>'
            '<p>Kirschgarten, Mainz\'in en iyi korunmuş tarihi sokak dokusuna sahip köşelerinden biridir. '
            'Renkli ahşap çerçeveli evleri ve kaldırım taşlı yollarıyla adeta açık hava müzesi gibidir.</p>'
            '<div class="info-box"><strong>📍 Konum</strong><br>Altstadt\'ın kalbinde, Dom\'dan yürüme mesafesinde<br>Giriş: Ücretsiz</div>'
        ),
    },
    {
        'ad': 'Mainz Zitadelle (Kale)',
        'kategori': 'gezi',
        'adres': 'Oberstadt',
        'sehir': 'Mainz',
        'maps_url': 'https://maps.google.com/?q=Zitadelle+Mainz',
        'kapak_resmi': wiki_img('Zitadelle_Mainz_-_Der_Kommandantenbau.JPG'),
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Zitadelle_Mainz',
        'icerik': (
            '<p>Şehrin tarihine yakından tanıklık eden, Roma döneminden kalma kalıntılara da ev sahipliği yapan bu büyük '
            'kalede yürüyüş yapabilir ve güzel manzaralar yakalayabilirsiniz.</p>'
            '<h4>Tarihi Önemi</h4>'
            '<p>Ortaçağ\'dan günümüze uzanan savunma yapılarıyla çevrili zitadel, Mainz\'in stratejik konumunu yüzyıllar '
            'boyunca korumuştur. Kale içindeki Roma dönemi kalıntıları ayrıca büyük ilgi çekmektedir.</p>'
            '<h4>Panoramik Manzara</h4>'
            '<p>Kale surlarından Ren Nehri ve Mainz şehir manzarası eşsiz bir panorama sunar.</p>'
            '<div class="info-box"><strong>📍 Ziyaret Bilgileri</strong><br>Giriş: Ücretsiz (dış alanlar)<br>Açık: Her gün</div>'
        ),
    },
    {
        'ad': 'Binger Mäuseturm (Fare Kulesi)',
        'kategori': 'gezi',
        'adres': 'Ren Nehri üzerinde, adacık',
        'sehir': 'Bingen am Rhein',
        'maps_url': 'https://maps.google.com/?q=Mäuseturm+Bingen',
        'kapak_resmi': wiki_img('Maeuseturm_bingen.JPG'),
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Mäuseturm',
        'icerik': (
            '<p>Bingen am Rhein\'da, Ren Nehri üzerinde küçük bir adacıkta yer alan tarihi bir gümrük kulesidir. '
            'Efsaneleri ve muhteşem nehir manzarasıyla ünlüdür.</p>'
            '<h4>Efsane</h4>'
            '<p>Kulenin adı, 10. yüzyılda yaşadığı rivayet edilen acımasız Mainz Piskoposu Hatto\'ya dayanan bir '
            'efsaneden gelir. Tanrının gazabıyla fareler tarafından yenildiği söylenir.</p>'
            '<h4>Tekneyle Ulaşım</h4>'
            '<p>Kuleye yaz aylarında Bingen iskelesinden tekneyle ulaşılabilir.</p>'
            '<div class="info-box"><strong>📍 Ziyaret</strong><br>Bingen am Rhein — Mainz\'e ~30 dk mesafe<br>Yaz aylarında tekne seferleri düzenlenir</div>'
        ),
    },
    {
        'ad': 'Rheinstein Kalesi (Burg Rheinstein)',
        'kategori': 'gezi',
        'adres': 'Burg Rheinstein 1',
        'sehir': 'Trechtingshausen',
        'website': 'https://www.burg-rheinstein.de/',
        'maps_url': 'https://maps.google.com/?q=Burg+Rheinstein',
        'kapak_resmi': wiki_img('Burg_Rheinstein_S_2012_06_17_14_15_51.JPG'),
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Burg_Rheinstein',
        'icerik': (
            '<p>Trechtingshausen yakınlarında, Ren Nehri\'ne tepeden bakan büyüleyici ve masalsı bir şatodur. '
            'Orta Çağ havasını hissetmek ve nehir manzarasına karşı kahve içmek için harikadır.</p>'
            '<h4>Romantik Dönem Restorasyonu</h4>'
            '<p>14. yüzyılda inşa edilen kale, 19. yüzyılda Prusya Prensi Friedrich tarafından satın alınarak '
            'romantik dönem zevkiyle restore edilmiştir. İçinde şapel, silah koleksiyonu ve tarihi odalar bulunmaktadır.</p>'
            '<h4>Manzara ve Şarap</h4>'
            '<p>Kalenin terasından Ren Vadisi\'nin eşsiz manzarası ve bölge şarapları tadılabilir.</p>'
            '<div class="info-box"><strong>📍 Ziyaret Bilgileri</strong><br>Mainz\'e ~45 dk mesafe<br>Giriş ücretli, yaz aylarında açık</div>'
        ),
    },
    {
        'ad': 'Steckeschlääferklamm (Binger Ormanı)',
        'kategori': 'gezi',
        'adres': 'Binger Stadtwald, Weiler bei Bingen',
        'sehir': 'Bingen am Rhein',
        'maps_url': 'https://maps.google.com/?q=Steckeschlääferklamm+Bingen',
        'kapak_resmi': 'https://images.unsplash.com/photo-1448375240586-882707db888b?w=1280&q=80',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Steckeschlääferklamm',
        'icerik': (
            '<p>Doğa yürüyüşü yapmayı seviyorsanız bu geçit harika bir seçenektir. Yol boyunca ağaçların gövdelerine '
            'oyulmuş ve boyanmış 60\'tan fazla gizemli "ağaç ruhu" veya goblin yüzü size eşlik eder.</p>'
            '<h4>Ormandaki Yüzler</h4>'
            '<p>1971\'den bu yana yerel yürüyüşçü derneği tarafından bakımı yapılan rotada, ağaç gövdelerine oyulmuş '
            'mistik yüzler ve figürler bulunmaktadır. Çocuklar için özellikle büyüleyici bir deneyimdir.</p>'
            '<h4>Rota Bilgisi</h4>'
            '<p>Klamm boyunca 15 köprü geçilir. Parkur kısa ve kolay yürünebilirdir, aile gezileri için idealdir.</p>'
            '<div class="info-box"><strong>📍 Ziyaret</strong><br>Bingen am Rhein — Mainz\'e ~30 dk<br>Giriş: Ücretsiz, her gün açık</div>'
        ),
    },
    {
        'ad': 'Ingelheimer Winzerkeller',
        'kategori': 'gezi',
        'adres': 'Binger Straße 32',
        'sehir': 'Ingelheim am Rhein',
        'website': 'https://www.ingelheimer-winzerkeller.de/',
        'maps_url': 'https://maps.google.com/?q=Ingelheimer+Winzerkeller',
        'kapak_resmi': 'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=1280&q=80',
        'wikipedia_url': 'https://de.wikipedia.org/wiki/Ingelheimer_Winzerkeller',
        'icerik': (
            '<p>Ingelheim am Rhein\'da yer alan bu tarihi mahzen ve tesis, bölgenin köklü şarap yapım geleneğini yansıtır. '
            'Bölgenin ünlü Riesling ve kırmızı şaraplarını tatmak, yerel kültürü deneyimlemek için idealdir.</p>'
            '<h4>Tarihi Bina</h4>'
            '<p>1904\'te inşa edilen eski bağcılar kooperatifi binası, bugün Ingelheim Vinoteki, turizm ofisi ve '
            'Winzerkeller Restoranı\'na ev sahipliği yapmaktadır.</p>'
            '<h4>Şarap Tadımı</h4>'
            '<p>Ingelheim, Ren Nehri kıyısındaki en eski şarap bölgelerinden biridir. Özellikle Blauer Spätburgunder '
            '(Pinot Noir) ve Riesling çeşitleriyle ünlüdür.</p>'
            '<div class="info-box"><strong>📍 Ulaşım</strong><br>Mainz\'e ~20 dk mesafe<br>Tadım: Rezervasyon önerilir</div>'
        ),
    },
]

eklendi = guncellendi = 0
for d in YERLER:
    obj, created = Yer.objects.get_or_create(ad=d['ad'], defaults={**d, 'aktif': True, 'tur': 'yer'})
    if created:
        eklendi += 1
        print(f'  ✓ {d["ad"]}')
    else:
        for k, v in d.items():
            setattr(obj, k, v)
        obj.save()
        guncellendi += 1
        print(f'  ↺ {d["ad"]} (güncellendi)')

print(f'✅ {eklendi} eklendi, {guncellendi} güncellendi.')
