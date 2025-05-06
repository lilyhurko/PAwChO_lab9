# ETAP 1: Budowanie zależności
FROM python:3.11-slim AS builder

WORKDIR /app

# Unowocześnienie pip i instalacja narzędzi buildowych
RUN pip install --upgrade pip setuptools wheel

# Kopiujemy plik z zależnościami osobno dla cache
COPY requirements.txt .

# Instalujemy zależności do katalogu tymczasowego
RUN pip install --prefix=/install -r requirements.txt


# ETAP 2: Obraz końcowy (runtime)
FROM python:3.11-slim

# OCI-standard labels
LABEL org.opencontainers.image.title="app" \
    org.opencontainers.image.description="Aplikacja pogodowa i serwer IP/Timezone" \
    org.opencontainers.image.authors="Lilia Hurko" \
    org.opencontainers.image.version="1.0.0" \
    org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=5000

WORKDIR /app

# Kopiujemy zależności z etapu budowania
COPY --from=builder /install /usr/local

# Kopiujemy resztę kodu aplikacji
COPY . .

# Instalacja curl do healthchecka i czyszczenie systemu
RUN apt-get update && apt-get install -y curl --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Healthcheck — sprawdza czy aplikacja działa
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s CMD curl -f http://localhost:5000/ || exit 1

EXPOSE 5000

CMD ["python", "app.py"]
