import numpy as np


def multiply(array1, array2):
    """
    This function multiplies two given arrays of same size element-by-element.
    :param array1: array of numbers
    :param array2: array of numbers
    :return: multiplied array of numbers
    """
    return np.multiply(array1, array2)


if __name__ == "__main__":
    matrix1 = np.random.randint(9, size=16).reshape(4, 4)
    matrix2 = np.random.randint(9, size=16).reshape(4, 4)
    print(matrix1)
    print(matrix2)
    print(multiply(matrix1, matrix2))
