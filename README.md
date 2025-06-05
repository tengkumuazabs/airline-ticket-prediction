# ✈️ Airline Ticket Price Prediction (FastAPI)

A web-based machine learning app built with **FastAPI** to predict airline ticket prices based on user inputs like airline, route, time, and stops.

## 🔧 Features

- 🧠 Real-time ML model predictions  
- 🖥️ HTML form interface with **Jinja2 templates**  
- 🗂️ Organized file structure with **static assets**  
- 📦 Docker support for deployment  
- 🔐 Environment-based config via `.env`  

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/tengkumuazabs/airline-ticket-prediction.git
cd airline-ticket-prediction
```
### 2. Create `.env` File
```bash
echo "MODEL_PATH=model.joblib" > .env
```

### 3. Build and Run with Docker
```bash
docker build -t airline-price-app .
docker run -d -p 8000:8000 airline-price-app
```

## 📊 User Inputs
- 📝 Airline (e.g., Air India, IndiGo, Jet Airways)
- 📝 Departure City & Time
- 📝 Arrival City & Time
- 📝 Total Stops
- 📝 App returns the predicted ticket price based on input data.


