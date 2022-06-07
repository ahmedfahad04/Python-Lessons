# Lab5Q2.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        5 Question 2
# Author:     Wasif
# Version:    2021/02/25
# 
# Purpose:    The purpose of the question to write a python program(script) to 
#             write a python program (script) that contains a function
#             that determines if a value passed to it is between a lower and upper bound.
# 
# values = input value of x


from time import ctime
print('\n---------------------------------------------\n')


def validateBoundedInt(value, bound):
    
    if type(value) is not int:
        return "{} is not an integer!".format(value)
    
    else:
       
        if value < (-1*bound):
            return "{} is too small!".format(value)
            
        elif value > bound:
            return "{} is too large!".format(value)
          
        else:  #check if the value is (-bound<=value<=bound)
            return "{}, is a valid integer!".format(value) 
        

values = [-101,-100,0,1,101,100,True,1.5,'hello'] #all input values

for item in values:
    print(validateBoundedInt(item, 100),"\n")



print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())