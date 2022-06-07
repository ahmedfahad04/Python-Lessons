# WasifA1Q1.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 1
# Author:     Wasif 
# Version:    2021/02/03
#
# Purpose:    The purpose of the program is to get
#             an integer number from input, reverse the order of its
#             digits and print the result in the output.
#
# var - the use / meaning of this varible 
#          
# number = the number which will be examined
# digits = this list holds all the single digits of given number
# num_of_digits = total number of digits in a number
# j = temporary variable hold the remainder
# power = used for indicating power of 10 while creating the reverse number
# reverse_num = holds the reverse number


from  time import ctime

print("\n-----------------------------------------------------------")

number = int(input("Enter an Integer Number: ")) #taking new number input


digits = [] #stores the digits as list 
num_of_digits = 0 #calculates the length of number using len of list

#this loop extracts the digits from given number and append it in 'digits' list
while True:
    j = int(number%10)
    digits.append(j)
    number /= 10
    num_of_digits+=1
    
    if int(number) == 0:
        break
#loop ends
   

power = num_of_digits #used to convert the reverse number

reverse_num = 0 #store the reversed number
for digit in digits:
    reverse_num += digit*(10**(power-1) ) 
    power -= 1


print("The number has", num_of_digits ,"digits and its reverse is: ", reverse_num)


print("""
Programmed by Wasif
Date: %s
End of processing."""% ctime())

      
      
      