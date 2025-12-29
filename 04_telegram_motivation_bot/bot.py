from telegram.ext import Updater, CommandHandler
from messages import get_random_message
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text(
        "Merhaba 👋\nGünlük motivasyon için /motivate yazabilirsin."
    )

def motivate(update, context):
    update.message.reply_text(get_random_message())

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("motivate", motivate))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
