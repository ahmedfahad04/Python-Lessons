import math
import cmath
import numpy.lib.scimath as nl
import numpy as np
#
# u = -2 + 8j
# v = 3 + 7j
# print(u / v)
# print(u.real)
#
# print(cmath.sin(u))
#
# print(cmath.sin(u.real), ">>", cmath.sin(8))  # always return complex number
# print(math.sin(u.real), ": ", math.sin(u.imag))  # always return real number
# print(np.sin(u.real), "-> ", np.sin(u.imag))  # same as math.sin
#
# print(cmath.sqrt(-4), ": ", nl.sqrt(-4))  # they are both same

# ----------------------------------------------------------------------
# print("Roots of Eqn: (Opt 1) ")
# a = 1
# b = 6
# c = 5
# r1 = (-b + nl.sqrt(b ** 2 - 4 * a * c)) / (2 * a)  # recommended to use numpy.lib.scimath
# r2 = (-b - nl.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
# print(r1)
# print(r2)
# print(30 * "--")
#
# print("Trajectory of a Ball: \n")
#
# v0 = float(input("Enter the initial velocity in m/s: "))
# y0 = float(input("Enter the initial height in m: "))
# theta = float(input("Enter the initial angle in degrees: "))
# x = float(input("Enter the distance x in m: "))
#
# G = 9.81
#
# print("""
# gravity     = %.2f m/s^2
# v0          = %.1f m/s
# y0          = %.1f m
# theta       = %g
# degrees x   = %.1f m
# """ % (G, v0, y0, theta, x))
#
# theta = theta * math.pi / 180
# y = x * math.tan(theta) - 1 / (v0 ** 2 * 2 * G * x ** 2)  / math.cos(theta) ** 2 + y0
# y1 = x * math.tan(theta) - 1 / (2 * v0 ** 2) * G * x ** 2 / math.cos(theta) ** 2 + y0
#
# print("The position of the ball is (%.2f, %.4f)" % (x, y))
# print("The position of the ball is (%.2f, %.4f)" % (x, y1))

print(30 * "--")

print("Find value of e: ")
places = int(input("Enter the number of decimal places: "))

one = 10**places
extra = 10**4
n = 1
term = one * extra
eee = 0
count = 0

while term > 0:
    eee += term
    count += 1
    term += term // n
    n += 1
eee = eee // extra
intPart = eee // one
fracPart = eee % one
eee = str(intPart) + '.' + '0' * (places - (int(math.log10(fracPart)) + 1)) + str(fracPart)

print("""
Python's value of e is:\n %.15f \n
e to %d decimal places is:\n %s \n
The number of terms in the series is %d""" % (math.exp(1), places, eee, count))