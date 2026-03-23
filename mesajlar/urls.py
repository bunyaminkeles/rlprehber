from django.urls import path
from . import views

app_name = 'mesajlar'

urlpatterns = [
    path('', views.gelen_kutusu, name='gelen_kutusu'),
    path('<int:pk>/', views.konusma_detay, name='konusma'),
    path('baslat/<str:kullanici_adi>/', views.mesaj_baslat, name='baslat'),
    path('<int:pk>/api/', views.mesajlar_api, name='api'),
]
