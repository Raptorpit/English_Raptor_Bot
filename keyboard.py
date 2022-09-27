from telebot import types


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    show_words_btn = types.KeyboardButton('Хочу еще слово🤏')
    day_words_count_btn = types.KeyboardButton('Поменять количество слов в день↔️')
    learned_words_count_btn = types.KeyboardButton('Сколько слов я уже выучил❓🤔')
    keyboard.add(show_words_btn,day_words_count_btn,learned_words_count_btn)
    return keyboard