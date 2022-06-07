f = open("Notes.txt")
# ==> these are the basic fucntion of python file reading
#print(f.read())  #reads the whole file
# print(f.readline()) #reads every line
# print(f.readline())
# print(f.readline())
#print(f.readlines()) #displays all lines as a list
#print(f.read(10)) #displays first 10 words

for lines in f.readlines(): #print every line
    print(lines,end='!**')

for word in f:          #print every line
    print(word, end="!!")

for lines in f:          #printing each words of file
    for word in lines.split():
        print(word)

f.close() #its a must