import os
import sqlite3
# .env Support
from dotenv import load_dotenv
# Telegram Bot API
import telebot

# Consts
load_dotenv()
TOKEN = os.getenv("TOKEN")
DB_File = os.getenv("DB")
Users=[]

def write_dict_to_json(dictionary, filename):
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)
def read_json_to_dict(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def DB_Check_table(name):
    conn = sqlite3.connect(DB_File)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Run bot handler
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def start(message):
    DB_Check_table(message.chat.username)
    bot.reply_to(message, f'Hi {message.chat.first_name}, use menu to see commands.')

@bot.message_handler(commands=['add'])
def add(message):
    DB_Check_table(message.chat.username)
    args = message.text.split(" ")[1:]
    #if len(args).
    bot.reply_to(message, f'Args: {args}')

@bot.message_handler(commands=['buttons'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()

    button1 = telebot.types.InlineKeyboardButton(text='Мани ведёт То искать краба.', callback_data='button1')
    button2 = telebot.types.InlineKeyboardButton(text='Мани рада.', callback_data='button2')
    button3 = telebot.types.InlineKeyboardButton(text='То рад.', callback_data='button3')
    button4 = telebot.types.InlineKeyboardButton(text='Мани привела То на поле.', callback_data='button4')

    markup.add(button1, button2)
    markup.add(button3, button4)

    bot.send_message(message.chat.id, "มานีคีใจ", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, "You pressed Button 1")
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, "You pressed Button 2")
    elif call.data == 'button3':
        bot.send_message(call.message.chat.id, "You pressed Button 3")
    elif call.data == 'button4':
        bot.send_message(call.message.chat.id, "You pressed Button 4")

bot.infinity_polling()
