import numpy as np
import time

a = np.linspace(0, 32, 10000000)
print(a)
startTime = time.process_time()
for i in range(len(a)):
    a[i] = a[i] * a[i]
endTime = time.process_time()
print(a)
print('Run time = {} seconds'.format(endTime - startTime))

"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Scripting example with formatted print output
"""
