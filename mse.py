import math


def devMse(
        y_true: list,
        y_pred: list) -> float:
    """
    Measures the average of the squares of the errors
    :param y_true: Ground truth (correct) target values.
    :param y_pred: Estimated target values.
    :return: MSE : float
        A non-negative floating point value (the best value is 0.0)
    """
    minimum_lenth = min(y_true.__len__(), y_pred.__len__())
    summation = 0
    for i in range(minimum_lenth):
        summation = summation + math.pow((y_true[i] - y_pred[i]), 2)
    mse = summation / minimum_lenth
    return mse
