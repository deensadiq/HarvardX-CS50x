import requests
import pandas as pd
from bs4 import BeautifulSoup

base_url = "https://www.politico.com/"
proxy = ""

# Get web page
page = requests.get(base_url)

# print(page.text)
location = 'Preston'
print(type(location) == int)

# Create soup
# soup = BeautifulSoup(page.text, "html")

# print(soup.text)