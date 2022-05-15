import numpy
import numpy as np


def replace_number(matrix: numpy.ndarray, number: int, action: chr) -> numpy.ndarray:
    """
    Function to replace all numbers in a given array that are equal, less, and greater than a given number.
    :param matrix: the matrix to change its numbers.
    :param number: the number to check.
    :param action:
    """
    if action == "=":
        print(np.where(matrix == number, 80, matrix))
    elif action == "<":
        print(np.where(matrix < number, 100, matrix))
    elif action == ">":
        print(np.where(matrix > number, -10, matrix))


if __name__ == '__main__':
    array = np.random.randint(1000, size=16).reshape(4, 4)
    number_to_compare = 20
    print(array)
    replace_number(array, number_to_compare, "=")
    replace_number(array, number_to_compare, "<")
    replace_number(array, number_to_compare, ">")
