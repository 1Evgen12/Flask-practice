"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):

    def _number_length(form: FlaskForm, field: Field):
        if field.data is None:
            return

        value = str(field.data)

        if not value.isdigit():
            raise ValidationError(message or "Введите число")

        length = len(value)

        if length < min or length > max:
            raise ValidationError(
                message or f"Введите от 1 до 10 цифр"
            )
    return _number_length


class NumberLength:
    def init(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def call(self, form: FlaskForm, field: Field):
        if field.data is None:
            return

        value = str(field.data)

        if not value.isdigit():
            raise ValidationError(self.message or "Введите число")

        length = len(value)

        if length < self.min or length > self.max:
            raise ValidationError(
                self.message or f"Введите от 1 до 10 цифр"
            )