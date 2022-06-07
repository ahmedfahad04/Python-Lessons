# WasifA1Q3.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Assignment: 1 Question 3
# Author:     Wasif 
# Version:    2021/02/03
#
# Purpose:    The purpose of the program is to generate a sequence like below
#               9
#               99
#               999
#               9999
#               99999
#               ...
# var - the use / meaning of this varible 
#
# lines = means total number of lines the output will show
# equation = prints the output according to this formulae


from  time import ctime
print("\n-----------------------------------------------------------")

lines = int(input("Enter the number of lines: "))
print(end='\n')


for i in range (1,lines+1,1):
        equation = int((10**i)-1) #equation is (10^line_number) - 1
        print(equation)
        

print("""
Programmed by Wasif
Date: %s
End of processing."""% ctime())
      
    