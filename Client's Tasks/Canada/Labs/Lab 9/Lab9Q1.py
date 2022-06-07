# Lab9Q1.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        9 Question 1
# Author:     Wasif
# Version:    2021/03/31
#
# Purpose:    The purpose of the question to write a python program (script) that plots six curves in two
#             subplots of a single figure
#


from time import ctime
import numpy as np
import matplotlib.pyplot as plt

print('\n---------------------------------------------')

plt.figure()  # figure for storing the subplots
x = np.arange(1.0, 5.1, 0.1)  # array of x values

# subplot 1
plt.subplot(2, 1, 1)
plt.plot(x, (1.0 - 1.0 / x), 'r-')  # plotting f1(x)
plt.plot(x, (0.5 - 1.0 / (2 * x * x)), 'b-')  # plotting f2(x)
plt.plot(x, ((1.0 / 3.0) - 1.0 / (3.0 * x * x * x)), 'g-')  # plotting f3(x)
plt.xlabel('x')  # x label
plt.ylabel('y')  # y label
plt.title("Diminishing Functions")  # title of subplot 1
plt.legend(['1-1/x', '1/2-1/(2x^2)', '1/3-1/(3x^3)'], loc='center', bbox_to_anchor=(0.5, 0.875),
           ncol=3)  # legend of subplot 1

# subplot 2
plt.subplot(2, 1, 2)
plt.plot(x, ((x * x * x - 1.0) / 3.0), 'm-')  # plotting f4(x)
plt.plot(x, ((x * x - 1.0) / 2.0), 'c-')  # plotting f5(x)
plt.plot(x, (x - 1.0), 'y-')  # plotting f6(x)
plt.xlabel('x')  # x label
plt.ylabel('y')  # y label
plt.title("Increasing Functions")  # title of subplot 2
plt.legend(["(x^3-1)/3", "(x^2-1)/2", "x-1"],
           loc='upper left')  # legend of subplot 2

# laying, showing and saving plots
plt.tight_layout()  # tight layout pretty plotting
plt.savefig('lab9q1.png')  # saving the plot as png file
plt.show()  # showing the plot

# termination message
print("""
Programmed by Md Wasif Bin Rahman Arko
Date: %s
End of processing.""" % ctime())
