def readFile(filename):
    infile = open(filename,"r")
    f = infile.read()       # read whole file as string
    infile.close()

    lines = f.splitlines()  # detect each line

    employee = {}


    for line in lines:
        slot = line.split(") (") # first full line

        for x in range(0,len(slot),1):  # check for each element.
            i,n,s = slot[x].split(",")
            if i[0] == "(":
                i = i[1:]
            if s[-1] == ")":
                s = s[:-1]

            if int(i) in employee.keys():
                employee[int(i)][1] = s
            else:
                employee[int(i)] = [n,s]

    return employee

# # NEVER INCLUDE these lines below IN EXAM. Before submitting you must delete it.
print(readFile("input.txt"))

