import numpy as np


def fill_array():
    """
    Function creates a three-dimension array with shape and sets it to a variable.
    then fills the array elements with values using unsigned integers.
    :return: array elements with values using unsigned integer.
    """
    return np.random.randint(low=0, high=256, size=(300, 400, 5))


if __name__ == "__main__":
    print(fill_array())