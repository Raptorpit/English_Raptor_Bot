import parsing
from db.db_commands import dict_commands

def record():
    for i in range(len(parsing.index)):
        w_id = parsing.index[i]
        en_word = parsing.en_w[i]
        rus_word = parsing.rus_w[i]
        w_link = parsing.w_link[i]
        dict_commands.record_words(w_id, en_word, rus_word, w_link)
