from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters
from config.auth import token

TOKEN="1478529541:AAH4BlDnjVB7tui30G7w_4MgKLU52scl_ww"

def start(update, context):
    update.message.reply_text("Welcome to your Telegram bot!")

def help_command(update, context):
    update.message.reply_text("You requested help. Here are some available commands:\n"
                              "/help - Show this help message\n"
                              "/start - Start the bot")

def handle_message(update, context):
    text = update.message.text
    if text == '/start':
        start(update, context)
    elif text == '/help':
        help_command(update, context)

def main():
    # Initialize the Updater with your bot token
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Define the command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Handle non-command messages using a filter
    ## dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()