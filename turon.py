from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://turonbank.uz/oz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
table = soup.findAll("tr")
usd = table[1].findAll('td')[0]
eur = table[1].findAll('td')[1]
rub  = table[1].findAll('td')[4]
data = {
    'title': 'Turon Bank',
    'usd': usd.text,
    'euro': eur.text,
    'rub': rub.text
}  
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)