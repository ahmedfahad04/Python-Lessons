# def computeXcoordinates(width, intervals):
#     # list using list comprehension
#     return [(-1*(width/2) + (width/intervals)*i )for i in range(0, intervals + 1)]

# data = computeXcoordinates(10,4)
# data2 = [data[i] for i in range(1, len(data)-1)]
# sum2 = sum([data[i] for i in range(1, len(data)-1)])

# print(computeXcoordinates(10, 4))
# print(data2)
# print(sum2)
# from math import sqrt


# def computeXcoordinates(width, intervals):
#     # list using list comprehension
#     return [(-1*(width/2) + (width/intervals)*i)for i in range(0, intervals + 1)]


# xValues = computeXcoordinates(4,10)
# def computeYcoordinates(xValues):
#     # xValues == list of X Coordinates

#     top_portion = [sqrt(1-(abs(x)-1)**2) for x in xValues]
#     bottom_portion = [-3*sqrt(1-sqrt(abs(x)/2.0)) for x in xValues]
#     return top_portion, bottom_portion

# y1, y2 = computeYcoordinates(xValues)
# # y2 = [-3*sqrt(1-sqrt(abs(x)/2.0)) for x in xValues]
# print(y1)
# print(y2)
from numpy.lib.function_base import diff


xCoord = [2,1,5]
yCoord_1 = [1,2,3,4,5]

diff_xcoord = xCoord[1]-xCoord[0]
print("DIFF: ", diff_xcoord)

summation = sum(yCoord_1[1:-1])
print("SUM: ", summation)

top_area = (diff_xcoord)*(0.5*(yCoord_1[0]+yCoord_1[-1])+summation)
print(top_area)
