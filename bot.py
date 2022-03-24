import telebot
token = '5230048546:AAHvCul2FoIWxU5lfGUT7zmVQPsiJ8iPdKA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    //markup=types.ReplyKeyboarMarkup(resize_keyboard=True)
    //but1=types.KeyboardButton("Глава 1")
    
    //markup.add(but1)
    bot.send_message(message.chat.id, text="Привет")
    
if __name__=='__main__':
    bot.infinity_polling()
