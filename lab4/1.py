import sys
from io import StringIO

# Замыкание для отслеживания HP героя
def create_hero(initial_hp=100):

    current_hp = max(0, min(initial_hp, 100))  # Ограничиваем начальное значение
    
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

# Декоратор для подавления вывода функции на консоль
def suppress_console_output(func):
    """
    Декоратор для подавления вывода функции на консоль.
    Перенаправляет stdout в буфер и восстанавливает после выполнения.
    """
    def wrapper(*args, **kwargs):
        # Сохраняем оригинальный stdout
        original_stdout = sys.stdout
        # Создаем буфер для перехвата вывода
        sys.stdout = StringIO()
        
        try:
            # Выполняем функцию
            result = func(*args, **kwargs)
            # Получаем перехваченный вывод (но не выводим его)
            captured_output = sys.stdout.getvalue()
            return result
        finally:
            # Восстанавливаем оригинальный stdout
            sys.stdout = original_stdout
    
    return wrapper

# Создаем героя с замыканием
hero = create_hero(100)

# Применяем декоратор к замыканию
@suppress_console_output
def use_hero_action(action, amount=0):
    """Обертка для использования действий героя с подавленным выводом"""
    return hero(action, amount)

# Тестирование
if __name__ == "__main__":
    print("=== Тестирование без декоратора (обычный вывод) ===")
    hero1 = create_hero(80)
    print(hero1("status"))
    print(hero1("damage", 30))
    print(hero1("heal", 60))  # Попытка вылечиться выше 100
    print(hero1("damage", 200))  # Попытка урона ниже 0
    
    print("\n=== Тестирование с декоратором (вывод подавлен) ===")
    hero2 = create_hero(80)
    
    # Эти вызовы не будут выводить ничего в консоль
    result1 = use_hero_action("damage", 30)
    result2 = use_hero_action("heal", 60)
    result3 = use_hero_action("damage", 200)
    
    # Но мы можем получить результаты как возвращаемые значения
    print(f"Результат урона: {result1}")
    print(f"Результат лечения: {result2}")
    print(f"Результат сильного урона: {result3}")
    
    print("\n=== Дополнительное тестирование граничных значений ===")
    hero3 = create_hero(50)
    
    @suppress_console_output
    def test_hero_actions():
        print(hero3("heal", 100))  # Должен показать 50 -> 100
        print(hero3("damage", 150))  # Должен показать 100 -> 0
        print(hero3("reset"))  # Должен показать 0 -> 100
        return "Все действия выполнены"
    
    final_result = test_hero_actions()
    print(f"Итоговый результат: {final_result}")
    print(hero3("status"))  # Проверяем финальное состояние
