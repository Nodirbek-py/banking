from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://poytaxtbank.uz/oz"
request = requests.get(url, verify=False).text
soup = bs4(request, 'html.parser')
usd = soup.findAll('td')[22].text.replace("UZS\xa0", "")
eur = soup.findAll('td')[18].text.replace("UZS\xa0", "")
rub = soup.findAll('td')[2].text.replace("UZS\xa0", "")
data = {
    'title': 'Poytaxt bank',
    'usd': usd,
    'euro': eur,
    'rub': rub
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')