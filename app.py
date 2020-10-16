import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=118'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, 'html.parser')
data = response.find_all('tr', 'table_highlight')
data = data[0]

salat = {}
i = 0

for d in data:
    if i == 1:
        salat['Fajr'] = d.get_text()
    elif i == 2:
        salat['Dhuhur'] = d.get_text()
    elif i == 3:
        salat['Asr'] = d.get_text()
    elif i == 4:
        salat['Maghrib'] = d.get_text()
    elif i == 5:
        salat['Isya'] = d.get_text()
    i += 1

print(f'Current Prayer Times in Kupang City, Indonesia:')
for j, k in salat.items():
    print(f'{j} : {k}')
print('-' * 50)
print(f"Fajr Times: {salat['Fajr']}")
