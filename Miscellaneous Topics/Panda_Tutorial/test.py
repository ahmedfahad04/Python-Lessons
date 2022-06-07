# import pandas as pd
#
# file = pd.read_csv("attendance.csv")
# third = file.Marks
# stat = dict()
# obj = dict()
# for item in third:
#     cnt = 0
#     for i in third:
#         if i == item:
#             cnt += 1
#     stat[item] = cnt
#
# sorted(stat.values())
# print(stat)

import pandas as pd

file = pd.read_csv(r"F:\FAHADS FILES\Python\NewExperiments\Panda_Tutorial\CSV_Files\data.csv",index_col=0)
country = file.Country[:]
check = []
bod = dict()
for item in country:
    if item in check:
        pass
    else:
        check.append(item)
print("Countries: ", check)
print("Total Different Countries: ", len(check))

age = file.Age[:]
Dage = file.Age[:]

for x in age:
    count = 0
    for k in Dage:
        if(k == x ):
            count += 1

    bod[x] = count

k = 0
max_age = []

for key , val in bod.items():
    print("Age: " + str(key) + "==>" + str(val) )
    k = max(k,val)

for key , val in bod.items():
    if(k == val):
        print(key)


