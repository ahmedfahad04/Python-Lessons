# Wasif2Q2.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        2 Question 2
# Author:     Wasif
# Version:    2021/02/28
# 
# Purpose:    The purpose of the question to write a python program(script) to
#             writing a code that can calculate the standard deviation of
#             a list of numbers that user enters.
#
# data = contains the values of which Standard Deviation will be calculated
# list_len = number of values
# total = summation of values
# sqr_diff = summation of the square of (value - average of values)
# variance = contains variance of the values
# average = contains average of values
# standard_deviation = standard deviation of values


from time import ctime
import math

print('\n---------------------------------------------')

data = []


def grablist():
    list_len = int(input("Enter the length of the list: "))

    # listing the values in a python list
    for i in range(1, list_len + 1, 1):
        x = int(input("\nEnter the element %d: " % (i)))
        data.append(x)

    print("\nSample data: ", data)


def avg_calc(dataList):
    total = 0

    # finding summation for calculating average
    for item in dataList:
        total += item

    return total / len(dataList)


def sd_calc(avg_cal, dataLs):
    sqr_diff = 0

    # calculating squared difference of values from their average for calculating standard deviation
    for item in dataLs:
        x = (item - avg_cal) ** 2
        sqr_diff += x

    variance = sqr_diff / (len(dataLs) - 1)
    sd = math.sqrt(variance)  # finally calculating standard deviation

    return sd


# display terminating message
def displayTerminationMessage():
    print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())


def main():
    grablist()  # taking and listing inputs(values)
    average = avg_calc(data)  # calculating average
    standard_deviation = sd_calc(average, data)  # calculating standard devation
    print("Standard Deviation: ", standard_deviation)
    displayTerminationMessage()


# Main function. Every other functions executes here.
main()
