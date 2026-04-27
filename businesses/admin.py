from django.contrib import admin
from django.utils.html import mark_safe
from unfold.admin import ModelAdmin
from .models import GlobalSetting, SubscriptionPlan, BusinessCategory, LocalBusiness, BusinessAnalytics


@admin.register(GlobalSetting)
class GlobalSettingAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True

    def has_add_permission(self, request):
        return not GlobalSetting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ('name', 'price', 'duration_days', 'is_active')
    list_editable = ('is_active',)


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ('name', 'slug', 'icon')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(LocalBusiness)
class LocalBusinessAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = (
        'name',
        'city',
        'category',
        'subscription_plan',
        'end_date',
        'active_status_icon',
        'is_verified',
    )
    list_filter = ('city', 'subscription_plan', 'is_published', 'is_verified', 'category')
    search_fields = ('name', 'slug', 'whatsapp_number')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Kimlik', {
            'fields': ('name', 'slug', 'city', 'category'),
        }),
        ('İçerik', {
            'fields': ('slogan', 'description'),
        }),
        ('Medya', {
            'fields': ('logo', 'logo_url', 'cover_image', 'cover_image_url'),
        }),
        ('İletişim', {
            'fields': ('whatsapp_number', 'instagram_url', 'website_url'),
        }),
        ('Abonelik & Yönetim', {
            'fields': (
                'subscription_plan',
                ('start_date', 'end_date'),
                ('is_published', 'is_verified'),
            ),
        }),
        ('Sistem', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def delete_model(self, request, obj):
        obj.analytics.all().delete()
        obj.delete()

    def delete_queryset(self, request, queryset):
        BusinessAnalytics.objects.filter(business__in=queryset).delete()
        queryset.delete()

    @admin.display(description='Durum', ordering='end_date')
    def active_status_icon(self, obj):
        if obj.is_currently_active:
            return mark_safe('<span style="color:#2e7d32;font-weight:bold;" title="Aktif">✔ Aktif</span>')
        return mark_safe('<span style="color:#c62828;font-weight:bold;" title="Pasif">✘ Pasif</span>')


@admin.register(BusinessAnalytics)
class BusinessAnalyticsAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_changes = True
    list_display = ('business', 'date', 'views', 'whatsapp_clicks')
    list_filter = ('date', 'business__city')
    readonly_fields = ('business', 'date', 'views', 'whatsapp_clicks')
    ordering = ('-date',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
