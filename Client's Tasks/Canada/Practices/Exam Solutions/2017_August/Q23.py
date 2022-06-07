import math

import numpy as np

# def spiral(a, revolutions, intervals):
#     X = []
#     Y = []
#     angles = np.linspace(0,2*np.pi*revolutions,intervals)
#     radius = a*angles
#     xCoords = radius*np.cos(angles)
#     X.append(xCoords)
#     yCoords = radius * np.sin(angles)
#     Y.append(yCoords)
#
#     return X, Y

def he(a, revolutions, intervals):
    xC = []
    yC = []

    for i in range(intervals+1):
        angle = i * 2 * math.pi * revolutions / intervals
        radius = a * angle
        xC.append(radius*math.cos(angle))
        yC.append(radius*math.sin(angle))

    return xC, yC


# # NEVER INCLUDE these lines IN EXAM. Before submitting you must delete it.
#x,y = spiral(10, 45, 5)
print("X: ", x)
print("Y: ", y)

a,b = he(10,45,5)
print("A: ", a)
print("B: ", b)


