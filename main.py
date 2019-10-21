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

acc = np.array([input_data['ACCELEROMETER X (m/sÂ²)']
                   , input_data['ACCELEROMETER Y (m/sÂ²)']
                   , input_data['ACCELEROMETER Z (m/sÂ²)']])

mag = np.array([input_data['MAGNETIC FIELD X (Î¼T)']
                   , input_data['MAGNETIC FIELD Y (Î¼T)']
                   , input_data['MAGNETIC FIELD Z (Î¼T)']])