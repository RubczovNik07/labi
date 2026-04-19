# Отчёт по лабораторной работе

## Задание

**Условие:**  
Реализовать генератор для объединения двух последовательностей по заданной стратегии (`zip`, `chain`, `interleave`). К генератору должна быть применена хотя бы одна из функций `map`, `reduce`, `filter`.  
Свёртка (редукция) полученной последовательности должна зависеть от типа данных элементов:
- `int` → сумма
- `str` → конкатенация
- `list` → слияние списков
- `tuple` → слияние кортежей
- `bool` → логическое И (all)
- другие типы → возвращаются в виде списка

## Описание проделанной работы

### 1. Генератор `merge_sequences`

Функция-генератор принимает две итерабельные последовательности и строку `strategy`.  
В зависимости от стратегии:

- `'zip'` – выдаёт элементы попарно, пока хватает короткой последовательности.  
- `'chain'` – сначала все элементы первой последовательности, затем все элементы второй.  
- `'interleave'` – чередует элементы, пока есть хотя бы один элемент в любой из последовательностей (с помощью `itertools.zip_longest`).

```python
def merge_sequences(seq1, seq2, strategy='zip'):
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
```

### 2. Функция свёртки reduce_by_type

Принимает последовательность, преобразует её в список, проверяет однородность типов и сворачивает в зависимости от типа:

```python
def reduce_by_type(sequence):
    items = list(sequence)
    if not items:
        return None
    elem_type = type(items[0])
    if not all(isinstance(x, elem_type) for x in items):
        return items
    if elem_type is int:
        return reduce(lambda x, y: x + y, items)
    elif elem_type is str:
        return reduce(lambda x, y: x + y, items)
    # ... и так для list, tuple, bool
```

### 3. Применение filter и map

В примере использования:

- Для целых чисел применён filter для отбора чётных элементов.
- Для строк применён map(str.upper) для перевода в верхний регистр.
- Для демонстрации reduce (через functools.reduce) используется внутри reduce_by_type.

### 4. Пример выполнения

```python
from itertools import zip_longest
from functools import reduce

# Пример 1: целые числа, filter + reduce
seq_a = [1, 2, 3, 4]
seq_b = [10, 20, 30]
merged = merge_sequences(seq_a, seq_b, strategy='interleave')
filtered = filter(lambda x: x % 2 == 0, merged)
result = reduce_by_type(filtered)
print(f"Сумма чётных элементов: {result}")   # 66

# Пример 2: строки, map + reduce
words1 = ["Hello", "world"]
words2 = [" from", " Python"]
merged_str = merge_sequences(words1, words2, strategy='chain')
mapped = map(str.upper, merged_str)
result_str = reduce_by_type(mapped)
print(f"Результат конкатенации: {result_str}")  # HELLOWORLD FROM PYTHON
```
**Вывод программы:**

<img width="563" height="92" alt="image" src="https://github.com/user-attachments/assets/045873ef-8b57-43a1-bb4e-5dea3cba131b" />

## Список использованных источников

1. [Python Documentation: itertools.zip_longest](https://docs.python.org/3/library/itertools.html#itertools.zip_longest)
2. [Python Documentation: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)
3. [PEP 255 – Simple Generators](https://peps.python.org/pep-0255/)
4. [Python Tutorial: Functional Programming Tools](https://docs.python.org/3/howto/functional.html)
