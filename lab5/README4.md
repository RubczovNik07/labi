# Отчёт по лабораторной работе

## Задание

**Условие:**  
Реализовать генератор для объединения нескольких последовательностей по заданной стратегии (chain, zip, round_robin).
К генератору должна быть применена хотя бы одна из функций map, filter, reduce.

Свёртка (редукция) полученной последовательности должна зависеть от типа данных элементов:
int, float → сумма
str → конкатенация
другие типы → список

## Описание проделанной работы

### 1. Генератор `merge_sequences`

Функция-генератор принимает список последовательностей и стратегию объединения.

В зависимости от стратегии:
chain – последовательности объединяются последовательно
zip – элементы берутся по индексам (с использованием zip_longest)
round_robin – элементы берутся поочерёдно из каждой последовательности

```python
from itertools import zip_longest

def merge_sequences(seqs, strategy="chain"):
    if strategy == "chain":
        for seq in seqs:
            for item in seq:
                yield item

    elif strategy == "zip":
        for items in zip_longest(*seqs, fillvalue=None):
            for item in items:
                if item is not None:
                    yield item

    elif strategy == "round_robin":
        seqs = [iter(s) for s in seqs]
        while seqs:
            next_seqs = []
            for it in seqs:
                try:
                    yield next(it)
                    next_seqs.append(it)
                except StopIteration:
                    continue
            seqs = next_seqs
```

### 2. Функция свёртки fold_sequence

Функция выполняет редукцию последовательности в зависимости от типа данных.

Используются:
filter — для удаления None
map — для приведения типов
reduce — для свёртки

```python
from functools import reduce

def fold_sequence(seq):
    seq = list(seq)

    if not seq:
        return None

    # filter — удаление None
    seq = list(filter(lambda x: x is not None, seq))

    # числа → сумма
    if all(isinstance(x, (int, float)) for x in seq):
        seq = list(map(float, seq))  # map
        return reduce(lambda a, b: a + b, seq)

    # строки → конкатенация
    elif all(isinstance(x, str) for x in seq):
        seq = list(map(str, seq))  # map
        return reduce(lambda a, b: a + b, seq)

    # остальные типы
    else:
        return list(map(str, seq))
```

### 3. Применение map, filter, reduce

В программе:

filter — удаляет значения None

map — приводит элементы к нужному типу (float, str)

reduce — выполняет свёртку (сумма или конкатенация)

### 4. Пример выполнения

```python
# Числовые последовательности
seq1 = ["a", "b"]
seq2 = ["c", "d"]
seq3 = ["e"]

# --- chain ---
gen_chain = merge_sequences([seq1, seq2, seq3], strategy="chain")
result_chain = fold_sequence(gen_chain)
print("chain:", result_chain)

# --- zip ---
gen_zip = merge_sequences([seq1, seq2, seq3], strategy="zip")
result_zip = fold_sequence(gen_zip)
print("zip:", result_zip)

# --- round_robin ---
gen_rr = merge_sequences([seq1, seq2, seq3], strategy="round_robin")
result_rr = fold_sequence(gen_rr)
print("round_robin:", result_rr)
```
**Вывод программы:**

<img width="265" height="145" alt="image" src="https://github.com/user-attachments/assets/bd72ff79-2405-4c0f-b7b5-4130573e996f" />

## Список использованных источников

1. [Python Documentation: itertools.zip_longest](https://docs.python.org/3/library/itertools.html#itertools.zip_longest)
2. [Python Documentation: functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce)
3. [PEP 255 – Simple Generators](https://peps.python.org/pep-0255/)
4. [Python Tutorial: Functional Programming Tools](https://docs.python.org/3/howto/functional.html)
