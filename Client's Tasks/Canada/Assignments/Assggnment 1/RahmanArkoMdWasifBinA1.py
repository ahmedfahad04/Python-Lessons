# RahmanArkoMdWasifBinA1Q1.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 1
# Author:     Md Wasif Bin Rahman Arko
# Version:    2021/02/03
#
# Purpose:    The purpose of the program is to get
#             an integer number from input, reverse the order of its
#             digits and print the result in the output.
#
# var - the use / meaning of this varible 
#          
# number = the number which will be examined
# digits = this list holds all the single digits of given number
# num_of_digits = total number of digits in a number
# j = temporary variable hold the remainder
# power = used for indicating power of 10 while creating the reverse number
# reverse_num = holds the reverse number


from time import ctime

print("\n-----------------------------------------------------------")

number = int(input("Enter an Integer Number: "))  # taking new number input

digits = []  # stores the digits as list
num_of_digits = 0  # calculates the length of number using len of list

# this loop extracts the digits from given number and append it in 'digits' list
while True:
    j = int(number % 10)  # takes the division reminder
    digits.append(j)
    number /= 10
    num_of_digits += 1  # increment

    if int(number) == 0:  # when the number becomes 0 the loop exits
        break
# loop ends


power = num_of_digits  # used to convert the reverse number

reverse_num = 0  # store the reversed number
for digit in digits:
    reverse_num += digit * (10 ** (power - 1))
    power -= 1  # decrement

print("The number has", num_of_digits, "digits and its reverse is: ", reverse_num)

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())

# ---------------------------------------------------------------------------------------------------


# RahmanArkoMdWasifBinA1Q2.py
#
# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 2
# Author:     Md Wasif Bin Rahman Arko
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

from math import pi
import cmath
from time import ctime

print("\n-----------------------------------------------------------")

tolerance = float(input("Enter the acceptable tollerance: "))
degree = float(input("Enter an angle in degree: "))

# degree to radian
x = degree * pi / 180

# python exponent function and its real and imaginary parts
exponent = cmath.exp(complex(0.0, x))  # e^ix
actual_real = exponent.real  # real portion of e^ix equivalent to cos(x)
actual_imaginary = exponent.imag  # imaginay portion of e^ix equivalent to sin(x)

# estimating sin(x) value
factor = 2
sine = 0.0
term = x
xSquared = x * x
count1 = 1
while abs(term) > tolerance:
    # enters a while loop
    sine += term
    term = -term * (xSquared / (factor * (factor + 1)))  # updating each term of sin function
    factor += 2  # factorial of n
    count1 += 1  # counting numbers of terms needed
# loop ends

# estimating cos(x) value
factor = 2
cosine = 0.0
term = 1.0
xSquared = x * x
count2 = 1
while abs(term) > tolerance:
    # enters a while loop
    cosine += term
    term = -term * xSquared / (factor * (factor - 1))  # updating each term of sin function
    factor += 2  # factorial of n
    count2 += 1  # counting numbers of terms needed
# loop ends


# calculating tolerance
actual_tolerance_real = actual_real - cosine
actual_tolerance_imaginary = actual_imaginary - sine

print("\nPython's value of e^ix(%.2f) = %.15f + %.15f i\n" % (degree, actual_real, actual_imaginary))
print("Approximate value of e^ix(%.2f) = %.15f + %.15f i\n" % (degree, cosine, sine))
print("Number of terms %d for real part and %d for imaginary part\n" % (count1, count2))
print("Tolerance= %.15f + %.15f i\n" % (actual_tolerance_real, actual_tolerance_imaginary))

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())

# ---------------------------------------------------------------------------------------------------


# RahmanArkoMdWasifBinA1Q3.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 3
# Author:     Md Wasif Bin Rahman Arko
# Version:    2021/02/03
#
# Purpose:    The purpose of the program is to generate a sequence like below
#               9
#               99
#               999
#               9999
#               99999
#               ...
# var - the use / meaning of this varible 
#
# lines = means total number of lines the output will show
# equation = prints the output according to this formulae


from time import ctime

print("\n-----------------------------------------------------------")

lines = int(input("Enter the number of lines: "))
print(end='\n')

for i in range(1, lines + 1, 1):
    equation = int((10 ** i) - 1)  # equation is (10^line_number) - 1
    print(equation)

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
