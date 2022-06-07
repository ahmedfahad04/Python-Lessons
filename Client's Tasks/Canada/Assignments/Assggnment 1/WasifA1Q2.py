# WasifA1Q2.py
#
# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 2
# Author:     Wasif 
# Version:    2021/02/10
#
# Purpose:    The purpose of the program is to write a program that computes the approximate value of e^ix 
#             where x>0 and i = sqrt(-1). It is obvious that e^ix may have real and imaginary parts.
#             Your program must get the maximum acceptable tolerance for both real and imaginary part of 
#             result in input and the variable of x.
#
# tolerance = Acceptable Tolerance entered by uer
# degree = Angle in Degree unit
# x = Angle in Radian unit
# exponent = Stores the value of e^ix
# actual_real = Stores the Real part's value of python calculated e^ix
# actual_imaginary = Stores the Imaginary part's of python calculated e^ix
# actual_tolerance_real = Difference between actual_real and user defined cosine function
# actual_tolerance_imaginary = Difference between actual_imaginary and user defined sine function
# factor = factorial of n
# sine = User defined sin function
# cosine = User defined cos function
# term = Holds the value of angle(radian)
# xSquared = Holds Square value of angle(radian)
# count1 = Total terms for calculating sine value
# count2 = Total terms for calculating cosine value

from math import pi, sin, cos
import cmath
from time import ctime
print("\n-----------------------------------------------------------")

tolerance = float(input("Enter the acceptable tollerance: "))
degree = float(input("Enter an angle in degree: "))

#degree to radian
x = degree * pi / 180

# python exponent function and its real and imaginary parts
exponent = cmath.exp(complex(0.0,x))
actual_real = exponent.real
actual_imaginary = exponent.imag


#estimating sin(x) value
factor = 2
sine = 0.0
term = x
xSquared = x*x
count1 = 1
while abs(term) > tolerance:
    sine += term
    term = -term * (xSquared / (factor * (factor+1)))
    factor += 2
    count1+=1
#loop ends

#estimating cos(x) value
factor = 2
cosine = 0.0
term = 1.0
xSquared = x*x
count2 = 1
while abs(term) > tolerance:
    cosine += term
    term = -term * xSquared / (factor * (factor-1))
    factor += 2
    count2+=1
#loop ends
 
    
#calculating tolerance
actual_tolerance_real = actual_real - cosine
actual_tolerance_imaginary = actual_imaginary - sine    
    

print("\nPython's value of e^ix(%.2f) = %.15f + %.15f i\n" % (degree, actual_real, actual_imaginary)) 
print("Approximate value of e^ix(%.2f) = %.15f + %.15f i\n" % (degree, cosine, sine))
print("Number of terms %d for real part and %d for imaginary part\n" % (count1, count2))
print("Tolerance= %.15f + %.15f i\n" % (actual_tolerance_real , actual_tolerance_imaginary))

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
