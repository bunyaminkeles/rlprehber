from django.contrib import admin
from .models import Yer, YerFoto, ReklamPaketi


class YerFotoInline(admin.TabularInline):
    model   = YerFoto
    extra   = 3
    fields  = ['foto', 'url', 'sira']
    ordering = ['sira']


@admin.register(Yer)
class YerAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'kategori', 'stadt', 'paket', 'paket_bitis', 'aktif']
    list_filter   = ['paket', 'aktif', 'kategori', 'stadt', 'scope']
    list_editable = ['paket', 'aktif']
    search_fields = ['ad', 'adres']
    inlines       = [YerFotoInline]
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('ad', 'kategori', 'stadt', 'scope', 'aktif', 'adres', 'kapak_foto', 'kapak_resmi')
        }),
        ('İletişim', {
            'fields': ('telefon', 'website', 'maps_url', 'instagram_url', 'whatsapp', 'calisma_saati')
        }),
        ('Paket', {
            'fields': ('paket', 'paket_bitis'),
            'description': 'Ödeme yapıldığında paketi güncelleyin. Süre bittiğinde "Ücretsiz" olarak geri alın.',
        }),
        ('İçerik', {
            'fields': ('aciklama', 'icerik', 'wikipedia_url'),
            'classes': ('collapse',),
        }),
    )


@admin.register(ReklamPaketi)
class ReklamPaketiAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'fiyat', 'sure_etiketi', 'vurgulu', 'aktif', 'sira']
    list_editable = ['aktif', 'vurgulu', 'sira']
    list_filter   = ['aktif', 'vurgulu']
    fields        = ['ad', 'aciklama', 'fiyat', 'sure_etiketi', 'renk', 'vurgulu', 'aktif', 'sira', 'ozellikler', 'iletisim_notu']
