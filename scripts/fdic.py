import csv

from bs4 import BeautifulSoup
import requests



url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'

response = requests.get(url)

# This is useful, but we might want to circle back and add this at the end
# in order to keep the initial coding simple.
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

fieldnames = []
results = []

table = soup.find('table')

table_head = table.find('thead')


"""
# This is surgical but I worry a bit advanced.

spans = table_head.find_all('span', {'class': 'dtfullname'})

fieldnames = []

for span in spans:
    fieldnames.append(span.text)

"""
# How about we start with the below strategy of drilling
# down into each subsequent layer of the header cells?
# That'll help emphasize the tree-like/nested structure of HTML.
# Then at the end, we could circle back and demo the more advanced technique
# that uses class selector.
for th in table_head.find_all('th'):
    fieldnames.append(th.p.span.text)

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
