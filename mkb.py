from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://mikrokreditbank.uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
table = soup.find("table", {"width":"100%"})
currencies = table.findAll("td")
usd = currencies[1].text
eur = currencies[5].text
data = {
    'title': 'Mikrokredit bank',
    'usd': usd,
    'euro': eur
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')