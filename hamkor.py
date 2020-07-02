from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://hamkorbank.uz/uz/exchange-rate/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
tables = soup.findAll(class_="body")
usd = tables[0].text.replace("AQSh dollariUSD10173.38", "")
usd = usd.replace("10220+0.62","")
eur = tables[1].text.replace("YevroEUR11411.48", "")
eur = eur.replace("12000+43.42", "")
data = {
    'title': 'Hamkor Bank',
    'usd': usd,
    'euro': eur
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')