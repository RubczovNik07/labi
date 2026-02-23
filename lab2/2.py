def task2():
    # Вычисляем выражение: 4^511 + 2^511 - 511
    value = 4**511 + 2**511 - 511
    
    # Переводим в двоичную строку и считаем единицы
    binary = bin(value)[2:]  # отбрасываем префикс '0b'
    ones_count = binary.count('1')
    
    return ones_count

print(f"Задача 2: {task2()} единиц")

