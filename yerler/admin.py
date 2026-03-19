from django.contrib import admin
from .models import Yer

@admin.register(Yer)
class YerAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'kategori', 'sehir', 'aktif']
    list_filter   = ['kategori', 'aktif', 'sehir']
    search_fields = ['ad', 'adres']
    list_editable = ['aktif']
