import sys

def get_mean_size(ls_output: str) -> float:
    lines = ls_output.strip().split('\n')[1:]  # Пропускаем первую строку (заголовок)

    total_size = 0
    file_count = 0

    for line in lines:
        parts = line.split()
        if len(parts) > 8:  # Проверяем, что строка корректная и содержит информацию о размере
            try:
                size = int(parts[4])
                total_size += size
                file_count += 1
            except ValueError:
                continue

    if file_count == 0:
        return 0.0  # Если файлов нет, возвращаем 0.0

    mean_size = total_size / file_count
    return mean_size


if __name__ == "__main__":
    data: str = sys.stdin.read()  # Читаем входные данные
    mean_size: float = get_mean_size(data)  # Вычисляем средний размер
    print(mean_size)  # Выводим результат

