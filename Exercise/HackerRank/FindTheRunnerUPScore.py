n = int(input())

# best way to take space separated int numbers
arr = map(int, input().split())

# converting map object to list items
num = list(arr) 

# making the list sorted in ascending order
num = sorted(num) 

# maximum in the num list
maxnum = max(num)

# finding the result by seaching through the list from the last index
for i in range(n-1, -1, -1):
    if maxnum != num[i]:
        print(num[i])
        break
