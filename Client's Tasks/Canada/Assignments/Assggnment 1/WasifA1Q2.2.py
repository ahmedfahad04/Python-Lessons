# WasifA1Q2.py
#
# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 2
# Author:     Wasif 
# Version:    2021/02/04
#
# Purpose:    The purpose of the program is to write a program that computes the approximate value of e^ix 
#             where x>0 and i = sqrt(-1). It is obvious that e^ix may have real and imaginary parts.
#             Your program must get the maximum acceptable tolerance for both real and imaginary part of 
#             result in input and the variable of x.

# tolerance = Acceptable Tolerance entered by uer
# degree_angle = Angle in Degree unit
# radian_angle = Angle in Radian unit
# k = Stores the value of e^ix
# actual_real = Stores the value of the Real part of python calculated e^ix
# actual_imaginary = Stores the value of the Imaginary part of python calculated e^ix
# actual_tolerance_real = Tolerance of the Real part of user calculated e^ix function
# actual_tolerance_imaginary = Tolarence of the Imaginary part of user calculated e^ix function
# term_real = Number of terms of the Real part of user calculated e^ix function
# term_imaginary = Number of terms of the Imaginary part of user calculated e^ix function
# ans = It holds the calculated sin/cos value in the following function
# check = It mainly decide where we need to put +/- sign
# term = how many terms to be calculated


import cmath
import math
from time import ctime
print("\n-----------------------------------------------------------")

def cos(angle, term):

    ans = 0
    check = 2
        
    for i in range(0, 2*(term-1), 2):
        fact = float(math.factorial(i))
        
        if check%2==0:
            ans += ((angle)**i/fact)
        else:
            ans += -1*((angle)**i/fact)
         
        check += 1
            
    return ans

        
def sin(angle, term):

    ans = 0
    check = 2
        
    for i in range(1, 2*(term-1), 2):
        fact = float(math.factorial(i))
        
        if check%2==0:
            ans += (((angle)**i)/fact)
        else:
            ans += -1*(((angle)**i)/fact)
        
       
        check += 1
    
    return ans
    

tolerance = float(input("Enter the acceptable tollerance: "))
degree_angle = float(input("Enter an angle in degree: "))

radian_angle = math.radians(degree_angle)

print("\nAngle in radians = %.6f, angle in degress = %.2f\n" % (radian_angle, degree_angle))

k = cmath.exp(complex(0.0,radian_angle))

actual_real = k.real
actual_imaginary = k.imag

print("Python's value of e^ix(%.2f) = %.15f + %.15f i\n" % (degree_angle, actual_real, actual_imaginary))


actual_tolerance_real = 0
actual_tolerance_imaginary = 0
term_real = 0
term_imaginary = 0
    
    
for i in range(1,100,1):
    actual_tolerance_real = actual_real - cos(radian_angle, i)
    term_real += 1
    if abs(actual_tolerance_real) <= tolerance:
        break
   

for i in range(1,100,1):
    actual_tolerance_imaginary = actual_imaginary - sin(radian_angle, i)
    term_imaginary += 1
    if abs(actual_tolerance_imaginary) <= tolerance:
        break
    
print("Approximate value of e^ix(%.2f) = %.15f + %.15f i\n" % (degree_angle, cos(radian_angle,term_real), sin(radian_angle, term_imaginary)))
print("Number of terms %d for real part and %d for imaginary part\n" % (term_real, term_imaginary))
print("Tolerance= %.15f + %.15f i\n" % (actual_tolerance_real , actual_tolerance_imaginary))


print("""
Programmed by Wasif
Date: %s
End of processing."""% ctime())
      

