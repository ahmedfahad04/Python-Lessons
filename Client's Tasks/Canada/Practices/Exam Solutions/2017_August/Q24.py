import numpy as np
def voltages(intervals, Vs, R, C):

    times = np.linspace(0, 5*R*C, intervals)
    ePower = np.exp(-times/(R*C))
    discharging = Vs*ePower
    charging = Vs*(1-ePower)

    return times, charging, discharging

voltages(10,5,3,7)

