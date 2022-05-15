import numpy as np
import matplotlib.pyplot as matp


def compute_coordinates():
    """
    Function computes the x and y coordinates of points on a sine curve and plots the points using matplotlib.
    This function computes the x and y coordinates for points on a sine curve and plots the points using matplotlib
    :return: None
    """
    x = np.arange(0, 3 * np.pi, 0.2)
    y = np.sin(x)
    matp.plot(x, y)
    matp.show()


if __name__ == "__main__":
    compute_coordinates()
