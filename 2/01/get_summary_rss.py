def get_summary_rss(file_path):
    total_rss = 0

    with open(file_path, 'r') as output_file:
        # Пропускаем заголовок и читаем остальные строки
        lines = output_file.readlines()[1:]

        for line in lines:
            columns = line.split()
            if len(columns) > 1:  # Проверяем, что строка корректная
                try:
                    rss = int(columns[5])  # Столбец RSS находится на 6-й позиции (индекс 5)
                    total_rss += rss
                except ValueError:
                    continue  # Игнорируем строки с некорректными данными

    # Преобразуем в человекочитаемый формат
    if total_rss < 1024:
        return f"{total_rss} B"
    elif total_rss < 1024 ** 2:
        return f"{total_rss / 1024:.2f} KB"
    elif total_rss < 1024 ** 3:
        return f"{total_rss / (1024 ** 2):.2f} MB"
    elif total_rss < 1024 ** 4:
        return f"{total_rss / (1024 ** 3):.2f} GB"
    else:
        return f"{total_rss / (1024 ** 4):.2f} TB"


if __name__ == "__main__":
    file_path = "output_file.txt"  # Путь к файлу с результатами ps aux
    summary_rss = get_summary_rss(file_path)
    print(f"Суммарный объём потребляемой памяти: {summary_rss}")
