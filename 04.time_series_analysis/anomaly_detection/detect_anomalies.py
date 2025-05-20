import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("data/time_series/metrics.csv")

features = data[["heart_rate", "speed"]]

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(features)

data["anomaly"] = model.predict(features)

data.to_csv("data/time_series/anomalies_detected.csv", index=False)