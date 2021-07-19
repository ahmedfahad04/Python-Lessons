# map, filter, reduce

# map
num = [2,4,5,6,9]
cube = list(map(lambda x: x**3, num))
print(cube)

num2 = ['1','2','14']
type_cast = list(map(int, num2))
print(num2)
print(type_cast)

# filter
greater_than_6 = list(filter(lambda x: x>5, num))
print(greater_than_6)

# reduce
from functools import reduce

cum_sum = reduce(lambda x,y: x+y, num)
print(cum_sum)
