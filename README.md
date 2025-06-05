✈️ Airline Ticket Price Prediction (FastAPI)
A web app built with FastAPI to predict airline ticket prices using a trained ML model and user input (airline, route, time, stops).

🚀 Features
🔍 Real-time ticket price prediction

🖥️ Web UI using Jinja2 templates

📦 Dockerized for easy deployment

🧠 Custom feature engineering

⚙️ .env for config (MODEL_PATH)

📁 Project Structure
plaintext
Copy
Edit
main.py                 # FastAPI app
feature_engineering.py # Feature logic
model.joblib            # Trained model
templates/              # HTML templates
static/                 # JS, CSS, Bootstrap
Dockerfile, .env, etc.
🛠️ Setup Instructions
1. Clone + Configure
bash
Copy
Edit
git clone https://github.com/tengkumuazabs/airline-ticket-prediction.git
cd airline-ticket-prediction
echo "MODEL_PATH=model.joblib" > .env
2. Build & Run
bash
Copy
Edit
docker build -t airline-app .
docker run -d -p 8000:8000 airline-app
Visit: http://localhost:8000

📊 Inputs
Airline (e.g., IndiGo, Air India)

Departure/Arrival City & Time

Total Stops

The app predicts and displays the ticket price instantly.