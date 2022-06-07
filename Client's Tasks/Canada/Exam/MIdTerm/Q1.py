# WasifQ1.py
#
# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: Question 1
# Author:     Wasif
# Version:    2021/02/10
#
from time import ctime

def etox(x, tolerance):
    term = 1
    cnt = 1
    summ = 0

    while abs(term) > tolerance:
        summ += term
        term = term * x / cnt
        cnt += 1

    return summ, cnt

# this is 100% wrong-----
x = float(input("Enter value for x: "))
tolerance = float(input("Enter the tolerance: "))

ex, counts = etox(x, tolerance)

print("\ne^x value is: ", ex)
print("Number of terms is: ", counts)
# this is 100% wrong-----



print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
