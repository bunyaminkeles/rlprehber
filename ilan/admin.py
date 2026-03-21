from django.contrib import admin
from .models import Ilan

@admin.register(Ilan)
class IlanAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'kategori', 'stadt', 'scope', 'sahip', 'onaylandi', 'aktif', 'olusturulma']
    list_filter  = ['kategori', 'onaylandi', 'aktif', 'stadt', 'scope']
    actions      = ['onayla']

    @admin.action(description='Seçili ilanları onayla')
    def onayla(self, request, queryset):
        queryset.update(onaylandi=True)
