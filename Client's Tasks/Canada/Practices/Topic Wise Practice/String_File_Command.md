# String
split()
strip()
lstrip()
rstrip()
.join()
splitlines()
upper()
lower()
find()
startswith()
replace()

->slicing

# File
1. file.read() --> returns the contents of the entire file as a string
2. /readlines() --> read each line separately as list of string
3. /readline() --> returns the empty string when the end of
the file is reached
   
`Must close the file before next operation; file.close()`

## techniques:
1. lines = **[line for line in infile]**; to extract lines of file
2. more things to find in last two examples of String.py
3. **pprint.pprint()** is used for pretty printing(row,col wise printing)
