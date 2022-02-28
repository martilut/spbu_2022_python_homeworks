from math import sqrt, acos


def check_vectors(*vectors):
    for vector in vectors:
        for coordinate in vector:
            if not isinstance(coordinate, int):
                raise TypeError("Coordinates must be int")


def are_vectors_equal(*vectors):
    vector_length = len(vectors[0])
    for vector in vectors:
        if len(vector) != vector_length:
            raise ArithmeticError("Vectors must be equal")


def get_vector_sum(*vectors):
    check_vectors(*vectors)
    are_vectors_equal(*vectors)
    result = [0] * len(vectors[0])
    for vector in vectors:
        for i in range(len(vector)):
            result[i] += vector[i]
    return result


def get_dot_product(first_vector, second_vector):
    check_vectors(first_vector, second_vector)
    are_vectors_equal(first_vector, second_vector)
    result = 0
    for i in range(len(first_vector)):
        result += first_vector[i] * second_vector[i]
    return result


def get_vector_length(vector):
    check_vectors(vector)
    answer = 0
    for coordinate in vector:
        answer += coordinate ** 2
    return sqrt(answer)


def get_degree(first_vector, second_vector):
    return acos(get_dot_product(first_vector, second_vector)
                / (get_vector_length(first_vector) * get_vector_length(second_vector)))
