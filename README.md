# US Automotive Market Insights

## Overview
US Automotive Market Insights aims to gather and analyze car pricing data across the United States to uncover trends and identify good values. The project focuses on collecting data from the top 10 car manufacturers in the US, covering car listings from 2010 to 2024. By scraping data from Cars.com, the project compiles a comprehensive dataset of used car listings from across the United States.

## Project Structure
The repository is organized into the following directories:

- `web-scraper/`: Contains the web scraper code and related documentation.
- `data-analysis/`: Contains the exploratory data analysis (EDA) and modeling notebooks.
  - `eda/`: Exploratory Data Analysis.
  - `price-predictor/`: Contains the price prediction system, including data cleaning, model comparison, optimization, and final model.
  - `price-recommender-gui/`: Contains the GUI for price recommendations.
  - `depreciation-analysis/`: Contains the analysis of car depreciation from 2010 to 2024, including different makes and types (gas, EV).
- `data/`: Contains sample raw and processed data used in the analyses.


## Motivation
As a car enthusiast, I embarked on a nationwide search to find my dream car. This project helps identify the best regions to buy cars by analyzing pricing data from various car selling websites.

### Web Scraper
Navigate to the `web-scraper/` directory and follow the instructions in the README.md to set up and run the web scraper.

### Data Analysis 
Navigate to the `data-analysis/` directory and explore the notebooks in the `EDA/`, `price-predictor/`, and `depreciation-analysis/` directories to see the analysis and insights derived from the collected data.

### Price Predictor
The `price-predictor/` directory contains the price prediction system. This includes:
- `data_cleaning.py`: Scripts for cleaning the data.
- `model_comparison.ipynb`: Notebook comparing six different machine learning models.
- `model_optimization.ipynb`: Notebook for optimizing the top two models.
- `final_model.py`: The final chosen model (XGBoost) for predictions.

### Price Recommender GUI
The `price-recommender-gui/` directory contains the GUI that uses the prediction models to recommend a price to be paid based on the entered details.

## Conclusion
This project demonstrates the complete workflow of a data science and machine learning project, from data collection and exploration to model building, optimization, and deployment through a user-friendly interface.
