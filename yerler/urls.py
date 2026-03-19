from django.urls import path
from . import views

app_name = 'yerler'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('<int:pk>/', views.detay, name='detay'),
]
