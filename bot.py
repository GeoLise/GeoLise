import telebot
from telebot import types
token = '5230048546:AAHvCul2FoIWxU5lfGUT7zmVQPsiJ8iPdKA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Глава 1")
    item2=types.KeyboardButton("Глава 2")
    item3=types.KeyboardButton("Глава 3")
    item4=types.KeyboardButton("хуй")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Глава 1":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyBoardButton("Gfh")
        markup.add(item1)
    if message.text=="Глава 2":
        bot.send_message(message.chat.id, "vk.com/goshkazavr")

@bot.message_handler(content_types='text')
def game(message):
    if message.text=="Игра":
        bot.send_message(message.chat.id, "игра началась")
if __name__ == '__main__':
     bot.infinity_polling() 
