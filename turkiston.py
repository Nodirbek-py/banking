from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://tb24.uz/oz/#anchor4"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.findAll(class_ = "rate__value")[0].text.strip()
eur = soup.findAll(class_ = "rate__value")[3].text.strip()
data = {
    'title': 'Turkiston bank',
    'usd': usd,
    'euro': eur,
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')
    