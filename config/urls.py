from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Eski URL'lerden /mainz/ prefix'li yeni URL'lere 301 redirect
OLD_MAINZ_REDIRECTS = [
    path('rehber/',    RedirectView.as_view(url='/mainz/rehber/', permanent=True)),
    path('duyurular/', RedirectView.as_view(url='/mainz/duyurular/', permanent=True)),
    path('forum/',     RedirectView.as_view(url='/mainz/forum/', permanent=True)),
    path('blog/',      RedirectView.as_view(url='/mainz/blog/', permanent=True)),
    path('ilan/',      RedirectView.as_view(url='/mainz/ilan/', permanent=True)),
    path('takvim/',    RedirectView.as_view(url='/mainz/takvim/', permanent=True)),
    path('yerler/',    RedirectView.as_view(url='/mainz/yerler/', permanent=True)),
    path('linkler/',   RedirectView.as_view(url='/mainz/linkler/', permanent=True)),
    path('almanca/',   RedirectView.as_view(url='/rlp/almanca/', permanent=True)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('accounts.urls')),
    path('mesajlar/', include('mesajlar.urls')),
    path('api/', include('api.urls')),

    # Ana sayfa (şehir seçici) ve statik sayfalar
    path('', include('core.urls')),

    # Eyalet geneli içerik
    path('rlp/', include('config.eyalet_urls')),

    # Eski URL'lere 301 redirect (SEO koruması)
    *OLD_MAINZ_REDIRECTS,

    # Şehir bazlı içerik — /<stadt_slug>/...
    path('<slug:stadt_slug>/', include('config.stadt_urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
