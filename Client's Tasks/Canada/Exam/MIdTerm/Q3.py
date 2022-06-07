# WasifA1Q2.py
#
# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 2
# Author:     Wasif
# Version:    2021/02/04
#

from math import cos, pi, tan, sqrt
from time import ctime
import numpy as np


def trajectory(a, b, c, distance, interval):
    # k = distance / interval
    x = np.linspace(0, distance, interval)
    # x = [k * i for i in range(0, interval + 1)]
    y = [(a * x ** 2 + b * x + c) for x in x]

    return x, y


while True:
    intervals = int(input("\nEnter the number of intervals (<=0 to quit): "))
    if intervals <= 0:
        break

    degree = float(input("\nEnter the launch angle of the projectile (> 0): "))
    if degree <= 0:
        print("\nThe launch angle, {}, must be greater than zero!".format(degree))
        continue

    # radian = (pi * degree) / 180

    a = -9.81 / (2 * (25.25 * 25.25) * (cos(degree) ** 2))
    # print(a)
    b = tan(degree)
    # print(b)
    c = 2.1
    dist = ((-b - sqrt((b ** 2) - 4 * a * c)) / 2 * a)
    # print(dist)

    xCoord, yCoord = trajectory(a, b, c, dist, intervals)
    print("X Coordinate  Y Coordinate")
    for x, y in zip(xCoord, yCoord):
        print("%12.4f %12.4f" % (x, y))

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
