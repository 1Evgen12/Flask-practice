import unittest
from block_errors import BlockErrors

class TestBlockErrors(unittest.TestCase):

    # --- Тесты для случая "Ошибка игнорируется" ---
    def test_error_is_ignored_valueerror(self):
        """Пример 1: ValueError игнорируется, код продолжает выполняться."""
        err_types = {ValueError}
        with BlockErrors(err_types):
            raise ValueError("This is a ValueError")
        # Если мы дошли сюда, значит, исключение было проигнорировано.
        self.assertTrue(True, "Дошли до конца, исключение было проигнорировано")

    def test_error_is_ignored_zero_division(self):
        err_types = {ZeroDivisionError}
        with BlockErrors(err_types):
            a = 1 / 0
        self.assertTrue(True, "ZeroDivisionError был проигнорирован")

    def test_error_is_ignored_exception_parent(self):
        """Игнорируем базовый Exception, дочерние тоже игнорируются."""
        err_types = {Exception}
        with BlockErrors(err_types):
            a = 1 / '0'  # Это вызовет TypeError
        self.assertTrue(True, "TypeError (наследник Exception) был проигнорирован")

    def test_error_is_re_raised_typeerror(self):
        """TypeError прокидывается, так как не указан для игнорирования."""
        err_types = {ZeroDivisionError}  # Игнорируем только ZeroDivisionError
        with self.assertRaises(TypeError):  # Ожидаем, что TypeError будет пойман снаружи
            with BlockErrors(err_types):
                a = 1 / '0'  # Это вызовет TypeError
        # Если мы дошли сюда, значит, assertRaises сработал, т.е. TypeError прокинулся.

    def test_nested_blocks_inner_re_raised_outer_ignored(self):
        outer_err_types = {TypeError}  # Внешний блок игнорирует TypeError
        with BlockErrors(outer_err_types):
            inner_err_types = {ZeroDivisionError}  # Внутренний блок игнорирует ZeroDivisionError
            with BlockErrors(inner_err_types):
                print("Внутри внутреннего блока: вызываем TypeError")
                raise TypeError("Inner TypeError")  # Этот TypeError должен быть пойман внешним блоком
            print("После внутреннего блока (если не было исключения)")
        self.assertTrue(True, "Внешний блок успешно проигнорировал TypeError")


if __name__ == '__main__':
    unittest.main()
