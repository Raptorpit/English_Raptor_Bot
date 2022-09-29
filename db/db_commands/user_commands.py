import sqlite3

def register_user(user_id: int, username: str):
    session = sqlite3.connect('db/anglo_bot.db', check_same_thread=False)
    cursor = session.cursor()
    try:
        cursor.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
        session.commit()
        cursor.close()
        session.close()
    except sqlite3.Error as error:
        print(error)
        cursor.close()
        session.close()


def words_count_update(user_id: int,words_count: int):
    session = sqlite3.connect('/home/raptorpit/PycharmProjects/Anglo_bot/db/anglo_bot.db', check_same_thread=False)
    cursor = session.cursor()
    try:
        cursor.execute('UPDATE users SET day_words_count =? WHERE user_id =?', (words_count, user_id))
        print(words_count,user_id)
        print(cursor.fetchone())
        session.commit()
        cursor.close()
        session.close()
    except sqlite3.Error as error:
        print(error)
        cursor.close()
        session.close()


def day_words_count(user_id: int):
    session = sqlite3.connect('db/anglo_bot.db', check_same_thread=False)
    cursor = session.cursor()
    try:
        cursor.execute('SELECT day_words_count FROM users WHERE user_id =?', (user_id,))
        word_count = cursor.fetchone()[0]
        session.commit()
        cursor.close()
        session.close()
        return word_count
    except sqlite3.Error as error:
        print(error)
        cursor.close()
        session.close()


def learned_words(user_id: int):
    session = sqlite3.connect('db/anglo_bot.db', check_same_thread=False)
    cursor = session.cursor()
    try:
        cursor.execute('SELECT learned_words_count FROM users WHERE user_id =?', (user_id,))
        word_count = cursor.fetchone()[0]
        session.commit()
        cursor.close()
        session.close()
        return word_count
    except sqlite3.Error as error:
        print(error)
        cursor.close()
        session.close()

def all_users_id():
    session = sqlite3.connect('db/anglo_bot.db', check_same_thread=False)
    cursor = session.cursor()
    try:
        cursor.execute('SELECT user_id FROM users')
        b = cursor.fetchall()
        return b
    except sqlite3.Error as error:
        print(error)
        cursor.close()
        session.close()
