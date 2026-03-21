from django.contrib import admin
from .models import Duyuru

@admin.register(Duyuru)
class DuyuruAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'kategori', 'stadt', 'scope', 'yayinda', 'olusturulma']
    list_filter  = ['kategori', 'yayinda', 'stadt', 'scope']
    search_fields = ['baslik']
