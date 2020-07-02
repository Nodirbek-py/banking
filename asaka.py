from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://www.asakabank.uz/uz"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.find("div", {"title":"Bir aqsh dollari sotib olish darajasi, 10160,00 so'm"}).text
eur = soup.find("div", {"title":"Evro biri hisoblanadi sotib olish kursi yig'indisi 10450,00"}).text
rub = soup.findAll("div", {"class": "pr voice_read"})[5].text
data = {
    'title': 'Asaka Bank',
    'usd': usd,
    'euro': eur,
    'rub': rub
} 
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')