# Lab11Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        11 Question 1
# Author:     Wasif
# Version:    2021/04/13
#
# Purpose:    The purpose of the question to write a Python program that reads data from a file and displays that data
#             on the screen
#

from time import ctime
import math
import numpy as np

# this function reads the file and make array of x and y coordinates
def readFile(filename):
    infile = open(filename)     # open the file
    file = infile.read()        # read the lines of file
    f = file.splitlines()       # split the file string in lines
    X = []                      # list to hold x coordinates
    Y = []                      # list to hold x coordinates
    for line in f:
        l = line.split(",")         # split line basis of comma(,)
        angle = float(l[0][1:])     # compute angle
        radius = float(l[1][:-1])   # comput radius

        X.append(radius * math.cos(angle))  # append the x coorrdinate value to list
        Y.append(radius * math.sin(angle))  # append the y coorrdinate value to list

    x = np.array(X)     # create array of x coordinate
    y = np.array(Y)     # create array of y coordinate

    return x, y         # return the array


# display the coordinates
def displayCoordinates(xCoords, yCoords):
    print("%21s  %21s" % ("X Coordinate", "Y Coordinate"))  # prints the headlines

    for x, y in zip(xCoords, yCoords):
        print("%21.14e  %21.14e" % (x, y))                  # print the values in pair

# display termination message
def displayTerminationMessage():
    print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())

# main function
def main():
    print("\n" + 50 * "--")                 # string replication

    xcoord, ycoord = readFile("data.txt")   # calling the readFile function to get the array of x and y coordinates
    displayCoordinates(xcoord, ycoord)      # calling displayCoordinates to print the values
    displayTerminationMessage()             # calling displayTerminationMessage

# calling main function to execute the program
main()

