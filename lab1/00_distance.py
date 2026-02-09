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
