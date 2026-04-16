def create_n_dim_array_recursive(n, size):
    if n < 1:
        return []

    def helper(level):
        if level == 1:
            return [f'level {n}' for _ in range(size)]
        return [helper(level - 1) for _ in range(size)]

    arr = helper(n)

    def pretty_print(data, indent=0):
        if indent == 0:
            print("[")
        if data and isinstance(data[0], list) and data[0] and isinstance(data[0][0], list):
            for i, block in enumerate(data):
                print("    " * (indent + 1) + "[")
                for j, sub in enumerate(block):
                    print("    " * (indent + 2) + "[" + ",".join(f"'{x}'" for x in sub) + "]", end="")
                    if j < len(block) - 1:
                        print(",")
                    else:
                        print()
                print("    " * (indent + 1) + "]", end="")
                if i < len(data) - 1:
                    print(",")
                else:
                    print()
        else:
            for i, sub in enumerate(data):
                print("    " * (indent + 1) + "[" + ", ".join(f"'{x}'" for x in sub) + "]", end="")
                if i < len(data) - 1:
                    print(",")
                else:
                    print()
        if indent == 0:
            print("]")

    pretty_print(arr)
    return arr

def create_n_dim_array_iterative(n, size):
    if n < 1:
        return []

    arr = [f'level {n}' for _ in range(size)]
    for _ in range(n - 1):
        arr = [arr.copy() for _ in range(size)]

    def pretty_print(data, indent=0):
        if indent == 0:
            print("[")
        if data and isinstance(data[0], list) and data[0] and isinstance(data[0][0], list):
            for i, block in enumerate(data):
                print("    " * (indent + 1) + "[")
                for j, sub in enumerate(block):
                    print("    " * (indent + 2) + "[" + ", ".join(f"'{x}'" for x in sub) + "]", end="")
                    if j < len(block) - 1:
                        print(",")
                    else:
                        print()
                print("    " * (indent + 1) + "]", end="")
                if i < len(data) - 1:
                    print(",")
                else:
                    print()
        else:
            for i, sub in enumerate(data):
                print("    " * (indent + 1) + "[" + ", ".join(f"'{x}'" for x in sub) + "]", end="")
                if i < len(data) - 1:
                    print(",")
                else:
                    print()
        if indent == 0:
            print("]")

    pretty_print(arr)
    return arr

print("»> create_n_dim_array_recursive(2, 3)")
create_n_dim_array_recursive(2, 3)

print("\n»> create_n_dim_array_recursive(3, 2)")
create_n_dim_array_recursive(3, 2)

print("\n»> create_n_dim_array_iterative(2, 3)")
create_n_dim_array_iterative(2, 3)

print("\n»> create_n_dim_array_iterative(3, 2)")
create_n_dim_array_iterative(3, 2)
