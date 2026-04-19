from functools import reduce
from itertools import zip_longest
from typing import Iterable, Any, Callable, Union

def merge_sequences(seq1: Iterable, seq2: Iterable, strategy: str = 'zip') -> Iterable:
    """
    Генератор, объединяющий две последовательности по заданной стратегии.

    Стратегии:
    - 'zip'       : поочередно выдаёт элементы из обеих последовательностей,
                    пока хватает более короткой.
    - 'chain'     : сначала все элементы первой последовательности,
                    затем все элементы второй.
    - 'interleave': чередует элементы, пока есть хотя бы в одной из последовательностей.
    """
    if strategy == 'zip':
        for a, b in zip(seq1, seq2):
            yield a
            yield b
    elif strategy == 'chain':
        yield from seq1
        yield from seq2
    elif strategy == 'interleave':
        for a, b in zip_longest(seq1, seq2, fillvalue=None):
            if a is not None:
                yield a
            if b is not None:
                yield b
    else:
        raise ValueError(f"Неизвестная стратегия: {strategy}")

def reduce_by_type(sequence: Iterable) -> Any:
    """
    Сворачивает последовательность в одно значение в зависимости от типа её элементов.
    Поддерживаемые типы и действия:
    - int   : сумма
    - str   : конкатенация
    - list  : объединение списков
    - tuple : объединение кортежей
    - bool  : логическое И (all)
    - прочие: возвращаются в виде списка (без свёртки)
    """
    items = list(sequence)
    if not items:
        return None

    elem_type = type(items[0])
    # Проверяем, что все элементы одного типа (для корректной свёртки)
    if not all(isinstance(x, elem_type) for x in items):
        # Если типы различаются – просто возвращаем список
        return items

    if elem_type is int:
        return reduce(lambda x, y: x + y, items)
    elif elem_type is str:
        return reduce(lambda x, y: x + y, items)
    elif elem_type is list:
        return reduce(lambda x, y: x + y, items)
    elif elem_type is tuple:
        return reduce(lambda x, y: x + y, items)
    elif elem_type is bool:
        return reduce(lambda x, y: x and y, items)
    else:
        # Для пользовательских типов или других встроенных – просто список
        return items

# -------------------------------------------------------------------
# Пример использования (демонстрирует применение filter и reduce)
if __name__ == "__main__":
    # Пример 1: целые числа, стратегия interleave, фильтрация чётных
    seq_a = [1, 2, 3, 4]
    seq_b = [10, 20, 30]
    merged = merge_sequences(seq_a, seq_b, strategy='interleave')
    # Применяем filter (одна из трёх обязательных функций)
    filtered = filter(lambda x: x % 2 == 0, merged)   # оставляем только чётные
    result = reduce_by_type(filtered)                # сумма чётных чисел
    print(f"Сумма чётных элементов: {result}")        # 2 + 4 + 10 + 20 + 30 = 66

    # Пример 2: строки, стратегия chain, преобразование map + reduce
    words1 = ["Hello", "world"]
    words2 = [" from", " Python"]
    merged_str = merge_sequences(words1, words2, strategy='chain')
    # Применяем map (одна из трёх обязательных функций)
    mapped = map(str.upper, merged_str)               # перевод в верхний регистр
    result_str = reduce_by_type(mapped)               # конкатенация
    print(f"Результат конкатенации: {result_str}")    # "HELLOWORLD FROM PYTHON"

    # Пример 3: только reduce (без map/filter) – тоже допустимо
    nums = [1, 2, 3]
    nums2 = [4, 5]
    merged_nums = merge_sequences(nums, nums2, strategy='zip')
    total = reduce_by_type(merged_nums)               # сумма: 1+4+2+5 = 12
    print(f"Сумма при zip-объединении: {total}")
