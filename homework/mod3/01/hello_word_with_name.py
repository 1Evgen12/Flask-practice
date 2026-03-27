"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""
import datetime
from flask import Flask

weekdays_tuple = ('Понедельника','Вторника','Среды','Четверга','Пятницы','Субботы','Воскресенья')
app = Flask(__name__)

@app.route('/hello-world/<name>')
def hello_world(name):
    number = datetime.date.today().weekday()
    weekday = weekdays_tuple[number]
    return f'Привет, {name}. {weekday}!'



if __name__ == '__main__':
    app.run(debug=True)