def deriv(f, x, h=1.e-9, *params):
    return (f(x + h, *params) - f(x - h, *params)) / (2. * h)


"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Calculate derivative of function f with parameters
"""
