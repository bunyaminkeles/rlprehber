from django.urls import path
from . import views

app_name = 'isletmeler'

urlpatterns = [
    path('', views.isletmeler, name='liste'),
    path('<int:pk>/', views.detay, name='detay'),
]
