from bs4 import BeautifulSoup
import requests

req = requests.get('https://es.wikipedia.org/wiki/Python')
soup = BeautifulSoup(req.content, "html.parser")

indice = soup.find_all('li', {'class': 'toclevel-1'})

print("s")
for elem in indice:
    print(elem.find('span', class_ ="toctext").text)