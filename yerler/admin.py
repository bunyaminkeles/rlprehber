from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Yer, YerFoto, ReklamPaketi, YerKategori


# ── Toplu işlem aksiyonları ──────────────────────────────────────────────────

@admin.action(description='Seçilenleri aktif yap')
def aktif_yap(modeladmin, request, queryset):
    queryset.update(aktif=True)

@admin.action(description='Seçilenleri pasif yap')
def pasif_yap(modeladmin, request, queryset):
    queryset.update(aktif=False)


# ── Yer ─────────────────────────────────────────────────────────────────────

class YerFotoInline(TabularInline):
    model    = YerFoto
    extra    = 3
    fields   = ['foto', 'url', 'sira']
    ordering = ['sira']


@admin.register(Yer)
class YerAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display  = ['ad', 'tur', 'kategori_adi', 'eyalet', 'stadt', 'aktif_flag', 'paket', 'paket_bitis']
    list_display_links = ['ad']
    list_filter   = ['tur', 'paket', 'aktif', 'kategori', 'eyalet', 'stadt', 'scope']
    list_editable = []
    search_fields = ['ad', 'adres']
    actions       = [aktif_yap, pasif_yap]
    inlines       = [YerFotoInline]
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('ad', 'tur', 'kategori', 'stadt', 'eyalet', 'scope', 'aktif', 'adres', 'kapak_foto', 'kapak_resmi')
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

    @admin.display(description='Kategori', ordering='kategori')
    def kategori_adi(self, obj):
        kat = YerKategori.objects.filter(slug=obj.kategori).first()
        return kat.ad if kat else obj.kategori

    @admin.display(description='Aktif', boolean=True, ordering='aktif')
    def aktif_flag(self, obj):
        return obj.aktif


# ── YerKategori ──────────────────────────────────────────────────────────────

@admin.register(YerKategori)
class YerKategoriAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display  = ['ad', 'slug', 'tur', 'sira']
    list_editable = ['tur', 'sira']
    list_filter   = ['tur']
    prepopulated_fields = {'slug': ('ad',)}


# ── ReklamPaketi ─────────────────────────────────────────────────────────────

@admin.register(ReklamPaketi)
class ReklamPaketiAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display  = ['ad', 'fiyat', 'sure_etiketi', 'vurgulu', 'aktif_flag', 'sira']
    list_editable = ['vurgulu', 'sira']
    list_filter   = ['aktif', 'vurgulu']
    actions       = [aktif_yap, pasif_yap]
    fields        = ['ad', 'aciklama', 'fiyat', 'sure_etiketi', 'renk', 'vurgulu', 'aktif', 'sira', 'ozellikler', 'iletisim_notu']

    @admin.display(description='Aktif', boolean=True, ordering='aktif')
    def aktif_flag(self, obj):
        return obj.aktif
