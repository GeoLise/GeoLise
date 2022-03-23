import telebot
from telebot import types
token = '5249280440:AAHrphmP631_37CCHBdEjSdNSwRklnWI7KA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот.".format(message.from_user), reply_markup=markup)
 
