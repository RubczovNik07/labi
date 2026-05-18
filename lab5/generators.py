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

    else:
        raise ValueError(f"Неизвестная стратегия: {strategy}")


# Функция свёртки
def fold_sequence(seq):

    seq = list(seq)

    if not seq:
        return None

    # filter
    seq = list(filter(lambda x: x is not None, seq))

    # строки → конкатенация
    if all(isinstance(x, str) for x in seq):
        seq = list(map(str, seq))
        return reduce(lambda a, b: a + b, seq)

    return seq


# ===== ПРИМЕР =====
if __name__ == "__main__":

    seq1 = ["a", "b"]
    seq2 = ["c", "d"]
    seq3 = ["e"]

    gen_chain = merge_sequences([seq1, seq2, seq3], "chain")
    print("chain:", list(gen_chain))

    gen_chain = merge_sequences([seq1, seq2, seq3], "chain")
    print("chain (reduce):", fold_sequence(gen_chain))

    gen_zip = merge_sequences([seq1, seq2, seq3], "zip")
    print("zip:", list(gen_zip))

    gen_zip = merge_sequences([seq1, seq2, seq3], "zip")
    print("zip (reduce):", fold_sequence(gen_zip))

    gen_rr = merge_sequences([seq1, seq2, seq3], "round_robin")
    print("round_robin:", list(gen_rr))

    gen_rr = merge_sequences([seq1, seq2, seq3], "round_robin")
    print("round_robin (reduce):", fold_sequence(gen_rr))