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
    # list using list comprehension
    return [(a/intervals) * n for n in range(0, intervals + 1)]


def computeYcoordinates(a, b, xValues):
    # formula is b * sqrt(( 1 - x / a) ^ 2)
    # xValues == list of X Coordinates
    return [(b * sqrt(1 - (x / a) ** 2)) for x in xValues]


def calcCircumference(a, b, intervals):
    xCoord = computeXcoordinates(a, intervals)  # list of X Coordinates
    yCoord = computeYcoordinates(a, b, xCoord)  # list of Y Coordinates

    # this four list is made for calculating sqrt((x2-x1)^2 + (y2-y1)^2)
    p = xCoord[1:]     # list of x1
    q = xCoord[:-1]    # list of x2

    r = yCoord[1:]     # list of y1
    s = yCoord[:-1]    # list of y2

    # formula for calculating circumference
    circumference = 4 * sum([sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                             for x1, x2, y1, y2 in zip(p, q, r, s)])

    print("\nThe approximate circumference of the ellipse is {:.14e} cm.".format(
        circumference))


def displayTerminationMessage():
    print("""
Programmed by Md Wasif Bin Rahman Arko
Date: %s
End of processing.""" % ctime())


# main execution point starts here
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

    print("\nThe compute time using list is %.3f seconds." % computeTime)

displayTerminationMessage()
