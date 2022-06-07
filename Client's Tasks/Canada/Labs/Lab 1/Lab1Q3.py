# Lab1Q3.py
#
# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        1 Question 3
# Author:     Wasif
# Version:    2021/02/03
#
# Purpose:    Input the lengths of the semi-axes for an ellipsoid
#             and calculate the volume of the ellipsoid

from time import ctime
from math import pi

prompt = 'Enter the length of the semi x-axis in cm: '
semiX = float(input(prompt))
prompt = 'Enter the length of the semi y-axis in cm: '
semiY = float(input(prompt))
prompt = 'Enter the length of the semi z-axis in cm: '
semiZ = float(input(prompt))
volume = 4. * pi * semiX * semiY * semiZ / 3.

print('\nThe volume of the ellipsoid is %.2f cm^3' % volume)


print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    

