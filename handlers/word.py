import datetime

from db.db_commands.dict_commands import *
from main import bot

@bot.message_handler(commands=['word'])
def word_handler(message):
    us_id = message.from_user.id
    b = show_word(us_id)
    learned_words_update(us_id)
    bot.send_message(message.chat.id, f"{b[0]} — {b[1]}")
    bot.send_audio(message.chat.id, audio=b[2])


# def send_message():
#     for user in users:
#         time = datetime.datetime.now().strftime('%H:%M')
#         if time = '19:00':
#             bot.send_message(user,'eee')

