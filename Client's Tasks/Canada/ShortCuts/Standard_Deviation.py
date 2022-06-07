import math


def avg_calc(dataList):
    total = 0

    # finding summation for calculating average
    for item in dataList:
        total += item

    return total / len(dataList)


def sd_calc(avg_cal, dataLs):
    sqr_diff = 0

    # calculating squared difference of values from their average for calculating standard deviation
    for item in dataLs:
        x = (item - avg_cal) ** 2
        sqr_diff += x

    variance = sqr_diff / (len(dataLs) - 1)
    sd = math.sqrt(variance)  # finally calculating standard deviation

    return sd
