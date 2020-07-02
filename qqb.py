from bs4 import BeautifulSoup as bs4
import requests
import json
url = "http://www.qishloqqurilishbank.uz/uz/"
request = requests.get(url).text
soup = bs4(request, 'html.parser')
usd = soup.find(class_="text-bold text-color-43a047").text.strip()
eur = soup.find(class_="text-bold text-color-43a047").text.strip()
rub = soup.find(class_="text-bold text-color-43a047").text.strip()
data = {
    'title': 'Qishloq Qurilish Bank',
    'usd': usd,
    'euro': eur,
    'rub': rub
}
with open('data.json', 'a', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.write(',')