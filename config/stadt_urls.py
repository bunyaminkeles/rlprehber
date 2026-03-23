from django.urls import path, include
from stadt import views as stadt_views

urlpatterns = [
    path('', stadt_views.home, name='stadt_home'),
    path('rehber/', include('rehber.urls')),
    path('duyurular/', include('duyurular.urls')),
    path('takvim/', include('takvim.urls')),
    path('forum/', include('forum.urls')),
    path('blog/', include('blog.urls')),
    path('ilan/', include('ilan.urls')),
    path('yerler/', include('yerler.urls')),
    path('isletmeler/', include('yerler.isletme_urls')),
    path('linkler/', include('linkler.urls')),
]
