import numpy as np


def vector_with_evenly_distributed_values_from_5_50():
    """
    Function creates vector with evenly_distributed values between 5 - 50
    using numpy lin-space function.
    :return: Evenly_distributed vector.
    """
    vector = np.linspace(10, 49, 5)
    return vector


if __name__ == '__main__':
    print(vector_with_evenly_distributed_values_from_5_50())
