from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Profil


@admin.register(Profil)
class ProfilAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ['kullanici', 'sehir', 'olusturulma']
