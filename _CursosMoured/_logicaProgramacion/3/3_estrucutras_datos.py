
""" 
*
* EJERCICIO:
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.

*
 """
## Ejemplos de estructuras de datos en Python:
## Listas
frutras  = ['manzana', 'pera', 'uva', 'fresa', 'mango', 'kiwi', 'platano']

## Tuplas
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
## borrar elementos tupla = tupla[:1] + tupla[2:]
tupla = tupla[:1] + tupla[2:]
## añadir elementos tupla = tupla + (1,)
tupla = tupla + (1,)
## convertir tupla en lista lista = list(tupla)
# lista = list(tupla)
# print(lista)
# print(type(lista))
#   




## conjuntos
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
## borrar elementos conjunto.remove(1)
conjunto.remove(1)
## añadir elementos conjunto.add(1)
conjunto.add(1)


## Pilas
pila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


## Diccionarios
diccionario = {
    'nombre': 'Juan',
    'apellido': 'Perez',
    'edad': 25,
    'email': '',
    'telefono': '1234567890'
}

## listas enlazaadas
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None 

class ListaEnlazada:
   def __init__(self):
        self.primero = None
        self.ultimo = None    

   def insertar(self, dato):
      if self.primero is None:
         self.primero = self.ultimo = Nodo(dato)
      else:
         self.ultimo.siguiente = Nodo(dato)
         self.ultimo = self.ultimo.siguiente
