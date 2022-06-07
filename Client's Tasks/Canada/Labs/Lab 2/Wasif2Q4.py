# Wasif2Q4.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        2 Question 4
# Author:     Wasif
# Version:    2021/02/25
# 
# Purpose:    The purpose of the question to write a python program(script) that 
#             grabs a number and print the number of points that will be in its 
#             triangular sequence
# 
# n = the number for which triangle number will be asked
# formula = Number of points in the triangle


from time import ctime
print('\n---------------------------------------------')



n = int(input("Enter the value of n: "))

formula = int((n*(n+1))/2)

print("{}'s Triangular Number is {}".format(n,formula))



print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    