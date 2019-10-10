import math

def devMse(x, y):
    """
    Mean squared error division.
    :param x:
    :param y:
    :return: MSE result
    """
    # x = np.array(x)
    # y = np.array(y)
    n = min(x.__len__(), y.__len__())
    summation = 0
    for i in range(n):
        summation = summation + math.pow((x[i] - y[i]), 2)
    summation = summation / n
    return summation