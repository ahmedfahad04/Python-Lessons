a = 5
intervals = 10

# using by hand[list comprehension]
x = [(a / intervals) * i for i in range(0, intervals + 1)]

# - or - [loop]
for i in range(0, intervals+1):
    x = a/intervals * i
    print(x)

#------------------------------------------------------------------------------
# using numpy
import numpy as np
x = np.linspace(0,a,intervals+1)


print(x)
print(len(x))