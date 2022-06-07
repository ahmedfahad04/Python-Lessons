def readFile(filename):
    infile = open(filename,"r")
    f = infile.read()
    lines = f.splitlines()

    hour = []
    minute = []
    second = []

    for line in lines:
        slot = line.split() # 00:00:00, 01:12:59, 06:45:31
        for x in range(0,len(slot),1):
            k = slot[x].split()
            h,m,s = k[0].split(":")
            hour.append(int(h))
            minute.append(int(m))
            second.append(int(s))

    return hour, minute, second

# # NEVER INCLUDE these lines below IN EXAM. Before submitting you must delete it.
# h,m,s = readFile("input.txt")
# print("Hours: ", h)
# print("Minute: ", m)
# print("Second: ", s)

