# Lab2Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        2 Question 1
# Author:     Wasif
# Version:    2021/02/04

# Purpose:    The purpose of the question to write a python program(script) 
#             that is given an amount in pennies and converts it to an equivalent
#             amount in dollars, quarters, dimes, nickels and pennies. There are 100 pennies
#             in a dollar, 25 pennies in a quarter, 10 pennies in a dime and 5 pennies in a nickels
#
# pennies = Amount of pennies        
           

from time import ctime

print("\n-------------------------------------------")

pennies = int(input("Enter the number of pennies: "))
print("\n%d pennies is equivalent to: \n" % pennies)


print("%d dollars +" % (pennies//100))
pennies = pennies % 100

print("%d quarters +" % (pennies//25))
pennies = pennies % 25

print("%d dimes +" % (pennies//10))
pennies = pennies % 10

print("%d nickels +" % (pennies//5))
pennies = pennies % 5

print("%d pennies" % (pennies))



print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    