from django.contrib import admin
from django.urls import path, include, register_converter
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView
from django.http import Http404, HttpResponsePermanentRedirect
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import SITEMAPS
from config.converters import EyaletConverter
from blog.views import detay_root as blog_detay_root

register_converter(EyaletConverter, 'eyalet')


def legacy_stadt_redirect(request, old_slug, subpath=''):
    """Eski /<stadt_slug>/... URL'lerini /<eyalet_slug>/<stadt_slug>/... formatına yönlendirir (301)."""
    from stadt.models import Stadt
    try:
        stadt = Stadt.objects.select_related('eyalet').get(slug=old_slug)
        eyalet_slug = stadt.eyalet.slug if stadt.eyalet else 'rlp'
        if subpath:
            new_url = f'/{eyalet_slug}/{old_slug}/{subpath}'
        else:
            new_url = f'/{eyalet_slug}/{old_slug}/'
        return HttpResponsePermanentRedirect(new_url)
    except Stadt.DoesNotExist:
        raise Http404


# Eski kök URL'lerden doğrudan yeni URL'lere 301 redirect
OLD_MAINZ_REDIRECTS = [
    path('rehber/',    RedirectView.as_view(url='/rlp/mainz/rehber/',    permanent=True)),
    path('duyurular/', RedirectView.as_view(url='/rlp/mainz/duyurular/', permanent=True)),
    path('blog/',      RedirectView.as_view(url='/rlp/mainz/blog/',      permanent=True)),
    path('ilan/',      RedirectView.as_view(url='/rlp/mainz/ilan/',      permanent=True)),
    path('takvim/',    RedirectView.as_view(url='/rlp/mainz/takvim/',    permanent=True)),
    path('yerler/',    RedirectView.as_view(url='/rlp/mainz/yerler/',    permanent=True)),
    path('linkler/',   RedirectView.as_view(url='/rlp/mainz/yerler/',    permanent=True)),
    path('almanca/',   RedirectView.as_view(url='/rlp/almanca/',         permanent=True)),
]

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('robots.txt',  TemplateView.as_view(template_name='robots.txt',  content_type='text/plain')),
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.svg', permanent=True)),
    path('sitemap.xml', sitemap, {'sitemaps': SITEMAPS}, name='django.contrib.sitemaps.views.sitemap'),
    path('googlef882ed2d634aa7da.html',          TemplateView.as_view(template_name='googlef882ed2d634aa7da.html',          content_type='text/html')),
    path('BingSiteAuth.xml',                     TemplateView.as_view(template_name='BingSiteAuth.xml',                     content_type='text/xml')),
    path('yandex_74f18fa4e3ddff5c.html',         TemplateView.as_view(template_name='yandex_74f18fa4e3ddff5c.html',         content_type='text/html')),
    path('guzpm0nmoodr8tjb1bxn06wo4bk14o.html',  TemplateView.as_view(template_name='guzpm0nmoodr8tjb1bxn06wo4bk14o.html',  content_type='text/html')),

    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('accounts.urls')),
    path('mesajlar/', include('mesajlar.urls')),
    path('api/', include('api.urls')),

    # Ana sayfa (şehir seçici) ve statik sayfalar
    path('', include('core.urls')),

    # Lokal Uzmanlar (İşletme rehberi)
    path('lokal-uzmanlar/', include('businesses.urls')),

    # Blog yazısı kök URL'i (canonical, şehirden bağımsız)
    path('blog/<slug:slug>/', blog_detay_root, name='blog_detay_root'),

    # Eski kök URL'lere 301 redirect (SEO koruması)
    *OLD_MAINZ_REDIRECTS,

    # Eyalet geneli içerik: /<eyalet_slug>/...
    path('<eyalet:eyalet_slug>/', include('config.eyalet_urls')),

    # Şehir bazlı içerik: /<eyalet_slug>/<stadt_slug>/...
    path('<eyalet:eyalet_slug>/<slug:stadt_slug>/', include('config.stadt_urls')),

    # Eski /<stadt_slug>/... URL'leri → /<eyalet_slug>/<stadt_slug>/... (SEO koruması)
    path('<slug:old_slug>/',               legacy_stadt_redirect),
    path('<slug:old_slug>/<path:subpath>', legacy_stadt_redirect),

]
