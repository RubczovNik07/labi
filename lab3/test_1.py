from arrays import create_n_dim_array_recursive
from arrays import create_n_dim_array_iterative


def test_recursive_2d():

    expected = [
        ['level 2', 'level 2', 'level 2'],
        ['level 2', 'level 2', 'level 2'],
        ['level 2', 'level 2', 'level 2']
    ]

    assert create_n_dim_array_recursive(2, 3) == expected


def test_recursive_3d():

    expected = [
        [
            ['level 3', 'level 3'],
            ['level 3', 'level 3']
        ],

        [
            ['level 3', 'level 3'],
            ['level 3', 'level 3']
        ]
    ]

    assert create_n_dim_array_recursive(3, 2) == expected


def test_iterative_2d():

    expected = [
        ['level 2', 'level 2', 'level 2'],
        ['level 2', 'level 2', 'level 2'],
        ['level 2', 'level 2', 'level 2']
    ]

    assert create_n_dim_array_iterative(2, 3) == expected


def test_iterative_3d():

    expected = [
        [
            ['level 3', 'level 3'],
            ['level 3', 'level 3']
        ],

        [
            ['level 3', 'level 3'],
            ['level 3', 'level 3']
        ]
    ]

    assert create_n_dim_array_iterative(3, 2) == expected


def test_recursive_empty():

    assert create_n_dim_array_recursive(0, 3) == []


def test_iterative_empty():

    assert create_n_dim_array_iterative(0, 3) == []