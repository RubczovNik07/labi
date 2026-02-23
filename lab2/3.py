import math

def find_divisors(n):
    """Находит все делители числа n (кроме 1)"""
    divisors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i)
    return sorted(divisors)

def M(n):
    """Вычисляет M(n) - произведение 5 наименьших делителей"""
    divisors = find_divisors(n)
    if len(divisors) < 5:
        return 0
    
    # Берем 5 наименьших делителей
    smallest_5 = sorted(divisors)[:5]
    
    # Вычисляем произведение
    product = 1
    for d in smallest_5:
        product *= d
    
    return product

def task3():
    result = []
    n = 200000001
    
    while len(result) < 5:
        m_value = M(n)
        if 0 < m_value < n:
            result.append((n, m_value))
        n += 1
    
    return result

# Находим числа и их M(N)
numbers_with_m = task3()

print("Задача 3:")
for i, (n, m) in enumerate(numbers_with_m, 1):
    print(f"{i}. N = {n}, M(N) = {m}")
