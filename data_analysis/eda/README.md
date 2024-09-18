# Exploratory Data Analysis (EDA)

## Objective
The goal of this notebook is to perform an Exploratory Data Analysis (EDA) on a dataset of vehicle listings to identify key patterns, relationships, and outliers that will aid in the development of a predictive model for vehicle prices.

## Summary
This notebook contains the following steps:
- **Data Loading:** A cleaned dataset with 82,895 vehicle listings was loaded for analysis.
- **Descriptive Statistics:** Summary statistics and feature counts were generated to get a comprehensive understanding of the dataset.
- **Visualizations:** Various plots (histograms, boxplots, and heatmaps) were created to visualize distributions and relationships between key features such as `Price`, `Mileage`, `Year`, `Make`, and `Body Style`.
- **Outlier Detection:** Outliers in `Price` and `Mileage` were detected using both Interquartile Range (IQR) and Z-score methods.
- **Depreciation Analysis:** A linear regression model was used to estimate vehicle depreciation rates by car make.

## Key Steps
1. **Data Inspection:**
   - Loaded the dataset and checked data types and structure.
   - Dropped irrelevant columns such as `Listing ID` and `Stock Type`.

2. **Descriptive Statistics:**
   - Counted values for categorical features (`Make`, `Body Style`, `State`).
   - Computed summary statistics for numerical features (`Year`, `Price`, `Mileage`).

3. **Visualizations:**
   - **Histograms** to display distributions of `Price`, `Mileage`, and `Year`.
   - **Boxplots** to compare price distributions across `Make`, `Body Style`, and `Model`.
   - **Heatmaps** to show the distribution of `Make` across different `Body Styles`.

4. **Depreciation Rates by Make:**
   - Used linear regression to calculate the depreciation rate for each car make.

5. **Outlier Detection:**
   - Detected outliers in `Price` and `Mileage` using IQR and Z-score methods.

## Conclusion
The EDA provided a comprehensive understanding of the dataset, including key relationships between features, the identification of outliers, and the calculation of depreciation rates for different vehicle makes. These insights will guide feature engineering and model development in subsequent steps.
