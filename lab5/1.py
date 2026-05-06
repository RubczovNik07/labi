from functools import reduce
from itertools import zip_longest

# Генератор объединения последовательностей
def merge_sequences(seqs, strategy="chain"):
    if strategy == "chain":
        for seq in seqs:
            for item in seq:
                yield item

    elif strategy == "zip":
        for items in zip_longest(*seqs, fillvalue=None):
            for item in items:
                if item is not None:
                    yield item

    elif strategy == "round_robin":
        seqs = [iter(s) for s in seqs]
        while seqs:
            next_seqs = []
            for it in seqs:
                try:
                    yield next(it)
                    next_seqs.append(it)
                except StopIteration:
                    continue
            seqs = next_seqs

# Функция свёртки по типу данных
def fold_sequence(seq):
    seq = list(seq)

    if not seq:
        return None

    # filter
    seq = list(filter(lambda x: x is not None, seq))

    # числа → сумма
    if all(isinstance(x, (int, float)) for x in seq):
        seq = list(map(float, seq))  # map
        return reduce(lambda a, b: a + b, seq)

    # строки → склейка
    elif all(isinstance(x, str) for x in seq):
        seq = list(map(str, seq))  # map
        return reduce(lambda a, b: a + b, seq)

    # иначе
    else:
        return list(map(str, filter(lambda x: x is not None, seq)))

# ===== ПРИМЕРЫ =====

seq1 = ["a", "b"]
seq2 = ["c", "d"]
seq3 = ["e"]

# --- chain ---
gen_chain = merge_sequences([seq1, seq2, seq3], strategy="chain")
result_chain = fold_sequence(gen_chain)
print("chain:", result_chain)

# --- zip ---
gen_zip = merge_sequences([seq1, seq2, seq3], strategy="zip")
result_zip = fold_sequence(gen_zip)
print("zip:", result_zip)

# --- round_robin (у тебя уже был, оставим для полноты)
gen_rr = merge_sequences([seq1, seq2, seq3], strategy="round_robin")
result_rr = fold_sequence(gen_rr)
print("round_robin:", result_rr)
