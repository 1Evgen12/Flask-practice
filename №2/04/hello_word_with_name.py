"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""
import datetime
import sys
from flask import Flask

weekdays_tuple = ('Понедельника','Вторника','Среды','Четверга','Пятницы','Субботы','Воскресенья')
word_tuple= ('Хорошего', 'Хорошей')
app = Flask(__name__)

@app.route('/hello-world/<name>')
def hello_world(name):
    number = datetime.date.today().weekday()
    if (number == 0 or number == 1 or number ==3 or number ==6):
        word = word_tuple[0]
    else:
        word = word_tuple[1]

    weekday = weekdays_tuple[number]
    return f'Привет, {name}. {word} {weekday}!'



if __name__ == '__main__':
    app.run(debug=True)