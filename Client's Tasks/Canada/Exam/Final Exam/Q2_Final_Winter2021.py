def unique(words):
    frequency = dict()   # dictionary to hold the words along with their frequencies

    for word in words:

        if word not in frequency.keys(): # check if the element is in the dictionary or not
            frequency[word] = 1          # if not then add 1 to its frequency
        else:
            frequency[word] += 1         # otherwise increment its frequency by one

    return frequency     # return the list of words along with its frequency
