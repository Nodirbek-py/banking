from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://davrbank.uz/en"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.findAll("tr")[0].findAll("td")
usd = usd[2].text
eur = soup.findAll("tr")[1].findAll("td")
eur = eur[2].text
data = {
    'title': 'Davr Bank',
    'usd': usd,
    'euro': eur
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')