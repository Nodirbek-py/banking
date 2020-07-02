from bs4 import BeautifulSoup as bs4
import requests
import json
url = "http://www.trustbank.uz/oz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
currencies = soup.find(class_="row five-cols")
money = currencies.findAll(class_="item")
usd = money[15].text
eur = money[16].text
rub = money[18].text
data = {
    'title': 'Trust Bank',
    'usd': usd,
    'euro': eur,
    'rub': rub
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')
