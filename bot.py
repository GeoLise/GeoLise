import telebot
token = '5230048546:AAHvCul2FoIWxU5lfGUT7zmVQPsiJ8iPdKA'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, text = "Hello😀")
    
if __name__=='__main__':
    bot.infinity_polling()
