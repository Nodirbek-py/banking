from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://www.aab.uz/uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
currencies = soup.find(class_="col-xs-3")
money = currencies.findAll(class_="item")
usd = money[1].text
eur = money[2].text
rub = money[3].text
data = {
    'title': 'Asia Alliance Bank',
    'usd': usd,
    'euro': eur,
    'rub': rub
}
with open('data.json', 'a', encoding='utf-8') as file:
    file.write('[')
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')