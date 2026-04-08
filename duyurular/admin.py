from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Duyuru


@admin.register(Duyuru)
class DuyuruAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display  = ['baslik', 'kaynak_tipi', 'yazar', 'eyalet', 'stadt', 'scope', 'yayinda', 'yayin_bitis', 'olusturulma']
    list_filter   = ['kaynak_tipi', 'yayinda', 'eyalet', 'stadt', 'scope']
    search_fields = ['baslik']
    actions       = ['yayinla']

    @admin.action(description='Seçili duyuruları yayınla')
    def yayinla(self, request, queryset):
        queryset.update(yayinda=True)
