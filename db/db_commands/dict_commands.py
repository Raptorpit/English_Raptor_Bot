import sqlite3




def record_words(w_id: int, en_word: str, rus_word: str, w_link: str):
    session = sqlite3.connect('db/anglo_bot.db', check_same_thread=False)
    cursor = session.cursor()
    try:
        cursor.execute('INSERT INTO words (id, en, rus, link) VALUES (?, ?, ?, ?)', (w_id, en_word, rus_word, w_link))
        session.commit()
        cursor.close()
        session.close()
    except sqlite3.Error as error:
        print(error)
        session.close()

def show_word(user_id):
    session = sqlite3.connect('db/anglo_bot.db', check_same_thread=False)
    cursor = session.cursor()
    try:
        user_index_id = cursor.execute('SELECT id FROM users WHERE user_id=?', (user_id,))
        user_index_id = user_index_id.fetchone()[0]
        # Выбираем слова которые не входят в смежную таблицу выученных
        cursor.execute('SELECT * FROM words WHERE id NOT IN(SELECT word_id FROM user_words WHERE word_id = id and '
                       'user_id = ?) ORDER BY RANDOM() LIMIT 1', (user_index_id,))
        a = cursor.fetchall()
        word_id = a[0][0]
        # Добавляем в таблицу выученных слов
        cursor.execute('INSERT INTO user_words (user_id, word_id) VALUES(?, ?) ', (user_index_id, word_id))
        session.commit()
        return a[0][1], a[0][2], a[0][3]
    except sqlite3.Error as error:
        print(error)
        session.close()


def learned_words_update(user_id: int):
    session = sqlite3.connect('db/anglo_bot.db', check_same_thread=False)
    cursor = session.cursor()
    try:
        cursor.execute('UPDATE users SET learned_words_count = (SELECT COUNT(*) '
                       'FROM user_words WHERE user_id =(SELECT id FROM users WHERE user_id =?)) WHERE user_id = ?', (user_id, user_id))
        session.commit()
        cursor.close()
        session.close()
    except sqlite3.Error as error:
        print(error)
        cursor.close()
        session.close()
