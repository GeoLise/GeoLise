import telebot
from telebot import types
token = '5230048546:AAHvCul2FoIWxU5lfGUT7zmVQPsiJ8iPdKA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Привет")
    
