import numpy as np
import matplotlib.pyplot as plt


def plotCurveSignle(x, y, y2):
    plt.figure()
    plt.plot(x, y, "r-")
    plt.plot(x, y2, "b-")
    k = y*y2
    plt.plot(x, k, "c-")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("First Sinus Wave")
    plt.show()

def plotCurveMultiple(x,y,y1):
    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(x,y,'r-')

    plt.ylabel("Amplitude")
    #plt.legend(['sinx'], loc='lower left')
    plt.title('First Sinus Wave')

    plt.subplot(3,1,2)
    plt.plot(x,y1,'b-')

    plt.ylabel("Amplitude")
    #plt.legend(['sin10x'], loc='lower left')
    plt.title('Second Sinus Wave')

    plt.subplot(3, 1, 3)
    plt.plot(x, y1*y, 'm-')
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    #plt.legend(['sin15x'], loc='lower left')
    plt.title('Modulatd Wave')

    plt.tight_layout()
    plt.savefig("ASSignment.png")
    plt.show()

def displayTerminationMessage():
    print("""
Programmed by Md Wasif Bin Rahman Arko
Date: %s
End of processing.""" % ctime())

x = np.arange(0, 50, .05)
print(len(x))
y = 1*(np.sin(((2*np.pi)/10)*x))
y2 = 1*(np.sin(((2*np.pi)/1)*x))
#plotCurveSignle(x, y, y2)
plotCurveMultiple(x,y,y2)
