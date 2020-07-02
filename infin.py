from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://www.infinbank.com/uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
table = soup.find(class_="dtable currency-table")
usd = table.findAll("td")[1].text
eur = table.findAll("td")[2].text
data = {
    'title': 'Infin Bank',
    'usd': usd,
    'euro': eur
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')