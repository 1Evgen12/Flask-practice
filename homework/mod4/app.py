"""
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

1) email (текст, обязательно для заполнения, валидация формата);
2) phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
3) name (текст, обязательно для заполнения);
4) address (текст, обязательно для заполнения);
5) index (только числа, обязательно для заполнения);
6) comment (текст, необязательно для заполнения).
"""
import subprocess

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange
from hw2_validators import number_length, NumberLength

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(message="Введите email"), Email(message="Неверный формат email")])
    #phone = IntegerField(validators=[InputRequired(message="Введите номер телефона"),  NumberRange(min=1000000000, max=9999999999, message="Телефон должен содержать 10 цифр")])
    phone = IntegerField(validators=[InputRequired(message="Введите номер телефона"),
                         number_length(min=1, max=10, message="Телефон должен содержать 10 цифр")])
    name = StringField(validators=[InputRequired(message="Введите имя")])
    address = StringField(validators=[InputRequired(message="Введите адрес")])
    index = IntegerField(validators=[InputRequired(message="Введите индекс"), NumberRange(min=1, message="Введите число")])

@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400

@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    result = subprocess.run(
        ["uptime", "-p"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    uptime_str = result.stdout.strip()

    if uptime_str.startswith("up "):
        uptime_str = uptime_str[3:]

    return f"Текущее время безотказной работы составляет {uptime_str}"

@app.route("/ps", methods=["GET"])
def ps():
    errors = []
    # получаем аргументы списком
    args = request.args.getlist("arg")
    if not args:
        errors.append("Нет аргумента")
    if errors:
        return {"errors": errors}, 400
    # формируем команду без shell=True
    command = ["ps"] + args
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except Exception as e:
        return {"errors": [str(e)]}, 400

    if result.stderr:
        return {"errors": [result.stderr]}, 400

    return f"<pre>{result.stdout}</pre>"

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
