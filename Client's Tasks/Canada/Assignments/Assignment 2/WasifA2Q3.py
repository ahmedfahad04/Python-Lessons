# Wasif2Q3.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        2 Question 3
# Author:     Wasif
# Version:    2021/02/28
#
# Purpose:    The purpose of the question to write a python program(script) to
#             write a function that can return the first row of Pascal’s triangle
#
# n = number of rows
# l1 = values of each row
# l2 = holds the list values in reverse order
# k = Index of lists

from time import ctime

print('\n---------------------------------------------')

n = 6 # number of rows
print("PasTri({})\n".format(n))


def PasTri(n):
    l1 = [1] # stores the row's values(initially just 1 is stored)
    l2 = []  # this list will hold the reverse ordering of l1
    for i in range(n):

        print(l1)      # print the sequence
        l1 = l1 + [0]  # every time after printing the sequence a '0' is added to make calculation easy(eg. 1+0 = 0+1 = 1)

        l1.reverse()   # reversed the order of l1
        l2 = l1.copy() # storing reversed order of l1
        l1.reverse()   # after copying the reversed version of l1 in l2, l1 is again reversed to get the actual sequence

        k = 0 # l1 index(initially 0)
        for x, y in zip(l1, l2):
            l1[k] = x + y # mainly this portion adds the value of l1 and l2 to find out Pascle Triangle sequence
            k += 1

# display terminating message
def displayTerminationMessage():

    print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())

def main():
    PasTri(n) # call the function
    displayTerminationMessage()

main()


