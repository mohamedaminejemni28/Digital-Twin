# 🏃‍♂️🏋️‍♀️ Athlete Performance Digital Twin



![Athlete Digital Twin Banner](https://your-image-link.com/banner.png)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Architecture](#architecture)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Data Simulation](#data-simulation)
  - [Simulator Script](#simulator-script)
  - [Running the Simulation](#running-the-simulation)
- [API Endpoints](#api-endpoints)
- [Frontend](#frontend)
- [Deployment](#deployment)
  - [Docker Compose](#docker-compose)
  - [Kubernetes](#kubernetes)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

**Athlete Performance Digital Twin** is a cutting-edge platform designed to create a real-time digital replica of an athlete’s physical state by collecting, processing, and analyzing live biometric and location data. This system enables coaches, trainers, and athletes to monitor performance metrics, detect anomalies, and optimize training regimens through rich visualizations and data-driven insights.

---

## Motivation

With the rise of IoT devices and wearable sensors, capturing live physiological and positional data from athletes is more accessible than ever. However, transforming raw sensor data into actionable insights requires robust infrastructure that can handle real-time ingestion, processing, inference, and visualization. This project bridges that gap by providing a scalable digital twin that mirrors the athlete's current condition for performance enhancement and health monitoring.

---

## Architecture

```text
+-------------------------+        +-------------------------+        +---------------------+
| 01. Data Ingestion      | -----> | 02. Data Processing      | -----> | 03. Real-time       |
| - Simulator             |        | - PySpark Pipeline       |        |     Inference       |
| - Sensor Connector      |        | - NiFi Flow              |        | - Model Training    |
+-------------------------+        +-------------------------+        | - Inference Service |
                                                                        +---------------------+
                                                                             |
                                                                             v
                                                                   +----------------------+
                                                                   | 04. Time Series       |
                                                                   | - Anomaly Detection   |
                                                                   | - Trend Analysis      |
                                                                   +----------------------+
                                                                             |
                                                                             v
                                                                    +--------------------+
                                                                    | Frontend (React)   |
                                                                    | Backend (FastAPI)  |
                                                                    +--------------------+
````

---

## Features

* **Real-Time Data Ingestion:** From simulated sources or actual IoT sensors.
* **Data Processing Pipelines:** Batch and streaming processing via PySpark and NiFi.
* **Model Training and Inference:** Machine learning models for performance prediction and anomaly detection.
* **Time-Series Analysis:** Detects trends and anomalies over athlete’s training sessions.
* **Interactive Frontend:** Dynamic dashboard to monitor live data with charts and maps.
* **Scalable Deployment:** Dockerized and Kubernetes-ready for flexible deployment.

---

## Technologies Used

| Component            | Technology / Framework                    |
| -------------------- | ----------------------------------------- |
| Data Ingestion       | Python, Requests, MQTT (optional)         |
| Data Processing      | Apache PySpark, Apache NiFi               |
| Real-Time Inference  | Python, Scikit-learn, TensorFlow, FastAPI |
| Time Series Analysis | Pandas, NumPy, Prophet, PyOD              |
| Backend API          | FastAPI, Uvicorn                          |
| Frontend             | React, Chart.js / Plotly                  |
| Storage              | Redis, InfluxDB, PostgreSQL               |
| Containerization     | Docker, Docker Compose                    |
| Orchestration        | Kubernetes                                |

---

## Getting Started

### Prerequisites

* Python 3.10 or higher
* Git
* Docker & Docker Compose (optional but recommended)
* Redis or InfluxDB instance running locally or in cloud

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/athlete-digital-twin.git
   cd athlete-digital-twin
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Setup environment variables:

   Create a `.env` file in the project root with content like:

   ```
   DEBUG=True
   API_KEY=your_api_key_here
   REDIS_URL=redis://localhost:6379/0
   ```

---

## Data Simulation

This project supports simulating realistic athlete biometric and GPS data to test the system in the absence of real sensors.

### Simulator Script

The script `01.data_ingestion/simulator/simulate_data.py` generates and sends simulated data every second to the backend API.

```python
import time
import requests
import random
from datetime import datetime

API_URL = "http://localhost:8000/api/data"

def generate_data():
    return {
        "athlete_id": "athlete_01",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "heart_rate": random.randint(60, 180),
        "speed": round(random.uniform(3.0, 10.0), 2),
        "gps_lat": 40.7128 + random.uniform(-0.001, 0.001),
        "gps_lon": -74.0060 + random.uniform(-0.001, 0.001),
    }

def simulate_and_send(interval_sec=1):
    while True:
        data = generate_data()
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print(f"Sent: {data}")
        else:
            print(f"Failed to send data: {response.status_code}")
        time.sleep(interval_sec)

if __name__ == "__main__":
    simulate_and_send()
```

---

### Running the Simulation

1. Start your backend API server (example with FastAPI):

   ```bash
   uvicorn backend.app.main:app --reload
   ```

2. Run the simulator script:

   ```bash
   python 01.data_ingestion/simulator/simulate_data.py
   ```

The simulator will continuously send athlete data every second to the API endpoint.

---

## API Endpoints (Example)

| Method | Endpoint            | Description                      |
| ------ | ------------------- | -------------------------------- |
| POST   | `/api/data`         | Ingest athlete biometric data    |
| GET    | `/api/athlete/{id}` | Get athlete info and stats       |
| GET    | `/api/metrics`      | Fetch processed performance data |

Example POST payload:

```json
{
  "athlete_id": "athlete_01",
  "timestamp": "2025-05-20T12:00:00Z",
  "heart_rate": 140,
  "speed": 7.8,
  "gps_lat": 40.7128,
  "gps_lon": -74.0060
}
```

---

## Frontend

The frontend is built using React.js, leveraging libraries such as Chart.js or Plotly for dynamic visualizations of:

* Heart rate and speed over time
* Live GPS tracking on maps
* Alerts for anomalies or performance thresholds

Start the frontend development server:

```bash
cd frontend
npm install
npm start
```

---

## Deployment

### Docker Compose

The project includes Dockerfiles and a `docker-compose.yml` for easy setup of all components:

```bash
docker-compose up --build -d
```

This will launch:

* Backend API
* Frontend React app
* Redis or InfluxDB instance
* Optional data simulator container

---

### Kubernetes

For scalable production deployment, Kubernetes manifests are provided in the `k8s/` folder.

Deploy using:

```bash
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
```

Configure ingress and scaling policies as needed.
