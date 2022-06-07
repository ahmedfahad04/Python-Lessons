# Lab7Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        7 Question 1
# Author:     Wasif
# Version:    2021/02/16
#
# Purpose:    The purpose of the question to write a python
#             program (script) that manipulates arrays using vector arithmetic
#


from time import ctime
import numpy as np

print('\n---------------------------------------------')


# This Function verify if the size of triangle is a Positive integer
def getPosInt(prompt):
    while True:
        n = input(prompt).strip()  # take input of n

        if n != '':
            try:
                n = eval(n, {}, {})  # checking if it is an integer or not
            except:
                print("Invalid Input!")
            else:
                if type(n) is int or type(n) is float:
                    break
                else:
                    print(n, "is not a number!")
        else:
            print("Missing Input!")

    return n


# this function computes the Y values of Ellipse
def yOnEllipse(a, b, xValues):
    return b * np.sqrt(1 - xValues ** 2 / a ** 2)


# this function verify the points if it is on the Ellipse
def verifyPoints(a, b, xValues, yValues):
    return (xValues ** 2 / a ** 2 + yValues ** 2 / b ** 2) == 1


# main function
def main():
    a = getPosInt("\nEnter the length of the major axis: ")

    b = getPosInt("\nEnter the length of the minor axis: ")

    points = getPosInt("\nEnter the number of points along the major axis: ")

    X = np.linspace(0, a, points)  # array of x values
    Y = yOnEllipse(a, b, X)  # array of y values
    ON_Ellipse = verifyPoints(a, b, X, Y)  # array of the equation in form of boolean

    print("\n%2s %19s %23s" % ("X", "Y", "On Ellipse"))  # printing headlines
    for x, y, point in zip(X, Y, ON_Ellipse):
        print("%.2f\t\t\t%.10f\t\t%r" % (x, y, point))  # printing the values


# main driver program where everything executes
main()

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
