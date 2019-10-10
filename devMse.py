import math

def devMse(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    # x = np.array(x)
    # y = np.array(y)
    n = min(x.__len__(), y.__len__())
    summation = 0
    for i in range(n):
        summation = summation + math.pow((x[i] - y[i]), 2)
    summation = summation / n
    return summation