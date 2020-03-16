import pandas as pd

ewr = pd.read_csv('ewrFlights20180516.csv')

for airln, grp in ewr.groupby(ewr['Airline']):
    print('\nairln = {}: \ngrp:'.format(airln))
    print(grp)

    if airln == 'AVIANCA':
        break

"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Demonstrates how to itereate3 over groups using
Pandas.
"""
