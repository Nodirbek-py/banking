from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://nbu.uz/en/exchange-rates/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
table = soup.find('table')
rows = table.findAll('tr')
usd = rows[1].findAll('td')[2].text
eur = rows[2].findAll('td')[2].text
rub = rows[3].findAll('td')[2].text
data = {
    'title': 'National Bank of Uzbekistan, NBU',
    'usd': usd,
    'euro': eur,
    'rub': rub
} 
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')