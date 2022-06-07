#slicing a string

cube = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
print("Starts from 4th element: ", cube[3:])
print("Ranging from 3rd element to 4th element: ",cube[2:4])
print("Begining to 8th element: ",cube[:8])
print("3 elements from the last: ",cube[-3:])

#looping through a slice

for item in cube[1:4]:
    print(item)

#copying a list

newc = []
newc = cube #option 1
print(newc)

new_cube = cube[:] #option 2
print("Copy of real cube list is:\n",new_cube)

cube.append(125) #to prove that our copy is legit
new_cube.append(200)
print(cube)
print(new_cube)



