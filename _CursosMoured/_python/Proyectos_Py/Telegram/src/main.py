import telebot

### https://www.youtube.com/watch?v=wxOeEb2ElSU&t=38s

TOKEN = '5236422638:AAGJ9BPhqPm2SCcqBIhqqOgvOVOX2wkPNm0'
bot = telebot.TeleBot(TOKEN)


@bot.message_handlers(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola que tal,chato?') 


@bot.message_handlers(commands=['start'])
def sed_help(message):
    bot.reply_to(message, 'Ayuda,chato?')




@bot.message_handler(func=lambda m:True)
def echo_all(messaage):
    bot.reply_to(messaage, messaage.text)



if __name__ == "__main__":
    bot.polling(none_stop=True)




