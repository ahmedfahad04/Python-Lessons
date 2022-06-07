# Wasif2Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        2 Question 1
# Author:     Wasif
# Version:    2021/02/28
# 
# Purpose:    The purpose of the question to write a python program(script)  to
#             request input from the user using the ‘input’ function.
#
# list_len = number of elements
# data = contains the elements
# length = stores the length of frequency list


from time import ctime

print('\n---------------------------------------------')

data = [] # contains the elements
frequency = []  # stores the frequency of elements
distinct_data = []  # stores the distinct elements
index = [] # stores the index of those distinct elements

def grablist():
    
    list_len = int(input("Enter the length of the list: "))

    # listing the values of element in list
    for i in range(1,list_len+1,1):
        x = input("\nEnter the element %d: " % (i))
        data.append(x)

        # return statement missing


def listSearch():

    for item in data:
        cnt = 0

        # counting frequencies of elements
        for x in data:
            if item == x:
                cnt +=1
        frequency.append(cnt)

        # counting distinct element and their indices
        if item not in distinct_data:
            distinct_data.append(item) # distinct elements
            idx = [i for i in range(len(data)) if data[i] == item] # their indices in a list
            index.append(idx)


def delDup():
    
    length = len(frequency)
    j = 0

    # deleting the duplicated elements based on their frequencies
    for i in range(0,length, 1):
        if frequency[i] > 1:
            data.pop(i-j) # when any element deleted then the overal index of list is changed. To cope with the changed index of list we substruct j.
            j+=1


def status():

    # this function just prints the status about the occurrences of elements and their positoins
    for item,occr in zip(distinct_data,index):
        if len(occr) > 1:
            print("\nThe element {} occurs {} times at".format(item, len(occr)), end=' ')
            print(', '.join(str(x) for x in occr),end=' ')
            print("=> it is removed")
        else:
            print("\nThe element {} occurs {} time at".format(item, len(occr)),end=' ')
            print(' '.join(str(x) for x in occr),end='.\n')


# display terminating message
def displayTerminationMessage():

    print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())

def main():

    grablist() 	 # stores the elements in a list
    listSearch() # find out duplicated element and distinct elements along with indices
    delDup()     # delete duplicated elements

    # printing the final list elements
    print("\nThe final list is: [",end='')
    print(', '.join(str(x) for x in data),end=']\n')

    # printing the occurrences of elements along with their positions
    status()
    displayTerminationMessage()


# Main function where all other functions executes
main()



      
    