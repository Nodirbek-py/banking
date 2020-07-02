from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://www.aloqabank.uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
tables = soup.find(id = "slider-inner")
currencies = tables.findAll("td")
usd = currencies[1].text
eur = currencies[4].text
data = {
    'title': 'Aloqa Bank',
    'usd': usd,
    'euro': eur
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')