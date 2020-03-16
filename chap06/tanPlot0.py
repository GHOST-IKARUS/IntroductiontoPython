import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0.01, 10., 0.04)
ytan = np.tan(theta)

plt.figure(figsize=(8.5, 4.2))
plt.plot(theta, ytan)
plt.savefig('figures/tanPlot0.pdf')
plt.show()

"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Simple tangent with unwanted spikes using matplotlib
"""
