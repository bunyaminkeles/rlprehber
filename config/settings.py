import os
from pathlib import Path
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
    'duyurular',
    'forum',
    'blog',
    'ilan',
    'takvim',
    'yerler',
    'linkler',
    'almanca',
    'mesajlar',
]

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
ACCOUNT_LOGIN_METHODS = {'username', 'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# E-posta — Resend HTTP API (django-anymail)
if config('RESEND_API_KEY', default=''):
    EMAIL_BACKEND       = 'anymail.backends.resend.EmailBackend'
    ANYMAIL = {
        'RESEND_API_KEY': config('RESEND_API_KEY'),
    }
    DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='Almanyalı Rehber <info@almanyalirehber.com>')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Zamanlanmış görevler
CRONJOBS = [
    # Her gece 02:00 — RSS duyurularını çek
    ('0 2 * * *', 'django.core.management.call_command', ['rss_cek']),
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
