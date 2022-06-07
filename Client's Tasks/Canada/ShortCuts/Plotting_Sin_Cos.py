import numpy as np
import matplotlib.pyplot as plt


def sinTest(A, F, time, numel):
    x = np.arange(0, time, time / numel)  # value of x axis(Time); here x is angle
    y = A * (np.sin(((2 * np.pi) / F) * x))  # value of y axis(Amplitude of sinx)
    z = A * (np.cos(((2 * np.pi) / F) * x))  # value of y axis(Amplitude of sinx)

    plt.plot(x, y, 'b-', x, z, 'r-')  # plot the graph
    plt.ylabel("Amplitude")  # setting y axis label
    plt.savefig("SIN.png")

    return plt


sinTest(1, 25, 50, 100).show()
