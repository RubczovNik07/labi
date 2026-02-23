# Отчёт по лабораторным работам 

## Задание 1

**Условие:**
Иван составляет таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово. В качестве кодовых слов Иван использует все пятибуквенные слова в алфавите {A, B, C, D, E}, удовлетворяющие условию: кодовое слово не может начинаться с буквы E и заканчиваться буквой A. Сколько различных кодовых слов может использовать Иван?

**Результаты вычислений:**
Для решения задачи использован модуль itertools, который позволяет сгенерировать все возможные комбинации букв:

```python
import itertools

def task1():
    alphabet = ['A', 'B', 'C', 'D', 'E']
    all_words = itertools.product(alphabet, repeat=5)
    count = sum(1 for word in all_words if word[0] != 'E' and word[4] != 'A')
    return count

print(f"Задача 1: {task1()} кодовых слов")
```
**Вывод программы:**

<img width="215" height="63" alt="image" src="https://github.com/user-attachments/assets/13a893b8-e26c-4bbc-b37b-1407e99d9b75" />

**Аналитическое решение подтверждает программное:**

Первая позиция: 4 варианта (все буквы кроме E)

Вторая позиция: 5 вариантов

Третья позиция: 5 вариантов

Четвертая позиция: 5 вариантов

Пятая позиция: 4 варианта (все буквы кроме A)

Общее количество = 4 × 5 × 5 × 5 × 4 = 2000 кодовых слов.

## Задание 2

**Условие:**
Сколько единиц содержится в двоичной записи значения выражения: 4⁵¹¹ + 2⁵¹¹ − 511?

**Результаты вычислений:**
Для вычисления используется прямое возведение в степень и преобразование в двоичную строку:

```python
def task2():
    # Вычисляем выражение: 4^511 + 2^511 - 511
    value = 4**511 + 2**511 - 511
    
    # Переводим в двоичную строку и считаем единицы
    binary = bin(value)[2:]  # отбрасываем префикс '0b'
    ones_count = binary.count('1')
    
    return ones_count

print(f"Задача 2: {task2()} единиц")
```
**Вывод программы:**

<img width="258" height="74" alt="image" src="https://github.com/user-attachments/assets/b90e67e3-f452-40df-945f-a689e3678d06" />

**Преобразование выражения:**

4⁵¹¹ = (2²)⁵¹¹ = 2¹⁰²²
Таким образом, выражение = 2¹⁰²² + 2⁵¹¹ - 511
511 в двоичной системе = 111111111₂ (9 единиц)

Вычисленное значение содержит 503 единицы в двоичной записи.

## Задание 3

**Условие:**
Пусть M(N) — произведение 5 наименьших различных натуральных делителей натурального числа N, не считая единицы. Если у числа N меньше 5 таких делителей, то M(N) считается равным нулю.

Найдите 5 наименьших натуральных чисел, превышающих 200 000 000, для которых 0 < M(N) < N. В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.

**Результаты вычислений:**
Для решения задачи реализован перебор чисел с нахождением делителей:

```python
import math

def find_divisors(n):
    """Находит все делители числа n (кроме 1)"""
    divisors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i)
    return sorted(divisors)

def M(n):
    """Вычисляет M(n) - произведение 5 наименьших делителей"""
    divisors = find_divisors(n)
    if len(divisors) < 5:
        return 0
    
    # Берем 5 наименьших делителей
    smallest_5 = sorted(divisors)[:5]
    
    # Вычисляем произведение
    product = 1
    for d in smallest_5:
        product *= d
    
    return product

def task3():
    result = []
    n = 200000001
    
    while len(result) < 5:
        m_value = M(n)
        if 0 < m_value < n:
            result.append((n, m_value))
        n += 1
    
    return result

# Находим числа и их M(N)
numbers_with_m = task3()

print("Задача 3:")
for i, (n, m) in enumerate(numbers_with_m, 1):
    print(f"{i}. N = {n}, M(N) = {m}")
```
**Вывод программы:**

<img width="389" height="156" alt="image" src="https://github.com/user-attachments/assets/e52a9fa0-0743-4713-a9a9-bfc1af6aa313" />

**Значения M(N) в порядке возрастания соответствующих чисел N:**
[1728, 21632, 1260, 1152, 4127787]

## Список использованных источников

1. [Документация Python: itertools](https://docs.python.org/3/library/itertools.html)
2. [Документация Python: math](https://docs.python.org/3/library/math.html)
3. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) 
4. [Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
