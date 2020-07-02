from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://www.agrobank.uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.findAll('td')[5].text
eur = soup.findAll('td')[9].text
rub = soup.findAll('td')[12].text
data = {
    'title': 'Agro Bank',
    'usd': usd,
    'euro': eur,
    'rub': rub
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')