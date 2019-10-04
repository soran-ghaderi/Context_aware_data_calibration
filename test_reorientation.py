import math
from unittest import TestCase
from reOrientation import reorientation
import numpy as np

import random as rd


class TestReorientation(TestCase):
    def test_reorientation(self):
        teta_x = 2 * math.pi * rd.random()
        teta_y = 2 * math.pi * rd.random()
        teta_z = 2 * math.pi * rd.random()
        v = np.random.rand(3, 3)
        res = reorientation(v, teta_x, teta_y, teta_z)
        self.assertIsNone(res, "Successfully Tested.")