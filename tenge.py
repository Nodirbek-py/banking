
from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://www.tengebank.uz/ru/exchange-rates"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.findAll(class_="currency__value up")[0].text
eur = soup.findAll(class_="currency__value up")[1].text
rub = soup.findAll(class_="currency__value up")[6].text
data = {
    'title': 'Tenge Bank',
    'usd': usd,
    'euro': eur,
    'rub': rub
} 
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')