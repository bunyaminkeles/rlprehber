from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import OnemliLink


@admin.register(OnemliLink)
class OnemliLinkAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display  = ['ad', 'kategori', 'eyalet', 'stadt', 'scope', 'sira', 'aktif']
    list_filter   = ['kategori', 'aktif', 'eyalet', 'stadt', 'scope']
    search_fields = ['ad']
    list_editable = ['sira', 'aktif']
