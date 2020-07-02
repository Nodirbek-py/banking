from bs4 import BeautifulSoup as bs4
import requests
import json
url = "http://uaeb.uz/ru"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.findAll("td")[1].text
eur = soup.findAll("td")[5].text
data = {
    'title': 'UzAgroExport Bank',
    'usd': usd,
    'euro': eur,
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')