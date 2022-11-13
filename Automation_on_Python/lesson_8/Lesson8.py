# Библиотека Requests
# API (Application programming interface) —  описание способов, которыми одна компьютерная программа может
# взаимодействовать с другой программой.

# https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html
import requests

response = requests.get(
    'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(response.content)

# Узнаем статус полученного ответа
response = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
print(response.status_code)

# Обращаемся к api json

r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
print(r.content)

# Трансформируем полученный текст в список
import json

response = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(response.content)
print(type(texts))  # проверяем тип

for text in texts:  # выводим полученный текст. Для более лаконичного отображения, оставим только первые 150 символов.
    print(text[:150], '\n')

# Возвращаемый тип, похожий на Словарь
# import requests
# import json

response = requests.get('https://api.github.com')
print(response.content)

# Тип Словарь
# import requests
# import json
response = requests.get('https://api.github.com')
d = json.loads(response.content)
print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту, как к словарю и выводим в консоль одно из его значений

# Post запрос
# import requests

response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.content)

# Меняем формат на json

data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=json.dumps(data))
print(response.content)

# Создание Telegram-бота

# Наберите в ТГ @BotFather и следуйте инструкциям:
# /newbot
#  Узнать подробности можно здесь:
# Чат
# Поле	                                                                                Описание
# id	                                                                    Уникальный идентификатор данного чата
# type	                                              Тип чата может быть «private», «group», «supergroup» or «channel»
# username	            Необязательное поле. Имя пользователя для приватных чатов, супергрупп и каналов, если доступно

# Сообщение
#
# Поле	                                                                                Описание
# message_id	                                                     Уникальный идентификатор сообщения в данном чате
# from	            Необязательное поле. Отправитель сообщения. Если сообщение отправлено каналом, то поле будет пустым
# date	                                                             Дата отправки сообщения в Unix-формате
# chat	                                                             Чат, куда было отправлено сообщение
# text	                                                             Необязательное поле. Текст сообщения

# Контент:
# audio — аудиозапись
# photo — фотография, картинка
# voice — голосовое сообщение
# video — видеозапись
# document — документ
# text — текстовое сообщение
# location — геолокация
# contact — контакт
# sticker — стикер

# pip3 install pyTelegramBotAPI

# Обработчик сообщений — это функция, которая будет выполняться при получении определённого сообщения.

# filters — фильтры, определяющие, надо ли вызывать декорированную функцию для соответствующего сообщения или нет.
# У одного обработчика может быть несколько фильтров.

# Название фильтра	                       Аргумент	                             Условие выполнения функции
# content_types	            Список строк, по умолчанию ['text']	       Если тип контента, содержащегося в сообщении,
#                                                                         совпадает с типом, указанным в качестве
#                                                                        аргумента. То есть обработчик по умолчанию
#                                                                        реагирует на все текстовые сообщения.
# commands	                              Список строк	              Если сообщение начинается с команды,
#                                                                       указанной в списке

import telebot

TOKEN = "5681702926:AAGKeRoV7W8g7E8C-MwUQj6l25iPfP7ZW8Q"
bot = telebot.TeleBot(TOKEN)
bot.polling(none_stop=True)


@bot.message_handler(filters)  # Добавляем декоратор
def function_name(message):
    bot.reply_to(message, "This is a message handler")

# Кэширование в Python
# Последовательность Фибоначчи: fib(5) = fib(4) + fib(3)
# Переходим в файл Cash.py

# python -m venv venv
# venv\scripts\activate
# pip3 install pyTelegramBot API
# pip3 install requests
