from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("03.real_time_inference/inference_service/model.joblib")

class InferenceInput(BaseModel):
    heart_rate: float
    speed: float
    distance: float

@app.post("/predict")
def predict(input: InferenceInput):
    features = np.array([[input.heart_rate, input.speed, input.distance]])
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}