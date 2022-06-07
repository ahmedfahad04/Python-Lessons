from math import sqrt, log, e
import Q24  # this was out previous mistake

interval = 10
Vs = 25
capacitance = float(input("Enter the capacitance in farads (>0): "))
while capacitance>0:

    resistance = float(input("Enter the resistance in ohms (>0): "))
    if resistance <= 0.0:
        print("The resistance, "+str(resistance)+", must be greater than zero!")
    else:
        time, charge, discharge = Q24.voltages(interval, Vs, resistance,capacitance)

        print("\n%21s %21s %21s" % ("Time (seconds)","Charging Voltage", "Discharging Voltage"))
        for t,c,d in zip(time, charge, discharge):
            print("%21.3f %21.14e %21.14e"%(t,c,d))

    capacitance = float(input("Enter the capacitance in farads (>0): ")) # remember***

print("\n Program by Wasif Arko")



