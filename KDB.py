from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://kdb.uz/uz/interactive-services/exchange-rates"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
table = soup.find(class_ = "d-none d-lg-block")
currencies = table.findAll("td")
usd = currencies[0].text.replace(" / 10220", "")
usd = usd.replace(" ", "")
eur = currencies[1].text.replace(" / 11800", "")
eur = eur.replace(" ", "")
data = {
    'title': 'KDB',
    'usd': usd,
    'euro': eur
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')