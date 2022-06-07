import matplotlib.pyplot as plt
import numpy as np

def plotCurves(xCoords, yCoords1, yCoords2, legend1, legend2):

    plt.figure()

    # both the plot can be in one argument
    plt.plot(xCoords,yCoords1,"k-")
    plt.plot(xCoords, yCoords2, "b--")

    plt.xlabel("Time in seconds")
    plt.ylabel("Voltage in volts")
    plt.title(legend1 + " vs "+legend2+" Voltages of a Capacitor")
    plt.legend([legend1,legend2], loc="center right")
    plt.savefig(legend1+legend2+".png")
    plt.show()

# # NEVER INCLUDE these lines IN EXAM. Before submitting you must delete it.

