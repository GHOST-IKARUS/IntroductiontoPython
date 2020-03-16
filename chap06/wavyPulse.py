import numpy as np
import matplotlib.pyplot as plt

# read data from file
xdata, ydata = np.loadtxt('wavyPulseData.txt', unpack=True)

# create x and y arrays for theory
x = np.linspace(-10., 10., 200)
y = np.sin(x) * np.exp(-(x / 5.0) ** 2)

# create plot
plt.figure(1, figsize=(6, 4))
plt.plot(x, y, 'g-', label='theory')
plt.plot(xdata, ydata, 'bo', label="data")
plt.xlabel('x')
plt.ylabel('transverse displacement')
plt.legend(loc='upper right', title='legend')
plt.axhline(color='gray', zorder=-1)
plt.axvline(color='gray', zorder=-1)

# save plot to file
plt.savefig('figures/WavyPulse.pdf')

# display plot on screen
plt.show()

"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Plot with symbols and lines using matplotlib
"""
