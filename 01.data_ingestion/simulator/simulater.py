import time
import random
import json
import datetime
import requests

API_ENDPOINT = "http://localhost:8000/api/data"

def generate_data():
    return {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "athlete_id": "athlete_001",
        "heart_rate": random.randint(60, 180),
        "speed": round(random.uniform(2.0, 8.0), 2),
        "distance": round(random.uniform(0.1, 0.5), 2),
        "latitude": round(random.uniform(36.80, 36.90), 6),
        "longitude": round(random.uniform(10.10, 10.20), 6)
    }

while True:
    data = generate_data()
    print(f"Sending: {data}")
    try:
        response = requests.post(API_ENDPOINT, json=data)
        print(f"Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to send data: {e}")
    time.sleep(1)
