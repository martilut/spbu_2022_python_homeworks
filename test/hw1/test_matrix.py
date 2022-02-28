import pytest
from src.hw1.matrix import *


def test_check_matrices_empty():
    a_matrix = []
    with pytest.raises(TypeError):
        check_matrices(a_matrix)


def test_check_matrices_incorrect():
    a_matrix = [[1, 2], [3, 4], [5, 6, 7]]
    with pytest.raises(TypeError):
        check_matrices(a_matrix)


def test_sum_matrices_incorrect():
    a_matrix = [[1, 2], [3, 4]]
    b_matrix = [[5, 6]]
    with pytest.raises(TypeError):
        sum_matrices(a_matrix, b_matrix)


def test_sum_matrices_correct():
    a_matrix = [[1, 2], [3, 4]]
    b_matrix = [[5, 6], [7, 8]]
    assert sum_matrices(a_matrix, b_matrix) == [[6, 8], [10, 12]]


def test_sum_matrices_nonsquare():
    a_matrix = [[1, 2, 3], [3, 4, 5]]
    b_matrix = [[5, 6, 7], [7, 8, 9]]
    assert sum_matrices(a_matrix, b_matrix) == [[6, 8, 10], [10, 12, 14]]


def test_sum_matrices_many():
    a_matrix = [[1, 2], [3, 4]]
    b_matrix = [[5, 6], [7, 8]]
    c_matrix = [[9, 10], [11, 12]]
    assert sum_matrices(a_matrix, b_matrix, c_matrix) == [[15, 18], [21, 24]]


def test_transpose_matrix_square():
    a_matrix = [[1, 2], [3, 4]]
    assert transpose_matrix(a_matrix) == [[1, 3], [2, 4]]


def test_multiply_matrices_incorrect():
    a_matrix = [[1, 2], [3, 4]]
    b_matrix = [[5, 6], [7, 8], [9, 10]]
    with pytest.raises(TypeError):
        multiply_matrices(a_matrix, b_matrix)


def test_multiply_matrices_square():
    a_matrix = [[1, 2], [3, 4]]
    b_matrix = [[5, 6], [7, 8]]
    assert multiply_matrices(a_matrix, b_matrix) == [[19, 22], [43, 50]]


def test_multiply_matrices_nonsquare():
    a_matrix = [[1, 2], [3, 4], [5, 6]]
    b_matrix = [[5, 6, 7], [7, 8, 9]]
    assert multiply_matrices(a_matrix, b_matrix) == [[19, 22, 25], [43, 50, 57], [67, 78, 89]]
