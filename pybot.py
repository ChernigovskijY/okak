import telebot

bot = telebot.TeleBot("Paste your ID there")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
  elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши Привет")
  else:
    bot.send_message(message.from_user.id, "Я не знаю такой команды. Напиши /help.")

bot.polling(none_stop=True, interval=0)
