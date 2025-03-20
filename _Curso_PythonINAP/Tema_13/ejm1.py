from bs4 import BeautifulSoup

import requests

req = requests.get('https://www.ign.es/web/ign/portal')

soup = BeautifulSoup(req.content, "html.parser")

print (soup)