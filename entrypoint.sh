#!/bin/bash
set -e

echo "==> Migrate..."
python manage.py migrate --no-input

echo "==> Superuser..."
python manage.py shell -c "
from django.contrib.auth.models import User
import os
u = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
e = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@mainzer-binger.de')
p = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '')
if p and not User.objects.filter(username=u).exists():
    User.objects.create_superuser(u, e, p)
    print(f'Superuser olusturuldu: {u}')
else:
    print('Superuser zaten var.')
"

echo "==> Sites tablosu..."
python manage.py shell -c "
from django.contrib.sites.models import Site
import os
domain = os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'localhost')
Site.objects.update_or_create(id=1, defaults={'domain': domain, 'name': 'Mainzer-Binger'})
print(f'Site: {domain}')
"

echo "==> Blog yazilari..."
python blog_yazilari_ekle.py || true

echo "==> Linkler ve rehber seed..."
python linkler_seed.py || true

echo "==> Yerler seed..."
python yerler_seed.py || true

echo "==> Takvim seed..."
python takvim_seed.py || true

echo "==> Forum seed..."
python forum_seed.py || true

echo "==> RSS duyurular..."
python manage.py rss_cek --sadece-rss || true

echo "==> Gunicorn basliyor..."
exec gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 2 --log-file -
