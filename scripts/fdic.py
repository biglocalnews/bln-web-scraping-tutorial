import csv

from bs4 import BeautifulSoup
import requests



url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

response = requests.get(url)

response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

results = []
fieldnames = []

table = soup.find('table')

thead = table.find('thead')

for th in thead.find_all('th'):
    fieldnames.append(th.p.span.text)

fieldnames.append('url')

results.append(fieldnames)

tbody = table.find('tbody')

trs = tbody.find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    values = []
    for td in tds:
        values.append(td.text)

    bank_link = tr.find('a')
    href = bank_link['href']
    bank_url = 'https://www.fdic.gov/' + href
    values.append(bank_url)

    results.append(values)

with open('./data/raw/fdic_failed_banks.csv', 'w') as outfile:
    output = csv.writer(outfile)
    output.writerows(results)
