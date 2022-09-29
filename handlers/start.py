import keyboard
from db.db_commands.user_commands import *
from main import bot


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я буду учить с тобой слова',reply_markup=keyboard.get_keyboard())
    us_id = message.from_user.id
    users_id.append(us_id)
    username = message.from_user.username
    register_user(us_id, username)
