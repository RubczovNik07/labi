def create_n_dim_array_recursive(n, size):
    if n < 1:
        return []

    def helper(level):
        if level == 1:
            return [f'level {n}' for _ in range(size)]
        return [helper(level - 1) for _ in range(size)]

    return helper(n)

def create_n_dim_array_iterative(n, size):
    if n < 1:
        return []

    arr = [f'level {n}' for _ in range(size)]

    for _ in range(n - 1):
        arr = [arr.copy() for _ in range(size)]

    return arr

arr2 = create_n_dim_array_recursive(2, 3)

print("»> create_n_dim_array_recursive(2, 3)")
print("[")
for i in range(len(arr2)):
    if i == len(arr2) - 1:
        print("    " + str(arr2[i]))
    else:
        print("    " + str(arr2[i]) + ",")
print("]")


arr3 = create_n_dim_array_recursive(3, 2)

print("\n»> create_n_dim_array_recursive(3, 2)")
print("[")
for i in range(len(arr3)):
    print("    [")
    for j in range(len(arr3[i])):
        if j == len(arr3[i]) - 1:
            print("        " + str(arr3[i][j])+ ",")
        else:
            print("        " + str(arr3[i][j]) + ",")
    if i == len(arr3) - 1:
        print("    ]")
    else:
        print("    ],")
print("]")

