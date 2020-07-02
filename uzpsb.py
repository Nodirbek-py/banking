from bs4 import BeautifulSoup as bs4
import requests
import json
url = "https://uzpsb.uz/uz/exchange-rate/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
table = soup.find(class_="list")
rows = table.findAll(class_="body usd")
usd = rows[0].text.replace("1 AQSh dollariUSD10173.38", "")
usd = usd.replace("10220.000.62", "")
eur = rows[1].text.replace("1 EvroEUR11411.48","")
eur = eur.replace("11500.0043.42", "")
rub = rows[2].text.replace("1 Rossiya rubliRUB145.97","")
rub = rub.replace("160.00-0.42", "")
data = {
    'title': 'Sanoat Qurilish Bank',
    'usd': usd,
    'euro': eur,
    'rub': rub
} 
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(']')

   

        