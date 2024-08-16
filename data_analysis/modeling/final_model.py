# Import necessary libraries
import pandas as pd
import numpy as np
from pathlib import Path
from sklearnex import patch_sklearn
patch_sklearn()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
car_data_df = pd.read_csv(data_path / 'car_data_cleaned.csv')

# Drop irrelevant columns
car_data_df.drop(columns=['Listing ID', 'Stock Type'], inplace=True)

# Define features and target
features = ['Year', 'Model', 'State', 'Mileage', 'Trim', 'Make', 'Body Style']
X = pd.get_dummies(car_data_df[features], drop_first=False)
y = car_data_df['Price'].values.reshape(-1, 1)

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=1)

# Print dataset information
print('Data imported & processed\n')
print('Train & Test Set Rows, Columns:', X_train.shape, X_test.shape)

# Define best hyperparameters
best_hyperparameters = {
    'subsample': 0.8, 
    'reg_lambda': 10, 
    'reg_alpha': 0.0001, 
    'n_estimators': 1000, 
    'min_child_weight': 2, 
    'max_depth': 5, 
    'learning_rate': 0.35, 
    'gamma': 0.075, 
    'colsample_bytree': 0.95
}

# Train model
XGBoost_model = xgb.XGBRegressor(**best_hyperparameters)
XGBoost_model.fit(X_train, y_train.ravel())

# Predictions on the test set
pred_XGBoost = XGBoost_model.predict(X_test)

# Print model performance metrics
print("\nOptimized XGBoost Model Performance:")
print("Mean Absolute Error (MAE): ", mean_absolute_error(y_test, pred_XGBoost))
print("Mean Squared Error  (MSE): ", mean_squared_error(y_test, pred_XGBoost))
print("R2 Score             (R2): ", r2_score(y_test, pred_XGBoost))