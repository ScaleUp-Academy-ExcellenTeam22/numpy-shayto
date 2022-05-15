import numpy as np


def sort_student(id_array, height_array):
    """
    Function sorts the students id with increasing height of the students from given students id and height.
    :param id_array: array of id
    :param height_array: array of heights
    :return: none
    """
    indices = np.lexsort((id_array, height_array))
    for index in indices:
        print(id_array[index], height_array[index])


if __name__ == "__main__":
    student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
    student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])
    sort_student(student_id, student_height)