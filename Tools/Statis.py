from numpy import ndarray as arr
import numpy as np

def err_relative(x, y):
    return err_relative(np.array(x), np.array(y))


def err_relative(x: arr, y: arr):
    return np.round(np.abs((x - y)/y), 4)

