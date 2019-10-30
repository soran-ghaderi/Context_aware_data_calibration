import secrets
import math
from unittest import TestCase
from re_orientation import reorientation
import numpy as np

class TestReorientation(TestCase):
    def test_reorientation(self):
        """

        :return:
        """
        teta_x = 2 * math.pi * secrets.SystemRandom().random()
        teta_y = 2 * math.pi * secrets.SystemRandom().random()
        teta_z = 2 * math.pi * secrets.SystemRandom().random()
        v = np.random.rand(3, 3)
        res = reorientation(v, teta_x, teta_y, teta_z)
        self.assertIsNone(res, "Successfully Tested.")
