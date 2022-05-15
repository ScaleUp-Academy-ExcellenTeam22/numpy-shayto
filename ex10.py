import numpy as np


def sort_array(array):
    """
    Function sorts an along the first, last axis of an array.
    :param array: array of numbers
    :return: None
    """
    return (f"The array After Sorting the first axis:\n {np.sort(array, axis=0)}.\n "
            f"The array After Sorting the last axis:\n {np.sort(np.sort(array, axis=0), axis=1)}")


if __name__ == "__main__":
    print(sort_array(np.array([[4, 6], [2, 1]])))