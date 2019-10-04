import numpy as np

def alphaBetaFilter(x, alpha, beta):
    """

    :param x:
    :param alpha:
    :param beta:
    :return:
    """
    # x = np.array(x)
    n = x.__len__()
    xk_1 = 0
    vk_1 = 0
    xk = 0
    vk = 0
    rk = 0
    f = np.zeros((n,), dtype=int)