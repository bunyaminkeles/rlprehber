from django.urls import path, include
from django.http import HttpResponsePermanentRedirect
from django.views.generic import RedirectView
from stadt import views as stadt_views
from yerler import views as yerler_views
from businesses import views as businesses_views


def _yerler_liste_redirect(request, eyalet_slug, stadt_slug):
    return HttpResponsePermanentRedirect(f'/{eyalet_slug}/{stadt_slug}/#onemli-yerler')


urlpatterns = [
    path('', stadt_views.home, name='stadt_home'),
    path('rehber/', include('rehber.urls')),
    path('duyurular/', include('duyurular.urls')),
    path('takvim/', include('takvim.urls')),
    path('forum/', include('forum.urls')),
    path('blog/', include('blog.urls')),
    path('ilan/', include('ilan.urls')),
    # yerler listesi artık ana sayfaya (#onemli-yerler) yönlendiriliyor
    path('yerler/', _yerler_liste_redirect),
    path('yerler/<int:pk>/', yerler_views.detay, name='yer_detay'),
    path('isletmeler/', include('yerler.isletme_urls')),
    path('lokal-uzmanlar/', businesses_views.stadt_business_list, name='stadt_business_list'),
    path('lokal-uzmanlar/<slug:kategori_slug>/', businesses_views.stadt_category_list, name='stadt_category_list'),
    # linkler app kaldırıldı — eski URL'ler ana sayfaya yönlendiriliyor
    path('linkler/', RedirectView.as_view(url='../#onemli-yerler', permanent=True)),
    path('linkler/git/<int:pk>/', RedirectView.as_view(url='../../#onemli-yerler', permanent=True)),
]
