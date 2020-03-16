import numpy as np


def sinc(x):
    if x == 0.0:
        y = 1.0
    else:
        y = np.sin(x) / x
    return y


"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Naive sinc function that works for single
variables but not for NumPy arrays
"""
