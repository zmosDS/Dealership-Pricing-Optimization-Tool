# Data Folder Overview

This folder contains the raw and cleaned datasets used in the vehicle price prediction project, as well as the notebook for data cleaning and preprocessing.

## Contents

1. `raw_data_july_21st.csv`  
   This file contains the original raw data collected from cars.com on July 21st. The data has not been processed or cleaned.

2. `raw_data_aug_16th.csv`  
   This file contains the raw data collected from cars.com on August 16th. The data has not been processed or cleaned.

3. `cleaned_data_july_21st.csv`  
   This is the cleaned and preprocessed version of the July 21st dataset, ready for modeling. It includes steps such as removing missing values, handling categorical features, and fixing inconsistencies.

4. `cleaned_data_aug_16th.csv`  
   This file contains the cleaned and preprocessed version of the August 16th dataset. Similar cleaning steps were applied as to the July dataset.

5. `data_cleaning.ipynb`  
   This notebook documents the full data cleaning and preprocessing pipeline applied to both the July 21st and August 16th datasets. The steps include handling missing values, converting categorical variables, feature scaling, and other data preparation tasks.

## Notes

- The **raw data** files should not be used directly for model training without first being cleaned.
- The **cleaned data** files are the final datasets used for training, validation, and testing of machine learning models.
- The **data_cleaning.ipynb** notebook provides the details of how the raw data was cleaned and transformed into the cleaned datasets.
