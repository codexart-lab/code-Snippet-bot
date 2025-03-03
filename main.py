import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Load environment variables
load_dotenv()

# Get the bot token from .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me code, and I will format it for easy copying!")

def format_code(update: Update, context: CallbackContext) -> None:
    user_code = update.message.text
    formatted_code = f"```\n{user_code}\n```"
    update.message.reply_text(formatted_code, parse_mode="Markdown")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, format_code))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
