import numpy as np
import math
import pandas as pd
import random as rd
from sklearn.metrics import mean_squared_error as mse
from dtaidistance import dtw

from alphaBetaFilter import alphaBetaFilter
from devMse import devMse
from reOrientation import reorientation

input_data = pd.read_excel(r'input.xlsx')

# --------------------------------
summation = np.zeros((6,), dtype=int)
mse_sum = np.zeros((6,), dtype=int)
b_mse_sum = np.zeros((6,), dtype=int)
dtw_sum = np.zeros((6,), dtype=int)
b_dtw_sum = np.zeros((6,), dtype=int)
iter = 0
index = 330
# --------------------------------
acc = np.array([input_data['ACCELEROMETER X (m/sÂ²)']
                   , input_data['ACCELEROMETER Y (m/sÂ²)']
                   , input_data['ACCELEROMETER Z (m/sÂ²)']])

mag = np.array([input_data['MAGNETIC FIELD X (Î¼T)']
                   , input_data['MAGNETIC FIELD Y (Î¼T)']
                   , input_data['MAGNETIC FIELD Z (Î¼T)']])

speed = np.array([input_data['LOCATION Speed ( Kmh)']])


# --------------------------------
def prand():
    r = rd.random() / 2 + 0.5
    return r


def increaseSpeed(speed):
    n = speed.__len__()
    c = 0
    for i in range(n - 1):
        c = speed(i + 1) - speed(i)
    c = c / (n - 1)
    if c > 0:
        r = 1
    else:
        r = -1
    return r


def makeYZero(ay, az):
    avgy = np.mean(ay)
    avgz = np.mean(az)
    teta_x = math.atan(avgy / avgz)
    if abs(teta_x) < 0.1:
        teta_x = 0
    return teta_x


def makeXZero(ax, az):
    avgx = np.mean(ax)
    avgz = np.mean(az)
    teta_y = math.atan(avgx / avgz)
    if abs(teta_y) < 0.1:
        teta_y = 0
    return teta_y


# --------------------------------
for k in range(100):
    teta_x = 2 * math.pi * rd.random()
    teta_y = 2 * math.pi * rd.random()
    teta_z = 2 * math.pi * rd.random()
    print("random degrees:\nteta_x: {}\nteta_y: {}\nteta_z: {}\n".format(teta_x, teta_y, teta_z))
    oAcc = reorientation(acc, teta_x, teta_y, teta_z)
    oMag = reorientation(mag, teta_x, teta_y, teta_z)

    for i in range(3):
        b_mse_sum[i] = b_mse_sum[i] + devMse(alphaBetaFilter(oAcc[i], 0.01, 0), alphaBetaFilter(acc[i], 0.01, 0))

    for i in range(3):
        b_mse_sum[i + 3] = b_mse_sum[i + 3] + mse(oMag[i], mag[i])

    teta = makeYZero(oAcc[1, index:index + 50], oAcc[2, index:index + 50])
    oAcc = reorientation(oAcc, teta, 0, 0)
    oMag = reorientation(oMag, teta, 0, 0)
    print('first teta: {}'.format(teta))

    teta = makeXZero(oAcc[0, index:index + 50], oAcc[2, index:index + 50])
    oAcc = reorientation(oAcc, teta, 0, 0)
    oMag = reorientation(oMag, teta, 0, 0)
    print('second teta: {}'.format(teta))

    if np.mean(oAcc[2]) < 0:
        oAcc = reorientation(oAcc, 0, math.pi, 0)
        oMag = reorientation(oMag, 0, math.pi, 0)

    # Final phase:
    teta = math.atan(np.mean(oAcc[0, index:index + 20]) / np.mean(oAcc[1, index:index + 20]))
    print('second teta: {}\n'.format(teta))
    oAcc = reorientation(oAcc, 0, 0, teta)
    oMag = reorientation(oMag, 0, 0, teta)
    if increaseSpeed(speed[index:index + 20] * np.mean(oAcc[1])) > 0:
        oAcc = reorientation(oAcc, 0, 0, math.pi)
        oMag = reorientation(oMag, 0, 0, math.pi)
        print("turned")
    # plt.plot(mag[0])
    # plt.plot(oMag[0])
    # plt.show()
    print("final cross correlation is: {}".format((np.mean(np.correlate(mag[1], oMag[1])) + 1) / 2))
    print(np.mean(oAcc[2]))
    iter = iter + 1
    for i in range(3):
        summation[i] = (np.mean(np.correlate(alphaBetaFilter(acc[i], 0.01, 0),
                                             alphaBetaFilter(oAcc[i], 0.01, 0)))) / 2 + summation[i]
        mse_sum[i] = mse_sum[i] + devMse(alphaBetaFilter(acc[i], 0.01, 0), alphaBetaFilter(oAcc[i], 0.01, 0))
        dtw_sum[i] = dtw.distance(alphaBetaFilter(acc[i], 0.01, 0), alphaBetaFilter(oAcc[i], 0.01, 0)) + dtw_sum[i]

    for i in range(3):
        summation[i + 3] = (np.mean(np.correlate(mag[i], oMag[i])) + 1) / 2 + summation[i + 3]
        mse_sum[i + 3] = mse_sum[i + 3] + devMse(mag[i], oMag[i])
        dtw_sum[i + 3] = dtw.distance(mag[i], oMag[i]) + dtw_sum[i + 3]
    print(iter)
    print('====&final result&=====')
    print('cross correlation:')
    for i in range(6):
        print(i, ') ', summation[i] / iter)
    print('MSE:')
    for i in range(6):
        print(i, ') ', mse_sum[i] / b_mse_sum[i])
    print('DTW:')
    for i in range(6):
        print(i, ') ', dtw_sum[i] / iter)
