# 1. finding divisors of n
# 2. perfect number finding

# Test Cases--------

# 15 = 1*15
#      3*5
# 30 = 1*30
#      2*15
#      3*5
# 36 = 1*36
#      2*18
#      3*12
#      4*9
#      6*6

# from numpy.lib.scimath import sqrt
from math import sqrt


def validInt(promt):
    while True:

        n = input(promt).strip()

        if n != '':
            try:
                n = eval(n, {}, {})
            except:
                print("Invalid Input")
            else:
                if type(n) is int:
                    if n > 0:
                        break
                    else:
                        print(n, "is not a positive integer")
                else:
                    print(n, " is not an Integer.")
        else:
            break

    return n


def findDivisors(n):
    divisors = []
    for i in range(1, int(sqrt(n)) + 1, 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)

    divisors.sort()
    return divisors


def perfect_number(divisors):
    if sum(divisors[:-1]) == divisors[-1]:
        print(divisors[-1], "is a perfect Number.")
        return True
    else:
        return False


def displayDivisors(divisors):
    print(", ".join(str(x) for x in divisors), end='\n\n')


def main():
    prompt = "Enter a Positive Integer "
    n = validInt(prompt + "(Enter to Quit): ")
    while type(n) is int:
        divs = findDivisors(n)
        print("Divisors of %d are: " % n)
        displayDivisors(divs)
        perfect_number(divs)
        n = validInt(prompt + "(Enter to Quit): ")


# 1
# main()

# 2
upr_bound = int(input("Enter Upper Bound: "))
cnt = 0
for i in range(2, upr_bound + 1, 1):
    divs = findDivisors(i)

    flag = perfect_number(divs)
    if flag == True:
        print("Divisors of %d are: " % i)
        displayDivisors(divs)
        cnt += 1

print("Total %d Perfect Numbers Exits between 2 to %d" % (cnt, upr_bound))
