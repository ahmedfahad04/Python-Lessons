x = int(input()) 
y = int(input()) 
z = int(input()) 
n = int(input())

# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             #print("[ ", i, ", ", j, ", ", k, " ]")

# list comprehension for 3 nested loops
result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
print(result)