import numpy as np


def compute_median(array):
    """
    Function computes the median of flattened given array.
    :param array: array of numbers
    :return: the median of flattened given array.
    """
    return np.median(array)


if __name__ == "__main__":
    print(compute_median(np.arange(12).reshape((2, 6))))
