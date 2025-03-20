
import sqlite3
dir = r'C:\BDSql\BBDD_Prueba.db'
conn = sqlite3.connect(dir)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Tabla1")
cursor.execute("CREATE TABLE Tabla1 (id INTEGER PRIMARY KEY, nombre char (25), ape1 char(25), ape2 char(25), dni int, edad char(25), origen char(25))")

a = open(r'C:\BDSql\DatosBBDD2.txt') 
linesa = a.readlines()
for i in range(len(linesa)-1):
    nom = str(linesa[i+1].split("\t")[0])
    ape1 = linesa[i+1].split("\t")[1]
    ape2 = linesa[i+1].split("\t")[2]
    dni = linesa[i+1].split("\t")[3]
    edad = linesa[i+1].split("\t")[4]
    provincia = linesa[i+1].split("\t")[5]
    id = linesa[i+1].split("\t")[6]

    datos = "'"+nom+"', '"+ape1+"', '"+ape2+"', '"+dni+"', '"+edad+"', '"+provincia+"', '"+id+"'"
    print (i, datos)
    cursor.execute("INSERT INTO Tabla1 (nombre, ape1, ape2, dni, edad, origen, id) VALUES ("+datos+")")
    
conn.commit()
print ("Hecho") 