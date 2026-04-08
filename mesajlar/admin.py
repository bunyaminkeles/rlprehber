from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Konusma, Mesaj


class MesajInline(TabularInline):
    model = Mesaj
    extra = 0
    readonly_fields = ('gonderen', 'icerik', 'okundu', 'olusturulma')


@admin.register(Konusma)
class KonusmaAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ('taraf1', 'taraf2', 'olusturulma')
    inlines = [MesajInline]


@admin.register(Mesaj)
class MesajAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ('gonderen', 'konusma', 'icerik', 'okundu', 'olusturulma')
    list_filter = ('okundu',)
