# Vehicle Value Estimator

## Overview

This project demonstrates the application of data science techniques to build a **Vehicle Value Estimator**. The tool predicts car prices based on various input features, including make, model, year, mileage, and trim, providing an accurate estimate to assist users in making data-driven decisions about vehicle pricing.

The project showcases a full end-to-end data science pipeline, from data collection and exploration to model development, tuning, and deployment. The final output is a user-friendly dashboard where users can input vehicle details to receive an estimated price, along with visual insights into how different factors influence vehicle value.

### Problem Statement
Pricing vehicles accurately is a common challenge. Underpricing leads to lost revenue, while overpricing can result in slow inventory turnover. This project provides a data-driven solution that predicts vehicle prices with a high degree of accuracy, enabling individuals or businesses to optimize their vehicle pricing strategies.

### Target Audience
This tool can be utilized by:
- **Car dealerships** seeking to optimize pricing strategies.
- **Private sellers** wanting to price their vehicles competitively.
- **Buyers** interested in estimating the value of a car based on specific features.

## Project Highlights

### 1. Data Collection and Preprocessing
- **Data Source**: Vehicle listings scraped from **cars.com**.
- **Preprocessing**: Data was cleaned to handle missing values, outliers, and categorical features. Features like **make**, **model**, **trim**, **mileage**, **year**, and **body style** were extracted and used for predictions.

### 2. Exploratory Data Analysis (EDA)
- **Goal**: Understand how various features (e.g., mileage, year) affect vehicle prices.
- **Key Insights**: Visualizations were created to show trends, such as how prices decline with higher mileage or older years.
  
### 3. Model Development
- **Initial Model**: The project started with **XGBoost** using manually encoded categorical features.
- **Final Model**: The final model was developed using **LightGBM**, which achieved the best performance, natively handling categorical features.
- **Performance**:
  - Mean Absolute Error (MAE): **~$1,600**
  - R² Score: **~0.96**
  
### 4. Dashboard Development
- **Framework**: The dashboard was built using **Dash**.
- **Features**: 
  - Users input vehicle details such as **make**, **model**, **trim**, **mileage**, **year**, and **body style**.
  - The dashboard outputs an **estimated price** and provides visualizations showing price distributions for similar vehicles and feature importance in the prediction.
  
### 5. Business Impact
- **Optimized Pricing**: Users can accurately price their vehicles, balancing profitability and competitiveness.
- **Actionable Insights**: Visualizations help users understand how various factors (e.g., mileage, trim) affect the value.
  
## Project Structure

- **`data/`**: Contains raw and cleaned datasets used for training and validation.
- **`data_collection/`**: Python scripts used for web scraping from cars.com.
- **`modeling/`**: Jupyter notebooks documenting model comparison, optimization, evaluation, and validation processes.
- **`vehicle_value_estimator_dashboard/`**: Code for the deployment-ready dashboard.

## Key Technologies

- **Data Scraping**: `requests`, `BeautifulSoup`
- **Data Processing and EDA**: `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Machine Learning**: `LightGBM`, `XGBoost`, `scikit-learn`
- **Dashboard**: `Dash`, `Plotly`
  
## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/vehicle-value-estimator.git```

### 2. Install dependencies
```bash
pip install -r requirements.txt```

### 3. Run the dashboard
```bash
python vehicle_value_estimator_dashboard/estimated_value_dashboard.py```

The dashboard will be available locally at `http://127.0.0.1:8050/` in your browser.

## Results and Conclusion

The **Vehicle Value Estimator** successfully predicts car prices with an impressive MAE of approximately $1,600. The LightGBM model's high performance, coupled with its ability to handle categorical data, ensures that the predictions are accurate and robust across a variety of vehicle types. The dashboard provides an intuitive interface, making the tool accessible even to non-technical users.

By building this project, I have demonstrated my ability to:
- Collect and preprocess data.
- Explore and analyze the relationships within the dataset.
- Build, tune, and evaluate machine learning models.
- Deploy a user-friendly tool that offers actionable insights.

This project showcases my end-to-end data science skills, from data acquisition to deployment, and is a valuable tool for optimizing vehicle pricing strategies.
