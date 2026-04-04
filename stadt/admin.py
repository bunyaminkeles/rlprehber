from django.contrib import admin
from .models import Eyalet, Stadt


@admin.register(Eyalet)
class EyaletAdmin(admin.ModelAdmin):
    list_display = ('ad', 'kod', 'slug', 'baskent', 'aktif', 'sehir_sayisi')
    list_editable = ('aktif',)
    prepopulated_fields = {'slug': ('ad',)}
    search_fields = ('ad', 'kod', 'baskent')
    actions = ['aktif_yap', 'pasif_yap']

    @admin.display(description='Şehir Sayısı')
    def sehir_sayisi(self, obj):
        return obj.sehirler.count()

    @admin.action(description='Seçili eyaletleri aktif et')
    def aktif_yap(self, request, queryset):
        queryset.update(aktif=True)

    @admin.action(description='Seçili eyaletleri pasif et')
    def pasif_yap(self, request, queryset):
        queryset.update(aktif=False)


@admin.register(Stadt)
class StadtAdmin(admin.ModelAdmin):
    list_display = ('name', 'eyalet', 'slug', 'typ', 'population', 'kapak_resmi_url', 'aktiv')
    list_filter = ('eyalet', 'typ', 'aktiv')
    list_editable = ('aktiv',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    autocomplete_fields = ('eyalet',)
    actions = ['aktif_yap', 'pasif_yap']

    @admin.action(description='Seçili şehirleri aktif et')
    def aktif_yap(self, request, queryset):
        queryset.update(aktiv=True)

    @admin.action(description='Seçili şehirleri pasif et')
    def pasif_yap(self, request, queryset):
        queryset.update(aktiv=False)
