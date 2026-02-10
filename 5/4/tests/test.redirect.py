import traceback
import unittest
import sys
import io
from redirect import Redirect

class TestRedirectManager(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.stdout_capture = io.StringIO()
        self.stderr_capture = io.StringIO()

    def tearDown(self):
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

    def test_redirect_stdout_only(self):
        with Redirect(stdout=self.stdout_capture):
            print("This should go to stdout_capture")
            print("Another line for stdout")
            sys.stderr.write("This should go to original stderr\n")
        # Проверяем, что stdout перенаправился
        self.assertIn("This should go to stdout_capture", self.stdout_capture.getvalue())
        self.assertIn("Another line for stdout", self.stdout_capture.getvalue())
        self.assertNotIn("This should go to original stderr", self.stdout_capture.getvalue())

    def test_redirect_stderr_only(self):
        with Redirect(stderr=self.stderr_capture):
            print("This should go to original stdout")
            sys.stderr.write("This should go to stderr_capture\n")
            sys.stderr.write("Another line for stderr\n")
        # Проверяем, что stderr перенаправился
        self.assertIn("This should go to stderr_capture", self.stderr_capture.getvalue())
        self.assertIn("Another line for stderr", self.stderr_capture.getvalue())
        # Проверяем, что stdout остался оригинальным
        self.assertNotIn("This should go to original stdout", self.stderr_capture.getvalue())

    def test_redirect_both(self):
        # Открываем файлы для записи
        stdout_file = io.StringIO()
        stderr_file = io.StringIO()

        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print("Hello stdout.txt")
            sys.stderr.write("Hello stderr.txt\n")
            print("Another stdout line")
            sys.stderr.write("Another stderr line\n")
            try:
                raise Exception("Simulated Exception")
            except Exception:
                # Исключение должно быть записано в stderr_file
                sys.stderr.write(traceback.format_exc())

        # Проверяем содержимое stdout_file
        self.assertIn("Hello stdout.txt", stdout_file.getvalue())
        self.assertIn("Another stdout line", stdout_file.getvalue())
        self.assertNotIn("Hello stderr.txt", stdout_file.getvalue())

        # Проверяем содержимое stderr_file
        self.assertIn("Hello stderr.txt", stderr_file.getvalue())
        self.assertIn("Another stderr line", stderr_file.getvalue())
        self.assertIn("Simulated Exception", stderr_file.getvalue())  # Проверяем, что traceback попал сюда

    def test_redirect_no_args(self):
        with Redirect():
            print("This should go to original stdout")
            sys.stderr.write("This should go to original stderr\n")
        self.assertNotIn("This should go to original stdout", self.stdout_capture.getvalue())
        self.assertNotIn("This should go to original stderr", self.stderr_capture.getvalue())



