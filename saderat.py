from bs4 import BeautifulSoup as bs4
import requests
import json
url = "http://www.saderatbank.uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.findAll("span", {"style":"color: #0000ff;"})[0].text.replace("$", "")
eur = soup.findAll("span", {"style":"color: #0000ff;"})[1].text.replace("€", "")
data = {
    'title': 'Saderat Bank',
    'usd': usd,
    'euro': eur,
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')