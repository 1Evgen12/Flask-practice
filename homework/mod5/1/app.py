"""
Консольная утилита lsof (List Open Files) выводит информацию о том, какие файлы используют какие-либо процессы.
Эта команда может рассказать много интересного, так как в Unix-подобных системах всё является файлом.

Но нам пока нужна лишь одна из её возможностей.
Запуск lsof -i :port выдаст список процессов, занимающих введённый порт.
Например, lsof -i :5000.

Как мы с вами выяснили, наш сервер отказывается запускаться, если кто-то занял его порт. Напишите функцию,
которая на вход принимает порт и запускает по нему сервер. Если порт будет занят,
она должна найти процесс по этому порту, завершить его и попытаться запустить сервер ещё раз.
"""
from typing import List

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Сервер запущен!"

def get_pids(port: int) -> List[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError

    pids: List[int] = []
    try:
        # Запускаем lsof. Флаг -t выводит только PIDы по одному в строке.
        result = subprocess.run(
            ["lsof", "-i", f":{port}", "-t"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout.strip()
        if output:
            # Превращаем строки с PID в список целых чисел
            pids = [int(pid) for pid in output.splitlines()]

    except Exception as e:
        print(f"Ошибка при поиске процессов: {e}")
    return pids


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: List[int] = get_pids(port)
    for pid in pids:
        try:
            # signal.SIGKILL — это аналог команды kill -9
            # Завершаем процесс принудительно
            os.kill(pid, signal.SIGKILL)
            print(f"Процесс {pid}, занимавший порт {port}, был завершен.")
        except OSError:
            # Бывает, что процесс уже закрылся сам
            print(f"Не удалось завершить процесс {pid}.")


def run(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)
