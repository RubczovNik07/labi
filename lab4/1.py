# task2_suppress_decorator.py
# Декоратор подавляет любой вывод в консоль внутри обёрнутой функции

import sys
from io import StringIO

# ---------- Замыкание из задания 1 ----------
def create_hero(initial_hp=100):
    current_hp = max(0, min(initial_hp, 100))
    
    def handle_action(action, amount=0):
        nonlocal current_hp
        old_hp = current_hp
        
        if action == "heal":
            current_hp = min(current_hp + amount, 100)
            result = f"Лечение +{amount}: {old_hp} -> {current_hp}"
        elif action == "damage":
            current_hp = max(current_hp - amount, 0)
            result = f"Урон -{amount}: {old_hp} -> {current_hp}"
        elif action == "status":
            result = f"Текущее HP: {current_hp}"
        elif action == "reset":
            current_hp = 100
            result = f"Сброс HP: {old_hp} -> {current_hp}"
        else:
            result = f"Неизвестное действие: {action}"
        
        return result
    
    return handle_action

# ---------- Декоратор для подавления вывода ----------
def suppress_console_output(func):
    def wrapper(*args, **kwargs):
        original_stdout = sys.stdout
        sys.stdout = StringIO()          # перехватываем вывод
        try:
            result = func(*args, **kwargs)
            # Перехваченный вывод игнорируется
            return result
        finally:
            sys.stdout = original_stdout  # восстанавливаем
    return wrapper

# ---------- Применяем декоратор к замыканию ----------
hero = create_hero(80)   # создаём героя

@suppress_console_output
def use_hero_action(action, amount=0):
    """Обёртка, которая вызывает hero и подавляет весь вывод внутри себя"""
    # Этот print не попадёт в консоль благодаря декоратору
    print(f"Логирование: действие {action} с amount={amount}")
    return hero(action, amount)

# ---------- Тестирование ----------
if __name__ == "__main__":
    print("=== Без декоратора (вывод виден) ===")
    h = create_hero(50)
    print(h("heal", 30))
    print(h("damage", 20))

    print("\n=== С декоратором (вывод подавлен) ===")
    # Все print внутри use_hero_action не выводятся
    res1 = use_hero_action("damage", 30)
    res2 = use_hero_action("heal", 60)
    res3 = use_hero_action("damage", 200)
    res4 = use_hero_action("status")

    print(f"Результат урона: {res1}")
    print(f"Результат лечения: {res2}")
    print(f"Результат сильного урона: {res3}")
    print(f"Результат статуса: {res4}")

    print("\n=== Дополнительная проверка: функция с несколькими print ===")
    @suppress_console_output
    def noisy():
        print("Этот текст не появится")
        print("И этот тоже")
        return "Всё подавлено"

    result = noisy()
    print(f"Возвращено: {result}")
