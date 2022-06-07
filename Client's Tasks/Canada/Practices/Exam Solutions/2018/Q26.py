import matplotlib.pyplot as plt
def plotCurves(times, voltages, currents, title1, title2):

    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(times,voltages,"b")
    plt.xlabel("Time in seconds")
    plt.ylabel(title1)
    plt.title(title1)
    plt.savefig(title1+".png")

    plt.subplot(2,1,2)
    plt.plot(times,currents, "b-")
    plt.xlabel("Time in seconds")
    plt.ylabel(title2)
    plt.title(title2)
    plt.tight_layout()
    plt.savefig(title2 + ".png")

    plt.show()

# # NEVER INCLUDE these lines IN EXAM. Before submitting you must delete it.
# t = np.arange(0,250,50)
# volt = t**2
# curnt = -1*(np.sqrt(t))
# plotCurves(t,volt,curnt,"Voltage vs Time","Current vs Time")
