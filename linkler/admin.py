from django.contrib import admin
from .models import OnemliLink

@admin.register(OnemliLink)
class OnemliLinkAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'kategori', 'sira', 'aktif']
    list_filter   = ['kategori', 'aktif']
    search_fields = ['ad']
    list_editable = ['sira', 'aktif']
