# Lab4Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        4 Question 1
# Author:     Wasif
# Version:    2021/02/19
# 
# Purpose:    The purpose of this question is to write a python program (script) 
#             that computes the squares for the integers from 1 to 10 by summing 
#             odd integers.
# 
# n = Square value of which to be calculated
# square = Square value of n


from time import ctime

print("\n" + "-" * 50 + "\n")

odds = [i for i in range(1,20,2)]
square = 0
n = 1

print("   n  n^2") # headline
for item in odds:
    square += item # square number using summing odd numbers
    print("%4d%4d"% (n,square))
    n+=1 # number of which square to be calculated

    
print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    