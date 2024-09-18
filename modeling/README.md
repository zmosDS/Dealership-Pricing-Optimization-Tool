# Modeling Section Overview

This section contains the machine learning modeling process for predicting vehicle prices, including comparisons, evaluations, and optimizations of various models. The following notebooks document each step, from the initial legacy model to the final optimized model ready for deployment.

## Contents

1. `legacy_model.ipynb` - **Legacy Model**
2. `model_comparison.ipynb` - **Model Comparison**
3. `model_optimization.ipynb` - **Model Optimization**
4. `model_evaluation.ipynb` - **Model Evaluation**
5. `model_validation.ipynb` - **Model Validation**
6. `final_model.py` - **Final Model for Deployment**

---

## 1. `legacy_model.ipynb` - Legacy Model

This notebook presents the **legacy model**, which used **XGBoost** with one-hot encoding for handling categorical features. Initially, this model was the primary solution for vehicle price prediction but required manual encoding of categorical variables, resulting in a large number of features (around 3,000).

### Key Details:
- **XGBoost** with **one-hot encoding**.
- Highlighted the challenges with encoding categorical features.
- The model performed adequately but lacked efficiency and generalization compared to newer models.

---

## 2. `model_comparison.ipynb` - Model Comparison

This notebook compares several machine learning models for vehicle price prediction, including:
- **Random Forest**
- **XGBoost**
- **CatBoost**
- **LightGBM**

The primary objective was to identify the top-performing model based on error metrics and computational efficiency.

### Key Findings:
- **LightGBM** outperformed other models, with the best balance of accuracy and speed.
- **CatBoost** also performed well but was slightly less efficient.
- **XGBoost** required manual encoding and did not perform as efficiently as the categorical-specific models.

---

## 3. `model_optimization.ipynb` - Model Optimization

This notebook documents the process of optimizing the **LightGBM** model. Hyperparameter tuning was conducted using **RandomizedSearchCV** to further reduce error metrics like **Mean Absolute Error (MAE)** and **Mean Squared Error (MSE)**.

### Key Findings:
- **Optimized LightGBM Model:**
  - Final MAE: `$1,609.03`
  - Final MSE: `7,441,905`
  - R² Score: `0.9573`
- Optimization improved the model’s performance, reducing error metrics and improving predictive accuracy compared to the legacy XGBoost model.

---

## 4. `model_evaluation.ipynb` - Model Evaluation

This notebook evaluates the optimized **LightGBM** model using cross-validation techniques to assess its generalization and identify any signs of overfitting.

### Key Findings:
- **Stratified K-Fold Cross-Validation** helped address variability across price ranges, leading to more consistent results.
- **Final Cross-Validation Performance:**
  - MAE: `$1,662.70`
  - MSE: `6,506,722`
  - R² Score: `0.9625`

---

## 5. `model_validation.ipynb` - Model Validation

This notebook validates the **LightGBM** model on new data collected nearly a month after the original training data. The goal was to assess the model’s ability to predict car prices accurately amidst market fluctuations.

### Key Findings:
- **Validation on New Data (August 16th):**
  - MAE: `$1,805.08` (Slight increase from the original model)
  - MSE: `8,084,573`
  - R² Score: `0.9527`
- Despite slight variations, the model maintained robust predictive accuracy across the new dataset.

---

## 6. `final_model.py` - Final Model for Deployment

This script contains the finalized **LightGBM** model after all optimization and validation processes. The model is ready for deployment and can be used to predict vehicle prices based on the features provided.

---

### Notes

- Each notebook documents the entire machine learning workflow from initial comparisons to final validation.
- **LightGBM** is the final selected model based on its performance and efficiency, and it is deployed in the `final_model.py` script.

---
