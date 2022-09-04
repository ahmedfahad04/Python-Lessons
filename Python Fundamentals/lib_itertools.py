from itertools import product

### Certain Products =====================================

# a = [[1,2,3],[4,5,6]]
# print(list(product(*a)))
# b = [1,2,3]
# print(list(product(b, repeat = 2)))

# Task1: finding certesian products
# a = input().split(" ")
# b = input().split(" ")

# a = [int(i) for i in a]
# b = [int(i) for i in b]

# ans = list(product(a,b))

# for i in ans:
#     print(i, end = " ")

### Permutations =====================================

# a = [1,2,3]
# print(list(permutations(a)))
# print(list(permutations(a, 2)))
# print(permutations(a))
# b = 'fahad'
# print(list(permutations(b, 2)))

## Your task is to print all possible permutation of the string in lexicographic sorted order.

# from itertools import permutations

# a = input().split(" ")

# a[0] = [i for i in a[0]]
# a[1] = int(a[1])

# ans = list(permutations(a[0], a[1]))
# ans = sorted(ans)

# for i in ans:
#     x = str.join("", i)
#     print(x)

### Combinations =====================================

# from itertools import combinations

# a = [1,2,3,4]
# print(list(combinations(a, 3)))
# b = 'fahad'
# print(list(combinations(b, 2)))
# print(list(permutations(b, 2)))

## Your task is to print all possible size replacement combinations of the string in lexicographic sorted order.
# a = input().split(" ")

# a[0] = [i for i in a[0]]
# a[1] = int(a[1])

# turn = a[1]
# for j in range(1, turn+1):
        
#     ans = list(combinations(a[0], j))
#     ans = [sorted(i) for i in ans]
#     ans = sorted(ans)

#     for i in ans:
#         x = str.join("", i)
#         print(x)

### Combinations with replacement =====================================

from itertools import combinations_with_replacement

# a = [1,2,7,3,4]
# print(list(combinations_with_replacement(sorted(a), 3)))

## Your task is to print all possible size replacement combinations of the string in lexicographic sorted order.
a = input().split(" ")

a[0] = [i for i in a[0]]
a[1] = int(a[1])

ans = list(combinations_with_replacement(sorted(a[0]), a[1]))

for i in ans:
    x = str.join("", i)
    print(x)