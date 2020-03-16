from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

fig = Figure(figsize=(6, 4))
canvas = FigureCanvas(fig)
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 2, 3, 4, 3, 4, 5])
ax.set_title('A simple plot')
ax.grid(True)
ax.set_xlabel('time')
ax.set_ylabel('volts')
canvas.print_figure('figures/oopTest.pdf')
canvas.show()

"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Plottingxample using only OOP (without pyplot) in
matplotlib
"""
