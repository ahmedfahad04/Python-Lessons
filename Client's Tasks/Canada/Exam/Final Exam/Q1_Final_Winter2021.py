def readFile(fileName):
    infile = open(fileName, "r")    # open the file
    f = infile.read()               # read the file
    infile.close()                  # close the file
    lines = f.splitlines()          # split the file in basis of lines

    hours = []      # empty list of hours
    minutes = []    # empty list of minutes
    seconds = []    # empty list of seconds

    for line in lines:
        slot = line.split()  # operate each lines

        for x in range(0, len(slot), 1):
            k = slot[x].split()         # operate on each element of lines
            h, m, s = k[0].split(":")   # distinguish hour, minute, second

            hours.append(int(h))        # append hour to hours list
            minutes.append(int(m))      # append minute to minutes list
            seconds.append(int(s))      # append second to seconds list

    return hours, minutes, seconds      # return list of hours, minutes, seconds in the given order