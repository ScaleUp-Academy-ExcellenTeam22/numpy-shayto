import numpy as np


def count_days(month: int, year: int):
    """
    Function counts the number of days in a specific month
    :param month: month number
    :param year: year number
    :return: number of days in that month
    """

    # December case
    if month == 12:
        end = f"{year}-{month}-31"
        begin = f"{year}-{month}-01"

    else:
        if month < 10:
            end_month = f"-0{month + 1}"
            begin_month = f"-0{month}"

        else:
            end_month = f"-{month + 1}"
            begin_month = f"-{month}"

        end = f"{year}{end_month}-01"
        begin = f"{year}{begin_month}-01"

    return np.datetime64(end) - np.datetime64(begin)


if __name__ == "__main__":
    print(count_days(2, 2016))
