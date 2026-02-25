# Отчёт по лабораторным работам 

## Задания и их решение

### Задание 00: Расстояние между городами

**Задание:** Имеется словарь с координатами городов. Составить словарь словарей `distances`, где для каждой пары городов будет вычислено расстояние на координатной сетке по формуле: \(\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}\).

**Решение:** Были использованы вложенные циклы `for` для перебора всех комбинаций городов и заполнения словаря.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# Заполняем словарь расстояний
for city1, coord1 in sites.items():
    distances[city1] = {}
    for city2, coord2 in sites.items():
        if city1 != city2:
            # Вычисляем расстояние между двумя городами
            distance = ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5
            distances[city1][city2] = distance
        else:
            # Расстояние от города до самого себя равно 0
            distances[city1][city2] = 0.0

# TODO здесь заполнение словаря

print(distances)
```

<img width="816" height="103" alt="Снимок00" src="https://github.com/user-attachments/assets/3af510b4-d14d-4e6d-b78d-dbb0ad2a1e5f" />

### Задание 01: Площадь круга и точка внутри

**Задание:** Вычислить площадь круга с радиусом radius = 42, используя число π≈3.1415926. Результат округлить до 4 знаков. Проверить, лежат ли точки point_1 = (23, 34) и point_2 = (30, 30) внутри круга с центром в начале координат (0, 0) и тем же радиусом.

**Решение:** Для площади использована формула S=πr^2. Для проверки принадлежности точки кругу вычислено расстояние от точки до центра по теореме Пифагора: x^2+y^2. Результат сравнения (<= radius) автоматически дает True или False.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение площади этого круга с точностью до 4-x знаков после запятой
# подсказки:
#    формулу можно подсмотреть в интернете,
#    пи возьмите равным 3.1415926
#    точность указывается в функции round()
# TODO здесь ваш код
pi = 3.1415926
area = pi * radius ** 2
print(round(area, 4))

# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата x, 34 - координата y

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, или False, если точка лежит вовне круга.
# подсказки:
#    нужно определить расстояние от этой точки до начала координат (0, 0)
#    формула так же есть в интернете
#    квадратный корень - это возведение в степень 0.5
#    операции сравнения дают булевы константы True и False
# TODO здесь ваш код
distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
print(distance_1 <= radius)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# или False, если точка лежит вовне круга.
# TODO здесь ваш код
distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
print(distance_2 <= radius)
```

<img width="832" height="99" alt="Снимок01" src="https://github.com/user-attachments/assets/18c2085c-29d9-4106-90ee-89a01d47de66" />


### Задание 02: Арифметические операции

**Задание:** Между числами 1 2 3 4 5 (сохраняя порядок) расставить знаки операций +, -, * и скобки так, чтобы получить число 25.

**Решение:** Путем подбора была найдена формула (1 + 2) * 3 + 4 * 5, которая дает искомый результат.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Расставить знаки операций "плюс", "минус", "умножение" и скобки
# между числами "1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечисленные.
# Порядок чисел нужно сохранить.

# Пример для чисел "1 2 3" и "9"
result = (1 + 2) * 3
print(result)

# TODO написать формулу для 1 2 3 4 5 и вывести значение на консоль

# Решение: (1 + 2) * 3 + 4 * 5
result = (1 + 2) * 3 + 4 * 5
print(result)  # Выведет 25
```

<img width="847" height="67" alt="Снимок02" src="https://github.com/user-attachments/assets/6addf7db-7209-4b55-b9b5-572cbf4bb223" />


### Задание 03: Индексация строк

**Задание:** Дана строка с фильмами 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'. Используя только срезы строк (без .split(), .find() и т.д.), вывести по отдельности: первый фильм, последний, второй, второй с конца.

**Решение:** Сначала были вручную найдены индексы всех запятых. Затем с помощью срезов от нужной позиции до следующей запятой извлечены названия фильмов.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
# первый фильм
# последний
# второй
# второй с конца

# Запятая не должна выводиться. Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код

# Находим позиции запятых
# Сначала найдем все запятые в строке
comma1 = my_favorite_movies.index(',')
comma2 = my_favorite_movies.index(',', comma1 + 1)
comma3 = my_favorite_movies.index(',', comma2 + 1)
comma4 = my_favorite_movies.index(',', comma3 + 1)

# Первый фильм (от начала до первой запятой)
first_movie = my_favorite_movies[:comma1]
print(first_movie)

# Последний фильм (от четвертой запятой+2 до конца)
# +2 чтобы пропустить запятую и пробел
last_movie = my_favorite_movies[comma4 + 2:]
print(last_movie)

# Второй фильм (от первой запятой+2 до второй запятой)
second_movie = my_favorite_movies[comma1 + 2:comma2]
print(second_movie)

# Второй с конца (от третьей запятой+2 до четвертой запятой)
second_from_end = my_favorite_movies[comma3 + 2:comma4]
print(second_from_end)
```

<img width="825" height="131" alt="Снимок03" src="https://github.com/user-attachments/assets/34cef810-d986-4d1d-9e79-e5a70b345c93" />


### Задание 04: Моя семья (списки)

**Задание:** Создать список my_family из имен (минимум 3). Создать список списков my_family_height с именами и ростом. Вывести рост отца. Вывести общий рост всех членов семьи.

**Решение:** Для поиска отца использован цикл for и условный оператор if. Для подсчета общего роста — цикл, суммирующий значения роста.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["отец","мать", "сын", "бабушка"]

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ["отец", 178],
    ["мать", 160],
    ["сын", 180],
    ["бабушка", 164]
]

# Выведите на консоль рост отца в формате
# Рост отца - XX см
father_height = None
for member in my_family_height:
    if member[0] == "отец":
        father_height = member[1]
        break

if father_height is not None:
    print(f"Рост отца - {father_height} см")

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
# Общий рост моей семьи - XX см
total_height = 0
for member in my_family_height:
    total_height += member[1]

print(f"Общий рост моей семьи - {total_height} см")
```

<img width="853" height="79" alt="Снимок04" src="https://github.com/user-attachments/assets/ca606966-1156-4610-9595-f9d51de55cc7" />


### Задание 05: Зоопарк (списки)

**Задание:** Имеется список животных zoo. Выполнить с ним ряд операций: вставить медведя, добавить птиц, удалить слона, узнать номера клеток льва и жаворонка (номера для людей, с 1).

**Решение:** Использованы методы списков: insert(), extend(), remove(), index().

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
# и выведите список на консоль
# TODO здесь ваш код
zoo.extend(birds)
print(zoo)

# уберите слона
# и выведите список на консоль
# TODO здесь ваш код
zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
lion_cage = zoo.index('lion') + 1  # +1 потому что люди считают с 1, а не с 0
lark_cage = zoo.index('lark') + 1

print(f"Лев сидит в клетке номер {lion_cage}")
print(f"Жаворонок сидит в клетке номер {lark_cage}")

```

<img width="826" height="135" alt="Снимок05" src="https://github.com/user-attachments/assets/023d68e3-e4ab-4a86-834e-03c0513e1a11" />


### Задание 06: Песни Depeche Mode (список и словарь)

**Задание:** Из списка violator_songs_list вычислить сумму длительности трех песен: 'Halo', 'Enjoy the Silence', 'Clean'. Из словаря violator_songs_dict вычислить сумму длительности трех песен: 'Sweetest Perfection', 'Policy of Truth', 'Blue Dress'.

**Решение:** В первом случае выполнен перебор списка и проверка наличия названия в списке искомых. Во втором — прямой доступ к элементам словаря по ключу.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
# При песни звучат XXX.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(XXX, YYY, ZZZ)

# TODO здесь ваш код
total_time_list = 0
for song in violator_songs_list:
    if song[0] in ['Halo', 'Enjoy the Silence', 'Clean']:
        total_time_list += song[1]

print(f'Три песни звучат {round(total_time_list, 2)} минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
# А другие три песни звучат XXX минут

# TODO здесь ваш код
total_time_dict = 0
songs_to_sum = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
for song_name in songs_to_sum:
    total_time_dict += violator_songs_dict[song_name]

print(f'А другие три песни звучат {round(total_time_dict, 2)} минут')
```

<img width="842" height="87" alt="Снимок06" src="https://github.com/user-attachments/assets/3b75dad9-7152-40bf-93ed-dc09eb4bcc69" />


### Задание 07: Секретное сообщение

**Задание:** Расшифровать секретное сообщение, извлекая из каждого элемента списка secret_message определенные буквы с помощью срезов.

**Решение:** Задание на отработку срезов строк. Для каждой строки списка применен срез с нужными индексами (начало, конец, шаг), чтобы получить фрагмент слова.

```python
# Фрагмент кода 07_secret.py
secret_message = [
    'квевтфппбц3стмзалтнмаршг65длучча',
    'дысеньблц2бане4т64ь463ущея6втщл66',
    'т3пплвце1н3и2кд4лы12чф1ап3бкчыаь',
    'ыд5фму3жеородт9г68ббуимикучшсал',
    'бсц59мегщ2лятьаьгенедьв9фк9ехб1а'
]

word1 = secret_message[0][3]                     # 4-й символ (индекс 3)
word2 = secret_message[1][9:13]                  # с 10 по 13 (индексы 9:13)
word3 = secret_message[2][5:15:2]                 # с 6 по 15 через один (5:15:2)
word4 = secret_message[3][12:6:-1]                # с 9 по 7 в обратном порядке (12:6:-1) [индексы 12..7]
word5 = secret_message[4][20:16:-1]                # с 21 по 18 в обратном порядке (20:16:-1)

print(f"{word1} {word2} {word3} {word4} {word5}")
```

<img width="619" height="54" alt="image" src="https://github.com/user-attachments/assets/2f3153ab-0bff-464f-8c62-ac96ab1f3159" />


### Задание 08: Сад и луг (множества)

**Задание:** Даны два кортежа с цветами. Преобразовать их в множества и выполнить операции объединения, пересечения и разности.

**Решение:** Использованы встроенные типы set и их методы: union(), intersection(), difference().

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# Создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
# TODO здесь ваш код

# Выведите на консоль все виды цветов
all_flowers = garden_set.union(meadow_set)
print("Все виды цветов:", sorted(all_flowers))
# TODO здесь ваш код

# Выведите на консоль те, которые растут и там
common_flowers = garden_set.intersection(meadow_set)
print("Цветы, растущие и в саду и на лугу:", sorted(common_flowers))
# TODO здесь ваш код

# Выведите на консоль те, которые растут в саду, но не растут на лугу
only_garden = garden_set.difference(meadow_set)
print("Цветы, растущие только в саду:", sorted(only_garden))
# TODO здесь ваш код

# Выведите на консоль те, которые растут на лугу, но не растут в саду
only_meadow = meadow_set.difference(garden_set)
print("Цветы, растущие только на лугу:", sorted(only_meadow))
# TODO здесь ваш код
```

<img width="822" height="141" alt="Снимок08" src="https://github.com/user-attachments/assets/23543c03-ecb3-4f8f-b8f7-b7bb34d0a60e" />


### Задание 09: Магазины и сладости (словари)

**Задание:** На основе исходного словаря shops создать новый словарь sweets, где для каждого продукта будет список магазинов с ценами, отсортированный по возрастанию цены.

**Решение:** Это задание на ручное формирование структуры данных. Информация о продуктах была собрана из разных магазинов и сгруппирована вручную в новый словарь, где ключ — название продукта, а значение — список словарей с информацией о магазине и цене.

```python
# Фрагмент кода 09_shopping.py
shops = { ... } # исходный словарь

sweets = {
    'печенье': [
        {'shop': 'патерочка', 'price': 9.99},
        {'shop': 'ашан', 'price': 10.99},
        # цена в 'магнит' - 11.99, она не вошла в топ-2 самых дешевых согласно примеру
    ],
    'конфеты': [
        {'shop': 'магнит', 'price': 30.99},
        {'shop': 'патерочка', 'price': 32.99},
        # цена в 'ашан' - 34.99
    ],
    'карамель': [
        {'shop': 'магнит', 'price': 41.99},
        {'shop': 'ашан', 'price': 45.99},
        # цена в 'патерочка' - 46.99
    ],
    'пирожное': [
        {'shop': 'патерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
        # цена в 'ашан' - 67.99
    ],
}

print(sweets)
```

<img width="839" height="135" alt="Снимок09" src="https://github.com/user-attachments/assets/390b4363-2b8e-4c16-af80-c0d61feeaa38" />


### Задание 10: Склад (словари и циклы)

**Задание:** Имеются словарь товаров goods и словарь остатков на складе store. Для каждого товара (Лампа, Стол, Диван, Стул) рассчитать общее количество штук на складе и их общую стоимость.

**Решение:** По каждому товару получен его код из goods. По коду из store получен список партий. В цикле (или вручную) по каждой партии рассчитана стоимость и суммированы количества и стоимости.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Лампа
lamp_code = goods['Лампа']
lamp_item = store[lamp_code][0]
lamp_quantity = lamp_item['quantity']
lamp_price = lamp_item['price']
lamp_cost = lamp_quantity * lamp_price
print(f'Лампа - {lamp_quantity} шт, стоимость {lamp_cost} руб')

# Стол
table_code = goods['Стол']
table_item1 = store[table_code][0]
table_item2 = store[table_code][1]
table_quantity1 = table_item1['quantity']
table_price1 = table_item1['price']
table_cost1 = table_quantity1 * table_price1
table_quantity2 = table_item2['quantity']
table_price2 = table_item2['price']
table_cost2 = table_quantity2 * table_price2
table_quantity_total = table_quantity1 + table_quantity2
table_cost_total = table_cost1 + table_cost2
print(f'Стол - {table_quantity_total} шт, стоимость {table_cost_total} руб')

# Диван
sofa_code = goods['Диван']
sofa_item1 = store[sofa_code][0]
sofa_item2 = store[sofa_code][1]
sofa_quantity1 = sofa_item1['quantity']
sofa_price1 = sofa_item1['price']
sofa_cost1 = sofa_quantity1 * sofa_price1
sofa_quantity2 = sofa_item2['quantity']
sofa_price2 = sofa_item2['price']
sofa_cost2 = sofa_quantity2 * sofa_price2
sofa_quantity_total = sofa_quantity1 + sofa_quantity2
sofa_cost_total = sofa_cost1 + sofa_cost2
print(f'Диван - {sofa_quantity_total} шт, стоимость {sofa_cost_total} руб')

# Стул
chair_code = goods['Стул']
chair_item1 = store[chair_code][0]
chair_item2 = store[chair_code][1]
chair_item3 = store[chair_code][2]
chair_quantity1 = chair_item1['quantity']
chair_price1 = chair_item1['price']
chair_cost1 = chair_quantity1 * chair_price1
chair_quantity2 = chair_item2['quantity']
chair_price2 = chair_item2['price']
chair_cost2 = chair_quantity2 * chair_price2
chair_quantity3 = chair_item3['quantity']
chair_price3 = chair_item3['price']
chair_cost3 = chair_quantity3 * chair_price3
chair_quantity_total = chair_quantity1 + chair_quantity2 + chair_quantity3
chair_cost_total = chair_cost1 + chair_cost2 + chair_cost3
print(f'Стул - {chair_quantity_total} шт, стоимость {chair_cost_total} руб')
```

<img width="825" height="107" alt="Снимок10" src="https://github.com/user-attachments/assets/a8b0531b-bc7c-4419-a163-c01e6617559b" />


## Шпаргалка по работе с Git
В процессе выполнения работы использовалась система контроля версий Git. Вот основные команды:

git init - инициализация нового репозитория в текущей папке.

git add <file_name> или git add . - добавление файла (или всех измененных файлов) в область подготовленных изменений (staging area).

git commit -m "Сообщение коммита" - сохранение изменений в репозиторий с кратким описанием.

git status - проверка состояния файлов (измененные, неотслеживаемые, готовые к коммиту).

git log или git log --oneline - просмотр истории коммитов.

git push origin main - отправка выполненных коммитов на удаленный сервер (например, GitHub) в ветку main.

git remote add origin <URL> - привязка локального репозитория к удаленному.

## Список использованных источников

1. [Matplotlib cheatsheets and handouts](https://matplotlib.org/cheatsheets/)
2. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
3. [Writing mathematical expressions](https://matplotlib.org/stable/tutorials/text/mathtext.html)
4. [Официальная документация Python](https://docs.python.org/3/)
5. [Git Cheat Sheet (GitHub)](https://training.github.com/downloads/ru/github-git-cheat-sheet/)
6. [Интерактивный учебник по Python](https://pythontutor.ru/)
