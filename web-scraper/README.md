# Cars.com Web Scraper for US Automotive Market Insights

## Goal
The goal of this project is to build a web scraper to gather data on used cars from the top 10 car manufacturers in the US, covering car listings from 2010 to 2024.

## Summary of Results
Each scrape of the top 10 car manufacturers (10 scrapes total, one for each manufacturer) resulted in approximately 8,200-8,700 rows, and each scrape took less than 5 minutes to complete.

### CSV file from Chevrolet Scrape (8,523 rows)
<img width="746" alt="Screenshot 2024-08-02 at 3 14 37 PM" src="https://github.com/user-attachments/assets/869c1bc7-598f-45b5-b998-9314a50881c2">

### Final CSV file after combining all 10 Top Car Manufacturers (84,676 rows)
<img width="749" alt="Screenshot 2024-08-02 at 3 18 25 PM" src="https://github.com/user-attachments/assets/fc7a0f3d-1213-439e-90ed-7219b878f63c">

- `july-21st-raw-data.csv`

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
- Specify make (e.g., Chevrolet)
- Nationwide search
- No mileage limit
- No monthly payment filter
- 100 listings per page
- Sorted by Newest listed
- Used cars only
- Year range: 2010-2024
- ZIP code: 00000 (avoid location bias)

#### Determine Listing Details to Scrape
The data points extracted include:
- `Listing ID`: Unique identifier for each listing
- `Trim`: Trim level of the car
- `Make`: Car manufacturer
- `Year`: Model year of the car
- `Model`: Car model
- `Price`: Listed price of the car
- `Body Style`: Body style of the car (e.g., sedan, SUV)
- `City`: City where the car is located
- `State`: State where the car is located
- `Mileage`: Mileage of the car
- `Stock Type`: Type of stock (e.g., used)

## Conclusion
#### The final dataset, which includes over 84,000 rows of used car listings from the top 10 car brands, is comprehensive and ready for further analysis.
