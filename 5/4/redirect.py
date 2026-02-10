import sys
import traceback

class Redirect:
    def __init__(self, *, stdout=None, stderr=None):
        self.new_stdout = stdout
        self.new_stderr = stderr

    def __enter__(self):
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

        if self.new_stdout:
            sys.stdout = self.new_stdout
        if self.new_stderr:
            sys.stderr = self.new_stderr

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Сначала пишем traceback в переданный stderr, если есть исключение
        if exc_type is not None and self.new_stderr is not None:
            self.new_stderr.write(''.join(traceback.format_exception(exc_type, exc_val, exc_tb)))
            self.new_stderr.flush()

        # Потом восстанавливаем старые потоки
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

        # Прокидываем исключение дальше (тесты ждут, что они могут делать try/except)
        return False