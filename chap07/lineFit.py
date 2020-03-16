def lineFit(x, y):
    ''' Returns slope and y-intercept of linear fit to (x,y)
    data set'''
    xavg = x.mean()
    slope = (y * (x - xavg)).sum() / (x * (x - xavg)).sum()
    yint = y.mean() - slope * xavg
    return slope, yint


"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Calculate derivative of function f with parameters
contained in a dictionary
"""
