
miLista=["María","Pepe","Marta", "Antonio"]

print(miLista[:])

print(miLista[2])

#Porciones de lista - coger varios elementos de la listas, empieza en el indice 0

print(miLista[0:3])

print(miLista[:3])


# Agregar elementos a listas

miLista.append("Chato")
print(miLista[:])

# Agregar elemento en una posición
miLista.insert(2,"usuario")
print(miLista[:])

# Agregar varios elementos al final de la lista

miLista.extend(["Lucas", "Leo" ,10 , 8.5])
print(miLista[:])


# devolver indice de la sista de la lista

print(miLista.index("Chato"))

# Comprobar si existe elemetno True/False

print("Chatoaaaa" in miLista)

# Eliminar elemento en una posición
miLista.remove("Pepe")
print(miLista[:])

# Eliminar elemento de la ultima posición

miLista.pop()
print(miLista[:])

# Sumar Listas
miLista2=["lista 2", "otra posicion"]

miLista3= miLista+miLista2

print(miLista3[:])

# REpetir o multiplicar listas

miLista4=["lista 2", "otra posicion"] * 5
print(miLista4[:])