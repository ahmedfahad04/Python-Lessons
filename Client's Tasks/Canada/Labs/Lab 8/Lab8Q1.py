# Lab8Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        8 Question 1
# Author:     Wasif
# Version:    2021/03/23
#
# Purpose:    The purpose of the question to write a python program(script) to create a
#             2-dimensional array and then displays the elements in the array along with
#             their coordinates.
#


from time import ctime
import numpy as np

print('\n---------------------------------------------')


def getPosInt(prompt, EOF):

    while True:
        flag = 1
        n = input(prompt).strip()  # take input of n

        if n != '':
            try:
                n = eval(n, {}, {})  # checking if it is an integer or not
            except:
                print("Invalid Input!")

            else:
                if type(n) is int:
                    if n == 0:      # check if n = 0 or not
                        flag = -1
                        break
                    elif n > 0:
                        flag = n
                        break
                    else:
                        print(n, " not a positive integer!")
                else:
                    print(n, " not an Integer!")
        else:
            print("Missing Input!")

    return flag



def getMatrix(rows, columns, EOF):
    elements = list()               # primary list for storing the elements of matrix

    flag = 1
    for row in range(rows):
        for col in range(columns):
            prompt = "\nEnter matrix[{},{}]: ".format(row, col)      
            x = getPosInt(prompt, -1)   # checking the value of user input

            if x == EOF:                # if the value equals to EOF it terminates
                flag = -1
                break

            elements.append(x)          # appending the elements into list
        if flag == -1:
            break

    if flag == -1:
        arr = -1
    else:
        arr = np.array(elements).reshape(rows, columns)  # turning list to array and making it matrix using reshape function

    return arr                          # returning array.


def displayMatrix(MM):
    print("\nThe matrix has "+str(MM.shape[0]) +
          " rows and "+str(MM.shape[1])+" columns.")    # showing the number of rows and columns

    for row in range(MM.shape[0]):
        for col in range(MM.shape[1]):
            print(MM[row, col], end=' ')                # printing the elments in matrix style
        print()


def main():
    flag = 1
    while True:
        row = getPosInt("Enter the number rows (> 0): ", -1)
        if row == -1:
            flag = -1
            break

        col = getPosInt("\nEnter the number columns (> 0): ", -1)
        if col == -1:
            flag = -1
            break

        matrix = getMatrix(row, col, -1)                # make array of matrix using the row and col numbers

        if type(matrix) is int and matrix == -1:        # checking if user enter any wrong value i.e EOF
            flag = -1
            break
        else:
            displayMatrix(matrix)                       # if everything is all right then print the matrix row wise
            break

    if flag == -1:
        print("Unexpected EOF, program terminates!")


# driver program
main()



print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
