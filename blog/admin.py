from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import BlogYazisi


@admin.register(BlogYazisi)
class BlogAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ['baslik', 'yazar', 'eyalet', 'stadt', 'scope', 'yayinda', 'olusturulma']
    list_filter  = ['yayinda', 'eyalet', 'stadt', 'scope']
    prepopulated_fields = {'slug': ('baslik',)}
