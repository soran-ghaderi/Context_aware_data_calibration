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