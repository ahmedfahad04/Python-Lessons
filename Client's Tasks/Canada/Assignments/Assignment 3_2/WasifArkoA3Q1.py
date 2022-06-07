# WasifArkoA3Q1.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        3 Question 1
# Author:     Wasif Arko
# Version:    2021/03/15
#
# Purpose:    The purpose of the question to write a python program(script)
#             to calculating the approximate circumference of an ellipse.


from time import ctime
from math import sqrt
import timeit


def getNonNegativeInt(promt):
    while True:

        n = input(promt).strip()

        if n != '':
            try:
                n = eval(n, {}, {})
            except:
                print("Invalid input!")
            else:
                if type(n) is int:
                    if n >= 0:
                        break
                    else:
                        print("{} must not be an negative!".format(n))
                else:
                    print("{} must be an integer!".format(n))
        else:
            print("Missing Input!")

    return n


def computeXcoordinates(width, intervals):
    # list using list comprehension
    return [(-1*(width/2) + (width/intervals)*i)for i in range(0, intervals + 1)]


def computeYcoordinates(xValues):
    # xValues == list of X Coordinates

    top_portion = [sqrt(1-(abs(x)-1)**2) for x in xValues]
    bottom_portion = [-3*sqrt(1-sqrt(abs(x)/2.0)) for x in xValues]
    return top_portion, bottom_portion


def computeArea(width, intervals):
    xCoord = computeXcoordinates(width, intervals)  # list of X Coordinates
    yCoord_1, yCoord_2 = computeYcoordinates(xCoord)  # list of Y Coordinates

    # calculating area of upper portion:
    diff_xcoord = xCoord[1]-xCoord[0]
    summation = sum(yCoord_1[1:-1])
    top_area = (diff_xcoord)*(0.5*(yCoord_1[0]+yCoord_1[-1])+summation)

    # calculating areaa of lower portion
    diff_xcoord = xCoord[1]-xCoord[0]
    summation = sum(yCoord_2[1:-1])
    bottom_area = (diff_xcoord)*(0.5*(yCoord_2[0]+yCoord_2[-1])+summation)

    total_area = 2*top_area + 2*bottom_area
    print(
        "\nThe approximate area of the heart is {:.14e} cm^2.".format(total_area))


def displayTerminationMessage():
    print("""
Programmed by <Name>
Date: %s
End of processing.""" % ctime())


# main execution point starts here
print("-" * 50)
width = 4

while True:
    intervals = getNonNegativeInt(
        "\nEnter the numbr of interval (0 to quit): ")

    if int(intervals) == 0:
        break

    t = timeit.Timer('computeArea(width, intervals)',
                     'from __main__ import computeArea, intervals, width')

    computeTime = t.timeit(1)
    print("Compute time using lists is %.3f seconds." % computeTime)

displayTerminationMessage()
