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
