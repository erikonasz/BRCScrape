import requests
from bs4 import BeautifulSoup
import json

URL = 'https://lt.brcauto.eu/automobiliu-paieska/'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'lxml')
pages = soup.find_all('li', class_='page-item')[-2]

auto_count = 0

for number in range(1, int(pages.text)):
    req = requests.get(URL + '?page=' + str(number))
soup = BeautifulSoup(req.text, 'lxml')

if auto_count == 10:
    exit()
out = []
for single_car in soup.find_all('div', class_='cars-wrapper'):

    if auto_count == 10:
        break

    auto_pavadinimas = single_car.find('h2', class_='cars__title')
    auto_parametrai = single_car.find('p', class_='cars__subtitle')

    print('\nAuto Numeris:', auto_count + 1)

    print(auto_pavadinimas.text)
    print(auto_parametrai.text)

    car = {}
    car["Pavadinimas"] = auto_pavadinimas.text
    subs = auto_parametrai.text.split(' | ')
    car["Metai"] = subs[0]
    car["KuroTipas"] = subs[1].split(" ")[1]
    car["Rida"] = subs[3].split(" ")[0]
    car["Spalva"] = subs[5]
    car["aNumeris"] = auto_count + 1
    out.append(car)
    auto_count += 1

print(json.dumps(out))
with open("automobiliu_data.json", "w") as f:
    f.write(json.dumps(out))