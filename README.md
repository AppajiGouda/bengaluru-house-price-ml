# 🏠 House Price Prediction System (Bengaluru)

## 📌 Overview

This project builds an end-to-end machine learning pipeline to predict house prices in Bengaluru using multiple regression models and ensemble techniques.

---

## 🚀 Features

* Data cleaning and preprocessing
* Feature engineering (BHK extraction, sqft conversion)
* Outlier detection and removal
* Model comparison:

  * Linear Regression
  * Decision Tree
  * Random Forest
  * KNN
  * Neural Network
* Stacking Ensemble Model
* Evaluation using MAE, RMSE, R²

---

## 📊 Dataset

* Bengaluru House Price Dataset (Kaggle)
* Features include location, sqft, BHK, bathrooms, etc.

---

## ⚙️ Models & Results

| Model             | MAE   | RMSE  | R²    |
| ----------------- | ----- | ----- | ----- |
| Linear Regression | ~19.5 | ~34.8 | ~0.84 |
| Random Forest     | ~22.5 | ~47.8 | ~0.69 |
| KNN               | ~23.6 | ~49.8 | ~0.67 |
| Stacking          | ~20.5 | ~45.3 | ~0.73 |

---

## 🧠 Key Learnings

* Importance of data cleaning and feature engineering
* Handling data leakage (price_per_sqft issue)
* Model comparison and evaluation
* Ensemble learning improves performance
* Limitations of models on tabular data

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📌 Future Improvements

* Hyperparameter tuning (GridSearch/Optuna)
* Feature importance visualization
* Deployment using Streamlit/Flask
* Integration of external data (geo/location insights)

---
