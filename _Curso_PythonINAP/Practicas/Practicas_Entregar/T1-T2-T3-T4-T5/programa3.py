print("**- Inicio del programa MAYOR, MENOR, MEDIA ARITMÉTICA Y MEDIANA-** ")

def solicitarNumero(num_valores):
    list_val = []
    if num_valores > 0:
        num = 0
        for _ in range(num_valores):
            num += 1
            numero = float(input(f"Introduzca {num}º de {num_valores} elementos: "))
            list_val.append(numero)         
        
        return list_val
    
def calcularMaximo(valores):
    valores.sort(reverse=True)
    return valores[:1][0]

def calcularMinimo(valores):
    valores.sort()
    return valores[:1][0]

def calcularMedia(valores):
    suma = 0
    for x in valores:
        suma += x
    
    media = suma/len(valores)
    return media

def calcularMediana(valores):

    mediana="valor medio" 

    return mediana

print ("¿Cuántos valores deseas introducir?")
num_val=int(input())
if num_val== None:
    print("el valor añadido no es valido.")
else:
   listaValores=solicitarNumero(num_val)

maximo= calcularMaximo(listaValores)
minimo= calcularMinimo(listaValores)
media= calcularMedia(listaValores)
mediana= calcularMediana(listaValores)

print(f"El máximo calculado es: {maximo}" )
print(f"El minimo calculado es: {minimo}" )
print(f"La media calculado es: {media}" )
print(f"La mediana calculado es: {mediana}" )

