from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace with your bot token
BOT_TOKEN = "7952390055:AAHa-kZFaa5wHfXslql_xPI9bINlHwRWHNU"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me code, and I will format it for easy copying!")

def format_code(update: Update, context: CallbackContext) -> None:
    user_code = update.message.text
    formatted_code = f"\n{user_code}\n``"
    update.message.reply_text(formatted_code, parse_mode="Markdown")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, format_code))

    updater.start_polling()
    updater.idle()

