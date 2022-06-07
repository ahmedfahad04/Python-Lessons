# Lab3Q2.py

# Course:     COMP 1012
# Instructor: Amirhossein Hosseinmemar
# Lab:        3 Question 2
# Author:     Wasif
# Version:    2021/02/12
# 
# Purpose:    The purpose of this question is to write a python program (script)
#             to evaluate equation (1) for equally sized intervals along the x-axis.
# 
# first = First value of x
# last = last value of x
# interval = number of interval
# a = calculate first value of x
# b = calculate final value of function f(x)

from time import ctime
print("\n------------------------------------------------------------------")

first = float(input("Enter the first value for x: ")) #first value of x
last = float(input("Enter the last value for x: ")) #last vlaue of x

interval = int(input("Enter the number of intervals: ")) #number of intervals

k = (last-first)/interval #total number of x values


print("\nf(x) = x^2 - 3x + 2 for x = %.1f to x = %.1f\n" %(first, last))

a = first #used for determinig first x value
data = [] #stores the x values
cnt = 0 #counts the number of x vlaues

b = 0 #used for determinig equation value f(x)
result = [] #stores the funcion's value



while True:
    cnt+=1
    data.append(a)
    
    b = a**2 - 3*a + 2
    result.append(b)
    
    a += k
    if cnt == interval+1: #terminates when the number of x values is 1 more than the number of intervals
        break

print(format('x', ">5"), format('f(x)', ">10"))    
for x,y in zip(data, result):
    print(format(x, ">5.2f" ), format(y, ">10.4f"))



print("""
Programmed by Wasif
Date: %s
End of processing.""" % ctime())
      
    


