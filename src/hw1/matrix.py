from src.hw1.vector_operations import *


def check_matrices(*matrices):
    for matrix in matrices:
        if len(matrix) == 0:
            raise TypeError("Matrix must not be empty")
        matrix_columns = len(matrix[0])
        for row in matrix:
            if len(row) != matrix_columns:
                raise TypeError("Matrix rows must have same length")
            check_vectors(row)


def are_matrices_equal(*matrices):
    matrix_rows = len(matrices[0])
    matrix_columns = len(matrices[0][0])
    for matrix in matrices:
        if len(matrix) != matrix_rows or len(matrix[0]) != matrix_columns:
            raise TypeError("Matrices must have equal size")


def is_multiplication_correct(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix[0]) or len(first_matrix[0]) != len(second_matrix):
        raise TypeError("Incorrect matrices")


def sum_matrices(*matrices):
    check_matrices(*matrices)
    are_matrices_equal(*matrices)
    return [get_vector_sum(*[matrix[i] for matrix in matrices]) for i in range(len(matrices[0]))]


def transpose_matrix(matrix):
    check_matrices(matrix)
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def multiply_matrices(first_matrix, second_matrix):
    check_matrices(first_matrix, second_matrix)
    is_multiplication_correct(first_matrix, second_matrix)
    result = []
    for row in range(len(first_matrix)):
        result_row = []
        for column in range(len(second_matrix[0])):
            result_row.append(
                get_dot_product(first_matrix[row], [second_matrix[k][column] for k in range(len(second_matrix))]))
        result.append(result_row)
    return result
