import unittest
from accounting import app, storage, add

class TestFinanceApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #Заполняем storage изначальными данными один раз для всех тестов
        storage.update({
            2020: {1: 1000, 2: 2000},
            2021: {12: 5000}
        })

    def setUp(self):
        #Настройка перед каждым тестом
        app.config["TESTING"] = True
        self.client = app.test_client()

    # ТЕСТЫ ДЛЯ /add/

    def test_add_success(self):
        #Проверка успешного добавления
        response = self.client.get("/add/20220101/500")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Добавлено 500 рублей", response.data.decode())
        self.assertEqual(storage[2022][1], 500)

    def test_add_accumulation(self):
        #Проверка суммирования данных при добавлении в тот же месяц
        self.client.get("/add/20200101/500") # В 2020.01 уже было 1000
        self.assertEqual(storage[2020][1], 1500)

    def test_add_invalid_date_format_fails(self):
        #Проверка, что некорректная дата вызывает ошибку (ValueError)
        with self.assertRaises(ValueError):
            add("notdate", 100)

    # ТЕСТЫ ДЛЯ /calculate/<year>

    def test_calculate_year_success(self):
        #Проверка расчета за существующий год
        response = self.client.get("/calculate/2020")
        # 1000 (январь) + 2000 (февраль) + 500 (из теста выше) = 3500
        self.assertIn("Потрачено за 2020 год 3500 рублей", response.data.decode())

    def test_calculate_year_not_found(self):
        #Проверка расчета за отсутствующий год
        response = self.client.get("/calculate/1999")
        self.assertIn("1999г. не найден", response.data.decode())

    def test_calculate_year_after_new_add(self):
        #Проверка изменения суммы года после добавления нового месяца
        self.client.get("/add/20210505/1000")
        response = self.client.get("/calculate/2021")
        # Было 5000 в декабре + 1000 в мае = 6000
        self.assertIn("6000", response.data.decode())

    # ТЕСТЫ ДЛЯ /calculate/<year>/<month>

    def test_calculate_month_success(self):
        #Проверка расчета за конкретный месяц
        response = self.client.get("/calculate/2021/12")
        self.assertIn("Потрачено за 12 месяц 2021 года: 5000 рублей", response.data.decode())

    def test_calculate_month_not_found(self):
        #Проверка при отсутствии месяца в году
        response = self.client.get("/calculate/2021/1")
        self.assertIn("не найдено", response.data.decode())

    def test_calculate_month_invalid_types(self):
        #Проверка, что при строковых данных вместо чисел сервер вернет 404 (Flask routing)
        response = self.client.get("/calculate/year/month")
        self.assertEqual(response.status_code, 404)

    # ТЕСТЫ С ПУСТЫМ STORAGE

    # def test_calculate_year_empty_storage(self):
    #     #Проверка /calculate/year, когда данных нет
    #     storage.clear()
    #     response = self.client.get("/calculate/2020")
    #     self.assertIn("2020г. не найден", response.data.decode())
    #
    # def test_calculate_month_empty_storage(self):
    #     #Проверка /calculate/year/month, когда данных нет
    #     storage.clear()
    #     response = self.client.get("/calculate/2020/1")
    #     self.assertIn("не найдено", response.data.decode())
    #
    # def test_add_to_empty_storage(self):
    #     #Проверка, что /add корректно создает структуру в пустом хранилище
    #     storage.clear()
    #     self.client.get("/add/20241010/777")
    #     self.assertEqual(storage[2024][10], 777)

if __name__ == "__main__":
    unittest.main()
