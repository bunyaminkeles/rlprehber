from django.urls import path, include
from stadt import views as stadt_views
from yerler import views as yerler_views

urlpatterns = [
    path('', stadt_views.eyalet_home, name='eyalet_home'),
    path('almanca/', include('almanca.urls')),
    path('reklam/', yerler_views.paketler, name='reklam_paketleri'),
    # RLP geneli rehber/blog/duyurular — ayrı namespace ile çakışma önleniyor
    path('rehber/', include(('rehber.urls', 'rehber'), namespace='rlp-rehber')),
    path('blog/', include(('blog.urls', 'blog'), namespace='rlp-blog')),
    path('duyurular/', include(('duyurular.urls', 'duyurular'), namespace='rlp-duyurular')),
    path('forum/', include(('forum.urls', 'forum'), namespace='rlp-forum')),
    path('ilan/', include(('ilan.urls', 'ilan'), namespace='rlp-ilan')),
]
