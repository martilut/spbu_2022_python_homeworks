import pytest
from src.hw1.vector_operations import *


def test_check_vectors():
    a_vector = [1, 2, 3, 4, "a", 5]
    with pytest.raises(TypeError):
        check_vectors(a_vector)


def test_get_vector_sum_error():
    a_vector = [1, 2, 3, 4, 5]
    c_vector = [11, 12, 13]
    with pytest.raises(ArithmeticError):
        get_vector_sum(a_vector, c_vector)


def test_get_vector_sum_right():
    a_vector = [1, 2, 3]
    b_vector = [6, 7, 8]
    assert get_vector_sum(a_vector, b_vector) == [7, 9, 11]


def test_get_dot_product_error():
    a_vector = [1, 2, 3, 4, 5]
    c_vector = [11, 12, 13]
    with pytest.raises(ArithmeticError):
        get_dot_product(a_vector, c_vector)


def test_get_dot_product_right():
    a_vector = [1, 2, 3]
    b_vector = [6, 7, 8]
    assert get_dot_product(a_vector, b_vector) == 44


def test_get_vector_length():
    vector = [5, 100, 6]
    assert get_vector_length(vector) == sqrt(10061)


def test_get_degree():
    a_vector = [1, 0, 0]
    b_vector = [0, 2, 0]
    assert get_degree(a_vector, b_vector) == acos(0)
