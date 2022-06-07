def readFile(fileName):
    infile = open(fileName, 'r')    # open the file
    f = infile.readline()           # read the file
    infile.close()                  # close the file
    data = f[1:-1].strip().split(",")
    return data        # return the file data as string


def unique(words):

    freq = dict()
    for item in words:
        if item not in freq.keys():
            freq[item] = 1
        else:
            freq[item] += 1

    return freq


filename = input("\nEnter the name of the text file: ")

while filename != "":
    listOfWords = readFile(filename)
    WordFrequency = unique(listOfWords)

    print("\n%-10s %-10s\n" % ("Word", "Frequency"))
    for word, freq in WordFrequency.items():
        print("%-10s %-10d" % (word, freq))

    filename = input("\nEnter the name of the text file: ")
