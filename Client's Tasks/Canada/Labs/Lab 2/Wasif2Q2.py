# Wasif2Q2.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        2 Question 2
# Author:     Wasif
# Version:    2021/02/25
# 
# Purpose:    The purpose of the question to write a python program(script) 
#             to convert strings to numbers using the int() or float() functions, which
#             convert strings into integer and float types, respectively.
#
# num1 = 1st Number
# num2 = 2nd Number
# num3 = 3rd Number
# num1Float = Converted 1st number to Floating point
# num2Float = Converted 2nd number to Floating point
# num3Float = Converted 3rd number to Floating point


from time import ctime
print('\n---------------------------------------------')

num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
num3 = input("Enter number 3: ")

num1Float = float(num1)
num2Float = float(num2)
num3Float = float(num3)

product = num1Float* num2Float* num3Float
mean = (num1Float+ num2Float+ num3Float)/3

print("""
The product of numbers [{},{},{}] is {}
The mean of numbers [{},{},{}] is {data:.2f} """.format(num1,num2,num3,product,num1,num2,num3,data=mean))


print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    