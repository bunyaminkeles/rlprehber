from django.urls import path
from . import views

app_name = 'almanca'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('<slug:slug>/', views.quiz, name='quiz'),
    path('<slug:slug>/cevapla/', views.cevapla, name='cevapla'),
    path('<slug:slug>/katalog/', views.katalog, name='katalog'),
]
