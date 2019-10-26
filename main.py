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

speed = np.array([input_data['LOCATION Speed ( Kmh)']])


def increaseSpeed(speed: list) -> int:
    """
    Returns 1 if the overal speed has increased otherwise returns -1.
    :param speed: A list of speeds at each point
    :return: Has the speed increased or not (1, -1)
    """
    number_of_points = speed.__len__()
    speed_change = 0
    for i in range(number_of_points - 1):
        speed_change = speed(i + 1) - speed(i)
    speed_change = speed_change / (number_of_points - 1)
    if speed_change > 0:
        has_increase = 1
    else:
        has_increase = -1
    return has_increase

def makeYZero(ay: list, az: list) -> float:
    """
    Calculate theta_x angle
    :param ay: A list of Y-axis accelerations
    :param az: A list of Z-axis accelerations
    :return: Theta_x angle
    """
    avgy = np.mean(ay)
    avgz = np.mean(az)
    theta_x = math.atan(avgy / avgz)
    if abs(theta_x) < 0.1:
        theta_x = 0
    return theta_x

def makeXZero(ax, az):
    """

    :param ax:
    :param az:
    :return:
    """