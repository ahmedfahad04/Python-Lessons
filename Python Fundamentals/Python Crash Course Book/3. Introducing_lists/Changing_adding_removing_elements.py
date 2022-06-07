#modify elements of list

dept = ['IIT','CSE','GE','Math'] 
print(dept)
dept[2] = "Physics" # modify single element
print(dept)

#adding elements to a list

dept.append('Chemistry')# addition of new element at the end of the lsit
print(dept)
dept.insert(1, 'English')# inserting new elements to certain position or index
print(dept)

print("---------------------------------------------------")
#removing elements

del dept[2] #removing elements using 'del' 
print(dept)
new_dept = dept.pop() #removing element using 'pop()'. It removes the last element
print(dept)

position_del = dept.pop(1) #pop() is also used to delete element of certain position
print(dept)
print("The item that I have deleted is: "+position_del)

dept.remove('Math') #remove item using value
print(dept)

my_dept = 'IIT' #we can store values before removing it
dept.remove(my_dept) 
print(dept)
print(my_dept+" is my Department")

print("---------------------------------------------------")