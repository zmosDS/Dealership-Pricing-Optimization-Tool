# Data

## Overview
This directory contains all the data related to the Cars.com web scraper project. It includes both raw and processed data files.

## File Structure
The directory is organized as follows:

- `raw_data.csv`: This file contains the raw data collected directly from the Cars.com web scraper.
- `processed_data.csv`: This file contains the cleaned and processed data, ready for analysis.

## Description

### raw_data.csv
This file includes the raw, unprocessed data scraped from Cars.com. It contains all the listings collected from the top 10 car manufacturers in the US for the years 2010-2024.

### processed_data.csv
This file contains the processed data, which has been cleaned and prepared for analysis. The processing steps may include:
- Removing duplicates
- Filling missing values
- Correcting data formats
- Filtering irrelevant data

#### Columns:
- `listing_id`: Unique identifier for each listing
- `trim`: Trim level of the car
- `make`: Car manufacturer
- `year`: Model year of the car
- `model`: Car model
- `price`: Listed price of the car
- `body_style`: Body style of the car (e.g., sedan, SUV)
- `city`: City where the car is located
- `state`: State where the car is located
- `mileage`: Mileage of the car
- `stock_type`: Type of stock (e.g., used)
