# WasifArkoA4Q1.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        4 Question 1
# Author:     Wasif Arko
# Version:    2021/03/27
#
# Purpose:    The purpose of this question is to write a Python program
#             how to read a file and recognize prime number in it.

from time import ctime
import numpy as np

# All functions
# it converts the string to int and return the numbers as an array
def txt2Int(filename):
    with open(filename, 'r') as f:
        file = f.readlines()        # read each line of txt file
        num = list()                # list for storing numbers fetched from file
        for item in file:
            num.append(int(item))   # add item in num list

    ans = np.array(num)             # convert the num list to num array
    return ans                      # return array of numbers


# detect if a number is prime or not and also find the divisors of non prime numbers and stores them in dictionary
def PrimeRec(Num):
    prime = set()                   # set for storing prime numbers
    non_prime = dict()              # dictionary for storing non prime numbers and divisors
    flag = 1                        # flag for detecting non prime and prime numbers

    for x in Num:
        for i in range((x // 2), 2, -1):
            if x % i == 0:
                flag = 0            # it means this a non prime number
                non_prime[x] = [i]  # store this non prime number in dictionary
                break

        if flag == 1:               # it means this a prime number
            prime.add(x)            # add this prime number to set 'prime'
        flag = 1

    return prime, non_prime         # return both the set and dicitionay of prime and non prime numbers


# termination message
def displayTerminationMessage():
    print("""
Programmed by Md Wasif Bin Rahman Arko
Date: %s
End of processing.""" % ctime())



# calling function and printing results
num_array = txt2Int('A4_Q3.txt')        # stores the array of numbers in num_array variable
primes, nonPrimes = PrimeRec(num_array) # stores prime number set in primes and non prime numbers in nonPrimes as dictionary

# printing the set of prime numbers as set
cnt = 0
print("Prime set is: {", end='')

for i in primes:                        # this loop is just for printing the prime set as directed in question
    if cnt == len(primes) - 1:
        print("and", i, end='')
    else:
        print(i, end=', ')
    cnt += 1
print("}")

# printing the non prime numbers and their largest divisor
print("Dictionary of none prime numbers and a divisor: ", end='')
print(nonPrimes)

# termination message
displayTerminationMessage()
