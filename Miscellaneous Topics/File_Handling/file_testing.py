with open ("Notes.txt",'r') as f:
    x =f.readlines()
    for t in x:
        print(t[-2])



#
# # seek(n) takes the file handle to the nth
# # bite from the beginning.
# file1.seek(0)
#
# print ("Output of Readline function is ")
# print (file1.readline())
#
#
# file1.seek(0)
#
# # To show difference between read and readline
# print ("Output of Read(9) function is ")
# print (file1.read(9) )
#
#
# file1.seek(0)
#
# print ("Output of Readline(9) function is ")
# print (file1.readline(9))
#
# file1.seek(0)
# # readlines function
# print ("Output of Readlines function is ")
# print (file1.readlines())
# file1.close()
