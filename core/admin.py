from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Oneri


@admin.register(Oneri)
class OneriAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ('tur', 'ad', 'eposta', 'olusturulma', 'okundu')
    list_filter = ('tur', 'okundu')
    list_editable = ('okundu',)
    readonly_fields = ('olusturulma',)
    search_fields = ('ad', 'eposta', 'mesaj')
