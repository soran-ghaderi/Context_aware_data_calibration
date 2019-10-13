import math


def devMse(
        y_true: list = [],
        y_pred: list = []) -> float:
    """
    Measures the average of the squares of the errors
    :param y_true: Ground truth (correct) target values.
    :param y_pred: Estimated target values.
    :return: MSE result
    """
    n = min(x.__len__(), y.__len__())
    summation = 0
    for i in range(n):
        summation = summation + math.pow((y_true[i] - y_pred[i]), 2)
    mse = summation / n
    return mse
