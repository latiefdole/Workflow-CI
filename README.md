# Workflow-CI

Repository untuk **Kriteria 3** — Workflow CI menggunakan MLflow Project dan GitHub Actions.

## 📋 Deskripsi

CI pipeline yang secara otomatis melatih model ML setiap kali ada push ke branch `main`,
menyimpan artefak ke GitHub, dan membangun Docker image ke Docker Hub.

## 🗂️ Struktur Folder

```
Workflow-CI/
├── .github/workflows/
│   └── ci.yml                  # GitHub Actions CI workflow
└── MLProject/
    ├── MLProject                # Konfigurasi MLflow Project
    ├── conda.yaml               # Environment dependencies
    ├── modelling.py             # Script training model
    ├── wine_quality_preprocessing/   # Dataset preprocessed
    └── docker_image_link.txt    # Link Docker Hub image
```

## 🚀 Cara Menjalankan Lokal

```bash
pip install mlflow==2.19.0 scikit-learn pandas dagshub
mlflow run MLProject/ --env-manager local
```

## ⚙️ GitHub Actions Secrets yang Diperlukan

| Secret | Keterangan |
|--------|-----------|
| `MLFLOW_TRACKING_URI` | URI DagsHub MLflow |
| `MLFLOW_TRACKING_USERNAME` | Username DagsHub |
| `MLFLOW_TRACKING_PASSWORD` | Token DagsHub |
| `DOCKER_USERNAME` | Username Docker Hub |
| `DOCKER_PASSWORD` | Token Docker Hub |

## 🐳 Docker Image

```bash
docker pull latiefdole/wine-quality-model:latest
docker run -p 5001:8080 latiefdole/wine-quality-model:latest
```
