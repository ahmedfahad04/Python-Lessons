data = []
for _ in range(int(input())):
    cmd, *digits = input().split()
    digits = list(map(int, digits))

    if cmd == "insert":
        data.insert(digits[0], digits[1])

    elif cmd == "print":
        print(data)

    elif cmd == "remove":
        data.remove(digits[0])


    elif cmd == "reverse":
        data.reverse()

    elif cmd == "append":
        data.append(digits[0])

    elif cmd == "sort":
        data.sort()
    
    elif cmd == "pop":
        data.pop()




# alternative solution

# n = input()
# l = []
# for _ in range(n):
#     s = input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd) # l.insert(0,1)
#     else:
#         print (l)