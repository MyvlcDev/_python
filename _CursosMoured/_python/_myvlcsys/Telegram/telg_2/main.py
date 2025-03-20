import telebot
from config import TOKEN

## @chatoMolina_bot

### https://www.google.com/search?q=bot+telegram+python+github&rlz=1C1GCEA_enES1083ES1083&oq=bot+telegra+py&gs_lcrp=EgZjaHJvbWUqCQgDEAAYDRiABDIGCAAQRRg5MgkIARAAGA0YgAQyCQgCEAAYDRiABDIJCAMQABgNGIAEMggIBBAAGBYYHjIGCAUQRRg8MgYIBhBFGDwyBggHEEUYQdIBCDU1NTBqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8#fpstate=ive&ip=1&vld=cid:2faaa131,vid:wt5IVr1eibE,st:0


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])

def send_welcome(message):
    bot.reply_to(message,"hola caracola")

bot.polling