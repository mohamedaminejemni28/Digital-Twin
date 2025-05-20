import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/time_series/metrics.csv", parse_dates=["timestamp"])
data.set_index("timestamp", inplace=True)

data_resampled = data.resample("1T").mean()
data_resampled["heart_rate_rolling"] = data_resampled["heart_rate"].rolling(window=5).mean()

plt.figure(figsize=(12, 6))
plt.plot(data_resampled.index, data_resampled["heart_rate"], label="Heart Rate")
plt.plot(data_resampled.index, data_resampled["heart_rate_rolling"], label="Rolling Mean")
plt.title("Heart Rate Trend Over Time")
plt.xlabel("Time")
plt.ylabel("Heart Rate")
plt.legend()
plt.savefig("outputs/heart_rate_trend.png")