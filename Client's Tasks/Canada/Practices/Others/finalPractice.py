# from math import sqrt, log, e
#
# def displayPrices(product):
#     print("\n")
#     print("%-15s %10s %10s %10s" % ("Product", "Cost", "Wholesale", "Retail"))
#
#     for k, v in product.items():
#         print("%-15s %10.2f %10.2f %10.2f" % (k, v[0], v[1], v[2]))
#
#
# prod = dict()
#
# # main
# print("\n")
# print(80 * "-")
#
# while True:
#     name = input("Enter the name of the product: ").strip()
#     if name == "":
#         break
#
#     if name in prod:
#         print("Duplicate product: " + name)
#         continue
#     else:
#         cost = float(input("Enter the cost of product: "))
#         if cost <= 0:
#             print("The cost of the product, {}, must be greater than zero!".format(cost))
#             continue
#         else:
#             wholesale = (sqrt(cost))**2.25
#             retail = (log(wholesale,(e)))**3
#             prod[name] = (cost,wholesale,retail)
#
# displayPrices(prod)

import matplotlib.pyplot as plt
import numpy as np
#
# def plotCurves(times, voltages, currents, title1, title2):
#
#     plt.figure()
#     plt.subplot(2,1,1)
#     plt.plot(times,voltages,"b")
#     plt.xlabel("Time in seconds")
#     plt.ylabel(title1)
#     plt.title(title1)
#     plt.savefig(title1+".png")
#
#     plt.subplot(2,1,2)
#     plt.plot(times,currents, "b-")
#     plt.xlabel("Time in seconds")
#     plt.ylabel(title2)
#     plt.title(title2)
#     plt.savefig(title2 + ".png")
#
#     plt.show()
#
# t = np.arange(0,250,50)
# volt = t*t
# curnt = -1*(np.sqrt(t))
#
# plotCurves(t,volt,curnt,"Time in seconds","Current vs Time")
# ls = ["this","is","A","test","at","home","a","with","good","book","is","good"]
#
# x = 5
# # f = x**2*np.cos(x)*np.e(x)+2
#
# y = int(f(x))
# print(y)



# def uniquwWordsByLength(words):
#
#     uniq = dict()
#
#     for item in words:
#         ln = len(item)
#         if ln not in uniq:
#             uniq[ln] = {item}
#         else:
#             uniq[ln].add(item)
#
#     return uniq
# x = uniquwWordsByLength(ls)
# print(x)
import matplotlib.pyplot as plt
import numpy as np

def plotCurves(angles, cosines, sines, legend1, legend2):

    plt.figure()

    plt.plot(angles,cosines,"b")
    plt.plot(angles, sines, "k")
    plt.xlabel("Angle in Degrees")
    plt.ylabel("Function value")
    plt.legend([legend1,legend2],loc='upper center')
    plt.title(legend1 + " and "+legend2+" vs Angle")
    plt.savefig(legend1+"And"+legend2+".png")
    plt.show()


while True:
    rev = int(input("Enter the number of revolution: "))
    if rev == 0:
        break
    if rev < 0:
        print("The number of revolutions, "+str(rev)+", must be greater than zero!")
        continue
    points = int(input("Enter the number of points: "))
    if points == 0:
        break
    if points < 0:
        print("The number of revolutions, " + str(points) + ", must be greater than zero!")
        continue

    x = np.linspace(0, rev*np.pi,(rev*400)//points)
    c = np.cos(x)
    s = np.sin(x)

    plotCurves(x,c,x,"Cosine","Sine")


