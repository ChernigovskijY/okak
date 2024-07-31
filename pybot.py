import telebot

bot = telebot.TeleBot("7486481919:AAG83GuZ5Qaq-3g3jEGxqw1EhiGHsROx7EY")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
  else:
    bot.send_message(message.from_user.id, "Я не знаю такой команды. Напиши /help.")

bot.polling(none_stop=True, interval=0)