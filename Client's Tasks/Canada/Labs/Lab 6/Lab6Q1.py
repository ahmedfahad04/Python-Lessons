# L6Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        6 Question 1
# Author:     Wasif
# Version:    2021/03/09
# 
# Purpose:    The purpose of the question to write a python program(script)  to
#             write a python program (script) that draws a series of triangles.
#
# n = Triangle size
# row = Rows of Triangle
# col = Columns of Triagnle
# size = Total rows of Triangle


from time import ctime


# This Function verify if the size of triangle is a Positive integer
def getPosInt(promt):
    while True:
        n = input(promt).strip()  # take input of n

        if n != '':
            try:
                n = eval(n, {}, {})  # checking if it is an integer or not
            except:
                print("Invalid Input!")
            else:
                if type(n) is int:
                    if n >= 0:
                        break
                    else:
                        print(n, "is not a positive integer!")
                else:
                    print(n, " is not an Integer!")
        else:
            print("Missing Output!")

    return n


# This function draw the Triangle
def drawTriangle(size):
    for row in range(size, 0, -1):  # check values of Triangle's row
        for col in range(row, 0, -1):  # prints the values column wise
            print('*', end='')
        print()


# Main Function where all execution happens
def main():
    prompt = "Enter the size of the triangle (0 to end): "

    while True:
        size = getPosInt(prompt)
        print(type(size))

        if size == 0:  # checking if size is 0
            break
        else:
            print("\nDraw a triangle whose size is %d." % size, "\n")
            drawTriangle(size)  # draw the triangle


# Driver Function            
main()

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
