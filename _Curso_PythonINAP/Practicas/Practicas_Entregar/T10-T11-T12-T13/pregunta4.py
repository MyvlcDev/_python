from bs4 import BeautifulSoup
import requests

url = requests.get( "https://www.ign.es/web/ign/portal/ultimos-terremotos/-/ultimos-terremotos/get30dias")
b_soup= BeautifulSoup(url.content,"lxml")

busca_tb= b_soup.find('table')

## print(busca_tb)

busca_filas= busca_tb.find_all('tr')

## print(busca_filas)

for linea in busca_filas:
    busca_col= linea.find_all('td')
    ##print(busca_col)
    if len(busca_col) >=2:
        col_1= busca_col[0].get_text()
        col_6= busca_col[6].get_text()
        print(f"{col_1:15}  {col_6:15}")
