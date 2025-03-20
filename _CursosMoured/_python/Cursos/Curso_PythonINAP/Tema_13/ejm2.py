from bs4 import BeautifulSoup
import requests
req = requests.get('https://www.ign.es/web/ign/portal')
soup = BeautifulSoup(req.content, "lxml")
 
links_a = soup.find_all('a', class_="taglib-language-list-text")
print(links_a)