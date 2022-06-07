import fnmatch
import os


def file_finder(addr, fileType):
    
    rootpath = addr+":/"
    pattern = "*."+fileType

    count = 0
    for root, dirs, files in os.walk(rootpath):
        for filename in fnmatch.filter(files, pattern):
            data = os.path.join(root, filename)
            print(data)
            count += 1

    print("Total audio file: ", count)

address = input("Enter directory where you want to search: ")
ft = input("Enter file type: ")

file_finder(address,ft)