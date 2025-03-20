###https://www.youtube.com/watch?v=kPNHKrOqedI

from bs4 import BeautifulSoup
import requests

wbesite= 'http://www.myvlcsys.com'
result = requests.get(wbesite)
content = result.text

soup= BeautifulSoup(content, 'lxml')
##print(soup.prettify())

box = soup.find('apa-article-box', clas_ = 'entry-title')

enlace = box.find('a').get_text()

print(enlace)