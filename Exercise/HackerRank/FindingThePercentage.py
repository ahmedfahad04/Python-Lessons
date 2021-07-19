data = []
# if any one give 2 then it will run 2 times
for _ in range(int(input())):

    # taking space separated input
    std = list(map(str , input().split()))

    # student name
    name = std[0] 
    
    # storing the numbers as float in a list
    numbers = []
    for num in std[1:]:
        numbers.append(float(num))
    
    # taking the average
    avg = sum(numbers)/3
    info = [name, avg]
    
    # adding names and their avg in list
    data.append(info)
    

# taking user name as input
user_name = input()

# printing the result
for name in data:
    if name[0] == user_name:
        print("%0.2f"%name[1])






### how to take input both string and int/float at a time using map
# n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()