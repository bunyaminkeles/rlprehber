from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
    path('rehber/', include('rehber.urls')),
    path('duyurular/', include('duyurular.urls')),
    path('forum/', include('forum.urls')),
    path('blog/', include('blog.urls')),
    path('ilan/', include('ilan.urls')),
    path('takvim/', include('takvim.urls')),
    path('', include('accounts.urls')),
    path('yerler/', include('yerler.urls')),
    path('linkler/', include('linkler.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
