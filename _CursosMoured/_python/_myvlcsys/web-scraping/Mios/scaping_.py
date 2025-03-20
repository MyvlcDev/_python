import requests # pip install requests
from bs4 import BeautifulSoup
from lxml import html # pip install lxml


# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
# URL SEMILLA
url = 'https://coinmarketcap.com/es/'
print()
print (url)
print()
#############################
###   NUEVO
#############################

# REQUERIMIENTO AL SERVIDOR
req = requests.get(url, headers=headers)
req.encoding = 'utf-8' # Codificar correctamente caracteres extranos

# PARSEO DEL ARBOL HTML QUE RECIBO COMO RESPUESTA CON LXML
parser = html.fromstring(req.content) # Uso .content para poder codificar los caracteres raros




##### EXTRACCION DE DATOS

## Titulo de web
req = requests.get(url)
soup = BeautifulSoup(req.content, "lxml")
soup.title

print(soup.title )
print()


contenedor_de_preguntas = soup.find(id="sc-4c05d6ef-0 bLqli") # ENCONTRAR UN ELEMENTO POR ID
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="s-post-summary") # ENCONTRAR VARIOS ELEMENTOS POR TAG Y POR CLASE
##(class="sc-4c05d6ef-0 bLqliP")
## <p class="sc-65e7f566-0 iPbTJf coin-item-name">Solana</p>  
## Titulo de web




#############################
###   ANTERIOR
#############################
""" 
# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url, headers=headers)
respuesta.encoding = 'utf-8' # Codificar correctamente caracteres extranos

# PARSEO DEL ARBOL HTML QUE RECIBO COMO RESPUESTA CON LXML
parser = html.fromstring(respuesta.content) # Uso .content para poder codificar los caracteres raros

# EXTRACCION DE IDIOMA INGLES
id_next = parser.get_element_by_id("__next")
print (id_next.text_content())



# EXTRACCION SOLO DEL TEXTO QUE DICE INGLES
ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
print(ingles[0])

# EXTRACCION DE TODOS LOS IDIOMAS POR CLASE
idiomas = parser.find_class('central-featured-lang')
for idioma in idiomas:
  print(idioma.text_content())

# EXTRACCION DE TODOS LOS IDIOMAS POR XPATH
idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
for idioma in idiomas:
  print(idioma)
 """