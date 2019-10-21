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