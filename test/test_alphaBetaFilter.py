from unittest import TestCase
import numpy as np
from alpha_beta_filter import alphaBetaFilter

class TestAlphaBetaFilter(TestCase):
    def test_alphaBetaFilter(self):
        """

        :return:
        """
        x = np.random.rand(6, 1)
        alpha = np.random.rand()
        beta = np.random.rand()
        res = alphaBetaFilter(x, alpha, beta)