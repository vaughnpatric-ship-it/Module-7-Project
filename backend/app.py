from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI(title='SuperKart Sales Prediction API')
model = joblib.load('superkart_model.joblib')

class PredictionInput(BaseModel):
    Product_Weight: float
    Product_Sugar_Content: str
    Product_Allocated_Area: float
    Product_MRP: float
    Store_Size: str
    Store_Location_City_Type: str
    Store_Type: str
    Product_Id_char: str
    Store_Age_Years: int
    Product_Type_Category: str

@app.get('/')
def read_root():
    return {'message': 'SuperKart Prediction API is running!'}

@app.post('/predict')
def predict(data: PredictionInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)[0]
    return {'prediction': float(prediction)}
