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
