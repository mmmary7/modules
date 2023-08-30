import telebot
import requests
from bs4 import BeautifulSoup
import random

token = "5806578008:AAEez5KCA9bIEBNKdn1g3hpUSmTLROJszuE"
bot = telebot.TeleBot(token)


# декоратор статик метод ещё есть
# def my_decorator(func_to_decorator):
#     def decorator_func():
#         print('Я начинаю работать')
#         func_to_decorator()
#         print('Я отработал!')
#
#     return decorator_func()
#
#
# @my_decorator
# def my_func():
#     print('Я работаю')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome = """ Привет! Я умею рассказывать стихи, знаю много красивых цитат и могу показывать милых котиков)"""
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton("Котики")
    button2 = telebot.types.KeyboardButton("Музыка")
    button3 = telebot.types.KeyboardButton("Стих")
    button4 = telebot.types.KeyboardButton("Цитата")
    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, welcome, reply_markup=keyboard)




@bot.message_handler(commands=['poem'])
def send_poem(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button_inline = telebot.types.InlineKeyboardButton("Больше стихотворений здесь", url="https://stihi.ru/")
    keyboard.add(button_inline)
    bot.send_message(message.chat.id, "Муха села на варенье, вот и всё стихотворенье.", reply_markup=keyboard)


@bot.message_handler(commands=['phrase'])
def send_phr(messange):
    per = requests.get('https://wikiphile.ru/570-fraz-o-motivacii/')
    per = per.content
    soup = BeautifulSoup(per, 'lxml')
    phr = random.choice(soup.find_all('li'))
    phr_text = phr
    bot.send_message(messange.chat.id, phr_text)


@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_img = open('cat' + str(random.randint(1, 3)) + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)


@bot.message_handler(commands=['audio'])
def send_song(message):
    songs = ['ABBA', 'Bon_Jovi', 'Dean_Martin']
    song = open(random.choice(songs)+".mp3", 'rb')
    bot.send_audio(message.chat.id, song)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.strip() == "Музыка":
        send_song(message)
    elif message.text.strip() == "Котики":
        send_cat(message)
    elif message.text.strip() == "Цитата":
        send_phr(message)
    elif message.text.strip() == "Стих":
        send_poem(message)


bot.polling()
