import numpy as np


def multiply(array1, array2):
    """
    This function multiplies two given arrays of same size element-by-element.
    :param array1: array of numbers
    :param array2: array of numbers
    :return: multiplied arrays of numbers
    """
    return np.multiply(array1, array2)


if __name__ == "__main__":
    first_array = np.arange(6).reshape((3, 2))
    second_array = np.arange(6).reshape((3, 2))
    print(multiply(first_array, second_array))
