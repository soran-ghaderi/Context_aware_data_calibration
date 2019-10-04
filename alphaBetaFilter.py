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
    for i in range(n):
        xk = xk_1 + vk_1
        vk = vk_1
        rk = x[i] - xk
        xk = alpha * rk + xk
        vk = vk + (beta * rk)
        xk_1 = xk
        vk_1 = vk
        f[i] = xk