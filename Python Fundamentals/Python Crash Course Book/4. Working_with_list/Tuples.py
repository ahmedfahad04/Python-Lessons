dim = (200,50,150,244,1789) #declear elements in tuple

print("Option 1") #looping over tuple
for i in range(0,len(dim)):
    print(">>",dim[i])

print("Option 2\t")
for item in dim:
    print(">> ",item)

dim =(200,50,150,244,1789)
print("Original Dim: ")
for item in dim:
    print(">> ",item)
dim = (200,50,150,5,2,10) #adding or changing tuple elements
print("Modified Dim: ")
for item in dim:
    print(">> ",item)



