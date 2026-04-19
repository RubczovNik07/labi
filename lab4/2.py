# Замыкание — это функция, которая «запоминает» переменные из объемлющей области видимости (функции, в которой она была создана), 
# даже после того,как внешняя функция завершила своё выполнение.
# Замыкание для отслеживания HP героя с ограничением [0, 100]

def create_hero(initial_hp=100):
    # Ограничиваем начальное значение
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


if __name__ == "__main__":
    print("=== Тестирование замыкания ===")
    hero = create_hero(80)
    print(hero("status"))
    print(hero("damage", 30))
    print(hero("heal", 60))      # 50 + 60 = 100 (ограничение)
    print(hero("damage", 200))   # 100 - 200 = 0 (ограничение)
    print(hero("reset"))
    print(hero("status"))
