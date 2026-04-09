import os
from pathlib import Path
from django.urls import reverse_lazy
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# cron-job.org tetikleyici için gizli token
CRON_SECRET = config('CRON_SECRET', default='')

# Render otomatik hostname desteği
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# HTTPS güvenlik ayarları (production'da aktif)
if not DEBUG:
    SECURE_SSL_REDIRECT         = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
    SECURE_PROXY_SSL_HEADER     = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE       = True
    CSRF_COOKIE_SECURE          = True
    SECURE_HSTS_SECONDS         = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Üçüncü parti
    'anymail',
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',

    # Zamanlayıcı
    'django_crontab',

    # SEO
    'django.contrib.sitemaps',

    # Proje app'leri
    'stadt',
    'core',
    'accounts',
    'rehber',
    'duyurular.apps.DuyurularConfig',
    'forum',
    'blog',
    'ilan.apps.IlanConfig',
    'takvim',
    'yerler',
    'linkler',
    'almanca',
    'mesajlar',
    'businesses',
]

UNFOLD = {
    "SITE_TITLE": "Almanyalı Rehber | Komuta Merkezi",
    "SITE_HEADER": "Almanyalı Rehber",
    "COLORS": {
        "primary": {
            "50":  "239 246 255",
            "100": "219 234 254",
            "200": "191 219 254",
            "300": "147 197 253",
            "400": "96 165 250",
            "500": "59 130 246",
            "600": "37 99 235",
            "700": "29 78 216",
            "800": "30 64 175",
            "900": "30 58 138",
            "950": "23 37 84",
        },
    },
    "SITE_URL": "https://almanyalirehber.com",
    "SIDEBAR": {
        "show_search": False,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "🇩🇪 Almanyalı Rehber",
                "separator": False,
                "collapsible": False,
                "items": [
                    {
                        "title": "Siteye Git →",
                        "icon": "open_in_new",
                        "link": "https://almanyalirehber.com",
                    },
                ],
            },
            {
                "title": "💼 Ekosistem & Ticaret",
                "separator": False,
                "collapsible": False,
                "items": [
                    {
                        "title": "Yerel İşletmeler",
                        "icon": "home_work",
                        "link": reverse_lazy("admin:businesses_localbusiness_changelist"),
                    },
                    {
                        "title": "İşletme Kategorileri",
                        "icon": "category",
                        "link": reverse_lazy("admin:businesses_businesscategory_changelist"),
                    },
                    {
                        "title": "Abonelik Paketleri",
                        "icon": "workspace_premium",
                        "link": reverse_lazy("admin:businesses_subscriptionplan_changelist"),
                    },
                    {
                        "title": "Analitik",
                        "icon": "analytics",
                        "link": reverse_lazy("admin:businesses_businessanalytics_changelist"),
                    },
                    {
                        "title": "İlanlar",
                        "icon": "receipt_long",
                        "link": reverse_lazy("admin:ilan_ilan_changelist"),
                    },
                    {
                        "title": "Reklam Paketleri",
                        "icon": "sell",
                        "link": reverse_lazy("admin:yerler_reklampaketi_changelist"),
                    },
                ],
            },
            {
                "title": "📚 İçerik Yönetimi",
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Şehirler",
                        "icon": "location_city",
                        "link": reverse_lazy("admin:stadt_stadt_changelist"),
                    },
                    {
                        "title": "Eyaletler",
                        "icon": "map",
                        "link": reverse_lazy("admin:stadt_eyalet_changelist"),
                    },
                    {
                        "title": "Yerler",
                        "icon": "place",
                        "link": reverse_lazy("admin:yerler_yer_changelist"),
                    },
                    {
                        "title": "Yer Kategorileri",
                        "icon": "folder_open",
                        "link": reverse_lazy("admin:yerler_yerkategori_changelist"),
                    },
                    {
                        "title": "Kaynaklar",
                        "icon": "menu_book",
                        "link": reverse_lazy("admin:rehber_kaynak_changelist"),
                    },
                    {
                        "title": "Belgeler",
                        "icon": "description",
                        "link": reverse_lazy("admin:rehber_belge_changelist"),
                    },
                    {
                        "title": "Blog Yazıları",
                        "icon": "article",
                        "link": reverse_lazy("admin:blog_blogyazisi_changelist"),
                    },
                    {
                        "title": "Etkinlikler",
                        "icon": "event",
                        "link": reverse_lazy("admin:takvim_etkinlik_changelist"),
                    },
                    {
                        "title": "Önemli Linkler",
                        "icon": "link",
                        "link": reverse_lazy("admin:linkler_onemlilink_changelist"),
                    },
                ],
            },
            {
                "title": "👥 Topluluk & İletişim",
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Forum Konuları",
                        "icon": "forum",
                        "link": reverse_lazy("admin:forum_konu_changelist"),
                    },
                    {
                        "title": "Forum Kategorileri",
                        "icon": "label",
                        "link": reverse_lazy("admin:forum_forumkategori_changelist"),
                    },
                    {
                        "title": "Duyurular",
                        "icon": "campaign",
                        "link": reverse_lazy("admin:duyurular_duyuru_changelist"),
                    },
                    {
                        "title": "Konuşmalar",
                        "icon": "chat",
                        "link": reverse_lazy("admin:mesajlar_konusma_changelist"),
                    },
                ],
            },
            {
                "title": "🛡️ Kullanıcılar",
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Kullanıcılar",
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Profiller",
                        "icon": "manage_accounts",
                        "link": reverse_lazy("admin:accounts_profil_changelist"),
                    },
                    {
                        "title": "Gruplar",
                        "icon": "groups",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                    {
                        "title": "Bülten Aboneleri",
                        "icon": "mark_email_read",
                        "link": reverse_lazy("admin:rehber_bultenabone_changelist"),
                    },
                ],
            },
            {
                "title": "⚙️ Sistem",
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Modül Ayarı",
                        "icon": "toggle_on",
                        "link": reverse_lazy("admin:businesses_globalsetting_changelist"),
                    },
                    {
                        "title": "Öneriler & Geri Bildirim",
                        "icon": "rate_review",
                        "link": reverse_lazy("admin:core_oneri_changelist"),
                    },
                    {
                        "title": "Site Ayarları",
                        "icon": "dns",
                        "link": reverse_lazy("admin:sites_site_changelist"),
                    },
                ],
            },
        ],
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'core.middleware.ZiyaretSayaciMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'stadt.context_processors.alle_staedte',
                'core.context_processors.ziyaret_sayisi',
                'businesses.context_processors.business_module',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default=f'sqlite:///{BASE_DIR}/db.sqlite3')
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# S3 — sadece env var tanımlıysa aktif olur, yoksa local media kullanılır
_AWS_KEY = config('AWS_ACCESS_KEY_ID', default='')
if _AWS_KEY:
    AWS_ACCESS_KEY_ID        = _AWS_KEY
    AWS_SECRET_ACCESS_KEY    = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME  = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME       = config('AWS_S3_REGION_NAME', default='eu-central-1')
    AWS_S3_FILE_OVERWRITE    = True
    AWS_DEFAULT_ACL          = None          # Yeni bucket'larda ACL devre dışı
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_CUSTOM_DOMAIN     = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
    STORAGES = {
        'default':    {'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage'},
        'staticfiles': {'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'},
    }
else:
    STORAGES = {
        'default':    {'BACKEND': 'django.core.files.storage.FileSystemStorage'},
        'staticfiles': {'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage'},
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Django Allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_ADAPTER = 'accounts.adapter.AccountAdapter'
ACCOUNT_LOGIN_METHODS = {'username', 'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.CustomSignupForm'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# E-posta — SMTP (mail.analizus.com)
EMAIL_BACKEND    = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST       = config('EMAIL_HOST', default='mail.analizus.com')
EMAIL_PORT       = config('EMAIL_PORT', default=465, cast=int)
EMAIL_USE_SSL    = config('EMAIL_USE_SSL', default=True, cast=bool)
EMAIL_USE_TLS    = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_HOST_USER  = config('EMAIL_HOST_USER', default='info@analizus.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='Almanyalı Rehber <info@analizus.com>')

# Zamanlanmış görevler
CRONJOBS = [
    # Her gece 02:00 — RSS duyurularını çek
    ('0 2 * * *', 'django.core.management.call_command', ['rss_cek']),

    # Her Cuma 10:00 — Haftalık bülteni gönder
    ('0 10 * * 5', 'django.core.management.call_command', ['bulten_gonder', 'Haftalık Bülten', 'rehber/email/bulten_icerik.html']),

    # Her gece 03:00 — Süresi dolan ilanları/duyuruları kapat, eski forum konularını sil
    ('0 3 * * *', 'django.core.management.call_command', ['icerik_temizle']),
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {'handlers': ['console'], 'level': 'WARNING', 'propagate': False},
        'django.request': {'handlers': ['console'], 'level': 'ERROR', 'propagate': False},
    },
}
