import numpy as np


def matrix_borders_1_inside_0():
    """
    Function creates vector 10*10 size where the borders are equal to 1 and the inside equal to 0.
    :return: Vector where the borders are equal 1 and inside 0.
    """
    vector = np.ones((10, 10))
    vector[1:-1, 1:-1] = 0
    return vector


if __name__ == '__main__':
    print(matrix_borders_1_inside_0())
