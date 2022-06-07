# WasifA1Q2.py
#
# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 2
# Author:     Wasif
# Version:    2021/02/04


from time import ctime

def computeTrajectory(a, b, c, distance, intervals):
    k = distance / intervals
    x = [k * i for i in range(0, intervals + 1)]
    y = [(a * x ** 2 + b * x + c) for x in x]
    return x, y

# this is 100% wrong-----
X, Y = computeTrajectory(5,3,2,10,20)
print("X")
print(X)
print("Y")
print(Y)
print("LenX: ", len(X), "LenY: ", len(Y))
# this is 100% wrong-----

print("""
Programmed by Wasif
Date: %s
End of processing."""% ctime())