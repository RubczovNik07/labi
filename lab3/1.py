# Функция с использованием рекурсии
def create_n_dim_array_recursive(n, size):
    if n == 1:
        return [f'level {n}' for _ in range(size)]
    return [create_n_dim_array_recursive(n-1, size) for _ in range(size)]

# Функция без использования рекурсии (итеративная)
def create_n_dim_array_iterative(n, size):
    result = [f'level {n}' for _ in range(size)]
    for _ in range(n-1):
        result = [result for _ in range(size)]
    return result

def pretty_print_lines(arr, level=0):
    if isinstance(arr, list):
        if not arr:
            print("[]")
            return
        
        print("[", end="")
        # Печатаем элементы первого уровня
        for i, item in enumerate(arr):
            if isinstance(item, list):
                # Если это вложенный список, печатаем его содержимое в строку
                print("[", end="")
                for j, subitem in enumerate(item):
                    if isinstance(subitem, list):
                        # Для глубины 3 и более
                        print("[", end="")
                        for k, subsubitem in enumerate(subitem):
                            print(f"'{subsubitem}'", end="")
                            if k < len(subitem) - 1:
                                print(", ", end="")
                        print("]", end="")
                    else:
                        print(f"'{subitem}'", end="")
                    if j < len(item) - 1:
                        print(", ", end="")
                print("]", end="")
            else:
                print(f"'{item}'", end="")
            
            if i < len(arr) - 1:
                print(",")
                print(" ", end="")
        print("]")

# Демонстрация
print("»> create_n_dim_array(2, 3)")
print("Рекурсивная версия:")
pretty_print_lines(create_n_dim_array_recursive(2, 3))
print()

print("Итеративная версия:")
pretty_print_lines(create_n_dim_array_iterative(2, 3))
print()

print("»> create_n_dim_array(3, 2)")
print("Рекурсивная версия:")
pretty_print_lines(create_n_dim_array_recursive(3, 2))
print()

print("Итеративная версия:")
pretty_print_lines(create_n_dim_array_iterative(3, 2))
