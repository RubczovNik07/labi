import itertools

def task1():
    alphabet = ['A', 'B', 'C', 'D', 'E']
    all_words = itertools.product(alphabet, repeat=5)
    count = sum(1 for word in all_words if word[0] != 'E' and word[4] != 'A')
    return count

print(f"Задача 1: {task1()}")
