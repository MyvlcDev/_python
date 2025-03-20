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

commands = {  
    'start': 'Empezar a mensajear con el bot',
    'ayuda': 'Da información sobre los comandos disponibles',
    'cd': 'Cambia el directorio actual',
    'exec': 'Ejecuta un comando',
    'execlist': 'Ejecuta una lista de comandos',
    'reboot': 'Reinicia el servidor'
}