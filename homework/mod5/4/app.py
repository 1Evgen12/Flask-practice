import sys
from redirect import Redirect

print("Hello stdout")

# создаём файлы для перенаправления
stdout_file = open("stdout.txt", "w")
stderr_file = open("stderr.txt", "w")

try:
    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print("Hello stdout.txt")
        raise Exception("Hello stderr.txt")
except Exception:
    # traceback записан в stderr_file автоматически
    pass

# закрываем файлы
stdout_file.close()
stderr_file.close()

print("Hello stdout again")

# исключение на экран (обычный stderr)
raise Exception("Hello stderr")