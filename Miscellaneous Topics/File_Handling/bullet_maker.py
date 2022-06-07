def converter(input_name, output_name, spliter):

    #1. reading file data
    with open(input_name, 'r') as f:
        file = f.read()

    #2. removes all the new line character in files
    x = file.split('\n')

    # print("FILE: "+str(len(file)))

    #3. this string and loop will store the lines without newline
    result = ''
    for item in x:
        result += str(item)

    # print("RESUTL: " + str(len(result)))

    #4. this will make new lines in basis of semicolons
    y = result.split(spliter)

    #5. lastly it will print out the fomated output
    out = open(output_name, 'a+')
    num = 1
    for items in y:
        k = str(num) + ". "+ items.strip(' ') + "\n\n"
        out.write(k)
        print(num, end='. ')
        print(items.strip(' '), end='\n\n')
        num += 1
name = input("Enter File Name: ")
separator = input("Enter separator: ")

converter('Notes.txt',name,separator)