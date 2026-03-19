# Отчёт по лабораторным работам 

## Задание 1

**Условие:**
Cоздать функцию, которая с помощью механизма замыкания управляет состоянием здоровья игрового персонажа. Здоровье должно всегда оставаться в пределах от 0 до 100. Герой может:Получать урон (damage)
Лечиться (heal)
Проверять текущий статус (status)
Сбрасывать здоровье до максимума (reset)

**Как решил**
Внешняя функция create_hero:
Принимает начальное значение HP
Создаёт замкнутую переменную current_hp с валидацией через max(0, min(initial_hp, 100))
Возвращает внутреннюю функцию handle_action
Внутренняя функция handle_action:
Использует nonlocal current_hp для доступа к переменной из внешней области видимости
Обрабатывает различные типы действий (heal, damage, status, reset)
Применяет ограничения через min() и max() для соблюдения границ
Возвращает строку с описанием произошедших изменений

```python
# Пример использования
hero = create_hero(80)
print(hero("status"))        # Текущее HP: 80
print(hero("damage", 30))    # Урон -30: 80 -> 50
print(hero("heal", 60))      # Лечение +60: 50 -> 100 (ограничение)
print(hero("damage", 200))   # Урон -200: 100 -> 0 (ограничение)
```
**Вывод программы:**

<img width="588" height="135" alt="image" src="https://github.com/user-attachments/assets/50ca872e-7cd5-482d-8b3b-775f284e6e4a" />

## Задание 2

**Условие:**
Разработать декоратор, который перехватывает и подавляет весь вывод функции в стандартный поток вывода (консоль), но при этом сохраняет возвращаемое значение функции. Применить декоратор к созданному замыканию.

**Как решил**
Создание декоратора suppress_console_output:
Сохраняет оригинальный sys.stdout
Перенаправляет вывод в StringIO (виртуальный буфер в памяти)
Выполняет функцию и перехватывает весь вывод в буфер
Восстанавливает оригинальный sys.stdout
Возвращает результат выполнения функции
Применение к замыканию:
Создаём функцию-обёртку use_hero_action
Применяем декоратор через синтаксис @suppress_console_output
Внутри обёртки вызываем замыкание hero

```python
# Создаём героя
hero = create_hero(80)

# Применяем декоратор к обёртке
@suppress_console_output
def use_hero_action(action, amount=0):
    return hero(action, amount)

# Эти вызовы НЕ будут выводить ничего в консоль
result1 = use_hero_action("damage", 30)  # Вывод подавлен
result2 = use_hero_action("heal", 60)    # Вывод подавлен

# Но результаты доступны
print(result1)  # "Урон -30: 80 -> 50"
```
**Вывод программы:**

<img width="536" height="90" alt="image" src="https://github.com/user-attachments/assets/f3cf2ae2-338b-4a1b-bc5f-8af276d6e4af" />


## Список использованных источников

1. [PEP 3104 — Access to Names in Outer Scopes](https://peps.python.org/pep-3104/)
2. [Python Documentation: sys.stdout](https://docs.python.org/3/library/sys.html#sys.stdout)
3. [Python Documentation: io.StringIO](https://docs.python.org/3/library/io.html#io.StringIO) 
