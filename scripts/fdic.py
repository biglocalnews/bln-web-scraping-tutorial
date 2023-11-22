import csv

from bs4 import BeautifulSoup
import requests



url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

response = requests.get(url)

response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

results = []

table = soup.find('table')

table_head = table.find('thead')
spans = table_head.find_all('span', {'class': 'dtfullname'})

fieldnames = []

for span in spans:
    fieldnames.append(span.text)

fieldnames.append('url')

results.append(fieldnames)

table_body = table.find('tbody')

rows = table_body.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    values = []
    for cell in cells:
        values.append(cell.text)

    bank_link = row.find('a')
    href = bank_link['href']
    bank_url = 'https://www.fdic.gov/' + href
    values.append(bank_url)

    results.append(values)


# TODO: write out results to csv file
