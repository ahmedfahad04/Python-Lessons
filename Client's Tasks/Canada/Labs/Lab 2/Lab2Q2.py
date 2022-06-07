# Lab2Q2.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        2 Question 2
# Author:     Wasif
# Version:    2021/02/04
# 
# Purpose:    The purpose of the question to write a python program(script) 
#             to convert a weight given in pounds and ounces to a weight in kilograms.
# 
# pounds = Weight in pounds
# ounces = Weight in ounces
# total_ounce = Contains value of the summation of ounces and converted value of ounce from pounds
# ounces_to_kg = Converted weight of ounce in kilograms

from time import ctime

while True:
    print("\n-------------------------------------------------------------------")
    pounds = int(input("Enter the integer number of pounds (<0 to quit): "))
    
    if pounds < 0:
        break
    
    ounces = float(input("Enter the number of ounces as a real number: "))
    
    total_ounce = pounds*16 + ounces
    ounces_to_kg = total_ounce*0.02835
    
    print("\nThe number of kilograms for %d pounds and %f ounces is %.4f" % (pounds, ounces, ounces_to_kg))



print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    