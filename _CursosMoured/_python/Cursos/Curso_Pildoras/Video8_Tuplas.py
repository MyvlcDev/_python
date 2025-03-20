#Crear un tupla

miTupla=("Juan", 18,6,1980,18,18) #Se puede crear la Tupla sin parentesis

print(miTupla[0])
print( miTupla)

print("Conversor Tupla a Lista")
miLista= list(miTupla)
print (miLista)

print("Conversora Lista a Tupla ")
miTupla2= tuple (miLista)
print( miTupla2)
print ("Juan" in miTupla2)

print("Cuenta las coincidencias en la  Tupla  ")
print(miTupla2.count(18))

print(len(miTupla))

# Desempaquetado de tuplas

miTupla4=("Juan", 18,6,1990)
nomb, dia, mes, agno=miTupla4
print (nomb)
print (dia)
print (agno)
print (mes)
 