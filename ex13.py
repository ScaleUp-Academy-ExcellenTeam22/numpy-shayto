import numpy as np


def convert_arrays(array1, array2):
    """
    Function converts (in sequence depth wise (along third axis)) two 1-D arrays into a 2-D array.
    :param array1: 1-D array
    :param array2: 1-D array
    :return: 2-D array
    """
    return np.dstack((array1, array2))


if __name__ == "__main__":
    print(convert_arrays(np.array([10, 20, 30]), np.array([40, 50, 60])))
