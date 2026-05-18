import itertools
import math

def task1():
    """
    Иван использует все пятибуквенные слова из алфавита {A, B, C, D, E},
    которые не начинаются на E и не заканчиваются на A.

    >>> task1()
    2000
    """
    alphabet = ['A', 'B', 'C', 'D', 'E']
    all_words = itertools.product(alphabet, repeat=5)

    count = sum(
        1
        for word in all_words
        if word[0] != 'E' and word[4] != 'A'
    )

    return count

def task2():
    """
    Сколько единиц содержится в двоичной записи выражения:
    4**511 + 2**511 - 511.

    >>> task2()
    504
    """
    value = 4**511 + 2**511 - 511

    binary = bin(value)[2:]

    return binary.count('1')

def find_divisors(n):
    """
    Находит все натуральные делители числа n, кроме 1.

    >>> find_divisors(12)
    [2, 3, 4, 6]
    """
    divisors = set()

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)

            if i != n // i:
                divisors.add(n // i)

    return sorted(divisors)

def M(n):
    """
    M(N) — произведение 5 наименьших различных делителей числа N,
    не считая единицы.
    Если делителей меньше 5, возвращается 0.

    >>> M(72)
    1152
    >>> M(13)
    0
    """
    divisors = find_divisors(n)

    if len(divisors) < 5:
        return 0

    smallest_5 = divisors[:5]

    product = 1

    for d in smallest_5:
        product *= d

    return product

def task3():
    """
    Находит 5 наименьших чисел N > 200000000,
    для которых 0 < M(N) < N.

    Возвращает значения M(N).

    >>> task3()
    [1728, 21632, 1260, 1152, 4127787]
    """
    result = []

    n = 200000001

    while len(result) < 5:
        m_value = M(n)

        if 0 < m_value < n:
            result.append(m_value)

        n += 1

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print("Задача 1:", task1())
    print("Задача 2:", task2())
    print("Задача 3:", task3())