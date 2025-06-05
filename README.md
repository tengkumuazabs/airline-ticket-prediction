✈️ Airline Ticket Price Prediction (FastAPI)
A web-based machine learning app built with FastAPI to predict airline ticket prices based on user inputs like airline, route, time, and stops.

🔧 Features
🧠 Real-time ML model predictions

🖥️ HTML form interface with Jinja2 templates

🗂️ Organized file structure with static assets

📦 Docker support for deployment

🔐 Environment-based config via .env

📁 Project Structure
text
Copy
Edit
.
├── main.py                 # FastAPI application
├── model.joblib            # Pre-trained ML model
├── feature_engineering.py  # Custom feature transformation
├── templates/              # HTML templates (Jinja2)
├── static/                 # CSS, JS, Bootstrap
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker image setup
├── .env                    # Model path config
├── .dockerignore
🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo.git
cd your-repo
2. Create .env File
bash
Copy
Edit
echo "MODEL_PATH=model.joblib" > .env
3. Build and Run with Docker
bash
Copy
Edit
docker build -t airline-price-app .
docker run -d -p 8000:8000 airline-price-app
Visit: http://localhost:8000

📊 User Inputs
Airline (e.g., IndiGo, Jet Airways)

Departure City & Time

Arrival City & Time

Total Stops

App returns the predicted ticket price based on input data.

