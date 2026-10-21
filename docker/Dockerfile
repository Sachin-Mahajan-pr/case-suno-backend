# Build Plan Section 13 (Page 19)
# Multi-stage production container for CASE SUNO Backend

FROM python:3.12-slim

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project source code
COPY . .

# Run as non-root user for security
RUN useradd -m casesuno && chown -R casesuno:casesuno /app
USER casesuno

EXPOSE 8000

# Default entrypoint starts gunicorn with WSGI application
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
