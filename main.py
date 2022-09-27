import telebot
import parsing
import record
import config
from handlers import word
import schedule
from db.db_commands.dict_commands import *

bot = telebot.TeleBot(config.TOKEN)


if __name__ == "__main__":
    from handlers import bot
    parsing.parsing()
    record.record()
#    word.send_message()
    bot.infinity_polling()
