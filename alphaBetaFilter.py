import numpy as np


def alphaBetaFilter(x: list, alpha: float = 1, beta: float = 0.1) -> list:
    """
    A simplified form of observer for estimation, data smoothing and control applications.

    A simplified form of observer for estimation, data smoothing and control applications.
    Algorithm summary:
    Initialize:
    Set the initial values of state estimates x and v, using prior information or additional measurements;
     otherwise, set the initial state values to zero.
    Select values of the alpha and beta correction gains.
    Update: Repeat for each time step ΔT.
    :param x: Initial sample
    :param alpha: Alpha factor
    :param beta: Beta factor
    :return: Generated results
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
    return f
