from django.contrib import admin
from .models import Konusma, Mesaj


class MesajInline(admin.TabularInline):
    model = Mesaj
    extra = 0
    readonly_fields = ('gonderen', 'icerik', 'okundu', 'olusturulma')


@admin.register(Konusma)
class KonusmaAdmin(admin.ModelAdmin):
    list_display = ('taraf1', 'taraf2', 'olusturulma')
    inlines = [MesajInline]


@admin.register(Mesaj)
class MesajAdmin(admin.ModelAdmin):
    list_display = ('gonderen', 'konusma', 'icerik', 'okundu', 'olusturulma')
    list_filter = ('okundu',)
