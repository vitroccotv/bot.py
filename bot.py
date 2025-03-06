import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Reemplaza 'TU_TOKEN' con tu token real
TOKEN = "7758812632:AAGDZoF_lFu6TjBQ4qiKMSHov7BkvRXWL5U"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy tu bot BodyTV.")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    caps_handler = CommandHandler('caps', caps)
    dispatcher.add_handler(caps_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()