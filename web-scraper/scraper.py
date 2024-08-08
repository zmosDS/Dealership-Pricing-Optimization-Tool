import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
from urllib.parse import parse_qs, urlparse

def scrape_pages(scrape_all_pages=False, max_pages=100):
    """
    Scrapes vehicle listings from the cars.com website and returns a DataFrame.

    Args:
        scrape_all_pages (bool): Whether to scrape all available pages or stop after a certain number.
        max_pages (int): Maximum number of pages to scrape if not scraping all pages.

    Returns:
        pd.DataFrame: DataFrame containing vehicle listings with columns:
                      ['Listing ID', 'Trim', 'Make', 'Year', 'Model', 'Price', 
                       'Body Style', 'City', 'State', 'Mileage', 'Stock Type']
    """
    url_template = "https://www.cars.com/shopping/results/?page={}&page_size=100&sort=listed_at_desc&stock_type=used&makes[]=chevrolet&year_max=2024&year_min=2010&zip=00000"
    headers = {'User-Agent': 'Safari/537.3'}
    df_columns = ['Listing ID', 'Trim', 'Make', 'Year', 'Model', 'Price', 'Body Style', 'City', 'State', 'Mileage', 'Stock Type']
    
    start_time = time.time()
    page_number = 1
    listings_collected = set()
    rows_list = []

    while True:
        url = url_template.format(page_number)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        vehicle_cards = soup.find_all('div', class_='vehicle-card')

        # Break if no more vehicle cards or max pages reached
        if not vehicle_cards or (not scrape_all_pages and page_number >= max_pages):
            break

        for card in vehicle_cards:
            button_element = card.find('button', {'data-qa': 'vehicle-badging'})
            if button_element and 'data-contents' in button_element.attrs:
                data_contents = button_element['data-contents']
                data_dict = json.loads(data_contents)
                href_data = data_dict.get('href_to_vdp', {}).get('href_to_vdp', '')

                query_params = parse_qs(urlparse(href_data).query)
                listing_id = query_params.get('listing_id', [None])[0]
                trim = query_params.get('trim', [None])[0]
                make = query_params.get('make', [None])[0]
                model_year = query_params.get('model_year', [None])[0]
                model = query_params.get('model', [None])[0]
                price = query_params.get('price', [None])[0]
                bodystyle = query_params.get('bodystyle', [None])[0]
                stock_type = query_params.get('stock_type', [None])[0]

                # Avoid duplicates
                if listing_id in listings_collected:
                    continue
                listings_collected.add(listing_id)

                # Extract city and state information
                city_state_text = card.select_one('div[data-qa="miles-from-user"]')
                city, state = (None, None)
                if city_state_text:
                    location_parts = city_state_text.get_text(strip=True).split(',')
                    if len(location_parts) >= 2:
                        city = location_parts[0].strip()
                        state = location_parts[1].split(' ')[1].strip()

                # Extract mileage information
                mileage_text = card.find('div', {'data-qa': 'mileage'})
                mileage = None
                if mileage_text:
                    mileage = mileage_text.get_text(strip=True).replace(' mi.', '').replace(',', '')

                # Add extracted data from rows list
                rows_list.append({
                    'Listing ID': listing_id,
                    'Trim': trim,
                    'Make': make,
                    'Year': model_year,
                    'Model': model,
                    'Price': price,
                    'Body Style': bodystyle,
                    'City': city,
                    'State': state,
                    'Mileage': mileage,
                    'Stock Type': stock_type
                })

        page_number += 1
        time.sleep(0.5)

    df = pd.DataFrame(rows_list, columns=df_columns)
    end_time = time.time()
    print(f"Scraping completed in {end_time - start_time:.2f} seconds.")
    return df

if __name__ == "__main__":
    df_100_pages = scrape_pages()
    df_100_pages.to_csv('Chevrolet_Scrape.csv', index=False)
    print('Chevrolet 100 page scrape completed.')
