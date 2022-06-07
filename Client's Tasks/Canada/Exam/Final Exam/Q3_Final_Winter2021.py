def readFile(fileName):
    infile = open(fileName, 'r')  # open the file
    f = infile.readline()  # read the file
    infile.close()  # close the file

    words = f[1:-1].split(",")  # strip out the opening and ending third bracket and splitting the data by comma(,)
    wordList = []  # empty list for storing the words

    for item in words:
        wordList.append(item.strip()[1:-1])  # adding words to the list

    return wordList  # return the file data as List


def unique(words):

    frequency = dict()  # dictionary to hold the words along with their frequencies
    for word in words:

        if word not in frequency.keys():  # check if the element is in the dictionary or not
            frequency[word] = 1  # if not then add 1 to its frequency
        else:
            frequency[word] += 1  # otherwise increment its frequency by one

    return frequency  # return the list of words along with its frequency


# input section
filename = input("\nEnter the name of the text file: ")

while filename != "":
    listOfWords = readFile(filename)  # get the list of words as a string from input file
    WordFrequency = unique(listOfWords)  # get the dictionary of words along with their frequencies.

    print("\n%-10s %-10s\n" % ("Word", "Frequency"))  # printing the headline
    for word, freq in WordFrequency.items():
        print("%-10s %-10d" % (word, freq))  # printing the values

    filename = input("\nEnter the name of the text file: ")  # again asking for file name
