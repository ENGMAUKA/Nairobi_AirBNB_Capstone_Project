# ==========================================================
# app.py — Airbnb Price Prediction Flask App
# ==========================================================
from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("rf_price_pipeline.pkl")

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form inputs
        data = {
            'listing_type': [request.form['listing_type']],
            'room_type': [request.form['room_type']],
            'is_superhost': [1 if request.form['is_superhost'] == 'yes' else 0],
            'instant_bookable': [1 if request.form['instant_bookable'] == 'yes' else 0],
            'bedrooms': [float(request.form['bedrooms'])],
            'beds': [float(request.form['beds'])],
            'bathrooms': [float(request.form['bathrooms'])],
            'guests': [float(request.form['guests'])],
            'num_photos': [float(request.form['num_photos'])],
            'num_reviews': [float(request.form['num_reviews'])],
            'overall_rating': [float(request.form['overall_rating'])],
            'cleanliness_rating': [float(request.form['cleanliness_rating'])],
            'location_rating': [float(request.form['location_rating'])],
            'value_rating': [float(request.form['value_rating'])],
            'communication_rating': [float(request.form['communication_rating'])],
            'occupancy_rate': [float(request.form['occupancy_rate'])],
            'booking_lead_time': [float(request.form['booking_lead_time'])],
            'avg_length_of_stay': [float(request.form['avg_length_of_stay'])],
            'min_nights': [float(request.form['min_nights'])]
        }

        # Convert to DataFrame
        input_df = pd.DataFrame(data)

        # Make prediction
        predicted_price = model.predict(input_df)[0]

        return render_template('index.html',
                               prediction_text=f"💰 Predicted Price: ${predicted_price:,.2f}")

    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"⚠️ Error: {e}")

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)

