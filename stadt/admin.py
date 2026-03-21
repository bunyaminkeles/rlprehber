from django.contrib import admin
from .models import Stadt


@admin.register(Stadt)
class StadtAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'typ', 'population', 'aktiv')
    list_filter = ('typ', 'aktiv')
    list_editable = ('aktiv',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    actions = ['aktif_yap', 'pasif_yap']

    @admin.action(description='Seçili şehirleri aktif et')
    def aktif_yap(self, request, queryset):
        queryset.update(aktiv=True)

    @admin.action(description='Seçili şehirleri pasif et')
    def pasif_yap(self, request, queryset):
        queryset.update(aktiv=False)
