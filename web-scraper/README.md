# Cars.com Web Scraper for US Automotive Market Insights

## Goal
The goal of this project is to build a web scraper to gather data on used cars from the top 10 car manufacturers in the US, covering car listings from 2010 to 2024.

## Implementation

### Step 1: Identify Target Cars/Listings
To manage the data volume, I focused on the top 10 car manufacturers in the US for 2023, identified using [Statista](https://www.statista.com/statistics/264362/leading-car-brands-in-the-us-based-on-vehicle-sales/).
https://www.carpro.com/blog/national-auto-sales-numbers-for-all-automakers-in-2023

### Step 2: Build the Web Scraper with BeautifulSoup
The web scraper was built using BeautifulSoup to parse the HTML and extract the required details. Each car make had its dedicated scraper script, modifying the URL to filter by make, page size, stock type, etc.

#### URL Filtering Criteria
- Clean title only
- All dealers
- No keyword filter
- No price range limits
- Specified make (e.g., Chevrolet)
- Nationwide search
- No mileage limit
- No monthly payment filter
- 100 listings per page
- Sorted by best match
- Used cars only
- Year range: 2010-2024
- Specific ZIP code

#### Determine Listing Details to Scrape
The data points extracted include:
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
<img width="500" alt="Screenshot 2024-07-05 at 4 47 39 PM" src="https://github.com/user-attachments/assets/6edf19c3-a803-4d33-975a-fbe68562122e">

## Results
Each scrape of the top 10 car manufacturers (10 scrapes total, one for each manufacturer) resulted in approximately 9,200-9,500 rows, and each scrape took about 60 minutes to complete.

### CSV file from Chevrolet Scrape (9,333 rows)
<img width="743" alt="Screenshot 2024-07-20 at 11 45 06 PM" src="https://github.com/user-attachments/assets/aecc890b-01a9-4d7f-86b3-d5e5d8a1299d">

### Final CSV file after combining all 10 Top Car Manufacturers
<img width="752" alt="Screenshot 2024-07-20 at 11 53 35 PM" src="https://github.com/user-attachments/assets/903bca73-b586-4575-b82c-649d0b930643">

#### The final dataset, which includes over 97,000 rows of used car listings from the top 10 car brands, is comprehensive and ready for further analysis.
