from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import ForumKategori, Konu, Yorum


class YorumInline(TabularInline):
    model = Yorum
    extra = 0
    fields = ['yazar', 'olusturulma']
    readonly_fields = ['yazar', 'olusturulma']


@admin.register(ForumKategori)
class ForumKategoriAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ['ad']


@admin.register(Konu)
class KonuAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ['baslik', 'kategori', 'eyalet', 'stadt', 'scope', 'yazar', 'sabitlendi', 'kapali', 'olusturulma']
    list_filter  = ['kategori', 'sabitlendi', 'kapali', 'eyalet', 'stadt', 'scope']
    inlines      = [YorumInline]
