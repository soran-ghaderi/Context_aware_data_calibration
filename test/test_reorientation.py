import os
import math
from unittest import TestCase
from reOrientation import reorientation
import numpy as np


class TestReorientation(TestCase):
    def test_reorientation(self):
        '''

        :return: Whether the 'res' is None or not?
        '''
        teta_x = 2 * math.pi * float(os.urandom(10) / 10)
        teta_y = 2 * math.pi * float(os.urandom(10) / 10)
        teta_z = 2 * math.pi * float(os.urandom(10) / 10)
        v = np.random.rand(3, 3)
        res = reorientation(v, teta_x, teta_y, teta_z)
        self.assertIsNone(res, "Successfully Tested.")
