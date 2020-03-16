"""Calculates time, gallons of gas used, and cost of gasoline
for a trip"""

distance = input("Input trip distance (miles): ")
distance = float(distance)

mpg = 30.             # car mileage
speed = 60.           # average speed
costPerGallon = 3.05  # price of gasoline

time = distance / speed
gallons = distance / mpg
cost = gallons * costPerGallon
print(time, gallons, cost)

"""
Introduction to Python
by Zekrifa DMS
Code last edited: 2018-01-06

Second scripting example
"""
