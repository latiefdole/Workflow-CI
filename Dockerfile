FROM python:3.10-slim

WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install dependencies (sesuaikan dengan conda.yaml)
RUN pip install --no-cache-dir \
    mlflow==2.19.0 \
    scikit-learn \
    pandas \
    numpy \
    matplotlib \
    dagshub \
    mlserver \
    mlserver-mlflow

# Copy model yang sudah di-download oleh CI
COPY model_artifact/model /app/model

# Expose port
EXPOSE 8080

# Environment tracking dikosongkan agar serve mode jalan murni tanpa ke DagsHub lagi
ENV MLFLOW_TRACKING_URI=""

# Jalankan mlflow serve
CMD ["mlflow", "models", "serve", "-m", "/app/model", "-h", "0.0.0.0", "-p", "8080", "--enable-mlserver", "--env-manager", "local"]
