# Функция с использованием рекурсии
def calculate_yk_recursive(x, k):
    if x == 0:
        raise ValueError("x не может быть равен 0")
    
    def calculate_b(step):
        if step == 0:
            return 1 / (2 * x)
        return calculate_b(step - 1) * (x ** 2)
    
    if k == 0:
        return 1
    
    b_k = calculate_b(k)
    return b_k * calculate_yk_recursive(x, k - 1)


# Функция без использования рекурсии (итеративная)
def calculate_yk_iterative(x, k):
    if x == 0:
        raise ValueError("x не может быть равен 0")
    
    y = 1  # y0
    b = 1 / (2 * x)  # b0
    
    for i in range(1, k + 1):
        b = b * (x ** 2)  # bk = b_{k-1} * x^2
        y = b * y          # yk = bk * y_{k-1}
    
    return y


# Примеры использования
print(f"y1 для x=2: {calculate_yk_recursive(2, 1)}") 
print(f"y2 для x=2: {calculate_yk_iterative(2, 2)}")  
print(f"y3 для x=2: {calculate_yk_recursive(2, 3)}")  
print(f"y2 для x=3: {calculate_yk_iterative(3, 2)}")  
