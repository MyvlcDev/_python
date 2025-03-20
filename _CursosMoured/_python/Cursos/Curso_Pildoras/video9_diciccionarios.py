midiccionario={"Alemania":"Berlin", "Francia":"Paris","Reino Unido" : "Londres", "España": "Madrid"}
print(midiccionario["España"])
print(midiccionario)

#Añadir al diccionario
midiccionario["Italia"] = "Lisbola"
print(midiccionario)

##Modificado
midiccionario["Italia"] = "Roma"
print(midiccionario)


##Borrado
del midiccionario["Reino Unido"]
print(midiccionario)

#tipos de datos dicionario

midiccionario_2={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros": 3}
print(midiccionario_2)

# tuplas y diccionarios

miTupla_1=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario__tuplas={miTupla_1[0]:"Madrid",miTupla_1[1]:"Paris",miTupla_1[2]:"Londres",miTupla_1[3]:"Berlin"}
print(midiccionario__tuplas)
print(midiccionario__tuplas["Francia"])

midiccionario__tuplas2={23:"Jordan", "Nombre": "Michel", "Equipo": "Chicago", "anillos" : [1992,1992,1993,1996,1997]}
print(midiccionario__tuplas2)
print(midiccionario__tuplas2[23])
print(midiccionario__tuplas2["anillos"])

#Metodos

print(midiccionario__tuplas2.keys())

print(midiccionario__tuplas2.values())

print(len(midiccionario__tuplas2))