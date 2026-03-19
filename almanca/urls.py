from django.urls import path
from . import views

app_name = 'almanca'

urlpatterns = [
    path('', views.liste, name='liste'),
    path('<str:thema>/', views.quiz, name='quiz'),
    path('<str:thema>/cevapla/', views.cevapla, name='cevapla'),
]
