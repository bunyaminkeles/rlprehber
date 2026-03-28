from django.contrib import admin
from .models import Kaynak, BultenAbone

@admin.register(Kaynak)
class KaynakAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tip', 'kategori', 'eyalet', 'stadt', 'scope', 'sira', 'yayinda']
    list_filter  = ['tip', 'kategori', 'yayinda', 'eyalet', 'stadt', 'scope']
    prepopulated_fields = {'slug': ('baslik',)}
    list_editable = ['sira', 'yayinda']

@admin.register(BultenAbone)
class BultenAboneAdmin(admin.ModelAdmin):
    list_display = ('email', 'aktif', 'kayit_tarihi')
    list_filter = ('aktif', 'kayit_tarihi')
    search_fields = ('email',)
    list_editable = ('aktif',)
