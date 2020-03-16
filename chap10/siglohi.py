def siglohi(x, x0=0, n=2):
    xplus = x[x > x0] - x0
    xminus = x0 - x[x < x0]
    sigplus = ((xplus ** n).mean()) ** (1 / n)
    sigminus = ((xminus ** n).mean()) ** (1 / n)
    return sigminus, sigplus


"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Function calculating the one-sided widths of a
data distribution.
"""
