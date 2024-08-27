import requests
import pandas as pd 
from bs4 import BeautifulSoup
        
def get_uk_cities(base_url):
    
    url = f'{base_url}/government/publications/list-of-cities/list-of-cities-html'
    
    # Get page information
    page = requests.get(url)
    
    # UK cities list
    data = []
    
    # Create soup
    soup = BeautifulSoup(page.text, 'html.parser')

    # Get main content
    content = soup.find('div', id='contents').find('div', class_='govspeak')

    territory_names = content.find_all('h3')
    territory_names = [territory.text.strip() for territory in territory_names]

    territories = content.find_all('h3')
    countries = content.find_all('h4')
    cities = content.find_all('ul')

    for x in range(len(countries)):
        # Get territory name
        territory = ''
        if x <= 3:
            territory = territories[0].text.strip()
        elif x == 4:
            territory = territories[1].text.strip()
        else:
            territory = territories[2].text.strip()
        
        # Get Country name
        country = countries[x].text.strip()
        
        # Get every city in country
        lis = cities[x].find_all('li')
        for li in lis:
            item = {}
            
            item['Territory'] = territory
            item['Country'] = country
            item['City'] = li.text.strip().replace('*', '')
            
            data.append(item)
    
    # Return uk cities
    return data
        
def get_boroughs(location, base_url):
    # Base URL
    url = f'{base_url}/service-search/find-an-nhs-sight-test/disambiguation?SeoFriendlyUrl=find-an-nhs-sight-test&location={location.strip()}'
    
    data = []
    
    # Get page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    boroughs = []
    
    if soup.find('ul', class_='nhsuk-list'):
        boroughs = soup.find('ul', class_='nhsuk-list').find_all('li')
    
    for borough in boroughs:
        item = {}
        
        place = borough.find('a').text.split(', ')
        
        item['County'] = place[0]
        item['Borough'] = place[1]
        item['PostalCode'] = place[2]
        item['Link'] = f'{base_url}/{borough.find('a').attrs['href']}'
        
        data.append(item)
        
    return data

def get_eye_service_centres(borough):
    # Get Eye Service Centre Page
    page = requests.get(borough['Link'])
    
    data = []
    
    # Create soup
    soup = BeautifulSoup(page.text, 'html.parser')
    
    testCentres = soup.find('ol', class_='nhsuk-list results').find_all('li')
    
    
    for x in range(len(testCentres)):
        item = {}
        
        item['County'] = borough['County']
        item['Borough'] = borough['Borough']
        
        # Get li tag
        li = testCentres[x]

        li.find('p', id=f'distance_{x}').span.decompose()
        item['Distance'] = li.find('p', id=f'distance_{x}').get_text(strip=True)
        li.find('h2', id=f'orgname_{x}').span.decompose()
        item['CentreName'] = li.find('h2', id=f'orgname_{x}').get_text(strip=True)
        li.find('p', id=f'address_{x}').span.decompose()
        item['Address'] = li.find('p', id=f'address_{x}').get_text(strip=True)
        if li.find('p', id=f'phone_{x}').span:
            li.find('p', id=f'phone_{x}').span.decompose()
        item['Phone'] = li.find('p', id=f'phone_{x}').get_text(strip=True)
        item['MapLink'] = li.find('a', id=f'map_link_{x}').attrs['href']
        
        data.append(item)
    
    # Return data
    return data

def main():
    # Proxy
    proxy = ''
    
    # UK cities base URL
    uk_gov_base_url = 'https://www.gov.uk'
    
    # UK sight test services center base URL
    nhs_base_url = 'https://www.nhs.uk'

    # Get UK cities
    uk_cities = get_uk_cities(uk_gov_base_url)
    
    # Get name of england cities
    england_cities = [city['City'] for city in uk_cities if city['Country'] == 'England']
    
    i = 0
    size = len(england_cities)
    
    while (i < size):
        # Generate records for a city
        city_name = england_cities[i]
        print(f'Generating record for {city_name}.')
        
        # # Get list of boroughs
        boroughs = get_boroughs(city_name, nhs_base_url)
        
        # # Initialize data
        data = []
            
        for borough in boroughs:
            eye_centres = get_eye_service_centres(borough)
            data.extend(eye_centres)
            
        df = pd.DataFrame(data)
        df.to_csv(f'{city_name.lower()}.csv')
        i += 1
    
main()