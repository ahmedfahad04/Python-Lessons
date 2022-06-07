# Lab1Q2.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        1 Question 2
# Author:     Wasif
# Version:    2021/02/03

# Purpose:    Convert a weight from kilograms to pounds and ounces

# kilograms - the weight in kilograms
# pounds - the number of pounds in the equivalent weight
# ounces - the number of  ounces in the equivalent weight
# LBS_PER_KGM - the nubmer pounds per kilogram
# OUNCES_PER_POUND - the number of ounces per pounds


from time import ctime
print("\n-----------------------------------------------------------")

LBS_PER_KGM = 2.20462262
OUNCES_PER_POUND = 16

kilograms = float(input("Enter the weight in kilograms: "))
pounds = kilograms * LBS_PER_KGM
ounces = pounds * OUNCES_PER_POUND
pounds = ounces // OUNCES_PER_POUND
ounces = ounces % OUNCES_PER_POUND

print("\n%f kilograms is equivalent to %g pounds and %f ounces." % (kilograms, pounds, ounces))


print("""
Programmed by Wasif
Date: %s
End of processing."""% ctime())
      
    