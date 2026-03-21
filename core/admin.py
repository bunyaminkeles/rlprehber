from django.contrib import admin
from .models import Oneri


@admin.register(Oneri)
class OneriAdmin(admin.ModelAdmin):
    list_display = ('tur', 'ad', 'eposta', 'olusturulma', 'okundu')
    list_filter = ('tur', 'okundu')
    list_editable = ('okundu',)
    readonly_fields = ('olusturulma',)
    search_fields = ('ad', 'eposta', 'mesaj')
