from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://kapitalbank.uz/uz/welcome.php"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.findAll(class_ = "item item-usd")
eur = soup.findAll(class_="item item-eur")
rub = soup.findAll(class_="item item-rub")
data = {
    'title': 'Kapital Bank',
    'usd': usd[0].find(class_="item-value").text,
    'euro': eur[0].find(class_="item-value").text,
    'rub': rub[0].find(class_="item-value").text
}    
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)