import telebot
botID = ('botID')
bot = telebot.TeleBot(botID)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(
        telebot.types.InlineKeyboardButton("mebyri", callback_data='liqod1'),
        telebot.types.InlineKeyboardButton("okak", callback_data='okak2')
    )
    bot.send_message(message.chat.id, "Выберите человека:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'liqod1':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(
            telebot.types.InlineKeyboardButton("YouTube", url="https://www.youtube.com/@mebyri"),
            telebot.types.InlineKeyboardButton("Twitch", url="https://www.twitch.tv/mebyri") 
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="Выберите платформу:", reply_markup=markup)
    elif call.data == 'okak2':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(
            telebot.types.InlineKeyboardButton("YouTube", url="https://www.youtube.com/channel/UCuL9MARHcuA17yIcpMrjkEQ"),
            telebot.types.InlineKeyboardButton("Twitch", url="https://www.twitch.tv/okak__")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="Выберите платформу:", reply_markup=markup)

bot.polling()
 
