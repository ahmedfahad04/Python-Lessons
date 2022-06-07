# import pprint
#
# std_info = dict(Name="Fahad", Roll="1204", Varsity="DU_IIT") # initialize dictionary(pprint doesnot work)
# std_info["Age"] = 12    # add new value to dictionary
#
# print("Before Deletion: ")
# for item in std_info:
#     print(item, ':', std_info[item])
#
# del std_info['Varsity'] # deleting elements
# print("\nAfter deletion: ")
# print(std_info)
#
# print("\nPretty Print")
# cp = {"Bangladesh" : "Dhaka", "India": "Delhi", "Pakistan":"Islamabad", "USA":"Washington DC"} # pprint works here
# pprint.pprint(cp)
#
# ls = [x for x in cp.keys()]
# print("\nCountries: ", ls)
# cap = [x for x in cp.values()]
# print("Capitals: ", cap)
# print("All Credentials: ")
# all = [x for x in cp.items()]
# pprint.pprint(all)


# ------------------------------------
# freq = dict()
#
# def displayFreqNum(f):
#     k = sorted(f.keys()) # not working at all as I didnot pass the instance to k
#
#     print("\n%10s    %10s"%("Numbers", "Frequencies"))  # problem(not attaching %)
#
#     for num  in k:
#         print("%10d    %11d" % (num, f[num]))  # problem(not attaching %), f[num] not k[num]
#
#
# def main():
#     while True:
#         num = eval(input("Enter a number(0 to quit): "))
#
#         if num == 0:
#             break  # problem(because num was string previously)
#
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
#
#     displayFreqNum(freq)
#
#
# main()

# ------------------------------------
s = {1,2,3,1,2,5}   # set initialization
k = {'a','b','b','d',5}
l = {'a','b','b','d'}
m = {"Fahad", "Ahmed"}

print("Basic Operation: ")
print(s)    # {1, 2, 3, 5}
s.add(15)   # add new  element
print(s)    # {1, 2, 3, 5, 15}
s.discard(2)# removing or deleting elements
print(s)    # {1, 3, 5, 15}

print("\nSet Operation: ")
print(s.union(k))   # {1, 3, 5, 'a', 'd', 'b', 15}

print(s.intersection(k))    # {5}
print(s&k)  # intersection

print(s.isdisjoint(m))  # True

print("Fahad" in k)     # False

print(l.issubset(k))    # True
print(m<=k) # subset

print(k.issuperset(l))  # True
print(m>=l) # superset

print("Length: ", len(k))

