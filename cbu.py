from bs4 import BeautifulSoup as bs4
import requests
import json
url = "http://www.cbu.uz/oz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
currencies = soup.findAll(class_="exchange__item_value")
usd = currencies[0].text.replace("USD = ", "")
eur = currencies[1].text.replace("EUR = ", "")
rub = currencies[2].text.replace("RUB = ", "")
data = {
    'title': 'Central Bank of Uzbekistan, CBU',
    'usd': usd,
    'euro': eur,
    'rub': rub
} 
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')
    