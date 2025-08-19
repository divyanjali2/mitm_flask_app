from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
from tensorflow.keras.models import load_model
from typing import List

# Load saved models & preprocessing
isolation_forest = joblib.load("isolation_forest.pkl")
linear_svm = joblib.load("linear_svm1.pkl")
scaler = joblib.load("scaler.pkl")
cnn = load_model("cnn_model.h5")

app = FastAPI()

# Enable CORS
origins = ["http://localhost", "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Features(BaseModel):
    features: List[float]

@app.post("/predict")
def predict(input_data: Features):
    X = np.array(input_data.features).reshape(1, -1)
    X_scaled = scaler.transform(X)

    if_pred = isolation_forest.predict(X_scaled).reshape(-1, 1)
    svm_pred = linear_svm.predict(X_scaled).reshape(-1, 1)

    cnn_input = np.concatenate([X_scaled, if_pred, svm_pred], axis=1)
    cnn_input = cnn_input.reshape(cnn_input.shape[0], cnn_input.shape[1], 1)

    prediction = cnn.predict(cnn_input)
    print("Raw CNN prediction:", prediction)

    attack_prob = float(prediction[0][0]) if prediction.shape[1] == 1 else float(prediction[0][1])

    return {
        "attack_probability": attack_prob,
        "label": "Attack" if attack_prob >= 0.5 else "Benign"
    }

print("Models loaded successfully!")
