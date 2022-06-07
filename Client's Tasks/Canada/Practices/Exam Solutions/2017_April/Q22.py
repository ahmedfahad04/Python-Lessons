def readFile(filename):
    infile = open(filename,"r")
    f = infile.read()       # read whole file as string
    infile.close()

    lines = f.splitlines()  # detect each line
    X = []
    Y = []

    for line in lines:
        slot = line[1:-1].split(")(") # first full line

        for i in range(0,len(slot),1):  # check for each element.
            part = slot[i].split(",")
            x = float(part[0])
            y = float(part[1])
            scale = float(part[2])
            X.append(x*scale)
            Y.append(y*scale)

    return X, Y

# # NEVER INCLUDE these lines below IN EXAM. Before submitting you must delete it.
x, y = readFile("input.txt")
print("X: ", x)
print("Y: ", y)
