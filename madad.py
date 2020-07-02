from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://www.madadinvestbank.uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.findAll(class_="val-item")[0].text.replace("Sotib olish", "").strip()
eur = soup.findAll(class_="val-item")[2].text.replace("Sotib olish", "").strip()
data = {
    'title': 'Madad Invest Bank',
    'usd': usd,
    'euro': eur
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')