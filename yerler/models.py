from django.db import models
from django.db.models import SET_NULL

SCOPE_SECENEKLERI = [
    ('stadt', 'Şehre Özel'),
    ('eyalet', 'RLP Geneli'),
]

YER_KATEGORI = [
    ('resmi_kurum', 'Resmi Kurum'),
    ('alisveris', 'Alışveriş Merkezi'),
    ('turk_market', 'Türk Marketi'),
    ('ibadet', 'Cami / İbadethane'),
    ('tuv', 'TÜV / GTÜ İstasyonu'),
    ('saglik', 'Sağlık'),
    ('egitim', 'Eğitim'),
    ('gezi', 'Gezi & Kültür'),
    ('yeme_icme', 'Yeme & İçme'),
    ('diger', 'Diğer'),
]

PAKET_SECENEKLERI = [
    ('ucretsiz', 'Ücretsiz'),
    ('standart', 'Standart'),
    ('one_cikan', 'Öne Çıkan'),
]


class Yer(models.Model):
    stadt           = models.ForeignKey('stadt.Stadt', null=True, blank=True, on_delete=SET_NULL, verbose_name='Şehir')
    scope           = models.CharField(max_length=10, choices=SCOPE_SECENEKLERI, default='stadt', verbose_name='Kapsam')
    ad              = models.CharField(max_length=200)
    kategori        = models.CharField(max_length=20, choices=YER_KATEGORI)
    adres           = models.TextField()
    sehir           = models.CharField(max_length=100, default='Mainz', help_text='Eski alan - migration sonrası kullanılmayacak')
    telefon         = models.CharField(max_length=50, blank=True)
    website         = models.URLField(blank=True)
    maps_url        = models.URLField(blank=True, help_text='Google Maps linki')
    aciklama        = models.TextField(blank=True)
    kapak_resmi     = models.URLField(blank=True, verbose_name='Kapak Resmi URL (harici)')
    kapak_foto      = models.ImageField(upload_to='yerler/kapak/', blank=True, null=True, verbose_name='Kapak Fotoğrafı (yükle)')
    icerik          = models.TextField(blank=True, verbose_name='Blog İçeriği (HTML)')
    wikipedia_url   = models.URLField(blank=True, verbose_name='Wikipedia Kaynak URL')
    aktif           = models.BooleanField(default=True)

    # Ücretli paket alanları
    paket           = models.CharField(max_length=10, choices=PAKET_SECENEKLERI, default='ucretsiz', verbose_name='Paket')
    paket_bitis     = models.DateField(null=True, blank=True, verbose_name='Paket Bitiş Tarihi')
    calisma_saati   = models.CharField(max_length=200, blank=True, verbose_name='Çalışma Saatleri', help_text='Örn: Pzt-Cum 09:00-18:00')
    instagram_url   = models.URLField(blank=True, verbose_name='Instagram')
    whatsapp        = models.CharField(max_length=20, blank=True, verbose_name='WhatsApp', help_text='Sadece rakamlar, örn: 4917612345678')

    class Meta:
        ordering = ['kategori', 'ad']
        verbose_name = 'Yer'
        verbose_name_plural = 'Yerler'

    def __str__(self):
        return f"{self.ad} ({self.get_kategori_display()})"


class YerFoto(models.Model):
    yer  = models.ForeignKey(Yer, on_delete=models.CASCADE, related_name='fotolar', verbose_name='Yer')
    url  = models.URLField(blank=True, verbose_name='Fotoğraf URL (harici)')
    foto = models.ImageField(upload_to='yerler/fotolar/', blank=True, null=True, verbose_name='Fotoğraf (yükle)')
    sira = models.PositiveSmallIntegerField(default=0, verbose_name='Sıra')

    class Meta:
        ordering = ['sira']
        verbose_name = 'Yer Fotoğrafı'
        verbose_name_plural = 'Yer Fotoğrafları'

    def __str__(self):
        return f"{self.yer.ad} — Foto {self.sira}"


class ReklamPaketi(models.Model):
    ad             = models.CharField(max_length=100, verbose_name='Paket Adı')
    aciklama       = models.CharField(max_length=200, blank=True, verbose_name='Kısa Açıklama', help_text='Paket kartında başlığın altında gösterilir')
    fiyat          = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Fiyat (€)')
    sure_etiketi   = models.CharField(max_length=50, default='/ ay', verbose_name='Süre Etiketi', help_text='Örn: "/ ay", "/ 3 ay"')
    ozellikler     = models.TextField(verbose_name='Özellikler', help_text='Her satır bir özellik olarak gösterilir')
    renk           = models.CharField(max_length=30, default='primary', verbose_name='Bootstrap Renk', help_text='primary, warning, success, dark...')
    vurgulu        = models.BooleanField(default=False, verbose_name='Vurgulu Göster', help_text='En popüler / tavsiye edilen paket')
    aktif          = models.BooleanField(default=True, verbose_name='Aktif')
    sira           = models.PositiveSmallIntegerField(default=0, verbose_name='Sıra')
    iletisim_notu  = models.TextField(blank=True, verbose_name='İletişim Notu', help_text='Sayfanın altında gösterilecek metin')

    class Meta:
        ordering = ['sira']
        verbose_name = 'Reklam Paketi'
        verbose_name_plural = 'Reklam Paketleri'

    def __str__(self):
        return f"{self.ad} — {self.fiyat}€ {self.sure_etiketi}"

    def ozellik_listesi(self):
        return [s.strip() for s in self.ozellikler.splitlines() if s.strip()]
