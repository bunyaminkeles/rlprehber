from django.urls import path, include

urlpatterns = [
    path('almanca/', include('almanca.urls')),
    # RLP geneli rehber/blog/duyurular — ayrı namespace ile çakışma önleniyor
    path('rehber/', include(('rehber.urls', 'rehber'), namespace='rlp-rehber')),
    path('blog/', include(('blog.urls', 'blog'), namespace='rlp-blog')),
    path('duyurular/', include(('duyurular.urls', 'duyurular'), namespace='rlp-duyurular')),
    path('forum/', include(('forum.urls', 'forum'), namespace='rlp-forum')),
]
