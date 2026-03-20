from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health, name='api_health'),
    path('rss-cek/', views.rss_cek, name='api_rss_cek'),
    path('seed/', views.seed_calistir, name='api_seed'),
]
