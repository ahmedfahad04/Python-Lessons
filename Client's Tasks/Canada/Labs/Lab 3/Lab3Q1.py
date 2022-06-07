# Lab3Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        3 Question 1
# Author:     Wasif
# Version:    2021/02/12
# 
# Purpose:    The purpose of this question is to write a python program (script) 
#             that uses list comprehension, the range function and the zip function.

# sevens = contains multiple of 7
# newlist = contains value of n/2-3


from time import ctime
print("\n------------------------------------------------------------------\n")

#stores multiples of 7
sevens = []
sevens = [N for N in range(7,141,7)]

#stores the equation's (N/2-3) value
newlist = []
newlist = [int(N/2-3) for N in range(7,141,7)]

#used format function for foramted output
print(format('N', ">10"), format('N/2-3', ">10"))    

for x,y in zip(sevens, newlist):
    print(format(x, ">10d" ), format(y, ">10d"))
    
    
print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    