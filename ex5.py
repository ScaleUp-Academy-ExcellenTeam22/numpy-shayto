import numpy as np


def add_vector_to_each_row(matrix, vector):
    """
    Function adds a vector to each row of the matrix.
    :param matrix:(np array) Given matrix.
    :param vector:(list) Given vector to add to each row in the matrix.
    :return: New Matrix: the new matrix after adding the vector to each row of the matrix.
    """
    result = np.empty_like(matrix)
    for i in range(len(matrix)):
        result[i, :] = matrix[i, :] + vector
    return result


if __name__ == '__main__':
    print(add_vector_to_each_row([1, 2], np.array([[4, 5], [6, 7], [8, 9]])))
