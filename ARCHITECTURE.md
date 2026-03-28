# almanyalirehber.com — Mimari ve Tasarım Kuralları (Master Prompt)

## 1. Vizyon ve Felsefe
* Bu site Almanya'ya gelen Türkler için sıradan bir ilan panosu veya blog değil; bir **"İşletim Sistemi"** ve **"Şehir Kokpiti"**dir.
* Kullanıcılar stresli, bürokrasiden yorulmuş ve anadili olmayan bir ülkede kaybolmuştur. Tasarım onları sakinleştirmeli, bilişsel yükü (cognitive load) sıfıra indirmelidir.
* **"Ultrathink" Kuralı:** Gürültüyü sil, sürtünmeyi yok et, sadeliği dayat. Karar felci (Choice Paralysis) yaratacak çoklu seçeneklerden kaçın.

## 2. Teknik Yığın (Tech Stack) ve Kodlama Standartları
* **CSS Framework:** KESİNLİKLE **Bootstrap 5** kullanılacaktır (Tailwind DEĞİL). Ancak klasik, ucuz "Default Bootstrap" görünümü kesinlikle reddedilir. Bootstrap'in utility class'ları (`shadow-sm`, `rounded-4`, `text-muted`, `gap-3` vb.) bir zanaatkar hassasiyetiyle, Apple/Stripe sadeliğini verecek şekilde kullanılacaktır.
* **JavaScript:** Ağır framework'ler (React/Vue) yasaktır. DOM manipülasyonları ve API istekleri saf (Vanilla) JavaScript ve modern `Fetch API` ile yazılacaktır.
* **Backend:** Django. View'larda her zaman veri tekrarını önleyen (`.distinct()` veya deduplication) temiz sorgular yazılacaktır.

## 3. Arayüz (UI/UX) Kalıpları
* **Hiyerarşik Butonlar:** Bir kartta veya formda asla eşdeğer 3 buton yan yana olamaz. Her zaman bir "Kral" (Primary Action - Dolu/Vurgulu) buton vardır. Diğerleri destekleyici (Outline/Şeffaf/Muted) olmak zorundadır.
* **Sürtünmesiz Formlar (Frictionless):** E-posta aboneliği veya küçük form gönderimleri sayfayı ASLA yenilemeyecek (No Reload). AJAX/Fetch ile arkada çözülüp, buton anında zarif bir "Kaydedildi ✓" statüsüne geçecek.
* **Kademeli Bilgi (Progressive Disclosure):** Kullanıcıyı sürekli yeni sayfalara atıp koparmak yerine, Bootstrap `Offcanvas` (yandan açılan panel) veya yumuşak kaydırmalı (Smooth Scroll) dikey tek sayfa (Single Page Directory) mimarileri tercih edilecektir. Hantal tab (sekme) yapıları kullanılmayacaktır.

## 4. İçerik Mimarisi (Taş, Su ve Merkez)
* **Merkez (Zeka):** Ana sayfanın kalbi olan Arama Çubuğu, aptal bir kelime arayıcısı değil; niyeti okuyup (Intent Recognition) kullanıcıyı doğru şehir paneline ışınlayan bir yönlendiricidir.
* **Taş (Sabit Bilgi):** Resmi işlemler, kurumlar ve rehberler ağırbaşlı, hiyerarşisi net kartlar halinde tasarlanacaktır. (Admin içerikleri).
* **Su (Akışkan Bilgi):** İlanlar, RSS haberleri (DW) ve topluluk verileri sayfanın altında akan, göz yormayan temiz bir liste/grid (Topluluğun Nabzı) halinde sunulacaktır. (UGC - Kullanıcı üretimi içerikler).