FROM python:3.12-slim

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Önce requirements (Docker cache katmanı için)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyaları
COPY . .

# Static dosyaları derle
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000", "--workers", "2", "--log-file", "-"]
