"""
Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) и RELATIVE_PATH —
и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.
В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах,
а во второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

docs/simple.txt:
hello world!

/preview/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/preview/100/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
"""

from flask import Flask, abort
import os

app = Flask(__name__)

@app.route("/preview/<path:relative_path>")
@app.route("/preview/<int:size>/<path:relative_path>")
def head_file(relative_path: str, size: int=None):
    # Получаем абсолютный путь к файлу
    abs_path = os.path.abspath(relative_path)

    # Проверяем, существует ли файл и является ли он файлом
    if not os.path.isfile(abs_path):
        abort(404, description="Файл не найден.")

    # Читаем содержимое файла
    with open(abs_path, 'r', encoding='utf-8') as file:
        if size is None:
            content = file.read()  #Если size не указан читаем весь файл
        else:
            content = file.read(size)  #Иначе считываем первые size символов

    # Получаем размер считанного текста
    result_size = len(content)

    # Формируем ответ в виде HTML
    response = f"<b>{abs_path}</b> {result_size}<br>{content}"

    return response

if __name__ == "__main__":
    app.run(debug=True)
