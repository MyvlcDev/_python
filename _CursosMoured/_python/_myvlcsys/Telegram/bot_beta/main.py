import telebot

TOKEN="1478529541:AAH4BlDnjVB7tui30G7w_4MgKLU52scl_ww"
b_nm="@chatoMolina_bot"

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands = ['greet','start'])
def greet(message):
    msg = ''' Hola que tal?  '''
    bot.reply_to(message, msg)

@bot.message_handler(commands=['help'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(telebot.types.InlineKeyboardButton(
       'Message the developer', url='telegram.me/artiomtb' )  
         )
   bot.send_message(
       message.chat.id,
       '1) To receive a list of available currencies press /exchange.\n' +
       '2) Click on the currency you are interested in.\n' +
       '3) You will receive a message containing information regarding the source and the target currencies, ' +
       'buying rates and selling rates.\n' +
       '4) Click “Update” to receive the current information regarding the request. ' +
       'The bot will also show the difference between the previous and the current exchange rates.\n' +
       '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
       reply_markup=keyboard
   )