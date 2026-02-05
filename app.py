import datetime
import os
from flask import Flask
import random
import re

app = Flask(__name__)
cars = ['Chevrolet, Renault, Ford, Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
count = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

@app.route('/')
def test_function():
    return f'OK'

@app.route('/hello_world')
def hello_function():
    return f'Привет мир!'

@app.route('/cars')
def cars_function():
    return ",".join(cars)

@app.route('/cats')
def cats_function():
    return random.choice(cats)

@app.route('/get_time/now')
def time_function():
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second
    current_time = f'{hours}:{minutes}:{seconds}'
    return f'Точное время: {current_time}'

@app.route('/get_time/future')
def time_future_function():
    now = datetime.datetime.now()
    time_after_hour = now + datetime.timedelta(0,0,0,0,0,1)
    hours = time_after_hour.hour
    minutes = time_after_hour.minute
    seconds = time_after_hour.second
    current_time_after_hour = f'{hours}:{minutes}:{seconds}'
    return f'Точное время через час будет: {current_time_after_hour}'

#Читает файл, находит в нем все слова и возвращает их в виде списка.    
def get_words_from_file(path):    
    try:
        with open(path, 'r', encoding='utf-8') as book:
            text = book.read()
            words = re.findall(r'\w+', text)
            return words
    except FileNotFoundError:
        return []
    
WAR_AND_PEACE_WORDS = get_words_from_file(BOOK_FILE)

@app.route('/get_random_word')
def rand_word_function():        
    # Выбираем случайное слово
    word = random.choice(WAR_AND_PEACE_WORDS)
    return f"Случайное слово из книги: {word}"

@app.route('/counter')
def counter():
    global count
    count += 1
    return f'Количество открытий страницы: {count} '



if __name__ == '__main__':
    app.run(debug=True)