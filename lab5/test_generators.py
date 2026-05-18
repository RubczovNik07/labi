import pytest
from generators import merge_sequences, fold_sequence


# =========================
# merge_sequences tests
# =========================

def test_chain():
    seq1 = ["a", "b"]
    seq2 = ["c"]
    seq3 = ["d"]

    result = list(merge_sequences([seq1, seq2, seq3], "chain"))
    assert result == ["a", "b", "c", "d"]


def test_zip():
    seq1 = ["a", "b"]
    seq2 = ["c", "d"]
    seq3 = ["e"]

    result = list(merge_sequences([seq1, seq2, seq3], "zip"))
    assert result == ["a", "c", "e", "b", "d"]


def test_round_robin():
    seq1 = ["a", "b"]
    seq2 = ["c"]
    seq3 = ["d", "e"]

    result = list(merge_sequences([seq1, seq2, seq3], "round_robin"))
    assert result == ["a", "c", "d", "b", "e"]


def test_invalid_strategy():
    with pytest.raises(ValueError):
        list(merge_sequences([["a"]], "wrong"))


# =========================
# fold_sequence tests
# =========================

def test_fold_strings():
    assert fold_sequence(["a", "b", "c"]) == "abc"


def test_fold_with_none():
    assert fold_sequence(["a", None, "b"]) == "ab"


def test_fold_empty():
    assert fold_sequence([]) is None


def test_fold_numbers():
    assert fold_sequence([1, 2, 3]) == [1, 2, 3]