from django.db import migrations

ICERIK = """
<p>Almanya'da, özellikle Mainz gibi gelişmiş şehirlerde bütçeye uygun kiralık ev bulmak oldukça zorlayıcı bir süreç olabilir. Ancak, devlet destekli ve kirası piyasa şartlarına göre çok daha uygun olan "sosyal konutlarda" (Sozialwohnung) yaşama hakkınız olabileceğini biliyor muydunuz? Bu hakkınızı kullanabilmeniz için ihtiyacınız olan temel belgeye <strong>Wohnberechtigungsschein</strong>, yani kısaca <strong>WBS</strong> denmektedir. Bu yazımızda, WBS'nin ne olduğu, kimlerin bu belgeye başvurabileceği ve sürecin nasıl işlediği hakkında temel bilgileri sizler için derledik.</p>

<h3>WBS (Wohnberechtigungsschein) Nedir?</h3>
<p>WBS, Almanya'da kamu fonlarıyla desteklenen sosyal konutlara taşınmaya hak kazandığınızı kanıtlayan resmi bir belgedir. Rheinland-Pfalz eyaleti sınırları içinde alınan bu belge onaylandıktan sonra <strong>en fazla 1 yıl</strong> süreyle geçerlidir. Eğer bu süre zarfında bir ev bulamazsanız, belgeyi tekrar yenilemeniz gerekir.</p>

<p>WBS iki farklı şekilde talep edilebilir:</p>
<ol>
  <li><strong>Genel WBS (Allgemeiner Wohnberechtigungsschein):</strong> Kriterlerinize uyan herhangi bir sosyal konuta başvuru yapmanıza olanak tanır.</li>
  <li><strong>Özel WBS (Spezieller Wohnberechtigungsschein):</strong> Sadece belirli bir sosyal konut için geçerlidir. Özellikleri belli olan bir daireye talip olduğunuzda bu belge türüne başvurulur.</li>
</ol>

<h3>Kimler WBS Alabilir? Başvuru Şartları Nelerdir?</h3>
<p>WBS alabilmek için en belirleyici kriter <strong>gelir sınırıdır (Einkommensgrenze)</strong>. Hanede yaşayan kişilerin toplam yıllık brüt gelirinin, eyalet tarafından belirlenen yasal sınırı aşmaması gerekir. Bu sınır, hanedeki kişi sayısına ve durumlarına göre değişiklik gösterir.</p>

<p>Bunun yanı sıra başvuru sahiplerinin genel olarak şu oturum şartlarından birini sağlaması beklenir:</p>
<ul>
  <li>Alman vatandaşı olmak,</li>
  <li>Avrupa Birliği (AB) vatandaşı olmak,</li>
  <li>Veya en az <strong>1 yıl geçerliliği olan bir oturum iznine</strong> (Aufenthaltstitel) sahip olmak.</li>
</ul>

<div class="info-box">
  <strong>Not:</strong> İstisnai durumlarda; hanedeki ağır engellilik, özel bakım ihtiyacı gibi özel zorlukların (härtefall) bulunduğu senaryolarda gelir sınırları ufak farklarla aşılsa bile duruma özel WBS verilebilmektedir.
</div>

<h3>Başvuru İçin Hangi Belgeler Gereklidir?</h3>
<p>İstenen evraklar kişisel veya ailevi durumunuza göre değişiklik gösterse de genel olarak hazırlamanız gereken evraklar şunlardır:</p>
<ul>
  <li>Kimlik kartı veya Pasaport (Pasaport ile birlikte güncel ikametgah belgesi),</li>
  <li>Gelir durumunuzu kanıtlayan belgeler (Son maaş bordroları, emeklilik bildirimleri vb.),</li>
  <li>Öğrenciler için BAföG, güncel okul belgeleri,</li>
  <li>Sosyal destek alanlar için güncel kurum bildirimleri (Bürgergeld, Wohngeld, Asylbewerberleistung veya Grundsicherung belgeleri),</li>
  <li>Varsa: Evlilik cüzdanı, ağır engellilik belgesi (Schwerbehindertenausweis - önlü arkalı fotokopi), hamilelik belgesi (Mutterpass) veya velayet hakkı belgesi.</li>
</ul>

<h3>Başvuru Süreci ve Önemli Uyarılar</h3>
<p>Başvuru sürecinde formunuzu ve evraklarınızı hazırladıktan sonra ilgili kurumun Sosyal Hizmetler Dairesine (Amt für soziale Leistungen) posta, faks veya e-posta yoluyla iletebilirsiniz. Yüz yüze görüşme sağlamak isterseniz mutlaka önceden arayıp randevu almanız gerekmektedir.</p>

<div class="info-box">
  <strong>Büyük Bir Yanılgı:</strong> WBS belgesi almak, size otomatik olarak bir ev tahsis edileceği anlamına gelmez! İlgili resmi daireler sadece bu belgeyi onaylar, ev kiralama işlemi yapmaz. Ev bulma ve kira sözleşmesi imzalama kararı tamamen ev sahiplerine veya "Wohnbau Mainz GmbH" gibi konut şirketlerine aittir. Belgenizle birlikte bu şirketlere kendiniz başvuru yapmalısınız.
</div>

<p>Eğer Mainz şehrinde ikamet ediyorsanız veya Mainz'a taşınmayı planlıyorsanız; başvuru formunu indirmek, güncel yetkili kişilere ulaşmak ve süreç hakkında tüm detayları birinci elden öğrenmek için <a href="https://www.mainz.de/vv/produkte/soziale_leistungen/Wohnberechtigungsschein-beantragen" target="_blank" rel="noopener">Mainz Belediyesi WBS Başvuru ve Bilgilendirme Sayfasını</a> ziyaret etmeniz gerekmektedir. İşlemlerinize bu linkteki yönergeleri takip ederek başlayabilirsiniz.</p>

<hr>

<p><small>
  <strong>Kaynakça ve Faydalı Bağlantılar:</strong><br>
  • Ana Kaynak: <a href="https://www.mainz.de/vv/produkte/soziale_leistungen/Wohnberechtigungsschein-beantragen" target="_blank" rel="noopener">Landeshauptstadt Mainz — Wohnberechtigungsschein beantragen</a><br>
  • Yasal Dayanak: Rheinland-Pfalz Eyaleti Konut Teşvik Kanunu (§ 13 Landeswohnraumförderungsgesetz — LWoFG)
</small></p>
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
        slug='wohnberechtigungsschein-wbs-nedir-nasil-alinir',
        defaults=dict(
            baslik='Almanya\'da Uygun Fiyatlı Ev Bulmanın Anahtarı: Wohnberechtigungsschein (WBS) Nedir ve Nasıl Alınır?',
            icerik=ICERIK.strip(),
            ozet='Mainz\'da sosyal konut (Sozialwohnung) için gereken WBS belgesi nedir, kimler alabilir, hangi belgeler gerekli? Tüm detaylar bu yazıda.',
            yazar=yazar,
            scope='stadt',
            stadt=mainz,
            yayinda=True,
        ),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogyazisi_scope_blogyazisi_stadt'),
        ('stadt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(ekle, migrations.RunPython.noop),
    ]
