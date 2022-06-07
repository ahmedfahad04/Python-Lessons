# WasifArkoA3Q3.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        3 Question 3
# Author:     Wasif Arko
# Version:    2021/03/15
#
# Purpose:    The purpose of the question to write a python program(script)
#             to calculating the approximate circumference of an ellipse.


from time import ctime
import numpy as np
import timeit


def getPositiveNumber(promt):
    while True:

        n = input(promt).strip()

        if n != '':
            try:
                n = eval(n, {}, {})
            except:
                print("{} is not valid!".format(n))
            else:
                if type(n) is int or type(n) is float:
                    if n >= 0:
                        break
                    else:
                        print(n, "is less than zero!")
                else:
                    print(n, " is not a number!")
        else:
            print("Missing Input!")

    return n


def computeXcoordinates(a, intervals):
    return np.linspace(0, a, intervals + 1)  # array


def computeYcoordinates(a, b, xValues):
    # formula is b * sqrt(( 1 - x / a) ^ 2)
    # array using vector arithmetic
    return (b * np.sqrt(1 - (xValues / a) ** 2))


def calcCircumference(a, b, intervals):
    xCoord = computeXcoordinates(a, intervals)  # array of X Coordinates
    yCoord = computeYcoordinates(a, b, xCoord)  # array of Y Coordinates

    # this four array is made for calculating sqrt((x2-x1)^2 + (y2-y1)^2)
    x1 = xCoord[1:]     # array of x1
    x2 = xCoord[:-1]   # array of x2

    y1 = yCoord[1:]     # array of y1
    y2 = yCoord[:-1]    # array of y2

    # formula for calculating circumference using "Vector Arithmetic"
    circumference = 4 * sum(np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))

    print("\nThe approximate circumference of the ellipse is {:.14e} cm.".format(
        circumference))


def displayTerminationMessage():
    print("""
Programmed by Md Wasif Bin Rahman Arko
Date: %s
End of processing.""" % ctime())


# main execution point
print("-" * 50)
print("To terminate the program enter 0 after any prompt")

while True:
    a = getPositiveNumber(
        "\nEnter the length of the semi-major axis in cm (> 0): ")
    if int(a) == 0:
        break

    b = getPositiveNumber(
        "\nEnter the length of the semi-minor axis in cm (> 0): ")
    if int(b) == 0:
        break

    intervals = getPositiveNumber("\nEnter the number of intervals (> 0): ")
    if int(intervals) == 0:
        break

    t = timeit.Timer('calcCircumference(a, b, intervals)',
                     'from __main__ import calcCircumference, a, b, intervals')
    computeTime = t.timeit(1)

    print("\nThe compute time using vector arithmetic is %.3f seconds." %
          computeTime)

displayTerminationMessage()
