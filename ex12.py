import numpy as np


def remove_dimension(shape):
    """
    Function removes single-dimensional entries from a specified shape.
    @:arg shape: array or list
    :return: The given shape without single-dimensional entries
    """
    return np.squeeze(shape).shape


if __name__ == "__main__":
    np.zeros((3, 1, 4))
    print(remove_dimension(np.zeros((3, 1, 4))))
