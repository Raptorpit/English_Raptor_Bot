import datetime

from db.db_commands.user_commands import *
from db.db_commands.dict_commands import *
from main import bot

@bot.message_handler(commands=['word'])
def word_handler(message):
    us_id = message.from_user.id
    send_word(us_id)

def send_word(user_id: int):
    us_id = user_id
    b = show_word(us_id)
    learned_words_update(us_id)
    bot.send_message(us_id, f"{b[0]} — {b[1]}")
    bot.send_audio(us_id, audio=b[2])

def send_day_words(user_id: int):
    words_count = day_words_count(user_id)
    for i in range(words_count):
        send_word(user_id)

