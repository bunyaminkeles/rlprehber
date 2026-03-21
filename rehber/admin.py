from django.contrib import admin
from .models import Kaynak

@admin.register(Kaynak)
class KaynakAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tip', 'kategori', 'stadt', 'scope', 'sira', 'yayinda']
    list_filter  = ['tip', 'kategori', 'yayinda', 'stadt', 'scope']
    prepopulated_fields = {'slug': ('baslik',)}
    list_editable = ['sira', 'yayinda']
