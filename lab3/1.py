# Функция с использованием рекурсии
def create_n_dim_array_recursive(n, size):
    if n == 1:
        return [f'level {n}' for _ in range(size)]
    return [create_n_dim_array_recursive(n-1, size) for _ in range(size)]

# Функция без использования рекурсии (итеративная)
def create_n_dim_array_iterative(n, size):
    result = f'level {n}'
    for _ in range(n):
        result = [result for _ in range(size)]
    return result

# Примеры использования
print(create_n_dim_array_recursive(2, 3))
print(create_n_dim_array_iterative(2, 3))
print(create_n_dim_array_recursive(3, 2))
print(create_n_dim_array_iterative(3, 2))
