import numpy as np


def find_rows_and_cols_of_matrix(matrix):
    """
    Functions gets a matrix and return the amount of rows and cols.
    :param matrix:
    :return:(tuple) rows and cols of the matrix.
    """
    return np.shape(matrix)


if __name__ == '__main__':
    print(find_rows_and_cols_of_matrix([1, 2, 3, 4, 5, 6, 7]))
    print(find_rows_and_cols_of_matrix([[1, 2], [3, 4], [5, 6]]))
    print(find_rows_and_cols_of_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))