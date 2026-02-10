from block_errors import BlockErrors

print("Пример 1")
err_types = {ZeroDivisionError, TypeError}
with BlockErrors(err_types):
    a = 1 / 0
print("Выполнено без ошибок\n")

print("Пример 2")
err_types = {ZeroDivisionError}
try:
    with BlockErrors(err_types):
        a = 1 / '0'
except TypeError as e:
    print("Поймано исключение:", e)
print("Демонстрация завершена\n")

print("Пример 3")
outer_err_types = {TypeError}
with BlockErrors(outer_err_types):
    inner_err_types = {ZeroDivisionError}
    with BlockErrors(inner_err_types):
        a = 1 / '0'
    print("Внутренний блок: выполнено без ошибок")
print("Внешний блок: выполнено без ошибок\n")

print("Пример 4")
err_types = {Exception}
with BlockErrors(err_types):
    a = 1 / '0'
print("Выполнено без ошибок")