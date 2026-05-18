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
