from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Ilan


@admin.register(Ilan)
class IlanAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ['baslik', 'kategori', 'eyalet', 'stadt', 'scope', 'sahip', 'onaylandi', 'aktif', 'yayin_bitis', 'olusturulma']
    list_filter  = ['kategori', 'onaylandi', 'aktif', 'eyalet', 'stadt', 'scope']
    actions      = ['onayla']

    @admin.action(description='Seçili ilanları onayla')
    def onayla(self, request, queryset):
        queryset.update(onaylandi=True)
