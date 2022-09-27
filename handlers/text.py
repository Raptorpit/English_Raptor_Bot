from handlers.word import *
from main import bot
from db.db_commands.user_commands import *
@bot.message_handler(content_types='text')
def answer(message):
        if message.text == "Хочу еще слово🤏":
            word_handler(message)
        elif message.text == "Сколько слов я уже выучил❓🤔":
            us_id = message.from_user.id
            b = learned_words(us_id)
            bot.send_message(message.chat.id, b)
        elif message.text == "Поменять количество слов в день↔️":
            msg = bot.send_message(message.chat.id, 'Сколько слов ты хочешь получать?')
            bot.register_next_step_handler(msg, word_count)
        else:
            bot.send_message(message.chat.id, 'Извини, я тебя не понимаю🤯')

def word_count(message):
    if message.text.isdigit():
        us_id = message.from_user.id
        msg = int(message.text)
        words_count_update(us_id, msg)
    else:
        bot.send_message(message.chat.id, 'Извини, я тебя не понимаю🤯')

