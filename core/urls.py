from django.urls import path
from . import views
from forum import views as forum_views

app_name = 'core'

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('hakkinda/', views.hakkinda, name='hakkinda'),
    path('arama/', views.arama, name='arama'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Global forum — tüm şehir ve eyaletleri kapsar
    path('forum/', forum_views.genel_liste, name='forum_genel'),
    path('forum/konu/<int:pk>/', forum_views.genel_konu_detay, name='forum_konu_genel'),
    path('forum/konu/<int:pk>/yorum/', forum_views.genel_yorum_ekle, name='forum_yorum_genel'),
    path('forum/kategori/<int:kategori_pk>/yeni/', forum_views.genel_konu_ac, name='forum_konu_ac_genel'),
]
