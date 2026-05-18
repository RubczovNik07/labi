import pytest

from recursion import calculate_yk_recursive
from recursion import calculate_yk_iterative


def test_recursive_1():

    assert calculate_yk_recursive(2, 1) == 1.0


def test_recursive_2():

    assert calculate_yk_recursive(2, 3) == 64.0


def test_iterative_1():

    assert calculate_yk_iterative(2, 2) == 4.0


def test_iterative_2():

    assert calculate_yk_iterative(3, 2) == 20.25


def test_recursive_error():

    with pytest.raises(ValueError):

        calculate_yk_recursive(0, 1)


def test_iterative_error():

    with pytest.raises(ValueError):

        calculate_yk_iterative(0, 1)