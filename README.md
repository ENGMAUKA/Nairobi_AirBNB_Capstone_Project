# Nairobi_AirBNB_Capstone_Project

---

## 📑 Table of Contents

1. [Introduction](#introduction)
2. [Business Understanding](#business-understanding)
3. [Data Understanding](#data-understanding)
4. [Modeling](#modeling)
5. [Visualization](#visualization)
6. [Recommendations](#reommendations)
7. [Conclusion](#conclusion)
8. [Collaborators](#collaborators)

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

The following models were adopted for both **price** and **occupancy** predictions:

* Linear Regression Baseline Model
* Random Forest
* XGBoost Baseline
* XGBoost Hyperparameter Tuning

Evaluation metrics:

* **RMSE (Root Mean Squared Error)**
* **MAE (Mean Absolute Error)**
* **R² Score**

---

## 📈 Visualization

### Price Distribution of Listings:

<img width="1384" height="484" alt="image" src="https://github.com/user-attachments/assets/a036d7e4-1e46-4b45-bd08-b7c59362f5dd" />

### Frequencies:

<img width="1784" height="483" alt="image" src="https://github.com/user-attachments/assets/362a4032-fcd8-4e58-bc61-542ebc797ff5" />

### Time-based Analysis:

<img width="867" height="489" alt="image" src="https://github.com/user-attachments/assets/8d6cdbf0-e483-483d-88a1-98459a2cbe7a" />

<img width="872" height="489" alt="image" src="https://github.com/user-attachments/assets/0524e8af-0f70-4d1e-b9a1-7545a2dfbd9c" />

<img width="1184" height="584" alt="image" src="https://github.com/user-attachments/assets/cc03a0a4-bd28-4bf8-8b9e-5b96bd66c6a3" />

### Correlation Heatmap:

<img width="880" height="784" alt="image" src="https://github.com/user-attachments/assets/9715fc94-bd7e-423a-8ee9-5a3bee7a0f58" />

### Geospatial Map of Listings & Sentiment Overlay:

<img width="838" height="650" alt="image" src="https://github.com/user-attachments/assets/791e33cc-050d-41be-8ecc-09bb58c39d96" />

### Pricing Determinants:
<img width="1065" height="529" alt="image" src="https://github.com/user-attachments/assets/b5bf0e25-7263-42f3-86bd-34a41d436c33" />
**Top key determinants of pricing in Airbnb listings in Nairobi:**
* Location
* Photos count
* Guests
* Listing type
* Number of reviews
* Beds per bedroom

### Occupancy Determinants:
<img width="984" height="584" alt="image" src="https://github.com/user-attachments/assets/48a61e59-f642-4bfd-8f90-60bc2a4cc3e3" />
**Top key determinants of occupancy in Airbnb listings in Nairobi:**
* Length of stay
* Available days
* Booking lead time
* Rate

---
## Recommendations

* Investors and hosts should invest more on entire homes as the bar chart on Average Revenue by Room Type shows entire homes generate the most revenue (64.3%), followed by private rooms (22.8%), with hotel rooms earning the least (12.8%).
* Investors and hosts should focus on high-demand central zones for consistent bookings, while premium pricing strategies can succeed in select outlying neighborhoods.
* Investors should target locations where listings are highly concentrated in central Nairobi areas such as Westlands, Kilimani, and Kileleshwa, which combine high revenues with strong occupancy rates
* Hosts to eye on the weekends for boosted revenues since the trend from the EDA shows that occupancy is generally lower on weekdays, with a peak on Saturday. Thursday shows particularly low occupancy, likely because most bookings occur over the weekend.

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
