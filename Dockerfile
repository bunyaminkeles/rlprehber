FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Build sırasında geçici SECRET_KEY — sadece collectstatic için
RUN SECRET_KEY=build-only-dummy-key DATABASE_URL=sqlite:///dummy.db \
    python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000", "--workers", "2", "--log-file", "-"]
