import numpy as np


def combine_array(one_D_array, two_D_array):
    """
    Function combines a one and a two-dimensional array together and displays their elements.
    :param one_D_array:  one dimensional array
    :param two_D_array:  two-dimensional array
    :return:
    """
    for x, y in np.nditer([one_D_array, two_D_array]):
        print(f" {x} : {y}")


if __name__ == "__main__":
    combine_array(np.arange(4), np.arange(8).reshape(2,4))
