import numpy as np

dataPt, time, height, error = np.loadtxt("mydata.txt",
                                         skiprows=5,
                                         unpack=True)
np.savetxt("mydatawritten.txt",
           list(zip(dataPt, time, height, error)),
           fmt="%12.1f")

np.savetxt('mydataout.csv',
           list(zip(dataPt, time, height, error)),
           fmt="%0.1f", delimiter=",")

"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06
Scripting example with formatted print output
"""
