# WasifArkoA4Q1.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        4 Question 1
# Author:     Wasif Arko
# Version:    2021/03/30
#
# Purpose:    The purpose of this question is to write a Python program that can work with lists
#             and dictionaries.


from time import ctime


# function for taking user input.
def getInput(prompt, flag, val):
    while True:

        n = input(prompt).strip()       # ask for user input

        if n != '':
            try:
                n = eval(n, {}, {})
            except:
                print("{} is not valid!".format(n)) # if input is string it will ask for another input
            else:
                if type(n) is int:
                    if flag == 'min':
                        if n < val:                 # check if it is in the desired range
                            print("Out of range!")
                        else:
                            return n
                    elif flag == 'max':
                        if n > val:                 # check if it is in the desired range
                            print("Out of range!")
                        else:
                            return n
                else:
                    print("{} is not valid!".format(n)) # if input is float it will ask for another input

        else:
            print("Missing Input!")


# build possible set of answers of mentioned equation under the limited range of x,y,z
def buildPossibleAnswers(Coeff, Xmin, Xmax, Ymin, Ymax, Zmin, Zmax):

    # Prompt for taking inputs of ranges from user
    Xmaximum = getInput("\nEnter maximum value of X: ", "max", Xmax)
    Xminimum = getInput("\nEnter minimum value of X: ", "min", Xmin)
    Ymaximum = getInput("\nEnter maximum value of Y: ", "max", Ymax)
    Yminimum = getInput("\nEnter minimum value of Y: ", "min", Ymin)
    Zmaximum = getInput("\nEnter maximum value of Z: ", "max", Zmax)
    Zminimum = getInput("\nEnter minimum value of Z: ", "min", Zmin)

    possible_ans = list()   # list to store possible set of answers

    for x in range(Xminimum, Xmaximum + 1, 1):
        for y in range(Yminimum, Ymaximum + 1, 1):
            for z in range(Zminimum, Zmaximum + 1, 1):
                res = Coeff[0] * x - Coeff[1] * y + Coeff[2] * z

                possible_ans.append([x, y, z, res])     # enlisting the possible answers

    return possible_ans     # returning the list


# store the possible answers in a dictionary where key is the set of answers
# and value is the difference between value of right hand side and calculated
# value form expected set of answers.
def computeError(a, k):
    err = dict()    # dictionary to store the possible set of answers along with their calculated values

    for item in a:
        err[str(item)] = k - item[3]    # calculate the right sided value of expected answers ans stores them in dictionary

    return err      # return the dictionary


# sort out the answers from possible answer set got from previous function.
def findSolutions(R):
    final_ans = list()  # list for storing final solutions

    for key, value in R.items():
        if value == 0:
            final_ans.append(key)   # enlist the final solution to the equation

    return final_ans      # returning the list


# print the final answers in the way mentioned in the question.
def printAnswers(anslist):
    print("\nThere are total {} possible answers for this equations in the desired range: ".format(len(anslist)))
    print(" %3s %3s %3s" % ("X","Y","Z"))

    i = 1
    for x in anslist:
        print(str(i) + ":" + x[:-4] + "]") # printing the final solutions the way mentioned in the question.
        i += 1


# termination message
def displayTerminationMessage():
    print("""
Programmed by Md Wasif Bin Rahman Arko
Date: %s
End of processing.""" % ctime())


# call the above mentioned functions
print(50 * "--")        # string replication.
li = buildPossibleAnswers([2, -3, 1], -9, 9, -9, 9, -9, 9) # call for building possible set of solution
di = computeError(li, 5)    # call for listing possible set of solution in a dictionary
ans = findSolutions(di)     # call for listing final solutions in a list
printAnswers(ans)           # print all the solutions to the equation
displayTerminationMessage() # termination message
