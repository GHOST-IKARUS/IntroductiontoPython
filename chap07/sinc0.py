import numpy as np


def sinc(x):
    y = np.sin(x) / x
    return y


"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Naive sinc function. Fails at x=0.
"""
