import numpy as np


def swap_rows(array):
    """
    This function creates a new array from given array swapping first and last rows
    :param array: given array
    :return: array from given array swapping first and last rows
    """
    return array[::-1]


def create_rand_array():
    """
    This function creates a 4x4 array with random values
    :return: 4x4 array with random values
    """
    array = np.arange(16, dtype='int').reshape(-1, 4)
    return array


if __name__ == "__main__":
    print(swap_rows(create_rand_array()))
