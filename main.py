import secrets
import numpy as np
import math
import pandas as pd
from sklearn.metrics import mean_squared_error as mse
from dtaidistance import dtw

from alphaBetaFilter import alphaBetaFilter
from devMse import devMse
from reOrientation import reorientation

input_data = pd.read_excel(r'input.xlsx')

summation = np.zeros((6,), dtype=int)
mse_sum = np.zeros((6,), dtype=int)
b_mse_sum = np.zeros((6,), dtype=int)
dtw_sum = np.zeros((6,), dtype=int)
b_dtw_sum = np.zeros((6,), dtype=int)
iter_num = 0
index = 330