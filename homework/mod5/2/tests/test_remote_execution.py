import unittest

from flask import json

from remote_execution import app

def setUp(self):
    """Настройка тестового клиента перед каждым тестом"""
    app.config['TESTING'] = True
    # FlaskForm требует SECRET_KEY для CSRF защиты, даже в тестах
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SECRET_KEY'] = 'test_secret_key'
    self.client = app.test_client()


def test_successful_code_execution(self):
    """Тест на успешное выполнение простого кода"""
    code_to_run = "print('Hello, World!')"
    timeout_val = 5  # Секунды

    response = self.client.post(
        '/run_code',
        data={'code': code_to_run, 'timeout': timeout_val},
        follow_redirects=True  # Чтобы отслеживать редиректы, если есть
    )

    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertIn('stdout', data)
    self.assertIn('stderr', data)
    self.assertEqual(data['stdout'].strip(), 'Hello, World!')
    self.assertEqual(data['stderr'].strip(), '')


def test_timeout_expired(self):
    """Тест на превышение времени выполнения"""
    # Код, который будет выполняться дольше, чем timeout
    code_to_run = "import time; time.sleep(2)"
    timeout_val = 1  # Устанавливаем таймаут меньше времени выполнения

    response = self.client.post(
        '/run_code',
        data={'code': code_to_run, 'timeout': timeout_val},
        follow_redirects=True
    )

    self.assertEqual(response.status_code, 408)  # 408 Request Timeout
    data = json.loads(response.data)
    self.assertIn('error', data)
    self.assertEqual(data['error'], 'Execution time exceeded')


if __name__ == '__main__':
    unittest.main()
