from django.db import migrations

ICERIK = """
<p>Almanya sokaklarında dolaşırken aniden rengarenk kostümler içindeki insanların birbirlerine üç kez yüksek sesle <strong>"Helau!"</strong> diye bağırdığını duyarsanız, şaşırmayın. Resmi bir takvim yaprağında "Helau Bayramı" diye bir gün göremezsiniz; ancak bu kelime, Almanya'nın kış aylarını ısıtan, sokakları adeta bir açık hava partisine çeviren meşhur <strong>Karnaval (Fastnacht, Karneval veya Fasching)</strong> döneminin en bilindik parolasıdır.</p>

<p>Özellikle şu an bulunduğumuz Mainz şehri, bu coşkunun Almanya'daki en büyük başkentlerinden biridir. Peki, herkesin dilindeki bu "Helau" tam olarak nedir ve bu renkli festivalde neler yaşanır? Gelin, Almanya'nın bu en eğlenceli geleneğine yakından bakalım.</p>

<h3>"Helau" Ne Anlama Geliyor?</h3>
<p>"Helau" (genellikle tek 'l' ile yazılır), karnaval döneminde insanların birbirlerini selamlama ve neşelerini paylaşma şeklidir. Özellikle Mainz, Düsseldorf ve Frankfurt gibi şehirlerde karnavalın simgesi haline gelmiştir. Almanya'nın bir diğer karnaval başkenti olan Köln'de ise bunun yerine "Alaaf" kelimesi kullanılır. Yani hangi şehre gittiğinize bağlı olarak selamlama şekliniz de değişir!</p>

<h3>Karnaval Ne Zaman Kutlanır?</h3>
<p>Karnaval dönemi sadece birkaç günlük bir eğlenceden ibaret değildir; aylar süren bir "Beşinci Mevsim" (Fünfte Jahreszeit) olarak kabul edilir.</p>
<ul>
  <li><strong>Başlangıç (11.11):</strong> Karnaval sezonu, her yıl geleneksel olarak 11. ayın 11'inde, saat tam 11:11'de coşkulu etkinliklerle başlar.</li>
  <li><strong>Zirve Noktası (Rosenmontag):</strong> Asıl büyük sokak şenlikleri, geçit törenleri ve partiler genellikle Şubat ayının sonu veya Mart ayının başında gerçekleşir. En görkemli gün "Gül Pazartesisi" anlamına gelen Rosenmontag'dır.</li>
  <li><strong>Kapanış (Aschermittwoch):</strong> Tüm bu renkli kutlamalar, "Kül Çarşambası" adı verilen günde sona erer ve normal hayata geri dönülür.</li>
</ul>

<h3>Sokaklarda Sizi Neler Bekliyor?</h3>
<p>Karnaval döneminde Almanya, alıştığımız disiplinli ve sessiz halinden tamamen sıyrılır. Bu dönemde sokaklarda şunlarla karşılaşmanız garanti:</p>
<ul>
  <li><strong>Yaratıcı Kostümler:</strong> 7'den 70'e herkes, aylar öncesinden hazırladıkları komik, korkutucu veya popüler kültür karakterlerinden ilham alan kostümler giyer.</li>
  <li><strong>Görkemli Geçit Törenleri:</strong> Dev maketlerin bulunduğu araçlar sokaklardan geçerken müzikler çalar ve dans gösterileri yapılır.</li>
  <li><strong>Şeker Yağmuru:</strong> Geçit araçlarının üzerinden kalabalığa tonlarca şeker, çikolata ve küçük oyuncak atılır. Çocuklar (ve tabii yetişkinler) bunları toplamak için birbiriyle yarışır.</li>
  <li><strong>Siyasi Taşlamalar:</strong> Geçit törenlerindeki dev maketler genellikle sadece görsel bir şölen sunmakla kalmaz; aynı zamanda yerel ve küresel siyasetçilerin, güncel olayların mizahi ve oldukça cesur bir dille eleştirildiği bir platformdur.</li>
</ul>

<h3>Kışa Veda, Bahara Merhaba!</h3>
<p>Kökleri hem dini ritüellere hem de kışın karanlığından ve soğuğundan kurtulup baharı karşılama arzusuna dayanan bu festival, insanların doyasıya eğlenip deşarj olduğu harika bir kültürel deneyimdir. Eğer yolunuz kış sonlarında Mainz veya çevresine düşerse, kendinize renkli bir şapka alın, sokaklara karışın ve kalabalıkla birlikte bağırmaya hazır olun: <strong>Helau! Helau! Helau!</strong></p>
"""


def ekle(apps, schema_editor):
    BlogYazisi = apps.get_model('blog', 'BlogYazisi')
    Stadt = apps.get_model('stadt', 'Stadt')
    User = apps.get_model('auth', 'User')

    mainz = Stadt.objects.filter(slug='mainz').first()
    yazar = User.objects.filter(is_superuser=True).first() or User.objects.first()

    if not yazar:
        return

    BlogYazisi.objects.get_or_create(
        slug='helau-mainz-karnavali-nedir',
        defaults=dict(
            baslik='Almanya\'nın En Renkli Zamanı: "Helau" Coşkusu ve Mainz Karnavalı',
            icerik=ICERIK.strip(),
            ozet='Mainz\'ın meşhur karnaval geleneği Fastnacht nedir? "Helau" ne anlama gelir, Rosenmontag nasıl kutlanır? Tüm detaylar bu yazıda.',
            yazar=yazar,
            scope='stadt',
            stadt=mainz,
            yayinda=True,
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_wbs_blog_yazisi'),
        ('stadt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
