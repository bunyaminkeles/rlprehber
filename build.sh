#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Superuser otomatik oluştur (env var'lardan alır, zaten varsa atlar)
python manage.py shell -c "
from django.contrib.auth.models import User
import os
u = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
e = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'info@analizus.com')
p = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
if p and not User.objects.filter(username=u).exists():
    User.objects.create_superuser(u, e, p)
    print(f'Superuser olusturuldu: {u}')
else:
    print('Superuser zaten var, atlandi.')
"

# Sites tablosunu Render domain'e ayarla
python manage.py shell -c "
from django.contrib.sites.models import Site
import os
domain = os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'localhost')
Site.objects.update_or_create(id=1, defaults={'domain': domain, 'name': 'RLP Rehber'})
print(f'Site domain ayarlandi: {domain}')
"

# Blog yazılarını yükle
python blog_yazilari_ekle.py

# Reklam paketlerini yükle
python reklam_paketleri_seed.py

# RSS duyurularını çek
python manage.py rss_cek --sadece-rss || true
