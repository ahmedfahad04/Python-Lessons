# Lab10Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        10 Question 1
# Author:     Wasif
# Version:    2021/04/08
#
# Purpose:    he purpose of this question is to write a python program (script) that that computes the
#             area of an ellipse using the Monte Carlo technique.
#

from time import ctime
import numpy as np
from math import pi

print('\n---------------------------------------------')


def MonteAreaEllipse(a, b, points):
    x = np.random.uniform(-a, a, points)    # random x coordinates of rectangle
    y = np.random.uniform(-b, b, points)    # random y coordinates of rectangle
    eqn = (x / a) ** 2 + (y / b) ** 2       # equation of ellipse
    
    # find how many points are inside the ellipse
    estimated_points = np.sum(eqn <= 1)

    # Monte Carlo Technique. probability of points inside the ellipse
    probability = estimated_points / points
    
    # find approximate area of ellipse using the probabilty of points inside the ellipse mulptiplying with rectangle area.
    approx_area = 4 * a * b * probability

    return approx_area, probability         # return the area and probability


def main():

    # taking input of the length of semi major axis
    a = eval(input("\nEnter the length of the semi-major axis in cm (> 0): "))
    if a <= 0:
        # boundary check
        print("The semi-major axis must be greater than zero.")
        return

    # taking input of the length of semi minor axis
    b = eval(input("\nEnter the length of the semi-minor axis in cm (> 0): "))
    if b <= 0:
        # boundary check
        print("The semi-minor axis must be greater than zero.")
        return

    # calling the MonteAreaEllipse function to calculate area and probability
    estemated_area, prob = MonteAreaEllipse(a, b, 10000000)
    
    # actual area of an ellipsse
    actual_area = pi * a * b
    
    # calculating difference between approx and actual area.
    error = abs(estemated_area - actual_area)

    # all desired output
    print("\nThe probability of a point being in the ellipse is %.6f" % prob)
    print("The approximate area of the ellipse is %.14e cm^2" % estemated_area)
    print("     The actual area of the ellipse is %.14e cm^2" % actual_area)
    print("     The error in the approximation is %e cm^2" % error)


# calling the main function
main()

# termination message
print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
