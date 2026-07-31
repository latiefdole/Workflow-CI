import requests
import json
import time
import random

url = "http://localhost:8080/invocations"

headers = {
    'Content-Type': 'application/json'
}

# Contoh fitur Maternal Health (6 fitur)
columns = [
    "Age", "SystolicBP", "DiastolicBP", 
    "BS", "BodyTemp", "HeartRate"
]

print("Mulai mengirim payload ke MLflow model...")

for i in range(15):
    # Buat data dummy random biar grafiknya gerak
    data_row = [
        random.uniform(20.0, 50.0),   # Age
        random.uniform(90.0, 140.0),  # SystolicBP
        random.uniform(60.0, 90.0),   # DiastolicBP
        random.uniform(6.0, 15.0),    # BS
        random.uniform(98.0, 102.0),  # BodyTemp
        random.uniform(60.0, 90.0)    # HeartRate
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
