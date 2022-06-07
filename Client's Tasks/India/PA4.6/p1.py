try:
    f = open("names.txt", "r")

except:

    print("The file names.txt does not exist. Would you like to create it? (Y or YES if you do...) ")
    answer = input()

    if answer == 'Y' or answer == 'YES':
        f = open("names.txt", "w")
        print("I created the file names.txt")
        f.close()
