import requests
import json
import time
import random

url = "http://localhost:8080/invocations"

headers = {
    'Content-Type': 'application/json'
}

# Contoh fitur Wine Quality (11 fitur)
columns = [
    "fixed acidity", "volatile acidity", "citric acid", 
    "residual sugar", "chlorides", "free sulfur dioxide", 
    "total sulfur dioxide", "density", "pH", 
    "sulphates", "alcohol"
]

print("Mulai mengirim payload ke MLflow model...")

for i in range(15):
    # Buat data dummy random biar grafiknya gerak
    data_row = [
        random.uniform(6.0, 8.0),   # fixed acidity
        random.uniform(0.1, 0.9),   # volatile acidity
        random.uniform(0.0, 0.5),   # citric acid
        random.uniform(1.0, 10.0),  # residual sugar
        random.uniform(0.01, 0.1),  # chlorides
        random.uniform(5.0, 50.0),  # free sulfur dioxide
        random.uniform(10.0, 150.0),# total sulfur dioxide
        random.uniform(0.990, 1.0), # density
        random.uniform(3.0, 4.0),   # pH
        random.uniform(0.3, 1.0),   # sulphates
        random.uniform(8.0, 14.0)   # alcohol
    ]
    
    payload = {
        "dataframe_split": {
            "columns": columns,
            "data": [data_row]
        }
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(f"Request {i+1}/15 - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Request {i+1} failed: {e}")
        
    time.sleep(1) # delay 1 detik per request

print("Selesai mengirim payload! Cek dashboard Grafana sekarang.")
