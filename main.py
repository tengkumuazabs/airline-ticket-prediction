from fastapi import FastAPI, HTTPException, Form, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np
import pandas as pd
import logging
import os
from dotenv import load_dotenv
from feature_engineering import FeatureEngineer

# initialize FastAPI app
app = FastAPI()

# load the saved pipeline
load_dotenv()
model_path = os.getenv('MODEL_PATH', 'model.joblib')
model = joblib.load(model_path)

# mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# initialize jinja2template engine
templates = Jinja2Templates(directory='templates')

# home endpoint
@app.get('/')
def home(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse('index.html', {"request": request})

# endpoint for the prediction 
@app.get('/predict', response_class=HTMLResponse)
def predict(request: Request):
    return templates.TemplateResponse('predict.html', {'request': request, 'price': None})

@app.post('/predict')
def predict_price(request: Request,
                        airline: str = Form(...),
                        departure_city: str = Form(...),
                        dep_hour: str = Form(...),
                        dep_minute: str = Form(...),
                        arrival_city: str = Form(...),
                        arrival_hour: str = Form(...),
                        arrival_minute: str = Form(...),
                        stops: str = Form(...)
                ):

    price = None

    if airline is not None:
        try:
            # construct time strings
            dep_time = f"{int(dep_hour):02d}:{int(dep_minute):02d}"
            arrival_time = f"{int(arrival_hour):02d}:{int(arrival_minute):02d}"

            # prepare the data as a dataframe to keep the column names
            data = pd.DataFrame([{
                'airline': airline,
                'source': departure_city,
                'dep_time': dep_time,
                'destination': arrival_city,
                'arrival_time': arrival_time,
                'total_stops': stops 
            }])

            # make the prediction using the loaded pipeline
            pred = model.predict(data)[0]
            price = f"₹{pred:,.0f}" 
            
        except Exception as e:
            logging.error(f'error during prediction: {str(e)}')
            price = 'there was an issue with the prediction request, please try again later.'
            
    form_data = {
        'airline': airline,
        'departure_city': departure_city,
        'dep_hour': dep_hour,
        'dep_minute': dep_minute,
        'arrival_city': arrival_city,
        'arrival_hour': arrival_hour,
        'arrival_minute': arrival_minute,
        'stops': stops
    }
    
    return templates.TemplateResponse('predict.html', {'request': request, 'price': price, 'form_data': form_data})

    
