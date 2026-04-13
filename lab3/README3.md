# Отчёт по лабораторным работам 

## Задание 1

**Условие:**
Напишите функцию create_n_dim_array(n, size), которая создаёт n-мерный массив (список) заданного размера, заполненный строками 'level n'.

**Описание проделанной работы:**
В ходе выполнения лабораторной работы я реализовал две функции для создания n-мерных массивов.
Сначала я проанализировал условие задачи и примеры. Понял, что мне нужно создать структуру данных, где при n=2 получается список списков, при n=3 — список списков списков, и так далее. Все элементы должны содержать строку с указанием текущего уровня вложенности.

Для рекурсивной функции я использовал следующий подход:
Если n равно 1, значит нужно создать одномерный массив. Я возвращаю список из size элементов, каждый из которых содержит строку f'level {n}'.
Для остальных случаев функция вызывает саму себя с параметром n-1, и создаёт список из size таких вызовов. Таким образом, каждый уровень создаётся через рекурсивный вызов.

Для итеративной функции я пошёл другим путём:
Начал с простого значения — строки f'level {n}'.
В цикле, который выполняется n раз, я последовательно использовал текущее значение в список нужного размера. На каждом шаге получалась структура на один уровень вложенности больше. После завершения цикла получается готовый n-мерный массив.

В итоге я получил две рабочие функции, которые решают поставленную задачу разными 
способами, что позволяет сравнить рекурсивный и итеративный подходы.

```python
def create_n_dim_array_recursive(n, size):
    if n < 1:
        return []

    def helper(level):
        if level == 1:
            return [f'level {n}' for _ in range(size)]
        return [helper(level - 1) for _ in range(size)]

    return helper(n)

def create_n_dim_array_iterative(n, size):
    if n < 1:
        return []

    arr = [f'level {n}' for _ in range(size)]

    for _ in range(n - 1):
        arr = [arr.copy() for _ in range(size)]

    return arr

arr2 = create_n_dim_array_recursive(2, 3)

print("»> create_n_dim_array_recursive(2, 3)")
print("[")
for i in range(len(arr2)):
    if i == len(arr2) - 1:
        print("    " + str(arr2[i]))
    else:
        print("    " + str(arr2[i]) + ",")
print("]")


arr3 = create_n_dim_array_recursive(3, 2)

print("\n»> create_n_dim_array_recursive(3, 2)")
print("[")
for i in range(len(arr3)):
    print("    [")
    for j in range(len(arr3[i])):
        if j == len(arr3[i]) - 1:
            print("        " + str(arr3[i][j])+ ",")
        else:
            print("        " + str(arr3[i][j]) + ",")
    if i == len(arr3) - 1:
        print("    ]")
    else:
        print("    ],")
print("]")

```
**Вывод программы:**

<img width="555" height="647" alt="image" src="https://github.com/user-attachments/assets/b5d0e2ee-78e2-461e-af7a-167cfa1147ed" />




## Задание 2

**Условие:**
Дана система уравнений:
y₀ = 1
b₀ = 1/(2x), где x ≠ 0
bₖ = bₖ₋₁ · x²
yₖ = bₖ · yₖ₋₁
Необходимо вычислить yₖ для заданных x и k.

**Описание проделанной работы:**
В ходе выполнения лабораторной работы я реализовал две функции для вычисления значений по рекуррентной формуле.
Сначала я разобрался с математической постановкой задачи. Мне нужно было вычислить последовательность, где каждый следующий член зависит от предыдущего через промежуточный коэффициент bₖ.

Для рекурсивной функции я использовал следующий подход:
Создал вложенную функцию calculate_b(step), которая рекурсивно вычисляет коэффициент bₖ. При step=0 возвращает 1/(2x). Иначе умножает предыдущее значение на x².
Основная функция calculate_yk_recursive имеет базовый случай при k=0 (возвращает 1).
Для k>0 сначала вычисляет bₖ через вложенную функцию, затем умножает его на результат рекурсивного вызова для yₖ₋₁.

Для итеративной функции я пошёл по пути последовательного вычисления:
Задал начальные значения: y = 1 (y₀) и b = 1/(2x) (b₀).
В цикле от 1 до k последовательно обновлял значения: сначала вычислял новое b по формуле b = b * x², затем вычислял новое y по формуле y = b * y.
После завершения цикла получается искомое значение yₖ.

```python
# Функция с использованием рекурсии
def calculate_yk_recursive(x, k):
    if x == 0:
        raise ValueError("x не может быть равен 0")
    def calculate_b(step):
        if step == 0:
            return 1 / (2 * x)
        return calculate_b(step - 1) * (x ** 2)
    if k == 0:
        return 1
    b_k = calculate_b(k)
    return b_k * calculate_yk_recursive(x, k - 1)
# Функция без использования рекурсии (итеративная)
def calculate_yk_iterative(x, k):
    if x == 0:
        raise ValueError("x не может быть равен 0")
    y = 1  # y0
    b = 1 / (2 * x)  # b0
    for i in range(1, k + 1):
        b = b * (x ** 2)  # bk = b_{k-1} * x^2
        y = b * y          # yk = bk * y_{k-1}
    return y
# Примеры использования
print(f"y1 для x=2: {calculate_yk_recursive(2, 1)}")  
print(f"y2 для x=2: {calculate_yk_iterative(2, 2)}")  
print(f"y3 для x=2: {calculate_yk_recursive(2, 3)}")  
print(f"y2 для x=3: {calculate_yk_iterative(3, 2)}")  


```
**Вывод программы:**

<img width="245" height="131" alt="image" src="https://github.com/user-attachments/assets/3065e6ba-9328-41df-9db6-99c5dd990c78" />

## Список использованных источников

1. [Рекурсивные функции в Python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
2. [Рекуррентные соотношения ](https://ru.wikipedia.org/wiki/Рекуррентная_формула)
3. [Рекурсия в программировании](https://ru.wikipedia.org/wiki/Рекурсия) 
4. [Генераторы списков (list comprehensions)](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
