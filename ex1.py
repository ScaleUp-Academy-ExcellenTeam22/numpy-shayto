import numpy as np


def change_signs_in_array_in_given_range(numpy_array, starting_range, ending_range):
    """
    Function gets a numpy array and changes the -/+ of the numbers in the array
    according to the range we get:
    :param numpy_array:(np.array)
    :param starting_range:(int) Starting place from where we want to change the numbers +/- sign.
    :param ending_range:(int) Ending place until where we want to change the numbers +/- sign.
    :return: Numpy array with different sign -/+ in range of starting_range - ending_range.
    """
    numpy_array[starting_range:ending_range + 1] *= -1
    return numpy_array


if __name__ == '__main__':
    print(np.array(range(21)))
    print(change_signs_in_array_in_given_range(np.array(range(21)), 9, 15))
