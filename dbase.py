import sqlite3

import parsing

v1 = 8
v2 = parsing.en[0]
print(v2)
v3 = 'ret'
try:
    sqlite_connection = sqlite3.connect('db/anglo_bot.db')
    sqlite_create_table = '''CREATE TABLE users ( 
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    learned_words TEXT); '''
    sqlite_insert =''' INSERT INTO users
    (id,username,learned_words)
    VALUES
    ('1','sobak','v1')'''
    cursor = sqlite_connection.cursor()
    cursor.execute("INSERT INTO users (id,username) VALUES (?,?);",(v1, v2))
    sqlite_connection.commit()
    print("OK")
    cursor.close()
except sqlite3.Error as error:
    print(error)

finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение закрыто")