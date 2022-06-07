# WasifArkoA3Q5.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        3 Question 5
# Author:     Wasif Arko
# Version:    2021/03/10
#
# Purpose:    The purpose of the question to write a python program(script)  to
#             write a python program that computes the frequencies of palindromes
#             in some English language text.
#


from time import ctime


def getWords(filename):
    infile = open(filename, 'r')  # open a new file
    data = infile.read()   # reading file data using read() function
    infile.close()  # closing file

    return data.split()  # it splits the data word by word and returns it


def isPalindrome(word):
    n = len(word)  # length of 'word'
    flag = 1

    if n >= 3:      # check if the words' length is more or equal than 3
        for i in range(0, n // 2):
            if word[i] != word[n - i - 1]:  # checking for palindrome
                flag = 0
                break
    else:
        flag = 0

    return flag


def findPalindromes(text):
    palindromes = []  # stores palindrome words
    frequencies = []  # stores frequency of palindromic words

    for item in text:
        check = isPalindrome(item)

        if item not in palindromes and check == 1:  # checking for unique palindrom word
            palindromes.append(item)
            frequencies.append(1)
        elif item in palindromes and check == 1:  # incrementing frequency of repeated palindromic word
            frequencies[palindromes.index(item)] += 1

    return palindromes, frequencies


def displayPalindromes(palindromes, frequencies):
    sorted_list = sorted(palindromes)   # storing sorted list

    print("\nPalindrome        Frequency")
    for p, f in zip(sorted_list, frequencies):
        # formatted output
        print("%-20s%-9d" % (p, frequencies[palindromes.index(p)]))


def displayTerminationMessage():

    print("""
Programmed by Md Wasif Bin Rahman Arko
Date: %s
End of processing.""" % ctime())


# main function
def main():
    print("-" * 50)

    file_name = input("\nEnter the name of the file containing the text: ")
    while file_name == "":
        print("The name of the file must not be an empty string!")
        file_name = input("\nEnter the name of the file containing the text: ")

    # word list using getWords() function
    word_list = getWords(file_name)
    # finding palindrome and frequency using findPalindromes() function
    palin, freq = findPalindromes(word_list)
    # display output
    displayPalindromes(palin, freq)   
    # display termination message          
    displayTerminationMessage()                 


# Driver program
main()
