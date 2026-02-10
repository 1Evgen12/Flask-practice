"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""
import subprocess

from flask import Flask, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[DataRequired()])
    timeout = IntegerField("Timeout", validators=[DataRequired(), NumberRange(min=1, max=30)])


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()

    if not form.validate_on_submit():
        return jsonify({"error": "Invalid input"}), 400

    code = form.code.data
    timeout = form.timeout.data

    cmd = [
        "prlimit",
        "--nproc=1:1",
        "python3",
        "-c",
        code
    ]
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(timeout=timeout)
        return jsonify({
            "stdout": stdout,
            "stderr": stderr
        })
    except subprocess.TimeoutExpired:
        process.kill()
        return jsonify({
            "error": "Execution time exceeded"
        }), 408


if __name__ == '__main__':
    app.run(debug=True)
