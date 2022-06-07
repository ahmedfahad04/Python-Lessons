# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:01:50 2021

@author: Fahad
"""
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image

# def computeTrajectory(a, b, c, distance, intervals):
#     k = distance / intervals
#     x = [k * i for i in range(0, intervals + 1)]
#     y = [(a * x ** 2 + b * x + c) for x in x]
#     return x, y
#
# X, Y = computeTrajectory(10,20,13,10,20);
# print("X")
# print(X)
# print("Y")
# print(Y)
#
# ## general figure
# fig = plt.figure()
# #x = np.linspace(0,20,100)
#
# #plt.plot(x, np.sin(x), '--')
# #plt.plot(x, np.cos(x))
#
# plt.plot(X,Y,'--')
# plt.show()
# fig.savefig('my_figure.jpg') #saving my plot
# Image('my_figure.jpg')
# print(fig.canvas.get_supported_filetypes()) #supported filetypes

import numpy as np
import matplotlib.pyplot as plt
def plotCurve(xCoords,yCoords):
    plt.figure() # create a figure to hold the

    plt.plot(xCoords, yCoords) # create the plot
    plt.tight_layout()
    plt.show() # display the plot
def main():
    xCoords = np.arange(-5., 5.1, .1)
    yCoords = xCoords**2
    plotCurve(xCoords, yCoords)
main()


