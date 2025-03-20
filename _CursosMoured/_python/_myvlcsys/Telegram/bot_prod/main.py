import random
import mysql.connector
import telebot
import requests
import mysql
import misFucionoes
from asyncio.windows_events import NULL
from logging import NullHandler
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError


print("Bot en ejecución...")



# Conexión con nuetro BOT
TOKEN = "1478529541:AAH4BlDnjVB7tui30G7w_4MgKLU52scl_ww"
bot = telebot.TeleBot(TOKEN)
idGrupo = 1478529541
##chat_id = "1478529541"

print(bot.get_me())

# Conexión con nuetro BD


mydb = mysql.connector.connect(host="myvlcsys.com",user="u591865418_usu_myvlcsys",password="oD7TRr&2tO@",database="u591865418_bd_myvclsys_es")

mycursor = mydb.cursor()

mycursor.execute("select * from t_cont")
myresult = mycursor.fetchall()
######################º

commands = {  
    'start': 'Empezar a mensajear con el bot',
    'ayuda': 'Da información sobre los comandos disponibles',
    'cd': 'Cambia el directorio actual',
    'exec': 'Ejecuta un comando',
    'execlist': 'Ejecuta una lista de comandos',
    'reboot': 'Reinicia el servidor'
}

# Creación de comando simples como '/start' y '/help'
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hola mundo!")

@bot.message_handler(commands=["hola"])
def send_welcome(message):
    bot.reply_to(message, "Hola chato!")


@bot.message_handler(commands=["bd"])
def send_welcome(message):

    bot.reply_to(message, misFucionoes.f_saludo() )
    bot.send_message()

@bot.message_handler(commands=["bd2"])
def send_welcome(message):
    requests.post('https://api.telegram.org/bot' + TOKEN + '/sendMessage',
    data={'idGrupo': idGrupo, 'text': "mensaje desde bd2", 'parse_mode': 'HTML'})




######## CONSULTA BD 3

mycursor = mydb.cursor()

mycursor.execute("select * from t_cont")
myresult_BD3 = mycursor.fetchall()

@bot.message_handler(commands=["bd3"])
def send_welcome(message):
    for x in myresult_BD3:
        bot.reply_to(message, x )
       ## bot.send_message()

@bot.message_handler(commands=["bd4"])
def send_welcome(message):
    bot.reply_to(message, "Hola ! dime el id del usuario que quieres que te mestre sus registros")
    bot.reply_to(message, "Dime el id del usuario que quieres que te mestre sus registros")
    for x in myresult:
        bot.reply_to(message, x )
       ## bot.send_message()




@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "Puedes interactuar con este bot a través de /start y /help")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


def play_or_about(message):
    if message.text in ['Play','One more try!']:
        #Generate random number 
        real = random.randint(0, 5)
        
        message = bot.reply_to(message, " numero random"+real)
                               

@bot.message_handler(commands=["i"])
def mis_comandos(message):
    print( "comndo i")
    cid= message.chat.id
    ##bot.reply_to(message, "Hola chato!")
    bot.send_message(cid, "Entrando en comando i .....")
    bot.send_chat_action(cid, 'typing') # acción "escribiendo"
    ##time.sleep(3)





@bot.message_handler(commands=["bd"])
def send_welcome(message):

    bot.reply_to(message, misFucionoes.f_saludo() )




if __name__ == "__main__":
    bot.polling(none_stop=True)
    
    print("\n")


