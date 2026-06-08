import telebot
import os

TOKEN = os.getenv("8855670118:AAEooM141ZGH3lEsfV5efpnIeb8xM4xn5WI")

bot = telebot.TeleBot(8855670118:AAEooM141ZGH3lEsfV5efpnIeb8xM4xn5WI)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bienvenue sur Nexam Pay Africa !")

bot.infinity_polling()
