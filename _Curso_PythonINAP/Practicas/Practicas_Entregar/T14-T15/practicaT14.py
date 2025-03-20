import sqlite3
dir = r'C:\BDSql\BBDD_EJER_14.db'
conn = sqlite3.connect(dir)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS TABLA2")

archivo = open(r'')
lineas = 

cursor.execute("CREATE TABLE Tabla2 (id INTEGER PRIMARY KEY, dni int, numeroDespacho char(25), Telf char(25))")

conn.commit()
print ("Hecho") 