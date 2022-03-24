import telebot
token = '5230048546:AAHvCul2FoIWxU5lfGUT7zmVQPsiJ8iPdKA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    item2=types.KeyboardButton("Кнопка2")
    item3=types.KeyboardButton("Игра")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, text="Привет")
    
if __name__=='__main__':
    bot.infinity_polling()
