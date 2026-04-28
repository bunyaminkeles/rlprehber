from django import forms
from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Yer, YerFoto, ReklamPaketi, YerKategori


class YerAdminForm(forms.ModelForm):
    icerik = forms.CharField(
        widget=CKEditor5Widget(config_name='default'),
        required=False,
        label='Blog İçeriği (HTML)',
    )

    class Meta:
        model = Yer
        fields = '__all__'


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
    form = YerAdminForm
    compressed_fields = True
    warn_unsaved_changes = True
    list_display  = ['yer_adi', 'tur', 'kategori_adi', 'eyalet', 'stadt', 'aktif_flag', 'paket', 'paket_bitis']
    list_display_links = ['yer_adi']
    list_filter   = ['tur', 'paket', 'aktif', 'kategori', 'eyalet', 'stadt', 'scope']
    list_editable = []
    search_fields = ['ad', 'adres']
    actions       = [aktif_yap, pasif_yap]
    inlines       = [YerFotoInline]

    FIELDSETS_YER = (
        ('Temel Bilgiler', {
            'fields': ('ad', 'tur', 'kategori', 'stadt', 'eyalet', 'scope', 'aktif', 'sira'),
        }),
        ('Konum & Görsel', {
            'fields': ('adres', 'maps_url', 'kapak_foto', 'kapak_resmi'),
        }),
        ('İçerik', {
            'fields': ('aciklama', 'icerik', 'wikipedia_url'),
        }),
    )

    FIELDSETS_ISLETME = (
        ('Temel Bilgiler', {
            'fields': ('ad', 'tur', 'kategori', 'stadt', 'eyalet', 'scope', 'aktif', 'sira', 'adres', 'kapak_foto', 'kapak_resmi'),
        }),
        ('İletişim', {
            'fields': ('telefon', 'website', 'maps_url', 'instagram_url', 'whatsapp', 'calisma_saati'),
        }),
        ('Paket', {
            'fields': ('paket', 'paket_bitis'),
            'description': 'Ödeme gelince paketi güncelleyin, süre bitince "Ücretsiz" yapın.',
        }),
        ('İçerik', {
            'fields': ('aciklama', 'icerik', 'wikipedia_url'),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        if obj and obj.tur == 'isletme':
            return self.FIELDSETS_ISLETME
        return self.FIELDSETS_YER

    @admin.display(description='Yer Adı', ordering='ad')
    def yer_adi(self, obj):
        return obj.ad

    @admin.display(description='Kategori', ordering='kategori')
    def kategori_adi(self, obj):
        if not hasattr(self, '_kat_cache'):
            self._kat_cache = {k.slug: k.ad for k in YerKategori.objects.all()}
        return self._kat_cache.get(obj.kategori, obj.kategori)

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
