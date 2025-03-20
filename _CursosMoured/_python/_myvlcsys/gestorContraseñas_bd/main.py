import mysql.connector

mydb = mysql.connector.connect(
  host="myvlcsys.com",
  user="u591865418_usu_myvlcsys",
  password="oD7TRr&2tO@",
  database="u591865418_bd_myvclsys_es"
)

mycursor = mydb.cursor()

mycursor.execute("select * from t_cont")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)