from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://www.ipotekabank.uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
currencies = (soup.find(class_="purchase"))
money = currencies.findAll("span")
usd = money[0].text
eur = money[1].text
data = {
    'title': 'Ipoteka Bank',
    'usd': usd,
    'euro': eur
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')