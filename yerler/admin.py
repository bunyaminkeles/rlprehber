from django.contrib import admin
from .models import Yer, YerFoto, ReklamPaketi


# ── Toplu işlem aksiyonları ──────────────────────────────────────────────────

@admin.action(description='Seçilenleri aktif yap')
def aktif_yap(modeladmin, request, queryset):
    queryset.update(aktif=True)

@admin.action(description='Seçilenleri pasif yap')
def pasif_yap(modeladmin, request, queryset):
    queryset.update(aktif=False)


# ── Yer ─────────────────────────────────────────────────────────────────────

class YerFotoInline(admin.TabularInline):
    model    = YerFoto
    extra    = 3
    fields   = ['foto', 'url', 'sira']
    ordering = ['sira']


@admin.register(Yer)
class YerAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'tur', 'kategori', 'stadt', 'paket', 'paket_bitis', 'aktif_flag']
    list_filter   = ['tur', 'paket', 'aktif', 'kategori', 'stadt', 'scope']
    list_editable = ['tur', 'paket']
    search_fields = ['ad', 'adres']
    actions       = [aktif_yap, pasif_yap]
    inlines       = [YerFotoInline]
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('ad', 'tur', 'kategori', 'stadt', 'scope', 'aktif', 'adres', 'kapak_foto', 'kapak_resmi')
        }),
        ('İletişim', {
            'fields': ('telefon', 'website', 'maps_url', 'instagram_url', 'whatsapp', 'calisma_saati')
        }),
        ('Paket (İşletmeler için)', {
            'fields': ('paket', 'paket_bitis'),
            'description': 'Sadece işletmeler için. Ödeme gelince paketi güncelleyin, süre bitince "Ücretsiz" yapın.',
        }),
        ('İçerik', {
            'fields': ('aciklama', 'icerik', 'wikipedia_url'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Aktif', boolean=True, ordering='aktif')
    def aktif_flag(self, obj):
        return obj.aktif


# ── ReklamPaketi ─────────────────────────────────────────────────────────────

@admin.register(ReklamPaketi)
class ReklamPaketiAdmin(admin.ModelAdmin):
    list_display  = ['ad', 'fiyat', 'sure_etiketi', 'vurgulu', 'aktif_flag', 'sira']
    list_editable = ['vurgulu', 'sira']
    list_filter   = ['aktif', 'vurgulu']
    actions       = [aktif_yap, pasif_yap]
    fields        = ['ad', 'aciklama', 'fiyat', 'sure_etiketi', 'renk', 'vurgulu', 'aktif', 'sira', 'ozellikler', 'iletisim_notu']

    @admin.display(description='Aktif', boolean=True, ordering='aktif')
    def aktif_flag(self, obj):
        return obj.aktif
