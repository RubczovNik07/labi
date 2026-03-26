def create_recursive(dim, size, level=None):
    if level is None:
        level = dim

    if dim == 1:
        return [f'level {level}'] * size

    return [create_recursive(dim - 1, size, level) for _ in range(size)]

def create_iterative(dim, size):
    arr = [f'level {dim}'] * size
    for _ in range(dim - 1):
        arr = [arr.copy() for _ in range(size)]
    return arr

def print_2d(arr):
    print("[")
    for i, row in enumerate(arr):
        line = "     ['" + "', '".join(row) + "']"
        if i != len(arr) - 1:
            line += ","  
        print(line)
    print("]")

def print_3d(arr):
    print("[")
    for i, block in enumerate(arr):
        print("    [")
        for row in block:
            print("        ['" + "', '".join(row) + "'],")
        print("    ]" + ("," if i != len(arr) - 1 else ""))
    print("]")

print("Рекурсивная:\n")
res1 = create_recursive(2, 3)
print_2d(res1)

print()
res2 = create_recursive(3, 2)
print_3d(res2)

print("\nНерекурсивная:\n")
res3 = create_iterative(2, 3)
print_2d(res3)

print()
res4 = create_iterative(3, 2)
print_3d(res4)
