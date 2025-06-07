import streamlit as st
import pandas as pd
import joblib
import os
from dotenv import load_dotenv
# from feature_engineering import FeatureEngineer

# Load model
load_dotenv()
model_path = os.getenv('MODEL_PATH', 'model.joblib')
# model = joblib.load(model_path)
model = joblib.load('model.joblib')

st.set_page_config(page_title="Airline Ticket Predictor", layout="wide")

# Create centered columns (empty - narrow - empty)
col1, col2, col3 = st.columns([3, 2.4, 3])  # Left space, Narrow Form, Right space

with col2:
    st.title("✈️ Predict Ticket Price")

    with st.form("prediction_form"):
        # st.markdown("Airline")
        airline = st.radio("Airline", [
            "Air Asia", "Air India", "Go Air", "IndiGo", "Jet Airways",
            "Multiple carriers", "SpiceJet", "Vistara"
        ])

        # st.subheader("Departure City")
        departure_city = st.radio("Departure City   ", [
            "Banglore", "Chennai", "Delhi", "Kolkata", "Mumbai"
        ])

        dep_hour = st.selectbox("Departure Time (Hour)", [f"{h:02d}" for h in range(24)], key="dep_hour")
        dep_minute = st.selectbox("Departure Time (Minute)", [f"{m:02d}" for m in range(60)], key="dep_minute")

        arrival_city = st.radio("Arrival City", [
            "Banglore", "Cochin", "Delhi", "Hyderabad", "Kolkata"
        ])

        arrival_hour = st.selectbox("Arrival Time (Hour)", [f"{h:02d}" for h in range(24)], key="arr_hour")
        arrival_minute = st.selectbox("Arrival Time (Minute)", [f"{m:02d}" for m in range(60)], key="arr_min")

        stops = st.radio("Total Stop(s)", ["0", "1", "2", "3"])

        submitted = st.form_submit_button("Predict")

    if submitted:
        try:
            dep_time = f"{dep_hour}:{dep_minute}"
            arrival_time = f"{arrival_hour}:{arrival_minute}"

            input_df = pd.DataFrame([{
                'airline': airline,
                'source': departure_city,
                'dep_time': dep_time,
                'destination': arrival_city,
                'arrival_time': arrival_time,
                'total_stops': stops
            }])

            # Optional: apply feature engineering here
            # input_df = FeatureEngineer().transform(input_df)

            prediction = model.predict(input_df)[0]
            st.success(f"✅ Predicted Price: ₹{prediction:,.0f}")

            with st.expander("View Input Summary", expanded=True):
                input_df = input_df.rename(columns={
                    'airline': 'Airline',
                    'source': 'Departure City',
                    'dep_time': 'Departure Time',
                    'destination': 'Arrival City',
                    'arrival_time': 'Arrival Time',
                    'total_stops': 'Total Stops(s)'
                })
                st.write(input_df.T.rename(columns={0: 'Value'}))

        except Exception as e:
            st.error("Prediction failed.")
            st.exception(e)
