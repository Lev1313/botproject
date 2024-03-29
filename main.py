# -*- coding: utf8 -*-
import telebot
import requests
import time
import random
# Указываем токен

bot = telebot.TeleBot('1592617905:AAEt8WNuHnMWChAGUfW_aOGFab269DNGwjk', threaded=False)
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «start»
    if message.text == "/start":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='Aries')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='Taurus')
        keyboard.add(key_telec)

        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='Gemini')
        keyboard.add(key_bliznecy)

        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='Cancer')
        keyboard.add(key_rak)

        key_lev = types.InlineKeyboardButton(text='лев', callback_data='Leo')
        keyboard.add(key_lev)

        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='Virgo')
        keyboard.add(key_deva)

        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='Libra')
        keyboard.add(key_vesy)

        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='Scorpio')
        keyboard.add(key_scorpion)

        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='Sagittarius')
        keyboard.add(key_strelec)

        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='Capricorn')
        keyboard.add(key_kozerog)

        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='Aquarius')
        keyboard.add(key_vodoley)

        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='Pisces')
        keyboard.add(key_ryby)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "Pisces":
        answ = requests.get('https://ohmanda.com/api/horoscope/pisces/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Aries":
        answ = requests.get('https://ohmanda.com/api/horoscope/aries/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Taurus":
        answ = requests.get('https://ohmanda.com/api/horoscope/taurus/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Gemini":
        answ = requests.get('https://ohmanda.com/api/horoscope/gemini/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Cancer":
        answ = requests.get('https://ohmanda.com/api/horoscope/cancer/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Leo":
        answ = requests.get('https://ohmanda.com/api/horoscope/leo/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Virgo":
        answ = requests.get('https://ohmanda.com/api/horoscope/virgo/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Libra":
        answ = requests.get('https://ohmanda.com/api/horoscope/libra/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Scorpio":
        answ = requests.get('https://ohmanda.com/api/horoscope/scorpio/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Sagittarius":
        answ = requests.get('https://ohmanda.com/api/horoscope/sagittarius/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Capricorn":
        answ = requests.get('https://ohmanda.com/api/horoscope/capricorn/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Aquarius":
        answ = requests.get('https://ohmanda.com/api/horoscope/aquarius/').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])


# Запускаем постоянный опрос бота в Телеграме
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
