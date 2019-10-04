import math


def devMse(x, y):
    # x = np.array(x)
    # y = np.array(y)
    n = min(x.__len__(), y.__len__())
    sum = 0
    for i in range(n):
        sum = sum + math.pow((x[i] - y[i]), 2)

    sum = sum / n
    return sum
