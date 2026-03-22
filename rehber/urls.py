from django.urls import path
from . import views

app_name = 'rehber'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('anabin-karar-araci/', views.anabin_widget, name='anabin_widget'),
    path('<slug:slug>/', views.detay, name='detay'),
]
