"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask, abort

app = Flask(__name__)

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    try:
        number_list = [int(num) for num in numbers.split('/')]
    except ValueError:
        # Если возникла ошибка преобразования, возвращаем 400 Bad Request
        abort(400, description="Все переданные значения должны быть целыми числами.")

    max_num = max(number_list)

    return f"Максимальное переданное число {{ <i>{max_num}</i> }}"

if __name__ == '__main__':
    app.run(debug=True)



