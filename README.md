# Nairobi_AirBNB_Capstone_Project

---

## 📑 Table of Contents

1. [Introduction](#introduction)
2. [Business Understanding](#business-understanding)
3. [Data Understanding](#data-understanding)
4. [Modeling](#modeling)
5. [Visualization](#visualization)
6. [Conclusion](#conclusion)
7. [Collaborators](#collaborators)

---

## 🔎 Introduction

This project explores **Airbnb listings in Nairobi City, Kenya**, focusing on two central tasks:

* **Price Prediction**: Estimating optimal nightly rates for listings.
* **Occupancy Prediction**: Understanding booking performance and drivers of high/low occupancy.

The analysis integrates **machine learning, sentiment analysis, and geospatial visualization** to provide actionable insights for hosts and stakeholders.

---

## 💼 Business Understanding

The key questions addressed:

* Which features drive listing **prices** in Nairobi?
* What factors influence **occupancy performance**?
* How do **guest sentiments** (reviews) correlate with listing performance?
* What geospatial patterns emerge in pricing and occupancy across Nairobi?

---

## 📊 Data Understanding

The dataset includes Airbnb listing attributes:

* **Numerical**: price, number of reviews, availability, occupancy rates
* **Categorical**: room type, property type, amenities
* **Textual**: guest reviews (for sentiment and topic modeling)
* **Geospatial**: latitude, longitude (for mapping)

Libraries used:

* **Data Handling**: Pandas, NumPy
* **Visualization**: Matplotlib, Seaborn, Plotly
* **Geospatial**: GeoPandas, Folium
* **NLP**: VADER Sentiment, BERTopic

---

## 🤖 Modeling

Several predictive approaches were tested:

* **Regression Models**: Linear Regression, Ridge, Lasso, ElasticNet
* **Ensemble Methods**: Random Forest Regressor, XGBoost Regressor
* **Text Analysis**:

  * **VADER Sentiment** → polarity scores from reviews
  * **BERTopic** → topic clusters of guest feedback

Evaluation metrics:

* **RMSE (Root Mean Squared Error)**
* **MAE (Mean Absolute Error)**
* **R² Score**

---

## 📈 Visualization

### Price Distribution of Listings

<img width="1384" height="484" alt="image" src="https://github.com/user-attachments/assets/a036d7e4-1e46-4b45-bd08-b7c59362f5dd" />

### Frequency of Room Type

<img width="1784" height="483" alt="image" src="https://github.com/user-attachments/assets/362a4032-fcd8-4e58-bc61-542ebc797ff5" />

### Time-based Analysis

<img width="867" height="489" alt="image" src="https://github.com/user-attachments/assets/8d6cdbf0-e483-483d-88a1-98459a2cbe7a" />

<img width="1184" height="584" alt="image" src="https://github.com/user-attachments/assets/cc03a0a4-bd28-4bf8-8b9e-5b96bd66c6a3" />

### Correlation Heatmap

<img width="880" height="784" alt="image" src="https://github.com/user-attachments/assets/9715fc94-bd7e-423a-8ee9-5a3bee7a0f58" />

### Geospatial Map of Listings & Sentiment Overlay

<img width="838" height="650" alt="image" src="https://github.com/user-attachments/assets/791e33cc-050d-41be-8ecc-09bb58c39d96" />

---

---

## ✅ Conclusion

* **Location, amenities, and property characteristics** strongly influence pricing and occupancy.
* **Sentiment analysis** reveals that positive reviews often correlate with higher occupancy and better ratings.
* **Geospatial mapping** highlights distinct clusters of high-performing Airbnb listings across Nairobi.
* Predictive models provide a solid foundation for hosts to optimize pricing strategies and improve competitiveness.
The Random Forest model demonstrates strong predictive performance, with predictions closely aligned to actual values. This validates its suitability for deployment in the Airbnb price prediction task.
---

## 👥 Collaborators

* **Maureen Auka (ENGMAUKA)**
* **Brian Kipchumba (Brian254596)**
* **Ochieng’ Ouma (Ochieng-Data)**
* **Andrew Chege (andrewc998)**


---
