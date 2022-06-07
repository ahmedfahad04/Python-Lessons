from math import sqrt, pi


def getPosNum(promt):
    while True:

        n = input(promt).strip()

        if n != '':
            try:
                n = eval(n, {}, {})
            except:
                print("Invalid Input!")
            else:
                if type(n) is int or type(n) is float:
                    if n >= 0:
                        break
                    else:
                        print(n, "is not a positive integer!")
                else:
                    print(n, " is not an Integer!")
        else:
            print("Missing Output!")

    return n


def fxCircle(radius, xCoords):
    rSquared = radius * radius
    return [sqrt(rSquared - min(x ** 2, rSquared)) for x in xCoords]


def areaCircle(fx, radius, intervals):
    xCoords = [i * radius / intervals for i in range(intervals + 1)]
    yCorrds = fx(radius, xCoords)
    area = 0

    for i in range(intervals):
        area += yCorrds[i] + yCorrds[i + 1]

    area *= 2 * radius / intervals

    return area


def main():
    print("\n" + '-' * 80)
    print("\nEnter 0 at any prompt to terminate the program.")
    while True:
        radius = float(getPosNum('Enter the radius in cm (>0): '))
        if radius == 0.0:
            break
        intervals = int(getPosNum('Enter the number of intervals (>0): '))
        if intervals == 0:
            break

        area = areaCircle(fxCircle, radius, intervals)
        actual = pi * radius * radius
        error = abs(actual - area)
        print("""
        Approximate area of circle is %.14e cm^2
        Actual area of circle is %.14e cm^2
        The error in the area is %e cm^2""" % (area, actual, error))


main()
