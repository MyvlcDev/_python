import telebot
import mysql.connector

#### Conexión con bd

mydb = mysql.connector.connect(
  host="myvlcsys.com",
  user="u591865418_v",
  password="vlcVicente2020",
  database="u591865418_v"
)

mycursor = mydb.cursor()

mycursor.execute("select * from z_mi_prog")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
####




##   https://www.youtube.com/watch?v=wt5IVr1eibE
##   minn 22:30
###  xsync_80_bot -> 
TELEGRAM_TOKEN= "8194628476:AAE7AoBzq-_oC9GmG3xPDPvJ1SLS82BoJeA"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,"Hola, bienvendi@")



@bot.message_handler(content_types=['text']) ## TIPO DE CADENA QUE DEVELVEMOS PUEDE SER AUDIO, TEXTO, IMAGEN ...ETC
def opciones_message(message):
    if message.text.lower() =="hola":
        bot.send_message(message.chat.id, "Hola, en que te puedo ayudar??") 
    elif message.text.lower() =="adios":
        bot.send_message(message.chat.id, "otro distinto??")
        print("sdfsmkdf")

    elif message.text.lower() =="cnt":
        bot.reply_to(message,"Envia el texto a contar.")
        bot.register_next_step_handler(message, contar_palabras) 
    
    elif message.text.lower() =="saludo":
        bot.send_message(message.chat.id,"Encatado de saludarte, cual es tu nombre.")
        bot.register_next_step_handler(message, f_saludar) 
        ##bot.reply_to(message,"Encatado de saludarte, cual es tu nombre.")
        bot.register_next_step_handler(message, menu) 
    
    elif message.text.lower() =="bd":
        
        print("Dentro de bd")
        bot.reply_to(message,"¿Que deseas consultar de tu bd?")
        bot.register_next_step_handler(message, fun_bd) 
    
    elif message.text.lower() =="cp":
        
        print("Dentro de Consulta Pesos")
        bot.reply_to(message,"¿Cuantos?")
        cp=message
        bot.register_next_step_handler(cp, fun_bd) 
    




        
def contar_palabras(message):
    words = message.text.split()
    bot.reply_to(message, f"el texto tiene {len(words)} palabras" )
    bot.send_message(message.chat.id, f"el texto tiene {len(words)} palabras 222")

def f_saludar(message):
    respuesta_saludo = message.text.split()
    print(respuesta_saludo)
    bot.send_message(message.chat.id,f"Buenas tardes {respuesta_saludo}" )
    
def menu(message):
    bot.send_message(message.chat.id, f"Selecciona una las siguientes opciones: " )
    bot.send_message(message.chat.id, f"Opcion A:\n Opcion B:\n Opcion C:\n"      ) 

####   LUNES NOCHE ME QUEDO AQUI NO ENTRA A ESTÉ MENU
def opcion_menu(message):  
    bot.send_message(message.chat.id, f"Dentro de opción menu " )
    op_menu = message.text.split()
    if message.text.lower() =="A":
        bot.send_message(message.chat.id, "Opción A") 
   
def fun_bd(message):  #### MODELOS SIN FUNCIONAR PARA AFINAR
    peticion_bd = message.text.split()
    print(peticion_bd)

    sql1 = "select * from z_mi_prog"
    print(sql1)
    mycursor1 = mydb.cursor()
    mycursor1.execute("select * from z_pesos")
    myresult = mycursor1.fetchall()
    for x in myresult:
        print(x)

    bot.send_message(message.chat.id,f"sQl desde Telegram {x}" )                


def cp(message): 

    peticion_bd = message.text.split()
    print("1" + peticion_bd)

    sql1 = "select * from z_mi_prog"
    print("2" + sql1)
    bot.send_message(message.chat.id,f"sql {sql1}" )    
    mycursor1 = mydb.cursor()
    mycursor1.execute("select * from z_pesos")
    myresult = mycursor1.fetchall()
    for x in myresult:
        print(3+"x")
        bot.send_message(message.chat.id,f"sQl desde Telegram {x}" )     
    

    bot.send_message(message.chat.id,f"sQl desde Telegram {x}" )     
   

bot.polling()

