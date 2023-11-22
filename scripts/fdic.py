import csv

from bs4 import BeautifulSoup
import requests



url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

response = requests.get(url)

response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

