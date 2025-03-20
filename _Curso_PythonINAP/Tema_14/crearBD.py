import sqlite3 
dir = r'C:\BDSql\BBDD_Prueba.db'
conn = sqlite3.connect(dir)
cursor = conn.cursor() 
cursor.execute("DROP TABLE IF EXISTS Tabla1") 
cursor.execute("CREATE TABLE Tabla1 (id INTEGER PRIMARY KEY, nombre char (25), ape1 char(25), ape2 char(25), dni TEXT, edad char(25), origen char(25))")
conn.commit()
print ("Hecho") 