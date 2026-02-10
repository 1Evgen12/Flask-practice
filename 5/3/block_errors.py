"""
Реализуйте контекстный менеджер, который будет игнорировать переданные типы исключений, возникающие внутри блока with.
Если выкидывается неожидаемый тип исключения, то он прокидывается выше.
"""

from typing import Collection, Type, Literal
from types import TracebackType


class BlockErrors:
    def __init__(self, errors: Collection) -> None:
        self.errors_to_block = errors

    def __enter__(self) -> None:
        pass

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        # Если исключения не было (None), просто выходим
        if exc_type is None:
            return None

        # Проверяем, есть ли тип исключения в нашей коллекции для игнорирования
        if exc_type in self.errors_to_block:
            print(f"Исключение типа '{exc_type.__name__}' было проигнорировано.")
            # Возвращаем True, чтобы исключение было подавлено
            return True
        else:
            # Если тип исключения не в нашем списке,
            # оставляем его не обработанным (возвращаем None)
            # и оно будет проброшено выше.
            print(f"Исключение типа '{exc_type.__name__}' НЕ было проигнорировано и будет проброшено.")
            return None
