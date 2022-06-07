import matplotlib.pyplot as plt
import numpy as np

def plotCurves(xCoords, yCoords, title):

    plt.figure()
    plt.plot(xCoords,yCoords,"r-")
    plt.xlabel("x")
    plt.ylabel("F(X)")
    plt.title(title)
    plt.show()

