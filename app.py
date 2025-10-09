# ==========================================================
# Nairobi Airbnb: Price & Occupancy Prediction Flask App
# ==========================================================

from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np
import joblib

# --- scikit-learn imports (required for unpickling pipelines)
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# ==========================================================
# Custom Function import
# ==========================================================
from custom_funcs import binary_mapper_occ

# ==========================================================
# Initialize Flask App
# ==========================================================
app = Flask(__name__)

# ==========================================================
# Load Trained Models & Preprocessors
# ==========================================================
try:
    occ_model = joblib.load("model/final_linear_regression.pkl")
    price_model = joblib.load("model/xgb_tuned_price_pipeline.pkl")
    preprocessor = joblib.load("model/preprocessor.pkl")
    preprocessor_occ = joblib.load("model/preprocessor_occ.pkl")
except Exception as e:
    print("Error loading models:", e)

# ==========================================================
# Flask Routes
# ==========================================================
@app.route('/')
def home():
    """Home route showing the prediction form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles user input and returns model predictions."""
    try:
        # --- Collect data from the HTML form ---
        data = {
            'listing_type': request.form['listing_type'],
            'room_type': request.form['room_type'],
            'guests': float(request.form['guests']),
            'baths': float(request.form['baths']),
            'bedrooms': float(request.form['bedrooms']),
            'beds': float(request.form['beds']),
            'rating_overall': float(request.form['rating_overall']),
        }

        # --- Convert to DataFrame ---
        df = pd.DataFrame([data])

        # --- Apply Preprocessors ---
        df_price = preprocessor.transform(df)
        df_occ = preprocessor_occ.transform(df)

        # --- Make Predictions ---
        price_pred = price_model.predict(df_price)[0]
        occ_pred = occ_model.predict(df_occ)[0]

        # --- Render Results on Page ---
        return render_template(
            'index.html',
            prediction_text=f"Predicted Occupancy: {occ_pred:.2f} | Estimated Price: ${price_pred:.2f}"
        )

    except Exception as e:
        return jsonify({'error': str(e)})

# ==========================================================
# Run App
# ==========================================================
if __name__ == "__main__":
    app.run(debug=True)
