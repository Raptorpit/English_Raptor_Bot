import time
import schedule
from handlers import word
from db.db_commands.user_commands import *


def sheduler():
    schedule.every().day.at('12:00').do(daily_word)
    while True:
        schedule.run_pending()
        time.sleep(1)



def daily_word():
    users_id = all_users_id()
    for user in users_id:
        id = user[0]
        word.send_day_words(id)
        print('working')



