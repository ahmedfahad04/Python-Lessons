# total number of inputs
n = int(input())

# stores pair of name and score of students
data = []

# store just the scores
all_scores = []

# taking inputs 
for i in range(n):
    name = input()
    score = float(input())
    
    info = [name, score]

    all_scores.append(score)
    data.append(info)

# sorted list of scores
num = sorted(all_scores) 

# maximum in the num list
maxnum = min(num)

# finding the result by seaching through the list 
for i in range(len(num)):
    if maxnum != num[i]:
        target = num[i]
        break

# # student names maching with target scores
# std = sorted([info[0] for info in data if info[1]==target])

# # printing those names 
# for name in std:
#     print(name)

# merging line 33,36,37 in one line using join operation
print("\n".join(sorted([info[0] for info in data if info[1]==target])))
















### alternate solution - 
# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))