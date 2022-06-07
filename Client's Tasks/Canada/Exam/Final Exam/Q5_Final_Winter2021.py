import matplotlib.pyplot as plt

def plotCurves(xCoords1, yCoords1, legend1, xCoords2, yCoords2, legend2):
    plt.figure()   # declare a figure to hold the curves

    plt.plot(xCoords1, yCoords1, "r-")              # plot the first curve "ellipse"
    plt.plot(xCoords2, yCoords2, "k--")             # plot the second curve "circle"
    plt.legend([legend1, legend2], loc="center")    # declare the legend and its position
    plt.xlabel("X")                                 # give the name of xLabel
    plt.ylabel("Y")                                 # give the name of yLabel
    plt.title(legend1 + " and " + legend2)          # set the name of title according to the legend names
    plt.savefig(legend1 + legend2 + ".png")         # save the figure according to the legend names

    plt.show()      # show the plot