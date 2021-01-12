# -*- coding: utf8 -*-
import telebot
import requests
import random
# Указываем токен
bot = telebot.TeleBot('1592617905:AAEt8WNuHnMWChAGUfW_aOGFab269DNGwjk')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
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
        answ = requests.get('http://ohmanda.com/api/horoscope/pisces').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Aries":
        answ = requests.get('http://ohmanda.com/api/horoscope/Aries').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Taurus":
        answ = requests.get('http://ohmanda.com/api/horoscope/Taurus').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Gemini":
        answ = requests.get('http://ohmanda.com/api/horoscope/Gemini').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Cancer":
        answ = requests.get('http://ohmanda.com/api/horoscope/Cancer').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Leo":
        answ = requests.get('http://ohmanda.com/api/horoscope/Leo').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Virgo":
        answ = requests.get('http://ohmanda.com/api/horoscope/Virgo').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Libra":
        answ = requests.get('http://ohmanda.com/api/horoscope/Libra').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Scorpio":
        answ = requests.get('http://ohmanda.com/api/horoscope/Scorpio').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Sagittarius":
        answ = requests.get('http://ohmanda.com/api/horoscope/Sagittarius').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Capricorn":
        answ = requests.get('http://ohmanda.com/api/horoscope/Capricorn').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])

    elif call.data == "Aquarius":
        answ = requests.get('http://ohmanda.com/api/horoscope/Aquarius').json()
        bot.send_message(call.message.chat.id, answ['horoscope'])


# Запускаем постоянный опрос бота в Телеграме
def telegram_polling():
    try:
        bot.polling(none_stop=True, timeout=60) #constantly get messages from Telegram
    except:
        traceback_error_string=traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

if __name__ == '__main__':
    telegram_polling()