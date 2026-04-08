from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Etkinlik


@admin.register(Etkinlik)
class EtkinlikAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ['baslik', 'tarih', 'tur', 'eyalet', 'stadt', 'scope']
    list_filter  = ['tur', 'eyalet', 'stadt', 'scope']
