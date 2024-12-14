import telebot
from telebot import types
import rus,eng,arm
from statuses_lib import load_statuses, write_statuses
token = "7271150426:AAEpI9DZ7q_b5WkpUXPHwsDvx9tYEaG_qjE"
bot = telebot.TeleBot(token)

language = "english"
language_change = False

statuses = load_statuses()
# statuses[user_id]: ["language", is_lang_changing]


def get_status_by_user_id(user_id):
    user_id = str(user_id)
    stat = statuses.get(user_id, None)
    if stat is None:
        return['english',False]
    else: 
       return stat

def set_status_by_user_id(user_id, status):
    user_id = str(user_id)
    if (status is None) or len(status) != 2:
        status = statuses.get(user_id,['english',False])
    statuses[user_id] = status
    write_statuses(statuses)


@bot.message_handler(commands=["language","start"])
def quiz(message):

    status = get_status_by_user_id(message.from_user.id)
    status[1] = True # is_lang_changing = True
    set_status_by_user_id(message.from_user.id, status)

    markup = types.InlineKeyboardMarkup(row_width=2)

    russian = types.InlineKeyboardButton(
        "Русский🇷🇺", callback_data='russian')
    english = types.InlineKeyboardButton(
        "English🇺🇸", callback_data='english')
    armenian = types.InlineKeyboardButton("Armenia🇦🇲", callback_data='armenia')

    markup.add(russian, english, armenian)

    bot.send_message(
        message.chat.id, "select the language", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def bot_answer(message):
    #global language_change , language
    status = get_status_by_user_id(message.from_user.id)
    print(statuses)
    if status[1]:
        if message.data == "russian":
            status[0] = "russian"
        elif message.data == "english":
            status[0] = "english"
        elif message.data == "armenia":
            status[0] = "armenia"
        status[1] = False 

        set_status_by_user_id(message.from_user.id, status)
        
    if status[0] == 'russian':
        rus.russian(bot,message)
    elif status[0] == 'english':
        eng.english(bot,message)
    elif status[0] == 'armenia':
        arm.armenia(bot,message)

bot.polling(non_stop=True)