# Lab5Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        5 Question 1
# Author:     Wasif
# Version:    2021/02/25
# 
# Purpose:    The purpose of the question to write a python program(script) to 
#             write a python program (script) that computes a stepwise function.
# 
# values = input value of x


from time import ctime
print('\n---------------------------------------------\n')


def f(x):
    if x == 0:
        return 0
    elif x%3 == 0: #tests if it is a multiple of 3
        return 3
    elif x%2 == 0: #tests if it is a multiple of 2
        return 2
    else:
        return 1
    
values = [x for x in range(-6,7,1)] #create a list of input of f(x)

print("%2c %9s "% ('x','f(x)'))
for item in values:
    print("%2d %7d " % (item,f(item)))


print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    