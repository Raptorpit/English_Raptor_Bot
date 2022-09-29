import telebot
import parsing
import record
import config
import threading
import daily_word

bot = telebot.TeleBot(config.TOKEN, threaded=True)
def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    from handlers import bot
    parsing.parsing()
    record.record()
    th1 = threading.Thread(target=daily_word.sheduler, name='1')
    th2 = threading.Thread(target=run_bot, name='2')
    th1.start()
    th2.start()



