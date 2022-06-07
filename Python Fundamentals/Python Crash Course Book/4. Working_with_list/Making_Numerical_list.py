#use range to make list of numbers

num = list(range(1,11))
print(num)

num2 = list(range(1,11,3))
print(num2)

squares = []
for item in range(1,11):
    squares.append(item**2)

print(squares) #showing first 10 square numbers

print("Minimum Number is:", min(squares))
print("Maximum Number is:", max(squares))
print("Summation of squares is:", sum(squares))

#List Comprehension**

squares2 = [item**2 for item in range(1,11)]
print("Generating Square numbers using list comprehension:\n\t",squares2)

nth_value = [int((n*(n+1))/2) for n in range(2,11)]
print("First nth value summatio:\n\t",nth_value)

