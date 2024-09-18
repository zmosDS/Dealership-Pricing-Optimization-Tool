# Vehicle Value Estimator Dashboard

## Overview

This dashboard is a vehicle value estimator that helps users estimate the price of a car based on several input features. It uses a machine learning model to predict the estimated value of the vehicle and provides visual insights into how the prediction was made.

### Features of the Dashboard:
- **Make, Model, Trim Selection**: Users can input the car's make, model, and trim.
- **Body Style, Mileage, and Year**: Additional inputs include body style, mileage, year, and state.
- **Price Distribution**: A visual plot that shows the distribution of prices for similar vehicles in the dataset.
- **Feature Importance**: A bar chart visualizing the importance of different features in determining the predicted value of the vehicle.

## Screenshot

![Dashboard Screenshot](./Users/z/Desktop/Screenshot 2024-09-18 at 3.00.37 AM.png)

## File Contents

### 1. `estimated_value_dashboard.py`
This Python script contains the code to build the dashboard using the **Dash** framework. The script loads the trained machine learning model and renders the following components:
- Input fields for users to select features like **make**, **model**, **trim**, **year**, **mileage**, **body style**, and **state**.
- A real-time calculation of the **estimated vehicle value** based on user inputs.
- A plot showing the **price distribution** for similar vehicles.
- A bar chart indicating **feature importance** in the prediction.

### 2. `README.md`
This file provides an overview of the dashboard and its functionality, explaining how users can interact with it and what insights are provided.

## Instructions

### Running the Dashboard:
1. Ensure that all required Python libraries are installed, including:
   - `dash`
   - `plotly`
   - `pandas`
   - `joblib` (for loading the trained machine learning model)
   
   You can install the dependencies using:
   ```bash
   pip install dash plotly pandas joblib
   
2. Run the dashboard by executing the `estimated_value_dashboard.py` script:
   ```bash
   python estimated_value_dashboard.py

3. The dashboard will be available at `http://127.0.0.1:8050/` in your browser.

### Usage:
- **Select Car Features**: Input the vehicle’s **make**, **model**, **trim**, **body style**, **mileage**, **year**, and **state**.
- **View Estimated Value**: The dashboard will output the **estimated value** of the vehicle in real-time.
- **Price Distribution**: Review the distribution of prices for similar vehicles based on the selected inputs.
- **Feature Importance**: The feature importance chart helps users understand how each feature contributes to the predicted vehicle value.

## Example

Here’s an example scenario:
- **Make**: Chevrolet
- **Model**: Malibu
- **Trim**: 1LT
- **Body Style**: Sedan
- **Mileage**: 25,000
- **Year**: 2019
- **State**: CA

Estimated value: **$27,770.01**

The dashboard will also display:
- A **price distribution** plot showing the prices of similar vehicles.
- A **feature importance** chart, demonstrating how different features, like **model** and **mileage**, influenced the estimated value.

## Notes
- The model was trained using data from **cars.com**, cleaned, and processed for vehicle price prediction.
- The dashboard allows for real-time price estimation based on user inputs.
