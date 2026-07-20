FROM python:3.12.7-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY MLProject/conda.yaml .

# Install dependencies dari conda.yaml menggunakan pip (karena ini base python, bukan miniconda)
RUN pip install --no-cache-dir \
    mlflow==2.19.0 \
    scikit-learn>=1.3.0 \
    pandas>=2.0.0 \
    mlserver \
    mlserver-mlflow

# Copy model yang sudah di-download oleh CI
COPY model_artifact/model /app/model

# Expose port
EXPOSE 8080

# Environment variables
ENV MLFLOW_TRACKING_URI=""
ENV MLSERVER_PARALLEL_WORKERS=0

# Jalankan mlflow serve
CMD ["mlflow", "models", "serve", "-m", "/app/model", "-h", "0.0.0.0", "-p", "8080", "--enable-mlserver", "--env-manager", "local"]
