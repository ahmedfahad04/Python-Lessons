import math

tolerance = float(input("Enter the acceptable tollerance: "))
degree = float(input("Enter an angle in degree: "))

# degree to radian
x = degree * math.pi / 180

# estimating sin(x) value
factor = 2
sine = 0.0
term = x
xSquared = x * x
count1 = 1
while abs(term) > tolerance:
    sine += term
    term = -term * (xSquared / (factor * (factor + 1)))
    factor += 2
    count1 += 1
# loop ends

# estimating cos(x) value
factor = 2
cosine = 0.0
term = 1.0
xSquared = x * x
count2 = 1
while abs(term) > tolerance:
    cosine += term
    term = -term * xSquared / (factor * (factor - 1))
    factor += 2
    count2 += 1
# loop ends
