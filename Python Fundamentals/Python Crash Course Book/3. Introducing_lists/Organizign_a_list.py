#parmanently sort a list using sort()

cars = ['bmw','audi','tyota','primeo']
print("Usnsorted list is: ")
print(cars)
cars.sort() #sort the list
print("Sorted List is: ")
print(cars)
print("Reversly sorted list is: ")
cars.sort(reverse=True) #reversly sort the list
print(cars)

#temporarily sort the list using sorted()
cars = ['bmw','audi','tyota','primeo']
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars)) #temporarily sort the list

print("\nHere is the original list again: ")
print(cars)

#print string in revese order
cars.reverse() 
print("List element in reverse order: ")
print(cars)

#finding length of a list
print(len(cars)) 