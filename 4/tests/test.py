"""
Для каждого поля и валидатора в эндпоинте /registration напишите юнит-тест,
который проверит корректность работы валидатора. Таким образом, нужно проверить, что существуют наборы данных,
которые проходят валидацию, и такие, которые валидацию не проходят.
"""


import unittest
from app import app

class TestRegistrationValidators(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        cls.client = app.test_client()

    def post(self, data: dict):
        return self.client.post("/registration", data=data)

    # EMAIL
    def test_email_valid(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 200)

    def test_email_invalid(self):
        response = self.post({
            "email": "not-an-email",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 400)

    # PHONE

    def test_phone_valid(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 200)

    def test_phone_too_short(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "123",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 400)

    # NAME

    def test_name_valid(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 200)

    def test_name_missing(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 400)

    # ADDRESS

    def test_address_valid(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 200)

    def test_address_missing(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 400)

    # INDEX

    def test_index_valid(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 200)

    def test_index_invalid(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "ABC"
        })
        self.assertEqual(response.status_code, 400)

    # COMMENT (OPTIONAL)

    def test_comment_optional(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456",
            "comment": "hello"
        })
        self.assertEqual(response.status_code, 200)

    def test_comment_missing(self):
        response = self.post({
            "email": "test@test.com",
            "phone": "9991234567",
            "name": "Ivan",
            "address": "Moscow",
            "index": "123456"
        })
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()

