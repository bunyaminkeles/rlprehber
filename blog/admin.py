from django.contrib import admin
from .models import BlogYazisi

@admin.register(BlogYazisi)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'yazar', 'stadt', 'scope', 'yayinda', 'olusturulma']
    list_filter  = ['yayinda', 'stadt', 'scope']
    prepopulated_fields = {'slug': ('baslik',)}
