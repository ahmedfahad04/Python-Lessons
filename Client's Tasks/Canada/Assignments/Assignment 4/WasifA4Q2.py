# WasifArkoA4Q1.py

# Course:     COMP 1012
# Instructor: Ramin Soltanzadeh
# Lab:        4 Question 1
# Author:     Wasif Arko
# Version:    2021/03/26
#
# Purpose:    The purpose of this question is to write a Python program to plot two modulate sinus on each other.

from time import ctime
import numpy as np
import matplotlib.pyplot as plt

# function for making single plot
def sinTest(A, F, time, numel):
    x = np.arange(0, time, time / numel)        # value of x axis(Time)
    y = A * (np.sin(((2 * np.pi) / F) * x))     # value of y axis(Amplitude of sinx)

    plt.plot(x, y, 'b-')                        # plot the graph
    plt.ylabel("Amplitude")                     # setting y axis label

    return plt

# function for managing multiple plots
def SinModule(A1, F1, A2, F2, time, numel):
    plt.figure()                                # holds all plots in one figure

    plt.subplot(3, 1, 1)                        # 3 subplots for showing 3 different plots
    p1 = sinTest(A1, F1, time, numel)           # calling SinTest Function for 1st sinus wave.
    p1.title("First Sinus Wave")                # plot title

    plt.subplot(3, 1, 2)
    p2 = sinTest(A2, F2, time, numel)           # calling SinTest function for 2nd sinus wave
    p2.title("Second Sinus Wave")               # plot title

    plt.subplot(3, 1, 3)
    X = np.arange(0, time, time / numel)        # x values (time)
    Y1 = A1 * (np.sin(((2 * np.pi) / F1) * X))  # y values of plot 1
    Y2 = A2 * (np.sin(((2 * np.pi) / F2) * X))  # y values of plot 2
    modulate = Y1 * Y2                          # new values of y for Modulated sin plot
    plt.plot(X, modulate, 'b-')
    plt.title("Modulated Wave")                 # plot title
    plt.xlabel("Time")                          # setting name of x label
    plt.ylabel("Amplitude")                     # setting name of y label

    plt.tight_layout()                          # setting layout for pretty output
    plt.savefig("Figure.png")                   # saving the plot file in png format
    plt.show()                                  # showing the plot


# termination message
def displayTerminationMessage():
    print("""
Programmed by Md Wasif Bin Rahman Arko
Date: %s
End of processing.""" % ctime())


# input values
print(50 * "--")
amplitude1 = eval(input("\nEnter Amplitude for First Sinus Wave: "))
amplitude2 = eval(input("\nEnter Amplitude for Second Sinus Wave: "))
freq1 = eval(input("\nEnter Frequency for First Sinus Wave: "))
freq2 = eval(input("\nEnter Frequency for Second Sinus Wave: "))
time = eval(input("\nEnter Time length: "))
Elements = eval(input("\nEnter number of sinus element to be calculated: "))

# calling functions
SinModule(amplitude1, freq1, amplitude2, freq2, time, Elements)
displayTerminationMessage()
