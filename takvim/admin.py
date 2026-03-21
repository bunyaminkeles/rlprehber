from django.contrib import admin
from .models import Etkinlik

@admin.register(Etkinlik)
class EtkinlikAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tarih', 'tur', 'stadt', 'scope']
    list_filter  = ['tur', 'stadt', 'scope']
