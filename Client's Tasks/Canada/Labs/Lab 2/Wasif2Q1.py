# Wasif2Q1.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        2 Question 1
# Author:     Wasif
# Version:    2021/02/25
# 
# Purpose:    The purpose of the question to write a python program(script)  to
#             request input from the user using the ‘input’ function.
# 
# country = Country name
# city = City name
# food = Food name


from time import ctime
print('\n---------------------------------------------')

country = input('I am the great and powerful fortune-teller. What is your favourite country for travelling?: ')
city = input('What is your favourite city for travelling?: ')
food = input('What is your favourite food for travelling?: ')

print("""
Your favorite city to travel to is {}, which is located in {}. 
I also know that your favorite food is {}!""".format(country,city,food))

print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      