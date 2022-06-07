# WasifQ4.py
#
# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: Question 4
# Author:     Wasif
# Version:    2021/02/10
#
from time import ctime

term = int(input("Enter value of n: "))
ans = []
a = 7
b = 10
result = []
for x in range(0,term+1,1):
    a = 7
    b = 10
    for i in range(1,x+1):

        if i%2 != 0:
            ans.append(a)
            print(a,end=', ')
            a+=1

        else:
            ans.append(b)
            print(b,end=', ')
            b+=1

    print()

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
