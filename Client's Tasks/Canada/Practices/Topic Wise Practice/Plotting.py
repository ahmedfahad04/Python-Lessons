import matplotlib.pyplot as plt
import numpy as np

# plt.figure()  # 1
# plt.subplot(1,2,1) # plt.subplot(row,col,serial)
#
# x = np.linspace(0, 10, 100)  # 2
# z = 2 * np.sin(((2 * np.pi) / 10) * x) # 3  # geo function must be used in this way
# plt.plot(x, z, "r--")  # 4
#
# plt.xlabel("x")
# plt.ylabel("y")
# plt.axis([0,5,0,5])    # plt.axis(xmin, xmax, ymin, ymax)
# plt.legend(['sin(x)'])
# plt.title('F(x) = SIN(X)')
#
# plt.subplot(1,2,2)
#
# x = np.linspace(0, 10, 100)  # 2
# z = 2 * np.cos(((2 * np.pi) / 10) * x) # 3  # geo function must be used in this way
# plt.semilogx(x, z, "c--")  # 4 logarithmic graph
#
# plt.xlabel("x")
# plt.ylabel("y")
# plt.axis([0,5,0,5])    # plt.axis(xmin, xmax, ymin, ymax)
# plt.legend(['cos(x)'])
# plt.title('F(x) = COS(X)')
#
#
# plt.savefig("New.png")
# plt.tight_layout()
# plt.show()  #

count = 100
while True:
    rands = np.random.randint(1, 101, count)
    print('%d random numbers in histogram.' % count)

    myTitle = 'Frequency vs Value for ' + str(count) + ' values.'

    plt.hist(rands, bins=100) # plot histogram
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title(myTitle)
    plt.savefig('PlotHistogram.png')
    plt.show()

    data = input("Press return to continue (any key to quit): ").strip()
    if data != '':
        break
    count += 100


