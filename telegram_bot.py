import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler
from weather_app import weather_report

bot_token = os.environ.get("BOT_TOKEN")
bot = Bot(token=bot_token)

def weather_command(update: Update, context):
    update.message.reply_text("Hi")
    command_text = update.message.text
    city_name = ' '.join(command_text.split()[1:])
    weather_data = weather_report(city_name)
    update.message.reply_text(weather_data)

def use_telegram():
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("weather", weather_command))
    updater.start_polling()
    updater.idle()
